# OPAL User Manual for Version 2.0

## Introduction

The _OPAL_ manual is written in Asciidoc and can be converted to other formats 
like PDF or HTML.

The script `asciidoc2html` can be used to render the manual into HTML. The script
requires `asciidoctor-katex` and `Node.js`.

The script `asciidoc2pdf` can be used to render the manual into PDF. The script
requires `asciidoctor`, TeX and `dblatex`.

## Usage

Assuming `asciidoc2pdf` is in your `PATH`:
```
git clone git@gitlab.psi.ch:OPAL/documentation/manual.git
cd manual
asciidoc2pdf
```

## Guidlines

To get good results for HTML and PDF ouput, you should follow some simple rules.


### Chapters and section

* Use one-line titles
* Include the base file name in the anchor name.
* For cross-chapter references use the form `link:FILENAME#ANCHOR[TEXT]`. 
  This is required for the Wiki where each chapter is a Wiki page.

Examples:
```
[[chp.introduction]]
== Introduction
```
```
[[sec.introduction.aim-of-opal-and-history]]
=== Aim of _OPAL_ and History
```
```
link:fieldsolvers#chp.fieldsolvers[Field Solver]
```

### Figures

* Prefix anchor names with `fig_`.
* Use inline anchors of the form `[#...]`.
* Define width for PDF output with `scaledwidth`.
* Define width for HTML (Wiki) output with `TO BE DEFINED`.

Example:
```
[#fig_walldrift]
.Parallel efficiency and particles pushed per latexmath:[\mu s] as a function of cores
image::figures/drift2c1.png[scaledwidth=10cm]
```

*NOTE*:: 
For some unknown reasons dots in inline anchor names cannot be used. Referencing them doesn't work as expected!

### Tables

* Column width must be specified.
* Use relative column width.
 
Example:
```
[#tab_commands]
[cols="<1,<4",options="header",]
|=======================================================================
|Command |Purpose
```

### LaTexMath

* inline math must be written on one line! Otherwise `asciidoc2pdf` will fail.
