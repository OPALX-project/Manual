# OPAL User Manual

This repository hosts the Quarto version of the historical OPAL manual. It is
retained for users of old OPAL and is no longer maintained.

The maintained successor manual is available at:

https://amas.pages.psi.ch/opal/

The published manual is deployed to:

https://opalx-project.github.io/opal-manual/

The equivalent AsciiDoc manual is archived and not publicly available anymore.

## Build

Render the Quarto manual with:

```sh
quarto render . --to html
```

The rendered site is written to `docs-quarto/` and deployed by the GitHub Pages
workflow.
