<div align="center">

# Template

A native desktop application written in Go with MyGo native UI.

[![CI](https://github.com/ydongy/template/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/template/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Go](https://img.shields.io/badge/go-1.27.1-00ADD8.svg)](.go-version)

**English** · [简体中文](README.zh-CN.md)

</div>

Template is a native desktop application written in Go with [MyGo](https://github.com/egoist/mygo) native UI. The
current baseline is a counter demonstration; replace it with your app.

## Features

- One native window on macOS 12+, Windows 10/11 and Linux with GTK 3 (amd64 and arm64); no WebView, HTML or Node.
- Follows the system language; all UI text lives in an embedded catalog.
- Native update window support.
- A documented design language ([docs/design.md](docs/design.md)), [design tokens](design/tokens.md) and [mockups](design/screens/example-appearance.html) in light and dark.

## Requirements

- Go: the version in [.go-version](.go-version) (it must match `go.mod`).
- Python 3 for the helper scripts.

## Quick start

Official downloads will live at https://example.com. Until the first release, build it yourself:

```bash
go tool mygo dev     # run the app
go tool mygo build   # package for this platform
```

## Development

```bash
scripts/check.sh --cross   # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go test -race ./...
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Commit messages and pull request titles follow
[Conventional Commits](https://www.conventionalcommits.org/).

## Security

Report vulnerabilities privately through GitHub: **Security → Report a vulnerability**, or
<https://github.com/ydongy/template/security/advisories/new>.

## Acknowledgements

Built on [MyGo](https://github.com/egoist/mygo); dependency notices are in [THIRD_PARTY.md](THIRD_PARTY.md).

## License

[MIT](LICENSE).
