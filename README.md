<div align="center">

# template-mygo-app

A GitHub template for pure Go desktop apps with MyGo native UI on macOS, Windows and Linux. No WebView, HTML, Node or Bun.

[![CI](https://github.com/ydongy/template-mygo-app/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/template-mygo-app/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Go](https://img.shields.io/badge/go-1.27.1-00ADD8.svg)](.go-version)

**English** · [简体中文](README.zh-CN.md)

</div>

This repository is a **GitHub template**. The product is called `Template` here (domain `example.com`) until
`scripts/init.sh` gives it its real name.

## Features

- One native window on macOS, Windows and Linux (amd64 and arm64), built with [MyGo](https://github.com/egoist/mygo); no frontend toolchain.
- A localized counter example with interaction tests, and a native update window.
- A design system: the [design language](docs/design.md) (native first, semantic colors and dark mode, component choice, accessibility, motion, localization), [design tokens](design/tokens.md) and [mockups](design/screens/example-appearance.html) in light and dark.
- One command (`scripts/check.sh --cross`) runs gofmt, `go mod tidy`, vet, tests, script tests and cross-compilation for six targets.
- Version bump script, redacted secret scan and a manual local packaging workflow.
- Two starting points chosen at init time: an open-source (MIT) project or a closed-source product skeleton.

## Requirements

- Go: the version pinned in [.go-version](.go-version) and `go.mod` (currently 1.27.1). `scripts/check.sh` fails if the two differ.
- Python 3 for the helper scripts.
- Target platforms of the generated app: macOS 12+, Windows 10/11, Linux with GTK 3.

## Quick start

1. On GitHub choose **Use this template** and create your repository.
2. Clone it and run `scripts/init.sh <Name> <domain>`:

   ```bash
   scripts/init.sh Acme acme.com                       # open-source project (MIT), the default
   scripts/init.sh Acme acme.com --license proprietary # closed-source product skeleton
   ```

3. Run `scripts/check.sh --cross`.
4. Run `go tool mygo dev`; package locally with `go tool mygo build`.
5. Replace the counter example, then review the changed file list before committing.

Initialization sets the Go module path and the reverse-DNS identifier, installs the skeleton for the chosen
license and removes itself. It never creates credentials or publishes, and commits nothing.

## Usage

### `scripts/init.sh` options

```text
scripts/init.sh <Name> <domain> [--license mit|proprietary] [--owner <github-user>] [--repo <name>]
```

| Option | Meaning |
|---|---|
| `<Name>` | Product name in PascalCase |
| `<domain>` | Product domain, lowercase; the identifier becomes `<domain-reversed>.app` (`acme.com` gives `com.acme.app`) |
| `--license mit` (default) | Open-source project, see the table below |
| `--license proprietary` | Closed-source product skeleton, see the table below |
| `--owner <user>` | GitHub user or organization for `CODEOWNERS` and the module path; inferred from `git remote origin` when omitted, otherwise `CODEOWNERS` gets a `* @<owner>` placeholder to fill in |
| `--repo <name>` | Repository name (default: the lowercase product name) |

### `mit` or `proprietary`

| | `--license mit` | `--license proprietary` |
|---|---|---|
| `LICENSE` | MIT | Terms of service, all rights reserved |
| `README.md` and `README.zh-CN.md` | Open-source README with an MIT badge and a CI badge | Product README with a proprietary badge and a pre-release status badge, no CI badge, and a documentation index |
| Shared files | `CONTRIBUTING.md`, `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`, `CODEOWNERS`, `ci.yml`, `pr-title.yml`, Dependabot | The same, with closed-source wording |
| Extra documents | none | `docs/spec.md`, `legal.md`, `website.md`, `releasing.md`, `launch.md` (pre-release launch checklist), `roadmap.md`, `docs/security/`, `CHANGELOG.zh.md` and a simplified `design/README.md` |

The skeleton files live in `.template/oss/` and `.template/product/`; `init.py` copies one of them over the tree,
rewrites names, identifier and URLs in every text file (including both READMEs), and deletes `.template/`,
itself and its test. The generated `README.md` and `README.zh-CN.md` replace the ones you are reading.
See [.template/README.md](.template/README.md).

### Generated project layout

| Path | Purpose |
|---|---|
| `main.go`, `internal/ui/example/` | Native window, native updater and localized counter with interaction tests |
| `go.mod`, `go.sum`, `.go-version` | Pinned Go, MyGo and CLI; no frontend toolchain |
| `mygo.json`, `resources/` | Packaging configuration and shipped dependency notices |
| `scripts/` | Version bump, checks, redacted secret scan and local packaging |
| `docs/`, `design/` | Design language (`docs/design.md`), design tokens, mockups and architecture decision records |
| `.github/workflows/` | `ci.yml`, `pr-title.yml` and a manual packaging workflow |

## Development

```bash
scripts/check.sh --cross          # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go test -race ./...
python3 scripts/test_init.py      # init on disposable copies, both licenses
```

`Template`, `example.com` and `com.example.template` are the placeholders `init` replaces; do not write a real
product name anywhere in this repository.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Commit messages and pull request titles follow
[Conventional Commits](https://www.conventionalcommits.org/).

## Security

Report vulnerabilities privately through GitHub: **Security → Report a vulnerability**, or
<https://github.com/ydongy/template-mygo-app/security/advisories/new>.

## Acknowledgements

Built on [MyGo](https://github.com/egoist/mygo); dependency notices are in [THIRD_PARTY.md](THIRD_PARTY.md).

## License

[MIT](LICENSE).
