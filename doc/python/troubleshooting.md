---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.6.8
  plotly:
    description: How to troubleshoot import and rendering problems in Plotly with
      Python.
    display_as: file_settings
    language: python
    layout: base
    name: Troubleshooting
    order: 26
    page_type: u-guide
    permalink: python/troubleshooting/
    thumbnail: thumbnail/modebar-icons.png
---

<!-- #region -->
### Version Problems

In order to follow the examples in this documentation, you should have the latest version of `plotly` installed (4.x), as detailed in the [Getting Started](/python/getting-started) guide. This documentation (under https://plot.ly/python) is incompatible with `plotly` version 3.x, for which the documentation is available under https://plot.ly/python/v3.

### Import Problems

Most `import` problems or `AttributeError`s can be traced back to having multiple versions of `plotly` installed, for example once with `conda` and once with `pip`. It's often worthwhile to uninstall with both methods before following the [Getting Started](/python/getting-started) instructions from scratch with one or the other. You can run the following commands in a terminal to fully remove `plotly` before installing again:

```bash
$ conda uninstall plotly
$ pip remove plotly
```

### Jupyter Notebook Classic Problems

The classic Jupyter Notebook (i.e. launched with `jupyter notebook`) sometimes suffers from a problem whereby if you close the window and reopen it, your plots render as blank spaces. The easiest solution is to run "Restart & Clear Output" from the Kernel menu and rerun your notebook.

If rerunning your notebook is prohibitive, you may safely run the following code in a Notebook (not in JupyterLab!) at any time and it should restore your figures:

```python
import plotly.io as pio
pio.renderers.default='notebook'
```

### JupyterLab Problems

In order to use `plotly` in JupyterLab, you *must have the extensions installed* as detailed in the [Getting Started guide](/python/getting-started). Please note that the *extension version matters*: the extension versions in the [Getting Started](/python/getting-started) guide match the version of `plotly` at the top of the guide and so they should be installed together. Note also that these extensions are meant to work with JupyterLab 1.x and not 0.x.

If you are having problems in JupyterLab, a good first step is to check that you have the extensions installed by running uninstall/reinstall the extensions.

To list your current extensions, run the following command in a terminal shell:

```bash
$ jupyter labextension list
```

To uninstall your `plotly` extensions, run the following commands in a terminal shell before reinstalling them by following the instructions in the [Getting Started guide](/python/getting-started):

```bash
$ jupyter labextension uninstall jupyterlab-plotly
$ jupyter labextension uninstall plotlywidget
```
<!-- #endregion -->

```python

```
