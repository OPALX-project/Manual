# OPAL User Manual for Version 2

## Introduction

Since _OPAL_ version 2 the manual is maintained in the Wiki of this project:

https://gitlab.psi.ch/OPAL/Manual-2.2/wikis/home

The Wiki pages are written in Asciidoc and thus can be converted to other formats 
like PDF or HTML. The Asciidoc support in Gitlab is a bit limited. One main issue
is, that links to anchors - i.e. most references - are not working. We hope that
this issue will fixed in the near future. Another problem is that latexmath is not
correctly implemented in Gitlab. 

There are some "home-made" problems as well. In the Wiki each chapter is a separate 
document with a header containing a table of content, a "back to home" link and some
other stuff. These lines have to be removed for the rendering into *one* PDF document.

The script `asciidoc2pdf` can be used to render the Wiki Manual into PDF. The script
requires `asciidoctor`, TeX and `dblatex`.


## Converting to PDF

Assuming `asciidoc2pdf` is in your `PATH`:
```
git clone git@gitlab.psi.ch:OPAL/Manual-2.1.wiki.git
cd Manual-2.1.wiki
asciidoc2pdf home.asciidoc
```

## Editing the manual

> *Attention:* Do not edit the files in the Wiki itself. Changes must be done to
the files in the repository!

The Wiki is a mirror of the repository in this project. The mirror process is 
triggered by Gitlab after you commit changes to the repository. For this reason 
you shouldn't change the Wiki itself.

Changes to the Wiki follows the same rules as for code changes:
1. file an issue, document what you want to change
2. create a merge-request, set target branch to `master`
3. edit inside the branch created for this merge-request
4. resolve the merge-request and select at least two aprovers
5. wait till the merge-request has been aproved, if more changes are required, go back to 3.
6. merge your changes into the `master`branch and delete the branch of the merge-request

## Writing guidelines

To get good results for PDF output, you should follow some simple rules.


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

