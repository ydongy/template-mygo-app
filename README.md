# template-mygo-app

[![CI](https://github.com/ydongy/template-mygo-app/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/template-mygo-app/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A GitHub template for pure Go desktop apps with MyGo native UI on macOS, Windows and Linux. The neutral product is
called `Template` until `scripts/init.sh` names it. No WebView, HTML, Node or Bun.

## Quick start

1. On GitHub choose **Use this template** and create your repository.
2. Clone it and run `scripts/init.sh <Name> <domain> [--license mit|proprietary] [--owner <github-user>] [--repo <name>]`:

   ```bash
   scripts/init.sh Acme acme.com                       # open-source project (MIT), the default
   scripts/init.sh Acme acme.com --license proprietary # closed-source product skeleton
   ```

3. Run `scripts/check.sh --cross`.
4. Run `go tool mygo dev`; package locally with `go tool mygo build`.
5. Replace the counter example, then review the changed file list before committing.

Initialization sets the Go module path and the reverse-DNS identifier, installs the skeleton for the chosen
license and removes itself. It never creates credentials or publishes.

## init options

| Option | Meaning |
|---|---|
| `<Name>` | Product name in PascalCase |
| `<domain>` | Product domain, lowercase; the identifier becomes `<domain-reversed>.app` |
| `--license mit` (default) | Open-source project: MIT `LICENSE`, `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`, self-contained `ci.yml`, `pr-title.yml`, Dependabot and `CODEOWNERS` |
| `--license proprietary` | Closed-source product skeleton: proprietary terms as `LICENSE`, specification, legal, roadmap, website, process and release-plan documents, the repository-type marker and documents-check config, and workflows that call ydongy's shared CI and documents-check workflows |
| `--owner <user>` | GitHub user or organisation for `CODEOWNERS` and the module path; inferred from `git remote origin` when omitted, otherwise `CODEOWNERS` gets a `* @<owner>` placeholder to fill in |
| `--repo <name>` | Repository name (default: the lowercase product name) |

The skeleton files for each option live in `.template/oss/` and `.template/product/`; see
[.template/README.md](.template/README.md).

## Project layout

| Path | Purpose |
|---|---|
| `main.go`, `internal/ui/example/` | Native window, native updater and localized counter with interaction tests |
| `go.mod`, `go.sum`, `.go-version` | Pinned Go, MyGo and CLI; no frontend toolchain |
| `mygo.json`, `resources/` | Packaging configuration and shipped dependency notices |
| `scripts/` | Initialization, version bump, checks, redacted secret scan and local packaging |
| `docs/`, `design/` | Design language, architecture decision records and mockups |
| `.template/` | Optional skeletons that `init` installs |
| `.github/workflows/` | `ci.yml`, `pr-title.yml` and a manual packaging workflow |

## Development

```bash
scripts/check.sh --cross          # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go test -race ./...
python3 scripts/test_init.py      # init on disposable copies, both licenses
```

`Template`, `example.com` and `com.example.template` are the placeholders `init` replaces; do not write a real
product name anywhere.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Dependency notices are in [THIRD_PARTY.md](THIRD_PARTY.md).
