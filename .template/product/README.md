<div align="center">

# Template

A native desktop application written in Go.

[![License](https://img.shields.io/badge/license-proprietary-lightgrey.svg)](LICENSE)
[![Go](https://img.shields.io/badge/go-1.27.1-00ADD8.svg)](.go-version)
[![Website](https://img.shields.io/badge/website-example.com-informational.svg)](https://example.com)

**English** · [简体中文](README.zh-CN.md)

</div>

Status: development baseline 0.1.0, a counter demonstration. No public release is available yet; see
[the roadmap](docs/roadmap.md). Replace the baseline with the product specification before shipping.

## Features

- One native window on macOS 12+, Windows 10/11 and Linux with GTK 3 (amd64 and arm64).
- Changes an in-memory count and follows the system language.

## Requirements

- Go: the version in [.go-version](.go-version) (it must match `go.mod`).
- Python 3 for the helper scripts.

## Quick start

Official downloads will live at https://example.com. Development packages are local artifacts, not public signed
releases. Verify signatures and checksums as the website instructs.

## Development

```bash
scripts/check.sh --cross   # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go tool mygo dev           # run the app
go tool mygo build         # package for this platform
```

Use `python3 scripts/bump.py <version>` to advance the version and both changelogs.

### Documentation

| Document | Contents |
|---|---|
| [docs/spec.md](docs/spec.md) | Behavior and acceptance |
| [docs/design.md](docs/design.md) | Design language |
| [docs/roadmap.md](docs/roadmap.md) | Release scope |
| [docs/legal.md](docs/legal.md) | Legal facts and the code they must match |
| [docs/website.md](docs/website.md) | What the app needs from the website |
| [docs/releasing.md](docs/releasing.md) | How a release is made |
| [docs/security/](docs/security/README.md) | One security review per version |
| [docs/adr/](docs/adr/README.md) | Decisions |
| [CHANGELOG.md](CHANGELOG.md) | Changes |
| [THIRD_PARTY.md](THIRD_PARTY.md) | Dependency notices |
| [AGENTS.md](AGENTS.md) | AI collaborator brief |

## Contributing

Contribution rules are in [CONTRIBUTING.md](CONTRIBUTING.md). Commit messages and pull request titles follow
[Conventional Commits](https://www.conventionalcommits.org/).

## Security

Report vulnerabilities privately to support@example.com; do not open a public issue. Security reviews are kept in
[docs/security/](docs/security/README.md).

## Acknowledgements

Built on [MyGo](https://github.com/egoist/mygo); dependency notices are in [THIRD_PARTY.md](THIRD_PARTY.md).

## License

Proprietary. All rights reserved. [LICENSE](LICENSE) contains the terms of service, to be published at
https://example.com/terms.
