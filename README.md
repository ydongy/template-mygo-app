<!-- template: template/README.md v1 -->
# template-mygo-app

A starting point for pure Go desktop apps with MyGo native UI on macOS, Windows and Linux.
The neutral product is Template until `scripts/init.sh` names it. No WebView, HTML, Node or Bun.

## What is here

| Path | Purpose |
|---|---|
| `main.go`, `internal/ui/example/` | Native window, native updater and localized counter with interaction tests |
| `go.mod`, `go.sum`, `.go-version` | Pinned Go, MyGo and CLI; no frontend toolchain |
| `mygo.json`, `resources/` | Packaging configuration and shipped dependency notices |
| `scripts/` | Initialization, version bump, checks, redacted secret scan and local packaging |
| `.template/` | Product README and AGENTS installed by initialization |
| `docs/`, `design/` | Product spec, design ledger, legal facts and ADRs |
| `.github/workflows/` | Shared CI/docs callers and manual packaging artifacts |

## Using it

1. Create a repository from this template (private or public), then clone it.
2. Run `scripts/init.sh <Name> <domain> [--repo <repository-name>]`.
3. Run `scripts/check.sh --cross`. Set `ORG_DOCS_ROOT` to a checkout of `ydongy/.github`
   when running document checks locally.
4. Replace the neutral example spec/design with the product, and review the explicit changed file list before committing.
5. Run `go tool mygo dev`. Package locally with `go tool mygo build`.
6. Configure the product icon, legal facts, signing and updates before a public release.

Initialization sets the module path and reverse-DNS identifier, switches the type to `mygo-app`,
installs product docs and removes itself and template planning notes. It never creates credentials
or publishes. The shared workflows and handbook are pinned to the same ydongy/.github commit, so document checks
recognize the new type before the handbook branch is merged. Update both pins together.

## Changing it

Run `scripts/check.sh --cross` and `python3 <dotgithub>/scripts/check-docs.py .`, then
exercise `scripts/init.sh` on a disposable copy. Initialization tests compile and check that copy.
Products created earlier do not receive changes automatically; migrate useful changes explicitly.
The template is never released. Keep placeholder names neutral.

## License

This template is released under the [MIT License](LICENSE), copyright (c) 2026 ydongy. `scripts/init.sh` replaces `LICENSE` with a terms-of-service placeholder (from `.template/LICENSE`) for the new product; replace it with the license you choose. Dependency notices are in `THIRD_PARTY.md`.
