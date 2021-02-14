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
    description: How to dig into and learn more about the figure data structure.
    display_as: file_settings
    language: python
    layout: base
    name: Introspecting Figures
    order: 36
    page_type: u-guide
    permalink: python/figure-introspection/
    thumbnail: thumbnail/violin.jpg
---

### The Figure Lifecycle

As explained in the [Figure Data Structure documentation](/python/figure-structure/), when building a figure object with Plotly.py, it is not necessary to populate every possible attribute. At render-time, figure objects (whether generated via [Plotly Express](/python/plotly-express/) or [Graph Objects](/python/graph-objects/)) are passed from Plotly.py to [Plotly.js](/javascript/), which is the Javascript library responsible for turning JSON descriptions of figures into graphical representations.

As part of this rendering process, Plotly.js will determine, based on the attributes that have been set, which other attributes require values in order to draw the figure. Plotly.js will then apply either static or dynamic defaults to all of the remaining required attributes and render the figure. A good example of a static default would be the text font size: if unspecified, the default value is always the same. A good example of a dynamic default would be the range of an axis: if unspecified, the default will be computed based on the range of the data in traces associated with that axis.


### Introspecting Plotly Express Figures

Figure objects created by [Plotly Express](/python/plotly-express/) have a number of attributes automatically set, and these can be introspected using the Python `print()` function, or in JupyterLab, the special `fig.show("json")` renderer, which gives an interactive drilldown interface with search:

```python
import plotly.express as px

fig = px.scatter(x=[10, 20], y=[20, 10], height=400, width=400)
fig.show()
print(fig)
```

We can learn more about the attributes Plotly Express has set for us with the Python `help()` function:

```python
help(fig.data[0].__class__.mode)
```

### Accessing Javascript-Computed Defaults

_new in 4.10_

The `.full_figure_for_development()` method provides Python-level access to the default values computed by Plotly.js. This method requires [the Kaleido package](/python/static-image-export/), which is easy to install and also used for [static image export](/python/static-image-export/).

By way of example, here is an extremely simple figure created with [Graph Objects](/python/graph-objects/) (although it could have been made with [Plotly Express](/python/plotly-express/) as well just like above) where we have disabled the default template for maximum readability. Note how in this figure the text labels on the markers are clipped, and sit on top of the markers.

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(
        mode="markers+text",
        x=[10,20],
        y=[20, 10],
        text=["Point A", "Point B"]
    )],
    layout=dict(height=400, width=400, template="none")
)
fig.show()
```

Let's print this figure to see the very small JSON object that is passed to Plotly.js as input:

```python
print(fig)
```

Now let's look at the "full" figure after Plotly.js has computed the default values for every necessary attribute.

> Heads-up: the full figure is quite long and intimidating, and this page is meant to help demystify things so **please read on**!

Please also note that the `.full_figure_for_development()` function is really meant for interactive learning and debugging, rather than production use, hence its name and the warning it produces by default, which you can see below, and which can be suppressed with `warn=False`.

```python
full_fig = fig.full_figure_for_development()
print(full_fig)
```

As you can see, Plotly.js does a lot of work filling things in for us! Let's look at the examples described at the top of the page of static and dynamic defaults. If we look just at `layout.font` and `layout.xaxis.range` we can see that the static default font size is 12 and that the dynamic default range is computed to be a bit beyond the data range which was 10-20:

```python
print("full_fig.layout.font.size: ", full_fig.layout.font.size)
print("full_fig.layout.xaxis.range: ", full_fig.layout.xaxis.range)
```

### Learning About Attributes


What else can we use this `full_fig` for? Let's start by looking at the first entry of the `data`

```python
print(full_fig.data[0])
```

We see that this is an instance of `go.Scatter` (as expected, given the input) and that it has an attribute we've maybe never heard of called `cliponaxis` which by default seems to be set to `True` in this case. Let's find out more about this attribute using the built-in Python `help()` function

```python
help(go.Scatter.cliponaxis)
```

Aha!  This explains why in our original figure above, the text was cut off by the edge of the plotting area! Let's try forcing that to `False`, and let's also use the attribute `textposition` which we see in the full figure is by default set to `"middle center"` to get our text off of our markers:

```python
fig.update_traces(cliponaxis=False, textposition="top right")
fig.show()
```

We can use this technique (of making a figure, and querying Plotly.js for the "full" version of that figure, and then exploring the attributes that are automatically set for us) to learn more about the range of possibilities that the figure schema makes available. We can drill down into `layout` attributes also:

```python
help(go.layout.XAxis.autorange)
```

### More about Layout

In the figure we introspected above, we had added [a `scatter` trace](/python/line-and-scatter/), and Plotly.js automatically filled in for us the `xaxis` and `yaxis` values of that trace object to be `x` and `y`, and then also filled out the corresponding `layout.xaxis` and `layout.yaxis` objects for us, complete with their [extensive set of defaults for gridlines, tick labels and so on](/python/axes/).

If we create a figure with [a `scattergeo` trace](/python/scatter-plots-on-maps/) instead, however, Plotly.js will fill in a totally different set of objects in `layout`, corresponding to [a `geo` subplot, with all of its defaults for whether or not to show rivers, lakes, country borders, coastlines etc](https://plotly.com/python/map-configuration/).

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scattergeo(
        mode="markers+text",
        lat=[10, 20],
        lon=[20, 10],
        text=["Point A", "Point B"]
    )],
    layout=dict(height=400, width=400,
                margin=dict(l=0,r=0,b=0,t=0),
                template="none")
)
fig.show()
full_fig = fig.full_figure_for_development()
print(full_fig)
```

If I then set `showrivers=True` and re-query the full figure, I see that new keys have appeared in the `layout.geo` object for `rivercolor` and `riverwidth`, showing the dynamic nature of these defaults.

```python
fig.update_geos(showrivers=True)
full_fig = fig.full_figure_for_development()
print(full_fig.layout.geo)
```

### Reference

You can learn more about [all the available attributes in the plotly figure schema](/python/reference/) (and read about its [high-level structure](/python/figure-structure/)) or about [all the classes and functions in the `plotly` module](/python-api-reference/).

```python

```
