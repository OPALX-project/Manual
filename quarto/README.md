# Quarto Pilot

This directory contains a parallel Quarto migration pilot for the legacy
Asciidoctor-based `Manual`.

Current scope:

- Quarto book scaffolding
- migrated main-manual body chapters up to the appendices:
  - `sections/introduction/index.qmd`
  - `sections/conventions/index.qmd`
  - `sections/pitfalls/index.qmd`
  - `sections/tutorial/index.qmd`
  - `sections/opalt/index.qmd`
  - `sections/opalcycl/index.qmd`
  - `sections/opalmap/index.qmd`
  - `sections/format/index.qmd`
  - `sections/control/index.qmd`
  - `sections/elements/index.qmd`
  - `sections/field-output/index.qmd`
  - `sections/lines/index.qmd`
  - `sections/beam-command/index.qmd`
  - `sections/distribution/index.qmd`
  - `sections/track/index.qmd`
  - `sections/emission-source/index.qmd`
  - `sections/energybins/index.qmd`
  - `sections/fieldsolvers/index.qmd`
  - `sections/wakefields/index.qmd`
  - `sections/geometry/index.qmd`
  - `sections/collisions/index.qmd`
  - `sections/partmatter/index.qmd`
  - `sections/optimiser/index.qmd`
  - `sections/sampler/index.qmd`
- chapter-local figures and examples where needed
- HTML feature toggle blocks for OPAL / OPALX specific content

Migration convention:

- content explicitly marked with `.feature-opalx` is OPALX-specific
- content not marked as OPALX defaults to OPAL content and should be wrapped in
  `.feature-opal` during migration

Render locally with:

```sh
quarto render /Users/adelmann/git/Manual/quarto --to html
```

Rendered output:

- `docs-quarto/index.html`
- `docs-quarto/sections/introduction/index.html`
- `docs-quarto/sections/control/index.html`
- `docs-quarto/sections/distribution/index.html`
- `docs-quarto/sections/track/index.html`

Appendices and standalone auxiliary pages are still outside the Quarto pilot.

This pilot does not replace the existing `Manual.asciidoc` build path.
