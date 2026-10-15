# Contributing

Template is closed source; this guide is for the maintainer, collaborators and any future contributor. Agent and
repository rules are in [AGENTS.md](AGENTS.md).

- Issues and pull requests may be written in English or Simplified Chinese.
- Open an issue before a large change so the direction is agreed first.

## Development setup

Requirements: the Go version in `.go-version`, Python 3 for the helper scripts. No Node, Bun or WebView.

```bash
scripts/check.sh --cross     # gofmt, go mod tidy, vet, tests, script tests, cross-compilation
go test -race ./...
python3 scripts/scan_secrets.py
go tool mygo dev             # run the app
go tool mygo build           # package locally
```

CI is one workflow, `.github/workflows/ci.yml`: a Linux job runs `scripts/check.sh --cross`, the secret scan of the
history and `go test -race ./...` on every pull request and push to `main`. `package.yml` builds unsigned
development packages on macOS, Windows and Linux only on manual dispatch.

## Commits, branches and pull requests

- Commit messages and pull request titles follow [Conventional Commits](https://www.conventionalcommits.org/):
  `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`. The scope is optional; usual ones:
  `app`, `example`, `i18n`, `scripts`, `docs`, `ci`. `pr-title.yml` checks the title.
- Name branches `<type>/<issue>-<slug>`, for example `fix/12-counter-reset`.
- The maintainer squash-merges, so the pull request title becomes the commit message. No DCO or sign-off is
  required.
- A UI change starts from the mockup in `design/screens/`; the maintainer confirms the visual direction before UI
  code is written. Screenshots (light and dark) go in the pull request body, not in the repository.
- Keep a change focused and add or update tests.

## Changelog

`CHANGELOG.md` (English) and `CHANGELOG.zh.md` (Chinese) carry the same bullets under `## [Unreleased]`. Write what
a user would notice, with no issue or PR numbers, hashes or tooling words. The Chinese file feeds the changelog
page of the product website, which is why it stays.

## Releasing

`python3 scripts/bump.py <version>` sets the version in `mygo.json` and dates `[Unreleased]` in both changelogs.
Every released version has a security review in `docs/security/`. The release steps and what is not yet automated
are in [docs/releasing.md](docs/releasing.md).
