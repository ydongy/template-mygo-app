"""Initialize disposable copies, never this working tree."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InitTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "app"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "build", ".mygo", "__pycache__"))

    def run_init(self, *args):
        return subprocess.run(["bash", "scripts/init.sh", *args], cwd=self.root, text=True, capture_output=True)

    def snapshot(self):
        return {str(p.relative_to(self.root)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in self.root.rglob("*") if p.is_file()}

    def test_product_initialization(self):
        result = self.run_init("Probe", "probe.test", "--repo", "probe-desktop")
        self.assertEqual(result.returncode, 0, result.stderr)
        config = json.loads((self.root / "mygo.json").read_text())
        self.assertEqual(config["name"], "Probe")
        self.assertEqual(config["identifier"], "test.probe.app")
        self.assertEqual((self.root / ".repo-type").read_text().strip(), "mygo-app")
        self.assertIn("github.com/ydongy/probe-desktop", (self.root / "go.mod").read_text())
        self.assertIn("https://probe.test", (self.root / "docs/website.md").read_text())
        self.assertIn("<!-- template: mygo-app/README.md v1 -->", (self.root / "README.md").read_text())
        for name in (".template", "scripts/init.sh", "scripts/init.py", "scripts/test_init.py", "docs/superpowers"):
            self.assertFalse((self.root / name).exists(), name)
        for p in self.root.rglob("*"):
            if p.is_file() and p.suffix in (".go", ".md", ".json", ".mod"):
                text = p.read_text()
                self.assertNotIn("example.com", text, str(p))
                self.assertNotIn("Template", text, str(p))
        result = subprocess.run(["go", "test", "./..."], cwd=self.root, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        checker = ROOT.parent / "github-mygo/scripts/check-docs.py"
        if checker.exists():
            subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
            # The checker scans tracked files; track the explicit copied file inventory.
            paths = [str(p.relative_to(self.root)) for p in self.root.rglob("*")
                     if p.is_file() and ".git" not in p.relative_to(self.root).parts]
            subprocess.run(["git", "add", "--", *paths], cwd=self.root, check=True)
            result = subprocess.run(["python3", str(checker), str(self.root)], text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_input_leaves_copy_unchanged(self):
        before = self.snapshot()
        for args in [("lower", "probe.test"), ("Template", "probe.test"), ("Probe", "example.com"),
                     ("Probe", "bad_domain"), ("Probe", "-bad.test"), ("Probe", "probe.test", "--repo", "../bad"),
                     ("Probe", "probe.test", "--unknown"), ("Probe", "probe.test", "--repo")]:
            with self.subTest(args=args):
                self.assertNotEqual(self.run_init(*args).returncode, 0)
                self.assertEqual(self.snapshot(), before)

    def test_initialized_repository_is_rejected(self):
        (self.root / ".repo-type").write_text("mygo-app\n")
        before = self.snapshot()
        self.assertNotEqual(self.run_init("Probe", "probe.test").returncode, 0)
        self.assertEqual(self.snapshot(), before)


if __name__ == "__main__":
    unittest.main()
