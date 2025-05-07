# plotly.py

<table>
    <tr>
        <td>Latest Release</td>
        <td>
            <a href="https://pypi.org/project/plotly/"/>
            <img src="https://badge.fury.io/py/plotly.svg"/>
        </td>
    </tr>
    <tr>
        <td>User forum</td>
        <td>
            <a href="https://community.plotly.com/"/>
            <img src="https://img.shields.io/badge/help_forum-discourse-blue.svg"/>
        </td>
    </tr>
    <tr>
        <td>PyPI Downloads</td>
        <td>
            <a href="https://pepy.tech/project/plotly"/>
            <img src="https://pepy.tech/badge/plotly/month"/>
        </td>
    </tr>
    <tr>
        <td>License</td>
        <td>
            <a href="https://opensource.org/licenses/MIT"/>
            <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/>
        </td>
    </tr>
</table>

<div align="center">
  <a href="https://dash.plotly.com/project-maintenance">
    <img src="https://dash.plotly.com/assets/images/maintained-by-plotly.png" width="400px" alt="Maintained by Plotly">
  </a>
</div>

## Quickstart

`pip install plotly`

```python
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.show()
```

See the [Python documentation](https://plotly.com/python/) for more examples.

## Overview

[plotly.py](https://plotly.com/python/) is an interactive, open-source, and browser-based graphing library for Python :sparkles:

Built on top of [plotly.js](https://github.com/plotly/plotly.js), `plotly.py` is a high-level, declarative charting library. plotly.js ships with over 30 chart types, including scientific charts, 3D graphs, statistical charts, SVG maps, financial charts, and more.

`plotly.py` is [MIT Licensed](https://github.com/plotly/plotly.py/blob/main/LICENSE.txt). Plotly graphs can be viewed in Jupyter notebooks, standalone HTML files, or integrated into [Dash applications](https://dash.plotly.com/).

[Contact us](https://plotly.com/consulting-and-oem/) for consulting, dashboard development, application integration, and feature additions.

<p align="center">
    <a href="https://plotly.com/python/" target="_blank">
    <img src="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/plotly_2017.png">
</a></p>

---

- [Online Documentation](https://plotly.com/python/)
- [Contributing to plotly](https://github.com/plotly/plotly.py/blob/main/CONTRIBUTING.md)
- [Changelog](https://github.com/plotly/plotly.py/blob/main/CHANGELOG.md)
- [Code of Conduct](https://github.com/plotly/plotly.py/blob/main/CODE_OF_CONDUCT.md)
- [Community forum](https://community.plotly.com)

---

## Installation

plotly.py may be installed using pip

```
pip install plotly
```

or conda.

```
conda install -c conda-forge plotly
```

### Jupyter Widget Support

For use as a Jupyter widget, install `jupyter` and `anywidget`
packages using `pip`:

```
pip install jupyter anywidget
```

or `conda`:

```
conda install jupyter anywidget
```

### Static Image Export

plotly.py supports [static image export](https://plotly.com/python/static-image-export/),
using either the [`kaleido`](https://github.com/plotly/Kaleido)
package (recommended, supported as of `plotly` version 4.9) or the [orca](https://github.com/plotly/orca)
command line utility (legacy as of `plotly` version 4.9).

#### Kaleido

The [`kaleido`](https://github.com/plotly/Kaleido) package has no dependencies and can be installed
using pip

```
pip install -U kaleido
```

or conda

```
conda install -c conda-forge python-kaleido
```

### Extended Geo Support

Some plotly.py features rely on fairly large geographic shape files. The county
choropleth figure factory is one such example. These shape files are distributed as a
separate `plotly-geo` package. This package can be installed using pip...

```
pip install plotly-geo==1.0.0
```

or conda

```
conda install -c plotly plotly-geo=1.0.0
```

`plotly-geo` can be found on Github at https://github.com/plotly/plotly-geo.

## Copyright and Licenses

Code and documentation copyright 2019 Plotly, Inc.

Code released under the [MIT license](https://github.com/plotly/plotly.py/blob/main/LICENSE.txt).

Docs released under the [Creative Commons license](https://github.com/plotly/documentation/blob/source/LICENSE).

