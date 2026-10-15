# AGENTS.md

## What it is

A GitHub template repository for pure Go desktop apps with MyGo native UI (macOS 12+, Windows 10/11, Linux with
GTK 3; amd64 and arm64). The neutral product is `Template`; `scripts/init.sh` turns it into a named project.
The template is MIT licensed and never released.

## Layout

```
main.go                    lifecycle and window
internal/ui/example/       screen state and native view (with copy.json catalog and tests)
mygo.json, go.mod          packaging, version, pinned MyGo library and CLI
resources/                 shipped dependency notices and product assets
scripts/                   checks, version bump, packaging, secret scan, init
docs/, design/             design language, ADRs, mockups
.template/oss/             files init installs for --license mit
.template/product/         files init installs for --license proprietary
```

## Commands

```sh
scripts/check.sh --cross     # format, module tidy, vet, tests, script tests, cross-compilation
go test -race ./...
go tool mygo dev
go tool mygo build
python3 scripts/bump.py <version>
scripts/release.sh --check
python3 scripts/scan_secrets.py
python3 scripts/test_init.py      # init on disposable copies, both licenses
```

## Conventions

- Only Go native views; use the native updater plugin. Every UI language is in the embedded catalog.
- Pin the CLI and the library together in `go.mod`. Update `THIRD_PARTY.md` and the notices when dependencies change.
- Signing, notarization and update hosting are not configured in the baseline.
- Keep `Template`, `example.com` and `com.example.template` as the only product placeholders; `init.py` rewrites
  exactly these. After changing initialization, run `python3 scripts/test_init.py` (it works on disposable copies).
- Commit messages and PR titles use Conventional Commits: `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`.
  Branches are `<type>/<issue>-<slug>`, for example `fix/12-counter-reset`; the maintainer squash-merges.
- Screenshots go in the pull request body, never in the repository.

## Issues and pull requests

`gh issue create` and `gh pr create --body` skip the issue forms and the pull request template, so write their
structure yourself. Search open issues first; one issue is one problem.

- Issue title: one short sentence that says the problem or the outcome, in English or Simplified Chinese. No type
  prefix such as `[feat]`; the label carries the type.
- Bug, `--label bug`: `## What happened`, `## What you expected`, `## Steps to reproduce`,
  `## Version and environment`.
- Feature or improvement, `--label enhancement`: `## Problem`, `## Proposed solution`,
  `## Alternatives considered` (when there were any), `## Done when`.
- Documentation, `--label documentation`: `## Where`, `## What is missing, unclear or wrong`, `## Suggested change`.
- Labels: `accessibility` marks screen-reader, keyboard and contrast work, together with `enhancement` or `bug`.
- Pull request: the title is the Conventional Commits subject (it becomes the squash commit). The body has
  `## Summary` (what changes and why), `## Related issue` (`Closes #<n>`, or `None.`), `## How tested` (the
  commands run and their results, and what was not run) and `## Checklist`:
  `- [ ] PR title follows Conventional Commits`, `- [ ] Tests pass`,
  `- [ ] Documentation updated where behavior changed`, ticked only when true.

## Red lines

- Credentials never go into pull requests, issues, logs or chat.
- Releases, signing and anything sent to an external service need the maintainer's confirmation.
- No blind `git add -A` of unknown files; review the staged file list before committing.
