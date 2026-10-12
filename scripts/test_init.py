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

    # Words that must not survive in an open-source project (spelled in parts so this file passes its own check).
    BANNED = ("hand" "book", "docs-" "check", "ORG_DOCS" "_ROOT", "ydongy/." "github", "mile" "stone")

    def text_files(self):
        return [p for p in self.root.rglob("*") if p.is_file() and ".git" not in p.relative_to(self.root).parts]

    def assert_neutral_names_gone(self):
        for p in self.text_files():
            if p.suffix in (".go", ".md", ".json", ".mod"):
                text = p.read_text()
                self.assertNotIn("example.com", text, str(p))
                self.assertNotIn("Template", text, str(p))

    def assert_helper_files_gone(self):
        for name in (".template", "scripts/init.sh", "scripts/init.py", "scripts/test_init.py", "docs/superpowers"):
            self.assertFalse((self.root / name).exists(), name)

    def go_test(self):
        result = subprocess.run(["go", "test", "./..."], cwd=self.root, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_mit_initialization(self):
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/acme-inc/probe-desktop.git"],
                       cwd=self.root, check=True)
        result = self.run_init("Probe", "probe.test", "--repo", "probe-desktop")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("warning", result.stdout)
        config = json.loads((self.root / "mygo.json").read_text())
        self.assertEqual(config["name"], "Probe")
        self.assertEqual(config["identifier"], "test.probe.app")
        self.assertIn("github.com/acme-inc/probe-desktop", (self.root / "go.mod").read_text())
        self.assertTrue((self.root / "LICENSE").read_text().startswith("MIT License"))
        self.assertEqual((self.root / ".github/CODEOWNERS").read_text(), "* @acme-inc\n")
        self.assertEqual((self.root / "CLAUDE.md").read_text().strip(), "@AGENTS.md")
        self.assertTrue((self.root / "README.md").read_text().startswith("# Probe\n"))
        for name in ("CONTRIBUTING.md", "CHANGELOG.md", "AGENTS.md", ".editorconfig", ".github/dependabot.yml",
                     ".github/workflows/ci.yml", ".github/workflows/pr-title.yml", "docs/design.md",
                     "docs/adr/README.md", "THIRD_PARTY.md"):
            self.assertTrue((self.root / name).is_file(), name)
        for name in (".repo-type", ".docs-" "check.json", "GEMINI.md", "SECURITY.md", "CHANGELOG.zh.md",
                     ".github/copilot-instructions.md", ".github/workflows/docs.yml", "docs/spec.md",
                     "docs/legal.md", "docs/roadmap.md", "docs/website.md", "docs/process.md", "docs/mile" "stones"):
            self.assertFalse((self.root / name).exists(), name)
        self.assert_helper_files_gone()
        self.assert_neutral_names_gone()
        for p in self.text_files():
            if p.suffix in (".md", ".yml", ".json", ".sh", ".py", ".go") and p.name != "test_bump.py":
                text = p.read_text()
                for word in self.BANNED:
                    self.assertNotIn(word, text, str(p))
        self.go_test()
        # the generated project passes its own script tests without a Chinese changelog
        result = subprocess.run(["python3", "-m", "unittest", "discover", "-s", "scripts", "-p", "test_*.py"],
                                cwd=self.root, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_mit_without_remote_uses_placeholder_and_owner_flag(self):
        result = self.run_init("Probe", "probe.test")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / ".github/CODEOWNERS").read_text(), "* @<owner>\n")
        self.assertIn("warning", result.stdout)
        self.assertIn("github.com/ydongy/probe", (self.root / "go.mod").read_text())

    def test_owner_flag(self):
        result = self.run_init("Probe", "probe.test", "--license", "mit", "--owner", "octo")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / ".github/CODEOWNERS").read_text(), "* @octo\n")
        self.assertIn("github.com/octo/probe", (self.root / "go.mod").read_text())

    def test_proprietary_initialization(self):
        result = self.run_init("Probe", "probe.test", "--repo", "probe-desktop", "--license", "proprietary")
        self.assertEqual(result.returncode, 0, result.stderr)
        config = json.loads((self.root / "mygo.json").read_text())
        self.assertEqual(config["identifier"], "test.probe.app")
        self.assertEqual((self.root / ".repo-type").read_text().strip(), "mygo-app")
        self.assertEqual(json.loads((self.root / ".docs-" "check.json").read_text()), {"ignore": [], "pending": []})
        self.assertIn("github.com/ydongy/probe-desktop", (self.root / "go.mod").read_text())
        self.assertIn("https://probe.test", (self.root / "docs/website.md").read_text())
        self.assertIn("<!-- template: mygo-app/README.md v1 -->", (self.root / "README.md").read_text())
        self.assertTrue((self.root / "LICENSE").read_text().startswith("Terms of Service"))
        for name in ("docs/spec.md", "docs/legal.md", "docs/roadmap.md", "docs/process.md", "docs/mile" "stones/v1.0.md",
                     "GEMINI.md", "SECURITY.md", "CHANGELOG.zh.md", ".github/copilot-instructions.md",
                     ".github/workflows/docs.yml", ".github/workflows/ci.yml", ".github/workflows/package.yml"):
            self.assertTrue((self.root / name).is_file(), name)
        for name in ("CONTRIBUTING.md", ".github/CODEOWNERS", ".github/workflows/pr-title.yml"):
            self.assertFalse((self.root / name).exists(), name)
        self.assertIn("uses: ydongy/", (self.root / ".github/workflows/ci.yml").read_text())
        self.assertIn("ORG_DOCS" "_ROOT", (self.root / "scripts/check.sh").read_text())
        self.assert_helper_files_gone()
        self.assert_neutral_names_gone()
        self.go_test()
        checker = ROOT.parent / ".github/scripts/check-docs.py"
        if checker.exists():
            subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
            # The checker scans tracked files; track the explicit copied file inventory.
            paths = [str(p.relative_to(self.root)) for p in self.text_files()]
            subprocess.run(["git", "add", "--", *paths], cwd=self.root, check=True)
            result = subprocess.run(["python3", str(checker), str(self.root)], text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_input_leaves_copy_unchanged(self):
        before = self.snapshot()
        for args in [("lower", "probe.test"), ("Template", "probe.test"), ("Probe", "example.com"),
                     ("Probe", "bad_domain"), ("Probe", "-bad.test"), ("Probe", "probe.test", "--repo", "../bad"),
                     ("Probe", "probe.test", "--unknown"), ("Probe", "probe.test", "--repo"),
                     ("Probe", "probe.test", "--license", "gpl"), ("Probe", "probe.test", "--owner"),
                     ("Probe", "probe.test", "--owner", "bad owner")]:
            with self.subTest(args=args):
                self.assertNotEqual(self.run_init(*args).returncode, 0)
                self.assertEqual(self.snapshot(), before)

    def test_initialized_repository_is_rejected(self):
        shutil.rmtree(self.root / ".template")
        before = self.snapshot()
        self.assertNotEqual(self.run_init("Probe", "probe.test").returncode, 0)
        self.assertEqual(self.snapshot(), before)


if __name__ == "__main__":
    unittest.main()
