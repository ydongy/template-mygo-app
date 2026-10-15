"""Initialize disposable copies, never this working tree."""
import hashlib
import json
import re
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

    # Words that must not survive in any generated project (spelled in parts so this file passes its own check).
    BANNED = ("hand" "book", "docs-" "check", "ORG_DOCS" "_ROOT", "ydongy/." "github", "template" ": ")

    def assert_no_banned_words(self):
        for p in self.text_files():
            if p.suffix in (".md", ".yml", ".json", ".sh", ".py", ".go", ".toml", ".mod", "") and p.name != "test_bump.py":
                text = p.read_text()
                for word in self.BANNED:
                    self.assertNotIn(word, text, str(p))

    def text_files(self):
        return [p for p in self.root.rglob("*") if p.is_file() and ".git" not in p.relative_to(self.root).parts]

    def assert_neutral_names_gone(self):
        for p in self.text_files():
            if p.suffix in (".go", ".md", ".json", ".mod"):
                text = p.read_text()
                self.assertNotIn("example.com", text, str(p))
                self.assertNotIn("Template", text, str(p))

    def assert_readmes(self, owner, proprietary):
        en = (self.root / "README.md").read_text()
        zh = (self.root / "README.zh-CN.md").read_text()
        for text in (en, zh):
            self.assertIn("# Probe\n", text.split("</div>")[0])
            self.assertNotIn("template-mygo-app", text)
        self.assertIn("[简体中文](README.zh-CN.md)", en)
        self.assertIn("[English](README.md)", zh)
        self.assertIn("## Features", en)
        self.assertIn("## 功能特性", zh)
        self.assertIsNone(re.search("[\u4e00-\u9fff]", en.replace("简体中文", "")))
        for text in (en, zh):
            if proprietary:
                self.assertIn("license-proprietary", text)
                self.assertIn("status-pre--release", text)
                self.assertNotIn("support@", text)
                self.assertNotIn("actions/workflows/ci.yml/badge", text)
            else:
                self.assertIn(f"github.com/{owner}/", text)
                self.assertIn("actions/workflows/ci.yml/badge", text)
            for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", text):
                if not target.startswith("http"):
                    self.assertTrue((self.root / target).exists(), target)

    def assert_agents_guide(self):
        agents = (self.root / "AGENTS.md").read_text()
        for heading in ("## Issues and pull requests", "## Red lines", "## What happened", "## Done when",
                        "## Suggested change", "## How tested", "git add -A"):
            self.assertIn(heading, agents)

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
        self.assert_readmes("acme-inc", proprietary=False)
        for name in ("README.md", "README.zh-CN.md", "CONTRIBUTING.md", "CHANGELOG.md", "AGENTS.md", ".editorconfig", ".github/dependabot.yml",
                     ".github/workflows/ci.yml", ".github/workflows/pr-title.yml", "docs/design.md",
                     "docs/adr/README.md", "THIRD_PARTY.md"):
            self.assertTrue((self.root / name).is_file(), name)
        for name in (".repo-type", ".docs-" "check.json", "GEMINI.md", "SECURITY.md", "CHANGELOG.zh.md",
                     ".github/copilot-instructions.md", ".github/workflows/docs.yml", "docs/spec.md",
                     "docs/legal.md", "docs/roadmap.md", "docs/website.md", "docs/releasing.md", "docs/launch.md", "docs/security",
                     "docs/pro" "cess.md", "docs/mile" "stones"):
            self.assertFalse((self.root / name).exists(), name)
        self.assert_agents_guide()
        self.assert_helper_files_gone()
        self.assert_neutral_names_gone()
        self.assert_no_banned_words()
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
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/ydongy/probe-desktop.git"],
                       cwd=self.root, check=True)
        result = self.run_init("Probe", "probe.test", "--repo", "probe-desktop", "--license", "proprietary")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("warning", result.stdout)
        config = json.loads((self.root / "mygo.json").read_text())
        self.assertEqual(config["identifier"], "test.probe.app")
        self.assertIn("github.com/ydongy/probe-desktop", (self.root / "go.mod").read_text())
        self.assertIn("https://probe.test", (self.root / "docs/website.md").read_text())
        self.assert_readmes("ydongy", proprietary=True)
        license_text = (self.root / "LICENSE").read_text()
        self.assertTrue(license_text.startswith("Terms of Service\n"))
        self.assertIn("Copyright (c) 2026 ydongy. All rights reserved.", license_text)
        self.assertEqual((self.root / ".github/CODEOWNERS").read_text(), "* @ydongy\n")
        self.assertEqual((self.root / "CLAUDE.md").read_text().strip(), "@AGENTS.md")
        for name in ("README.md", "README.zh-CN.md", "docs/spec.md", "docs/design.md", "docs/legal.md", "docs/roadmap.md", "docs/website.md",
                     "docs/releasing.md", "docs/launch.md", "docs/security/README.md", "docs/adr/README.md", "design/README.md",
                     "CONTRIBUTING.md", "CHANGELOG.md", "CHANGELOG.zh.md", "THIRD_PARTY.md", "AGENTS.md",
                     ".editorconfig", ".github/dependabot.yml", ".github/workflows/ci.yml",
                     ".github/workflows/pr-title.yml", ".github/workflows/package.yml"):
            self.assertTrue((self.root / name).is_file(), name)
        for name in (".repo-type", ".docs-" "check.json", "GEMINI.md", "SECURITY.md",
                     ".github/copilot-instructions.md", ".github/workflows/docs.yml", "docs/pro" "cess.md",
                     "docs/mile" "stones"):
            self.assertFalse((self.root / name).exists(), name)
        ci = (self.root / ".github/workflows/ci.yml").read_text()
        self.assertNotIn("uses: ydongy/", ci)
        self.assertIn("scripts/check.sh", ci)
        self.assertNotIn("ORG_DOCS" "_ROOT", (self.root / "scripts/check.sh").read_text())
        self.assert_agents_guide()
        self.assert_helper_files_gone()
        self.assert_neutral_names_gone()
        self.assert_no_banned_words()
        self.go_test()
        result = subprocess.run(["python3", "-m", "unittest", "discover", "-s", "scripts", "-p", "test_*.py"],
                                cwd=self.root, text=True, capture_output=True)
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
