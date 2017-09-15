# Add Your Figure Factory to the Plotly [Python Library](https://plot.ly/python/)

If you have ever wanted to contribute to the Plotly Python Library by adding a new chart type we don't have, now you have the resources to do so. This README will help you get started cloning the plotly.py repo, forking a new branch, creating a new figure factory, and pushing your results to the cloud to get feedback for merging. Just follow all these steps and you'll be ready to go.

## Getting Started:
1. Clone the `plotly.py` repo locally and then check out the master branch.

```
$ git clone git@github.com:plotly/plotly.py.git
$ git fetch origin
$ git checkout master
```

2. Checkout a new branch and give it an appropriate name.

```
$ git checkout -b "my-new-ff"
```

## Create A figure_factory file
1. Creating python file and updating `__init__.py`

You are now ready to start writing your code. Begin by moving to the `plotly.figure_factory` directory in the `plotly.py` repo. Notice that there is an `__init__.py` file as well as a bunch of `_figure_factory_chart.py` files in this directory. Each type of unique plotly chart gets its own python file, and the name of each python file is found in the `__init__.py` file.

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

If you want to make, for example, a chart called `foo`, then you must create a python file `_foo.py` and then add the following line to the end of `__init__.py`:

```
from plotly.figure_factory._foo import create_foo
```

2. Imports
In `_foo.py` write

```
from __future__ import absolute_import
```

at line 1. You can add other imports later if you will need them.

3. The main function

It's now time to write the main function `create_foo` that will be called directly by the user. It has the form:

```
def create_foo(data, height=450, width=600, ...):
    """
    Returns figure for a foo plot.

    :param (list) data: description of what 'data' is.
    :param (int) height: description of what 'height' is.
    :param (int) width: description of what 'width' is.
    # ...
    
    Example 1:
    '''
    
    '''
    
    Example 2:
    '''
    
    '''
    """
    # code
    # ...
    # return fig
```

You _must_ include what is known as a documentation string or doc string in your function, which is just a block string taht contains useful information about what the function does, the arguments of the function and their descriptions, and examples of this function in use. The doc string is displayed when the help method is run by a user: `help(create_foo)` or `create_foo?` in Jupyter.

The parameters are listed in the doc string with the format `:param (param_type) param_name: description.` Afterwards, you must include Examples which demonstrate the different capabilities and features of the function. For more information on proper doc string syntax see [PEP-257 page](https://www.python.org/dev/peps/pep-0257/).

After the doc string, you may write the main code of your function, which should result in returning the `fig`. Users will use your function in the following way:

```
# create figure
fig = create_foo(...)

# plot figure
py.iplot(fig, filename='my_figure')
```

The figure `fig` must be a Plotly Figure, meaning it must have the form `fig = graph_objs.Figure(data=data, layout=layout)`.

4. Useful Tips

It is often not a good idea to put all your code into your `create_foo()` function. It is best practice to not repeat yourself and this requires taking repeated blocks of code and puting them into a seperate function. Usually it is best to make all other functions besides `create_foo()` secret so a user cannot access them. This is done by placing a `_` before the name of the function, so `_aux_func()` for example.


## Push to GitHub

When you are finally finished your first draft of your figure factory, it is time to push it to the cloud and to get feedback from the Plotly team and other voluntary GitHub users. After you have added and commited all of your changes on the local branch, push the changes to a new remote branch on Git:

```
$ git push origin my-new-ff
```

Thank you for reading and thanks for contributing to Plotly's Graphing Library!