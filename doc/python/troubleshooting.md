---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
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
    version: 3.8.8
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

It's very important that you not have a file named `plotly.py` in the same directory as the Python script you're running, and this includes not naming the script itself `plotly.py`, otherwise importing `plotly` can fail with mysterious error messages.

Beyond this, most `import` problems or `AttributeError`s can be traced back to having multiple versions of `plotly` installed, for example once with `conda` and once with `pip`. It's often worthwhile to uninstall with both methods before following the [Getting Started](/python/getting-started) instructions from scratch with one or the other. You can run the following commands in a terminal to fully remove `plotly` before installing again:

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
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'renderers', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### VSCode Notebook, Nteract and Streamlit Problems

Plotly figures render in VSCode using a Plotly.js version bundled with the [vscode-python extension](https://code.visualstudio.com/docs/languages/python), and unfortunately it's often a little out of date compared to the latest version of the `plotly` module, so the very latest features may not work until the following release of the vscode-python extension. In any case, regularly upgrading your vscode-python extension to the latest version will ensure you have access to the greatest number of recent features.

The situation is similar for environments like Nteract and Streamlit: in these environments you will need a version of these projects that bundles a version Plotly.js that supports the features in the version of `plotly` that you are running.

### Orca Problems

> Note: as of `plotly` version 4.9, we recommend using [`kaleido`](https://github.com/plotly/Kaleido)
> instead of Orca for [static image export](/python/static-image-export/)

If you get an error message stating that the `orca` executable that was found is not valid, this may be because another executable with the same name was found on your system. Please specify the complete path to the Plotly-Orca binary that you downloaded (for instance in the Miniconda folder) with the following command:

`plotly.io.orca.config.executable = '/home/your_name/miniconda3/bin/orca'`
