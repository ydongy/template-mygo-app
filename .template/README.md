<!-- template: mygo-app/README.md v1 -->
# Template

A native desktop application written in Go. The current baseline is a counter demonstration.

## Status

Development baseline 0.1.0. macOS 12+, Windows 10/11, Linux with GTK 3; amd64 and arm64.
See [the roadmap](docs/roadmap.md). No public release is available.

## Product

The baseline opens one native window, changes an in-memory count and follows the system language.
Replace it with the product specification before shipping.

## Install

Official downloads will live at https://example.com. Development packages are local artifacts,
not public signed releases. Verify signatures and checksums as the website instructs.

## Development

Install Go 1.27.1 and Python 3. Run `scripts/check.sh --cross`, `go tool mygo dev`
and `go tool mygo build`. Run `python3 <dotgithub>/scripts/check-docs.py .` for documents.
Use `python3 scripts/bump.py <version>` to advance the version and both changelogs.
The handbook is https://github.com/ydongy/.github/tree/6b48552c969c28a954498123bb502a556f8eed79/handbook.

## Documentation

| Document | Contents |
|---|---|
| [docs/spec.md](docs/spec.md) | Behavior and acceptance |
| [docs/design.md](docs/design.md) | Design language |
| [docs/roadmap.md](docs/roadmap.md) | Release scope |
| [docs/adr/](docs/adr/README.md) | Decisions |
| [CHANGELOG.md](CHANGELOG.md) | Changes |
| [AGENTS.md](AGENTS.md) | AI collaborator brief |

## License

Closed source. `LICENSE` contains the terms of service, to be published at
https://example.com/terms. Dependency notices are in `THIRD_PARTY.md`.
