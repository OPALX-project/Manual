# OPAL User Manual for Version 2.1

## Introduction

Since _OPAL_ version 2 the manual is maintained in the Wiki of this project:

https://gitlab.psi.ch/OPAL/Manual-2.1/wikis/home

The Wiki pages are written in Asciidoc and thus can be converted to other formats 
like PDF or HTML. The Aciidoc support in Gitlab is a bit limited. One main issue
is, that links to anchors - i.e. most references - are not working. Another problem
is that latexmath is not correctly implemented in Gitlab. 

There are some "home-made" problems as well. In the Wiki each chapter is a separate 
document with a header containing a table of content, a "back to home" link and some
other stuff. These lines have to be removed for the rendering into *one* PDF document.

The script `asciidoc2pdf` can be used to render the Wiki Manual into PDF. The script
requires `asciidoctor`, TeX and `dblatex`.

For the time being we use another master document named `home.adoc` for PDF rendering.
In the futuer we may adapt the master document of the Wiki (`home.asciidoc`) and
`asciidoc2pdf` in a way which makes `home.adoc`obsolete`.

## Usage

Assuming `asciidoc2pdf` is in your `PATH`:
```
git clone git@gitlab.psi.ch:OPAL/Manual-2.1.wiki.git
cd Manual-2.0.wiki
asciidoc2pdf home.asciidoc
```

## Guidlines

To get good results for PDF ouput, you should follow some simple rules.


### Chapters and section

* Use one-line titles
* Include the base file name in the anchor name.
* For cross-chapter references use the form `link:FILENAME#ANCHOR[TEXT]`. This is required for the Wiki where chapter a standalone documents.

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