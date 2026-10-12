# AGENTS.md

## What it is

Template is a pure Go desktop app using MyGo native UI and native update windows. It is closed source. It targets macOS 12+, Windows 10/11 and Linux with GTK 3 on amd64 and arm64.

## Sources of truth

`docs/spec.md` owns behavior, `docs/design.md` presentation, `mygo.json` packaging and version, and `docs/legal.md` the matching legal facts. How a release is made: `docs/releasing.md`. Security reviews, one per version: `docs/security/`. Decisions: `docs/adr/README.md`. Contribution rules: `CONTRIBUTING.md`. Documents win over code: if they disagree, fix the documents first, then the code, and say so in the PR.

## Directory boundaries

```
main.go                    lifecycle and window
internal/ui/example/       screen state and native view (with copy.json catalog and tests)
mygo.json, go.mod          packaging, version, pinned MyGo library and CLI
resources/                 shipped dependency notices and product assets
scripts/                   checks, version bump, packaging, secret scan
docs/, design/             spec, design language, legal, website, releasing, roadmap, adr/, security/, mockups
```

No external work runs during drawing.

## Commands

```sh
scripts/check.sh --cross     # format, module tidy, vet, tests, script tests, cross-compilation
go test -race ./...
go tool mygo dev
go tool mygo build
python3 scripts/bump.py <version>
scripts/release.sh --check
python3 scripts/scan_secrets.py
```

Commit messages and PR titles use Conventional Commits: `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`; scopes are in `CONTRIBUTING.md`. Branches are `<type>/<issue>-<slug>`; the maintainer squash-merges.

## Project rules

- A UI change starts from the mockup in `design/screens/`; the maintainer confirms the visual direction before UI code is written. Headless tests do not constitute device acceptance.
- Only Go native views; use the native updater plugin. Every UI language is in the embedded catalog.
- Pin the CLI and the library together in `go.mod`. Update `THIRD_PARTY.md` and the notices when dependencies change.
- Signing, notarization and update hosting are not configured in the baseline (`docs/releasing.md`).
- `CHANGELOG.md` and `CHANGELOG.zh.md` carry the same bullets; `scripts/bump.py` dates both.

## Red lines

- Credentials never appear in PRs, issues, logs, reports or chat.
- Signing, releases and anything sent to an external service need the maintainer's confirmation.
- Merging a version bump publishes a release once a release workflow exists (`docs/releasing.md`).
- No blind `git add -A` of unknown files; stage the files you checked.
- Never modify the user's dotfiles or global Git configuration.
- Changes involving credentials, signing, update keys or networking need a security walkthrough recorded in the PR.
- Never tell the maintainer the project is "secure" or "risk-free" without a complete scan or walkthrough.
