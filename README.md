# OPAL User Manual

## Introduction

Since vesion 2 the _OPAL_ manual is written in Asciidoc. AsciiDoc is a human-readable document format, semantically equivalent to DocBook XM. Documents written in Asciidoc can be converted to other formats like HTML, PDF, EPUB and others.

For more information about Asciidoc see

* https://en.wikipedia.org/wiki/AsciiDoc
* http://asciidoc.org
* https://asciidoctor.org

In the project OPAL/Documentation/asciidoc2x> we provide scripts to translate the _OPAL_ manual to HTML and PDF. Instructions about how to install these scripts and their requirements are documented in the projects README.

## Translating the manual to HTML and PDF

Assuming the scripts of the project OPAL/Documentation/asciidoc2x> are installed and in you `PATH`, change directory to a clone of the manual and run.
```
asciidoc2html
```
to convert to HTML and
```
asciidoc2pdf
```
to convert to PDF.

The hole procedure is something like
* clone the _OPAL_ manual with
  ```
  git clone git@gitlab.psi.ch:OPAL/documentation/manual.git
  ```
  or
  ```
  git clone https://gitlab.psi.ch/OPAL/documentation/manual.git
  ```
* change directory to cloned repository
* translate to HTML
  ```
  asciidoc2html
  ```
  translate to PDF
  ```
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
