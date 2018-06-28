# Add A Figure Factory to the Plotly [Python Library](https://plot.ly/python/)

## What is a Figure Factory?
In the Python Plotly Library:

We have basic plot types that are created using the `plotly.graph_objs` module.
These plot types include Scatter, Box and Bar types. For a complete list see the [graph_objs file](https://github.com/plotly/plotly.py/blob/master/plotly/graph_objs/graph_objs.py). They are the basis of the plots and charts instatiated by Plotly.

To create a basic chart like this, first we create the `data` using the tools in `plotly.graph_objs` and then we plot it. For example:

```
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Scatter(
    x = [1, 2, 3],
    y = [4, 5, 6],
    mode = 'markers',
)

data = [trace]

py.iplot(data, filename='new-scatter-plot')
```

There is another type of chart which uses these basic plot types to make other types of graphs, and these are the figure factories. These are wrappers that utilize the code from `plotly.graph_objs` to build charts that can use their structures. A good example of a figure factory is the [Scatterplot Matrix](https://plot.ly/python/scatterplot-matrix/) as it utilizes `go.Scatter`, `go.Box` and `go.Histogram`.

So if you have ever wanted to contribute to the Plotly Python Library by adding a new chart type we don't have, now you can! This README will help you get started by cloning the plotly.py repo, forking a new branch, creating a new figure factory, and creatng a new Pull Request to get feedback for merging. Just follow all these steps and you'll be ready to go.

## Getting Started:
1. In the Terminal, clone the `plotly.py` repo locally and then check out the master branch.

```
$ git clone git@github.com:plotly/plotly.py.git
$ git fetch origin
$ git checkout master
```

2. Create a new branch off the master branch and give it an appropriate name.

```
$ git checkout -b "add-ff-type"
```

## Create a figure_factory File
1. Creating python file

Move to the `plotly/figure_factory` directory in the `plotly.py` repo. To do this, open up the Terminal and excute the command:

```
cd plotly/figure_factory
```

By running `ls` in the Terminal, you will get a list of all files in your current directory. In the `plotly/figure_factory` directory there is an `__init__.py` file as well as a bunch of `_ff_type.py` files. Each figure factory chart gets its own python file, and the name of each of these python files are found in the `__init__.py` file.

If you are making a chart called `foo`, then you must create `_foo.py` in this directory.


2. Updating `__init__.py`

The inside of the `__init__.py` looks like:

```
from __future__ import absolute_import

# Require that numpy exists for figure_factory
import numpy

from plotly.figure_factory._2d_density import create_2d_density
from plotly.figure_factory._annotated_heatmap import create_annotated_heatmap
from plotly.figure_factory._candlestick import create_candlestick
...
```

Now add the following line to the end of `__init__.py`:

```
from plotly.figure_factory._foo import create_foo
```

3. Imports

In `_foo.py` write

```
from __future__ import absolute_import
```

at line 1. You can add other imports later if you will need them.

4. The main function

It's now time to write the main function `create_foo` that will be called directly by the user. It has the form:

```
def create_foo(attribute1, attribute2=value, ...):
    """
    Returns figure for a foo plot.

    :param (type) attribute1: description of 'attribute1'.
    :param (type) attribute2: description of what 'attribute2' is.
        Default = value
    # ...
    
    Example 1:
    '''
    
    '''
    
    Example 2:
    '''
    
    '''
    """
    # code goes here
    return fig
```

You _must_ include a documentation string in your function. A doc string is a block string that contains useful information about what the function does, the arguments of the function and their descriptions, and examples of this function in use. The doc string is displayed when the help method is run by a user: `help(create_foo)` or `create_foo?` in python.

The parameters are listed in the doc string with the format
```
:param (param_type) param_name: description.
```
Afterwards, you must include examples which demonstrate the different capabilities and features of the function. For more information on proper doc string syntax see [PEP-257 page](https://www.python.org/dev/peps/pep-0257/).

After the doc string, you will add the main code of your function which should result in returning the fig, i.e. `return fig`.

```
# create figure
fig = create_foo(...)

# plot figure
py.iplot(fig, filename='my_figure')
```

The figure `fig` must be a Plotly Figure, meaning it must have the form `fig = graph_objs.Figure(data=data, layout=layout)`.

5. Useful Tips

It is often not a good idea to put all your code into your `create_foo()` function. It is best practice to not repeat yourself and this requires taking repeated blocks of code and puting them into a seperate function.

It is best to make all other functions besides `create_foo()` secret so a user cannot access them. This is done by placing a `_` before the name of the function, so `_aux_func()` for example.


## Create a Pull Request

Now add changes to your current local branch

```
$ git add -a
```

and commit these changes and write a commit message.

```
$ git commit -m "this is the work that I did"
```

After you have added and commited all of your changes to the local branch, it is time to create your PR for the Plotly team to review.

```
$ git push origin add-ff-type
```

## Be Part of the Discussion

Go check out your newly pushed branch at https://github.com/plotly/plotly.py. If you have any other questions, check out the [Plotly Contributing Page](https://github.com/plotly/plotly.py/blob/master/contributing.md). Thanks for contributing to Plotly's Graphing Library!

### Table of Current Figure Factories
| Name              | Documentation                             | In GitHub     |
| ----------------- | ----------------------------------------- | ------------- |
| 2D Density        | https://plot.ly/python/density-plots/     |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_2d_density.py|
| Annotated Heatmap | https://plot.ly/python/annotated_heatmap/ |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_annotated_heatmap.py|
| Candlestick       | https://plot.ly/python/candlestick-charts/|https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_candlestick.py|
| Dendrogram        | https://plot.ly/python/dendrogram/        |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_dendrogram.py|
| Distplot          | https://plot.ly/python/distplot/          |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_distplot.py|
| Facet Grid        | https://plot.ly/python/facet-plots/       |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_facet_grid.py|
| Gantt             | https://plot.ly/python/gantt/             |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_gantt.py|
| Ohlc              | https://plot.ly/python/ohlc-charts/       |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_ohlc.py|
| Quiver            | https://plot.ly/python/quiver-plots/      |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_quiver.py|
| Scatterplot Matrix| https://plot.ly/python/scatterplot-matrix/|https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_scatterplot.py|
| Streamline        | https://plot.ly/python/streamline-plots/  |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_streamline.py|
| Table             | https://plot.ly/python/table/             |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_table.py|
| Trisurf           | https://plot.ly/python/trisurf/           |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_trisurf.py|
| Violin            | https://plot.ly/python/violin-plot/       |https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/_violin.py|
