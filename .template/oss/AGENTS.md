# AGENTS.md

## What it is

Template is a pure Go desktop app using MyGo native UI and native update windows. It targets macOS 12+,
Windows 10/11 and Linux with GTK 3 on amd64 and arm64. The baseline is a localized counter; replace it.

## Layout

```
main.go                    lifecycle and window
internal/ui/example/       screen state and native view (with copy.json catalog and tests)
mygo.json, go.mod          packaging, version, pinned MyGo library and CLI
resources/                 shipped dependency notices and product assets
scripts/                   checks, version bump, packaging, secret scan
docs/, design/             design language, ADRs, mockups
```

## Commands

```sh
scripts/check.sh --cross     # format, module tidy, vet, tests, script tests, cross-compilation
go test -race ./...
go tool mygo dev
go tool mygo build
python3 scripts/bump.py <version>
scripts/release.sh --check
```

## Conventions

- Only Go native views; use the native updater plugin. Every UI language is in the embedded catalog.
- Pin the CLI and the library together in `go.mod`. Update `THIRD_PARTY.md` and the notices when dependencies change.
- Signing, notarization and update hosting are not configured in the baseline.
- Commit messages and PR titles use Conventional Commits: `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`.

## Red lines

Credentials never appear in PRs, issues, logs or chat. Signing, release and anything sent to an external service
need the maintainer's confirmation. No blind staging.
