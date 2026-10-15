"""Initialize a disposable template checkout, validating all inputs before writing."""
import argparse
from pathlib import Path
import re
import shutil
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("name")
parser.add_argument("domain")
parser.add_argument("--repo")
parser.add_argument("--license", choices=("mit", "proprietary"), default="mit",
                    help="mit: open-source project (default); proprietary: the same standard plus the closed-source layer")
parser.add_argument("--owner", help="GitHub user or organisation (default: inferred from the origin remote)")
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
for rel in (".template/oss", ".template/product"):
    if not (root / rel).is_dir():
        parser.error("this is not an uninitialized template (missing " + rel + ")")
for rel in ("mygo.json", "go.mod", ".template/README.md"):
    if not (root / rel).is_file():
        parser.error(f"missing template file: {rel}")
owner = args.owner
if not owner:
    remote = subprocess.run(["git", "config", "--get", "remote.origin.url"], cwd=root, text=True, capture_output=True)
    found = re.fullmatch(r"(?:https://(?:[^/@]+@)?github\.com/|git@github\.com:|ssh://git@github\.com/)"
                         r"([^/]+)/[^/]+", remote.stdout.strip()) if remote.returncode == 0 else None
    owner = found.group(1) if found else ""
owner_known = bool(owner)
owner = owner or "ydongy"
if not re.fullmatch(r"[A-Za-z0-9-]+", owner):
    parser.error("owner must be a GitHub user or organisation name")

rules = [("com.example.template", ".".join(reversed(labels)) + ".app"),
         ("github.com/ydongy/template", f"github.com/{owner}/{repo}"),
         ("example.com", args.domain), ("Template", args.name)]
# Prepare text before modifying the checkout. Skip Git metadata and generated outputs.
skip_parts = {".git", "build", ".mygo", "__pycache__"}
content = {}
for p in root.rglob("*"):
    rel = p.relative_to(root)
    if p.is_symlink() or not p.is_file() or any(part in skip_parts for part in rel.parts):
        continue
    if rel.parts[0] == ".template" or p.name in {"init.sh", "init.py", "test_init.py"}:
        continue
    try:
        content[rel] = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
# The skeleton files of the chosen license go over the tree. The template root already holds the shared
# open-source files (CONTRIBUTING, pr-title, Dependabot, CI); each skeleton adds or replaces the rest.
overlay = root / ".template" / ("product" if args.license == "proprietary" else "oss")
for p in overlay.rglob("*"):
    if p.is_file():
        content[p.relative_to(root.joinpath(overlay))] = p.read_text(encoding="utf-8")
content[Path(".github/CODEOWNERS")] = f"* @{owner}\n" if owner_known else "* @<owner>\n"
changes = {}
for rel, original in content.items():
    text = original
    if rel != Path(".github/CODEOWNERS"):
        for old, new in rules:
            text = text.replace(old, new)
    if text != original or not (root / rel).is_file() or (root / rel).read_text(encoding="utf-8") != text:
        changes[root / rel] = text
for p, text in changes.items():
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
shutil.rmtree(root / ".template")
for rel in ("scripts/test_init.py", "scripts/init.sh", "scripts/init.py"):
    (root / rel).unlink()
print(f"Initialized {args.name} ({args.domain}, repository {owner}/{repo}, license {args.license}).")
if args.license == "proprietary":
    print("Next: write the product spec and design, replace the example, run scripts/check.sh,")
    print("configure icon, legal facts and the release workflow (docs/releasing.md), check LICENSE and")
    print(".github/CODEOWNERS, then review explicit files before committing.")
else:
    print("Next: replace the example, run scripts/check.sh, check LICENSE (copyright holder) and")
    print(".github/CODEOWNERS, then review explicit files before committing.")
if not owner_known:
    print("warning: could not infer the GitHub owner; .github/CODEOWNERS contains the placeholder"
          " '* @<owner>'. Fix it (or rerun with --owner).")
