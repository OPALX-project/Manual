# OPAL(X) Manual

This repository now hosts the Quarto version of the OPAL(X) manual.

The published manual is deployed to:

https://opalx-project.github.io/Manual/

The legacy AsciiDoc manual has been moved to the separate repository:

https://github.com/OPALX-project/Manual-old

and is intended to publish at:

https://opalx-project.github.io/Manual-old/

## Build

Render the Quarto manual with:

```sh
quarto render ./quarto --to html
```

The rendered site is written to `quarto/docs-quarto/` and deployed by the
GitHub Pages workflow.
