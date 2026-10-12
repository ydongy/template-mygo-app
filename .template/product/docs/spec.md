# Template specification

## Decisions

Pure Go native UI; one module, one window, no product persistence or external service.
The native updater has no configured feed or public key in the baseline.

## Information architecture

One Example screen. [The mockup](../design/screens/example.html) illustrates zero, positive
and negative counts. The template fixture has no product sign-off or acceptance.

## Data model

`Screen.count`: signed integer, in memory only. `Screen.text`: selected copy for the system locale.
Neither is persisted; closing the last window quits the app.

## Modules

`main.go` owns lifecycle, menu and window; `internal/ui/example/` owns state, copy and view.
`mygo.json` owns the version, identifier and packaging.

## Key flows

### Counting

Increment and decrement buttons and arrow keys change the count. Reset returns it to zero
and is disabled while the count is zero. Appearance changes preserve the count.

### Licensing

No paid plan or activation. The demonstration is free; the product rewrites these terms before shipping.

### Updates

Use MyGo's native updater. No checks occur without a configured feed and public key.
Configured products offer signed updates from a public HTTPS source, with a native confirmation window.

## Technical baseline

Go 1.27.1, MyGo v0.3.6, no cgo in production, no frontend toolchain.
macOS 12+, Windows 10/11, Linux GTK 3; amd64 and arm64. Default window 480×320, minimum 360×280.
Nine UI languages with English fallback; no performance claim until measured on a device.

## Acceptance checklist

- [ ] Initialize a disposable copy and run its tests.
- [ ] Six target builds succeed and macOS packaging is inspected.
- [ ] Before product release: device interaction, screen reader, signing and update tests pass.
- [ ] Before product release: replace the example and have the maintainer confirm the design.
