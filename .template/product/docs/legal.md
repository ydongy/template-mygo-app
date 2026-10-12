# Legal pages: one source per fact

## Where each thing lives

| Thing | Where |
|---|---|
| Terms | `LICENSE`, published at https://example.com/terms |
| Privacy | https://example.com/privacy |
| Refund | https://example.com/refund |
| Support | support@example.com |

## Facts that must match the code

| Fact | Code | Website key | Check |
|---|---|---|---|
| Count stays in memory | `internal/ui/example/view.go` | Product privacy copy | Code review |
| No update source or license service configured | `mygo.json`, `main.go` | Product privacy and terms | Configuration review |
| Update UI is native | `native.Plugin` | Product update copy | Code review |
| No window geometry saved by the example | No `StateKey` in `main.go` | Product privacy copy | Code review |

A configured updater may store preferences and contact its source. Rewrite these facts when enabling it.

## Refund policy

No purchases exist in the baseline. A paid product defines its merchant, refund period and
activation behavior before shipping; do not publish the neutral terms unchanged.
