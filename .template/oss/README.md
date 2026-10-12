# Template

[![CI](https://github.com/ydongy/template/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/template/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A native desktop application written in Go with [MyGo](https://github.com/egoist/mygo) native UI. The current
baseline is a counter demonstration; replace it with your app.

## Features

- One native window on macOS 12+, Windows 10/11 and Linux with GTK 3 (amd64 and arm64); no WebView, HTML or Node.
- Follows the system language; all UI text lives in an embedded catalog.
- Native update window support.

## Quick start

Official downloads will live at https://example.com. Until the first release, build it yourself:

```bash
go tool mygo dev     # run the app
go tool mygo build   # package for this platform
```

## Development

Requirements: the Go version in `.go-version`, Python 3 for the helper scripts.

```bash
scripts/check.sh --cross   # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go test -race ./...
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE). Dependency notices are in [THIRD_PARTY.md](THIRD_PARTY.md).
