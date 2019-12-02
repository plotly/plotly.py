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
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: Getting Started with Plotly for Python
    has_thumbnail: false
    language: python
    layout: base
    page_type: u-guide
    permalink: python/userguide/
    thumbnail: null
---

# Plotly for Python User Guide





<iframe width="900" height="800" frameborder="0" scrolling="no" src="https://plot.ly/~kevintest/21.embed"></iframe>



This user guide will provide an in-depth overview of the steps required to get your first `Plotly` graph up and running, as well as more specific and thorough guides on a few of our most popular graph types. Hopefully by the end of this user guide you will have a good idea of how Plotly graphs are defined and constructed, and be on your way to creating amazing data visualizations of your own.


### What is the Python API for Plotly?



As you may know, Plotly is software written to enable users to easily create beautiful interactive plots and graphs to visualize data. All plots are generated using our [javascript library](https://plot.ly/javascript), but we have multiple API's that will allow us to create these plots in our preferred language. Thus the purpose of the Python API is to allow users to generate these plots within a Python environment, including IPython Notebooks!


### User Guide Sections:



The user guide is split into the following sections:

- Section 0. [Getting Started with Plotly](https://plot.ly/python/getting_started)
- Section 1. [Line and Scatter Plots](https://plot.ly/python/line-and-scatter-plots-tutorial)
- Section 2. [Bar Charts](https://plot.ly/python/bar-charts-tutorial)
- Section 3. [Bubble Charts](https://plot.ly/python/bubble-charts-tutorial)
- Section 4. [Histograms and Box Plots](https://plot.ly/python/histograms-and-box-plots-tutorial)
- Section 5. [Heatmaps, Contours and 2D Histograms](https://plot.ly/python/heatmaps-contours-and-2dhistograms-tutorial)
- Section 6. [Converting Matplotlib Figures to Plotly](https://plot.ly/python/matplotlib-to-plotly-tutorial)
- Section 7. [Streaming API](https://plot.ly/python/intro_streaming)
- [Appendix A: Getting Started with Python](https://plot.ly/python/python-tutorial)


### Want to know what's going on at Plotly?

* Follow us on twitter:
[@plotlygraphs](https://twitter.com/plotlygraphs)

### Issues or suggestions for the user guide?

* Let us know at: [Plotly Community Support](http://community.plot.ly)

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install publisher --upgrade
import publisher
publisher.publish(
    'user-g.ipynb', 'python/userguide//', 'Getting Started Plotly for Python',
    'Getting Started with Plotly for Python',
    title = 'Getting Started Plotly for Python',
    thumbnail='', language='python',
    layout='user-guide', has_thumbnail='false')
```

```python

```
