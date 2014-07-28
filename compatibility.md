#Migrating from Plotly's Python API, 0.5 to 1.0:

##Backwards Compatibility

* import statements and module locations have changed
* deprecated methods

### careful, modules may have shifted during flight

The functionality in within `plotly.plotly` has been moved to two locations:

* plotly.plotly
* plotly.tools

Read on to see how this might affect you!

### changed/moved/deprecated functionality

Some functionality has moved, or has been altogether deleted. Here's the
rundown of what got effected:

| Name                       | Action         |
| ------------------------   | -------------- |
| `plotly.embed()`           | moved          |
| `plotly.display()`         | deprecated    |
| `plotly.signup()`          | deprecated    |
| `plotly.plotly()`          | deprecated    |
| `plotly.plotly.ion()`      | deprecated    |
| `plotly.plotly.ioff()`     | deprecated    |
| `plotly.plotly.plot()`     | moved/changed  |
| `plotly.plotly.iplot()`    | moved/changed  |
| `plotly.plotly.layout()`   | deprecated    |
| `plotly.plotly.style()`    | deprecated    |
| `plotly.stream.init()`     | deprecated    |
| `plotly.stream.write()`    | moved          |
| `plotly.stream.close()`    | moved          |

###setting up credentials

Previously, you began your Plotly session by creating a `plotly` instance that
held your credentials. You can now choose to `sign_in` or if you've
`set_credentials`, you do not even need to sign in any longer.

```python

# old way
import plotly
py = plotly.plotly('username', 'api_key')  # py is a `plotly` instance
```

```python

# new way
import plotly.plotly as py  # py is now a name for the plotly.plotly module
py.sign_in('username', 'api_key')
```

See our guidebook for more information on logging in:


###`plot` and `iplot` call signatures:


```python

# old way to make a plot
import plotly
py = plotly.plotly('username', 'api_key')
py.plot(data, layout=layout, **plot_options)
py.iplot(data, layout=layout, **plot_options)
```

```python

# new way to make a plot
import plotly.plotly as py
py.sign_in('username', 'api_key')
py.plot(data_or_figure, **plot_options)
py.iplot(data_or_figure, **plot_options)
```

As before, `data` is a list of dictionary-like objects representing
individual traces on a graph. However, `layout` has now been included with
`data` in a new `figure` object:

```python

# you now send a figure dictionary
figure = {'data':data, 'layout':layout}
```

All objects in the JSON structure you're creating can now be represented as
actual Python classes.

See our guidebook for more information on the plot functions:

###'histogramx' and 'histogramy' are now just 'histogram'

This is a change in the actual JSON, but this change also effects the Python
API.

```python

# old way to make a histogram along the x-axis
option1 = dict(type='histogramx', x=[1,2,2,1,5,...,1])
option2 = dict(type='histogramy', y=[1,2,2,1,5,...,1])
```

```python

# new way to make a histogram along the x-axis
trace = dict(type='histogram', x=[1,2,2,1,5,...,1])
```

```python

# old way to make a histogram along the y-axis
option1 = dict(type='histogramx', x=[1,2,2,1,5,...,1], bardir='h')
option2 = dict(type='histogramy', y=[1,2,2,1,5,...,1], bardir='h')
```

```python

# new way to make a histogram along the x-axis
trace = dict(type='histogram', y=[1,2,2,1,5,...,1])
```

`'x'` data is now *always* plotted with vertical bars and `'y'` data is now
always plotted with horizontal bars. When you specify `'x'` *and* `'y'`,
you can use `'orientation'` to select whether `'x'` or `'y'` will be plotted
in their corresponding orientations.


###specifying filename now causes `fileopt='overwrite'`

Previously, to overwrite a file in your plotly account,
you needed to specify both `'filename'` *and* `'fileopt'`. Now,
if you specify a `'filename'` keyword argument when making a call to `plot()`
or `iplot()`, `'fileopt'` will default to `'overwrite'`,
and any existing plot with that filename will be overwritten.

Simply specify *both* to set a filename, but not overwrite if that filename
already exists.

###`plotly.embed()` has moved, and call signature has changed

```python

# old way
import plotly
plotly.embed('https://plot.ly/~PythonAPI/67/numpy-boxes/')
```

```python

# new way
import plotly.tools as tls
tls.embed('PythonAPI', 67)
```
Note that the location of this functionality has moved. More importantly,
though, you now receive figure information from Plotly by specifying a
case-insensitive string and a file_id number.


###`plotly.display()` is now `plotly.tools.embed()`

The `plotly.display()` function is deprecated and has been replaced with
`potly.tools.embed()`.

See the entry on `embed` for more details on new call signatures.

###for types `'bar'` and `'histogram'`, `'bardir'` is now `'orientation'`

In general, `'orientation'` now describes how x and y data relate to plots
and can be used more broadly than in just `'histogram'` and `'bar'`. Note,
however, the `'bardir'` still exists in `'layout'`.

###`ion` and `ioff` have been deprecated, use `auto_open=True`

Previously, you could set whether or not new plots created in Plotly from the
API caused a new browser tab to open.

By default it will open a new tab, to stop this, you should now use the
`auto_open` keyword:

```python

import plotly.plotly as py
py.plot(figure, auto_open=False)
```

###setting layout parameters

`layout` is now a member of a *figure* dictionary. You declare
layout options by setting keyword-value pairs in layout.

There are two ways to update layout options.

First, you can just add a `layout` dictionary into a new `figure` dictionary
along with your data:

```python

data = []  # put your data here
layout = {}  # set layout parameters here
figure = dict(data=data, layout=layout)  # assemble figure here
```

Second, if you're using the new 'graph objects' this version of the api
defines, you can use the `update` method on a figure instance, which has been
redefined to allow nested updating. You *basically* treat all of the new
graph objects as if they were dictionaries and lists.

```python

figure = Figure()  # auto-adds layout and data keys
figure['data'] += []  # put your data here
figure['layout'] = {}  # (option 1) set layout parameters here

# additionally, you can update in these ways
figure['layout'].update({})  # (option 2)
figure['layout'].update(key1=val1, key2=val2, key3=val3)  # (option 3)
```

###style() has been deprecated

All style parameters need to be declared within their resepctive objects.
That is, layout styles must be declared within the layout dictionary and data
object styles must be declared within their respective dictionaries.

###`plotly.stream` is now `plotly.plotly.Stream`, core functionality remains.

Aside from the class name being capitalized, the functionlity of the
streaming class has improved. Run help(plotly.plotly.Stream) for more
information.

###`plotly.signup()` has been deprecated

Users must signup initially at the plotly website, this can no longer be done
through the Python API.

###Axis and axis-references better support indexing

Previously the initial `xaxis` key needed to be named `'xaxis'`. It can now
be named `'xaxis1'`. Similarly references to this first axis used to required
 `'x'`, but now allow `'x1'` to refer to the same axis.

