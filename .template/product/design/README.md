# Design mockups

`screens/example.html` is a self-contained HTML page with no external resources. Open it in a browser; it
illustrates the template fixture, not real device captures. `?state=zero|positive|negative` shows one state and
`?scheme=light|dark` forces the color scheme.

## Working rules

A UI change starts from the mockup: edit or add `screens/<screen>.html`, get the visual direction confirmed by the
maintainer, then write the native view in `internal/ui/<screen>/`. Change the design text (`docs/design.md`) and the
native view together. Commit only real device captures as screenshots.
