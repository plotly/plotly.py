# Documentation of plotly.py

## Introduction: structure and required packages

The `doc` directory contains the source files of the documentation of plotly.py.
It is composed of two parts:

- inside the [`python/` directory](python), tutorials corresponding to https://plot.ly/python/
- inside the [`apidoc/` directory](apidoc), configuration files for generating
  the API reference documentation (hosted on https://plot.ly/python-api-reference/)

Python packages required to build the doc are listed in
[`requirements.txt`](requirements.txt) in the `doc` directory.

## Tutorials (`python` directory)

Each tutorial is a markdown (`.md`) file, which can be opened in the Jupyter
notebook or in Jupyterlab by installing [jupytext](https://jupytext.readthedocs.io/en/latest/install.html).

For small edits (e.g., correcting typos) to an existing tutorial, you can simply click on the "edit this
page on Github" link at the top right of the page (e.g. clicking on this link
on https://plot.ly/python/bar-charts/ will take you to
https://github.com/plotly/plotly.py/edit/doc-prod/doc/python/bar-charts.md,
where you can edit the page on Github).

For more important edits where you need to run the notebook to check the output,
clone the repository and setup an environment as described in the [main
contributing notes](../contributing.md). If you're writing documentation at the
same time as you are developing a feature, make sure to install with editable
install (`pip install -e`, as described in [main
contributing notes](../contributing.md)), so that you only need to restart
the Jupyter kernel when you have changed the source code of the feature.

### Branches

Two different cases exist, whether you are documenting a feature already
released, or which has just been included but not yet released.

- Case of an already released feature: your changes can be deployed to the
  documentation website as soon as they have been merged, and you should start
  your branch off the `doc-prod` branch and open your pull request against this
  `doc-prod` branch.
- Case of a new (not released yet) feature: start your branch / pull request
  against the `master` branch. `master` and `doc-prod` will be synchronized at
  release time, so that the documentation of the feature is only deployed when
  it is available in a released version of `plotly.py`.

### Guidelines

We try to write short, standalone and (almost) self-explaining examples. Most
examples should focus on a single feature.

Checklist

- Each example should have a clear title (titles are used for the navigation
  bar and indexed by search engines)
- Package imports should be called in the same cell as the example, so that it
  is possible to copy-paste a single cell to reproduce the example.
- Variable names should be consistent with other examples, for example use
  `fig` for a `Figure` object, `df` for a pandas dataframe, etc.
- Examples should not be too long to execute (typically < 10s), since the doc is
  built as part of the continuous integration (CI) process. Examples taking
  longer to execute should be discussed in a new issue to decide whether they
  can be accepted.

### Build process

Run `make` to build html pages for the tutorials. This uses `jupytext` to
execute the notebooks and `nbconvert` to convert notebook files to static html
pages. Note that the CI will build the doc, so you don't have to build it
yourself, it is enough to check that the markdown file runs correctly in
Jupyter.

The output of the `Makefile` is stored by CI in the `built` branch of the `plotly.py-docs` repo which is then used by the `documentation` repo to generate https://plot.ly/python.

## API reference documentation (`apidoc` directory)

We use [sphinx](http://www.sphinx-doc.org/en/master/) and its [`autodoc`
extension](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
in order to generate the documentation of the API. Sphinx uses the [reST markup
language](https://www.sphinx-doc.org/en/2.0/usage/restructuredtext/basics.html).

Run `make html` inside `apidoc` to build the API doc in the `_build/html`
directory.

Lists of objects to be documented are found in files corresponding to
submodules, such as [`plotly.express.rst`](plotly.express.rst). When a new
object is added to the exposed API, it needs to be added to the corresponding
file to appear in the API doc.

Other files

- `css` files are found in `_static`
- Template files are found in `_templates`. `.rst` templates describe how the
  autodoc of the different objects should look like.
