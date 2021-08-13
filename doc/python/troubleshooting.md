---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
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
    version: 3.7.7
  plotly:
    description: How to troubleshoot import and rendering problems in Plotly with
      Python.
    display_as: file_settings
    language: python
    layout: base
    name: Troubleshooting
    order: 27
    page_type: u-guide
    permalink: python/troubleshooting/
    thumbnail: thumbnail/modebar-icons.png
---

<!-- #region -->
### Version Problems

In order to follow the examples in this documentation site, you should have the latest version of `plotly` installed (5.x), as detailed in the [Getting Started](/python/getting-started) guide. This documentation (under https://plotly.com/python) is compatible with `plotly` version 4.x but *not* with version 3.x, for which the documentation is available under https://plotly.com/python/v3. In general you must also have the correct version of the underlying Plotly.js rendering engine installed, and the way to do that depends on the environment in which you are rendering figures: Dash, Jupyter Lab or Classic Notebook, VSCode etc. Read on for details about troubleshooting `plotly` in these environments.

### Import Problems

Most `import` problems or `AttributeError`s can be traced back to having multiple versions of `plotly` installed, for example once with `conda` and once with `pip`. It's often worthwhile to uninstall with both methods before following the [Getting Started](/python/getting-started) instructions from scratch with one or the other. You can run the following commands in a terminal to fully remove `plotly` before installing again:

```bash
$ conda uninstall plotly
$ pip uninstall plotly
```

> Problems can also arise if you have a file named `plotly.py` in the same directory as the code you are executing.

### Dash Problems

If you are encountering problems using `plotly` with [Dash](https://dash.plotly.com/) please first ensure that you have upgraded `dash` to the latest version, which will automatically upgrade `dash-core-components` to the latest version, ensuring that Dash is using an up-to-date version of the Plotly.js rendering engine for `plotly`. If this does not resolve your issue, please visit our [Dash Community Forum](https://community.plotly.com/) and we will be glad to help you out.

This is an example of a `plotly` graph correctly rendering inside `dash`:
<!-- #endregion -->

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'renderers', width='100%', height=630)
```

<!-- #region -->
### JupyterLab Problems

In order to use `plotly` in JupyterLab, you *must have the `jupyterlab-plotly` extension installed* as detailed in the [Getting Started guide](/python/getting-started). When you install `plotly`, this extension is automatically made available to any JupyterLab 3.x installation in the same Python environment. 

To list your current extensions, run the following command in a terminal shell **from the same environment as JupyterLab is launched**:

```bash
# Check that jupyterlab-plotly is installed
$ jupyter labextension list
```

Please note that the *extension version matters*: the extension versions in the [Getting Started](/python/getting-started) guide match the version of `plotly` at the top of the guide and so they should be installed together. Note also that these extensions are meant to work with JupyterLab 1 or above but not 0.x.

If automatic installation of the extension is not working in your environment, or if you are using JupyterLab 1.x or 2.0, you may install it manually using the following command, which requires `node` to be installed.

```bash
# Manually reinstall the extension
$ jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyterlab-plotly
```

If you have [installed additional python environments](https://ipython.readthedocs.io/en/stable/install/kernel_install.html) (or kernels) to use with JupyterLab, or if you are using a centrally hosted JupyterLab installation, you need to make sure that the extensions are installed in the python environment used to launch JupyterLab (the "server" environment). If you accidentally installed the extensions (and run the command above) in one of the additional python environments ("processing" environments), then it is possible for the command above to list the correct extensions but for them to not be available in the JupyterLab front-end you have loaded in your browser. To check if this is the problem, you can [look at the active extension list through your browser via the JupyterLab Extension Manager](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#using-the-extension-manager), which will always list the extensions in the "server" environment. To summarize: if you use JupyterLab with multiple python environments, the extensions must be installed in the "server" environment, and the plotly python library must be installed in each "processing" environment that you intend to use.

> Note that version 4.14.3 of `plotly` or earlier needed two extensions (`jupyterlab-plotly` and `plotlywidget`) to be installed manually running, and that `plotlywidget` requires `@jupyter-widgets/jupyterlab-manager` to be installed:

```bash
# Instructions for `plotly` 4.x
$ jupyter labextension install jupyterlab-plotly plotlywidget @jupyter-widgets/jupyterlab-manager 
```

If you have the correct version(s) of the extension(s) installed and active in your active JupyterLab sessions and are still seeing problems, the issue may clear up if you rebuild JupyterLab. This shouldn't be required in principle but some users have resolved their issues this way. To rebuild JupyterLab, shut down JupyterLab and run the following command in a terminal shell **from the same environment as JupyterLab was launched**:

```bash
# rebuilding JupyterLab
$ jupyter lab build
```

To uninstall your Plotly extensions prior to reinstalling them, run the following commands in a terminal shell before reinstalling them by following the instructions in the [Getting Started guide](/python/getting-started):

```bash
# uninstalling extensions to reinstall
$ jupyter labextension uninstall jupyterlab-plotly
$ jupyter labextension uninstall plotlywidget
```

If you run into "out of memory" problems while installing the extensions or building JupyterLab, try running these commands before running `jupyter labextension install`...

```bash
# Avoid "JavaScript heap out of memory" errors during extension installation
# (OS X/Linux)
export NODE_OPTIONS=--max-old-space-size=4096
# (Windows)
set NODE_OPTIONS=--max-old-space-size=4096
```

...and these commands afterwards.

```bash
# Unset NODE_OPTIONS environment variable
# (OS X/Linux)
unset NODE_OPTIONS
# (Windows)
set NODE_OPTIONS=
```

### Jupyter Classic Notebook Problems

The classic Jupyter Notebook (i.e. launched with `jupyter notebook`) sometimes suffers from a problem whereby if you close the window and reopen it, your plots render as blank spaces.

The easiest solution is to force the `notebook` renderer to reload by calling `fig.show("notebook")` instead of just `fig.show()`.

If this problem is recurrent, you may safely run the following code in a Notebook (not in JupyterLab!) at any time and it should restore your figures (for example, you may put it at the top of your notebook for easy access):

```python
import plotly.io as pio
pio.renderers.default='notebook'
```

As a last resort, you can "Restart & Clear Output" from the Kernel menu and rerun your notebook.

<!-- #endregion -->

### VSCode Notebook, Nteract and Streamlit Problems

Plotly figures render in VSCode using a Plotly.js version bundled with the [vscode-python extension](https://code.visualstudio.com/docs/languages/python), and unfortunately it's often a little out of date compared to the latest version of the `plotly` module, so the very latest features may not work until the following release of the vscode-python extension. In any case, regularly upgrading your vscode-python extension to the latest version will ensure you have access to the greatest number of recent features.

The situation is similar for environments like Nteract and Streamlit: in these environments you will need a version of these projects that bundles a version Plotly.js that supports the features in the version of `plotly` that you are running.

### Orca Problems

> Note: as of `plotly` version 4.9, we recommend using [`kaleido`](https://github.com/plotly/Kaleido)
> instead of Orca for [static image export](/python/static-image-export/)

If you get an error message stating that the `orca` executable that was found is not valid, this may be because another executable with the same name was found on your system. Please specify the complete path to the Plotly-Orca binary that you downloaded (for instance in the Miniconda folder) with the following command:

`plotly.io.orca.config.executable = '/home/your_name/miniconda3/bin/orca'`
