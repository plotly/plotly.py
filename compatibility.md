#Migrating from Plotly's Python API, 0.5 to 1.0:

##Backwards Compatibility

* import statements and module locations have changed
* depreciated methods

### careful, modules may have shifted during flight

The functionality in within `plotly.plotly` has been moved to two locations:

* plotly.plotly
* plotly.tools

Read on to see how this might affect you!

### changed/moved/depreciated functionality

Some functionality has moved, or has been altogether deleted. Here's the
rundown of what got effected:

| Name                       | Action         |
| ------------------------   | -------------- |
| `plotly.embed()`           | moved          |
| `plotly.display()`         | depreciated    |
| `plotly.signup()`          | depreciated    |
| `plotly.plotly()`          | depreciated    |
| `plotly.plotly.ion()`      | depreciated    |
| `plotly.plotly.ioff()`     | depreciated    |
| `plotly.plotly.plot()`     | moved          |
| `plotly.plotly.iplot()`    | moved          |
| `plotly.plotly.layout()`   | depreciated    |
| `plotly.plotly.style()`    | depreciated    |
| `plotly.stream.init()`     | depreciated    |
| `plotly.stream.write()`    | moved          |
| `plotly.stream.close()`    | moved          |


### `plot` and `iplot` call signatures:


```python
# old way to make a plot
import plotly
plotly.plot(data, layout=layout, **plot_options)
plotly.iplot(data, layout=layout, **plot_options)
```

```python
# new way to make a plot
import plotly.plotly as py
py.plot(data_or_figure, **plot_options)
py.iplot(data_or_figure, **plot_options)
```




