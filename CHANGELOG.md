# Changelog

All notable changes to this template are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed
- The template is organised as an open-source repository: MIT license, self-contained CI, contributor guide.
- `scripts/init.sh` takes `--license mit|proprietary` (default `mit`). `mit` produces an open-source project;
  `proprietary` produces everything `mit` does plus the closed-source layer (proprietary terms, specification,
  legal, website, releasing, roadmap and security-review documents, Chinese changelog).
- The closed-source skeleton moved to `.template/product/`, the open-source one to `.template/oss/`.
- `scripts/check.sh` no longer runs a documents check; `scripts/bump.py` treats `CHANGELOG.zh.md` as optional.
- The skeletons no longer depend on shared workflows or an external documents check.
- `AGENTS.md` (template and both skeletons) spells out the issue forms and the pull request body for `gh`, and the
  red lines name `git add -A` of unknown files.
- `CONTRIBUTING.md` states that issues and pull requests may be written in English or Simplified Chinese, and what
  CI runs.
- The proprietary skeleton starts pre-release: a status badge, `docs/launch.md` as the launch checklist, and no
  website badge, download address or support mailbox in the READMEs until launch.
- Screenshots go in the pull request body; `design/screenshots/` is ignored, and `.editorconfig` covers Swift.
- The open-source skeleton READMEs no longer name the init domain (no Website badge, no "official downloads"
  sentence; Quick start builds from source): init cannot know whether that site exists.
