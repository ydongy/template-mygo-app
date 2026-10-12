<!-- template: AGENTS.md v1 -->
# AGENTS.md

## What it is

Template is a pure Go desktop skeleton using MyGo native UI and native update windows.
It targets macOS 12+, Windows 10/11 and Linux with GTK 3 on amd64 and arm64.

## Sources of truth

Read `handbook/core/` first, then only the guides, stacks and type preset that apply to this project.
Its documented platforms, languages, architecture and distribution remain project decisions.
The handbook link and docs workflow pin one revision; upgrade them together in a migration PR.

`docs/spec.md` owns behavior, `docs/design.md` owns presentation, `mygo.json` owns packaging
and version, and `docs/legal.md` owns the matching legal facts. Documents win over code.
How we work: https://github.com/ydongy/.github/tree/f61354c75725bf3688632a9d3040e5664046f81a/handbook;
AI rules: `handbook/core/agents.md`.

## Directory boundaries

`main.go`: lifecycle and window. `internal/ui/example/`: screen state and native view.
`resources/`: shipped notices and product assets. `scripts/`: checks, version and packaging.
`docs/`, `design/`: spec, decisions and ledger. No external work runs during drawing.
See `handbook/types/mygo-app/layout.md`.

## Commands

```sh
scripts/check.sh --cross
go test -race ./...
go tool mygo dev
go tool mygo build
python3 scripts/bump.py <version>
scripts/release.sh --check
python3 <dotgithub>/scripts/check-docs.py .
```

## Project rules

Only Go native views; use the native updater plugin. Every UI language is in the embedded catalog.
A real screen follows `handbook/guides/ui-workflow.md`; headless tests do not constitute device acceptance.
Pin CLI and library together in go.mod. Update notices when dependencies change.
Signing, notarization and update hosting are not configured in the baseline.

## Red lines

Credentials never appear in PRs, issues, logs, reports or chat. Signing, release and anything sent to an
external service need the maintainer's confirmation. No blind staging. See `handbook/core/agents.md`.
