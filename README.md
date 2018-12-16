# plotly.py

## Quickstart

`pip install plotly`

Inside [Jupyter notebook](https://jupyter.org/install):
```python
import plotly.graph_objs as go
fig = go.FigureWidget()
# Display an empty figure
fig

# Add a scatter chart
fig.add_scatter(y=[2, 1, 4, 3])
# Add a bar chart
fig.add_bar(y=[1, 4, 3, 2])
# Add a title
fig.layout.title = 'Hello FigureWidget'
```

See the [Python documentation](https://plot.ly/python/) for more examples.

Read about what's new in [plotly.py v3](https://medium.com/@plotlygraphs/introducing-plotly-py-3-0-0-7bb1333f69c6)

## Overview
[plotly.py](https://plot.ly/d3-js-for-python-and-pandas-charts/) is an interactive, open-source, and browser-based graphing library for Python :sparkles:

Built on top of [plotly.js](https://github.com/plotly/plotly.js), `plotly.py` is a high-level, declarative charting library. plotly.js ships with over 30 chart types, including scientific charts, 3D graphs, statistical charts, SVG maps, financial charts, and more.

`plotly.py` is [MIT Licensed](LICENSE.txt). Plotly graphs can be viewed in Jupyter notebooks, standalone HTML files, or hosted online on [plot.ly](https://plot.ly).

[Contact us](https://plot.ly/products/consulting-and-oem/) for Plotly.js consulting, dashboard development, application integration, and feature additions. Sharing your graphs online or in dashboards? Consider a [plot.ly subscription](https://plot.ly/products/cloud).

<p align="center">
    <a href="https://plot.ly/python" target="_blank">
    <img src="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/plotly_2017.png">
</a></p>

***

- [Online Documentation](https://plot.ly/python)
- [Contributing](contributing.md)
- [Changelog](CHANGELOG.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Version 3 Migration Guide](migration-guide.md)
- [New! Announcing Dash](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503)
- [Community](https://community.plot.ly/c/api/python)

***

## Installation of plotly.py Version 3
To install plotly.py and enable Jupyter or Jupyter Lab support, run:
```
pip install plotly==3.1.1
pip install "notebook>=5.3" "ipywidgets>=7.2"  # only necessary for Jupyter Notebook environments
```

If you're using older versions of `notebook` or `ipywidgets` you may need to manually activate the widget extensions (this should not be needed for `notebook>=5.3` and `ipywidgets>=7.2`)

```
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension enable --py plotlywidget --sys-prefix
```

In addition, to add JupyterLab support run the following commands

```
pip install jupyterlab==0.33

# Avoid "JavaScript heap out of memory" errors during extension installation
# (OS X/Linux)
export NODE_OPTIONS=--max-old-space-size=4096
# (Windows)
set NODE_OPTIONS=--max-old-space-size=4096

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.36 --no-build

# FigureWidget support
jupyter labextension install plotlywidget@0.2.1  --no-build

# offline iplot support
jupyter labextension install @jupyterlab/plotly-extension@0.16  --no-build

# Build extensions (must be done to activate extensions since --no-build is used above)
jupyter lab build
```

If you're migrating from plotly.py version 2, please check out the [migration guide](migration-guide.md)

## Copyright and Licenses
Code and documentation copyright 2018 Plotly, Inc.

Code released under the [MIT license](LICENSE.txt).

Docs released under the [Creative Commons license](https://github.com/plotly/documentation/blob/source/LICENSE).
