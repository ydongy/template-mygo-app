"""Initialize a disposable template checkout, validating all inputs before writing."""
import argparse
import json
from pathlib import Path
import re
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("name")
parser.add_argument("domain")
parser.add_argument("--repo")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", args.name) or args.name == "Template":
    parser.error("name must be PascalCase and must not be Template")
labels = args.domain.split(".")
if (args.domain == "example.com" or len(labels) < 2 or len(args.domain) > 253
        or any(not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", label) for label in labels)):
    parser.error("domain must be a lowercase domain other than example.com")
repo = args.repo or args.name.lower()
if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", repo) or repo.endswith(".git"):
    parser.error("repository must be a lowercase GitHub repository name")
if not (root / ".repo-type").is_file() or (root / ".repo-type").read_text().strip() != "template":
    parser.error("this is not an uninitialized template")
for rel in ("mygo.json", "go.mod", ".template/README.md", ".template/AGENTS.md", ".template/LICENSE"):
    if not (root / rel).is_file():
        parser.error(f"missing template file: {rel}")

rules = [("com.example.template", ".".join(reversed(labels)) + ".app"),
         ("github.com/ydongy/template", f"github.com/ydongy/{repo}"),
         ("example.com", args.domain), ("Template", args.name)]
# Prepare text before modifying the checkout. Skip Git metadata and generated outputs.
changes = {}
for p in root.rglob("*"):
    rel = p.relative_to(root)
    if p.is_symlink() or not p.is_file() or any(part in {".git", "build", ".mygo", "__pycache__", "superpowers"} for part in rel.parts):
        continue
    if rel.parts[0] == ".template" or p.name in {"init.sh", "init.py", "test_init.py"}:
        continue
    try:
        original = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    text = original
    for old, new in rules:
        text = text.replace(old, new)
    if text != original:
        changes[p] = text
for name in ("README.md", "AGENTS.md", "LICENSE"):
    text = (root / ".template" / name).read_text()
    for old, new in rules:
        text = text.replace(old, new)
    changes[root / name] = text
changes[root / ".repo-type"] = "mygo-app\n"
changes[root / ".docs-check.json"] = json.dumps({"ignore": [], "pending": []}, indent=2) + "\n"
for p, text in changes.items():
    p.write_text(text, encoding="utf-8")
shutil.rmtree(root / ".template")
if (root / "docs/superpowers").exists():
    shutil.rmtree(root / "docs/superpowers")
for rel in ("scripts/test_init.py", "scripts/init.sh", "scripts/init.py"):
    (root / rel).unlink()
print(f"Initialized {args.name} ({args.domain}, repository {repo}).")
print("Next: write the product spec and design, replace the example, run scripts/check.sh,")
print("configure icon and legal facts, then review explicit files before committing.")
