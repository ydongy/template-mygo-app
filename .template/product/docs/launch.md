# Launch checklist

Template is pre-release: the code builds, but there is no domain, mailbox, download host or release credentials
yet. This file is the single source of truth for what remains. Check an item off only after its verification
passes; the launch pull request links this file.

## Domain and site

- [ ] Register `example.com` and point it at the product website. Verify: `https://example.com/` loads over HTTPS.
- [ ] Publish the pages listed in [website.md](website.md) (`/`, `/terms`, `/privacy`, `/refund`). Verify: each URL
      returns 200 and matches its source of truth.

## Mail

- [ ] Create `support@example.com` ([legal.md](legal.md)). Verify: a test message arrives and a reply is delivered.

## Downloads and updates

- [ ] Set up the downloads host and update manifests ([releasing.md](releasing.md), [website.md](website.md)).
      Verify: a development build updates from the manifest to a newer test build.

## Signing

- [ ] Signing and notarization credentials for each target platform and the update signing key pair, stored as
      secrets of the `release` environment (deployment branch policy: `main` only). Verify: the secrets table in
      [releasing.md](releasing.md) is filled in and a signed build passes the platform checks.
- [ ] A `release.yml` workflow as described in [releasing.md](releasing.md). Verify: a dry run builds and signs
      without publishing.

## Legal and content

- [ ] Rewrite `LICENSE` (terms), [legal.md](legal.md) (privacy, refund, support) and the facts that must match the
      code for the real product. Verify: every row of the facts table in `legal.md` is checked against the code.

## Places that depend on the domain

- [ ] [legal.md](legal.md): terms, privacy and refund URLs, support address.
- [ ] [website.md](website.md): pages and downloads host.
- [ ] [releasing.md](releasing.md): downloads host.

## Launch

- [ ] One pull request titled `chore(release): launch <version>` removes the pre-release state: the status badge
      and status sentence in `README.md` and `README.zh-CN.md`; it adds the Website badge, the download link and
      the support address back to both READMEs.
- [ ] The version bump pull request publishes the release ([releasing.md](releasing.md)).
- [ ] After the release: download and install from the website on each platform, check the update path, then
      archive this file (keep it, add the launch date and mark it as done).
