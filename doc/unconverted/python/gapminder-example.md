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
    description: How to make the classic Gapminder Animation using sliders and buttons
      in Python.
    display_as: animations
    language: python
    layout: base
    name: Adding Sliders to Animations
    order: 2
    page_type: example_index
    permalink: python/gapminder-example/
    thumbnail: thumbnail/gapminder_animation.gif
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Animations are available in version 1.12.10+
Run `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

#### Import Data
This tutorial walks you through how to make an example using the [Gapminder dataset](http://www.gapminder.org/world/) to present the GDP per Capita vs Life Expectancy across the years 1952 to 2007 in an animated Bubble Chart, in which the bubbles represent countries and their sizes represent the population.

First import the Gapminder data that we will be using for the example and store in a dataframe:

```python
import plotly.plotly as py
import plotly.figure_factory as ff
from plotly.grid_objs import Grid, Column

import pandas as pd
import time

url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
dataset = pd.read_csv(url)

table = ff.create_table(dataset.head(10))
py.iplot(table, filename='animations-gapminder-data-preview')
```

#### Make the Grid
Since we are using the v2 api for animations in Plotly, we need to first make a `grid`. You can learn more in the [introduction to animation doc](https://plot.ly/python/animations/).

We will first define a list of _string_ years which will represent the values that our `slider` will take on. Going through the dataset, we will take out all the unique continents from the column `continent` and store them as well. Finally, we make a grid with each column representing a slice of the dataframe by _year_, _continent_ and _column name_, making sure to name each column uniquly by these variables:

```python
years_from_col = set(dataset['year'])
years_ints = sorted(list(years_from_col))
years = [str(year) for year in years_ints]
years.remove('1957')

# make list of continents
continents = []
for continent in dataset['continent']:
    if continent not in continents:
        continents.append(continent)

columns = []
# make grid
for year in years:
    for continent in continents:
        dataset_by_year = dataset[dataset['year'] == int(year)]
        dataset_by_year_and_cont = dataset_by_year[dataset_by_year['continent'] == continent]
        for col_name in dataset_by_year_and_cont:
            # each column name is unique
            column_name = '{year}_{continent}_{header}_gapminder_grid'.format(
                year=year, continent=continent, header=col_name
            )
            a_column = Column(list(dataset_by_year_and_cont[col_name]), column_name)
            columns.append(a_column)

# upload grid
grid = Grid(columns)
url = py.grid_ops.upload(grid, 'gapminder_grid'+str(time.time()), auto_open=False)
url
```

#### Make the Figure

```python
figure = {
    'data': [],
    'layout': {},
    'frames': [],
    'config': {'scrollzoom': True}
}

# fill in most of layout
figure['layout']['xaxis'] = {'range': [30, 85], 'title': 'Life Expectancy', 'gridcolor': '#FFFFFF'}
figure['layout']['yaxis'] = {'title': 'GDP per Capita', 'type': 'log', 'gridcolor': '#FFFFFF'}
figure['layout']['hovermode'] = 'closest'
figure['layout']['plot_bgcolor'] = 'rgb(223, 232, 243)'
```

<!-- #region -->
#### Add Slider
For the slider to appear, we need to adda `sliders` dictionary to `layout`. The `sliders` dictionary is set in the following way:

```
figure['layout']['sliders] = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'text-before-value-on-display',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': [...]
}
```

- `yanchor` determines whether the slider is on the _top_ or _bottom_ of the chart page
- `xanchor` is similar, only with _left_ and _right_ as possible values
- `currentvalue` sets the display of the current value that the slider is hovering on. It contains args such as `prefix`, which sets the text that appears before the value.
- `steps` is a list of dictionaries each of which corresponds to a frame in the figure. They should be ordered in the sequence in which the frames occur in the animation.

Each dictionary in `steps` has the following form:

```
{
    'method': 'animate',
    'label': 'label-for-frame',
    'value': 'value-for-frame(defaults to label)',
    'args': [{'frame': {'duration': 300, 'redraw': False},
         'mode': 'immediate'}
    ],
}
```
- the first item in the list `args` is a list containing the slider-value of that frame
- `label` is the text that appears next to the `prefix` arg mentioned in the `slider` section (eg. _Year: 1952_)

For more information, check out the [documentation](https://plot.ly/python/reference/#layout-sliders).
<!-- #endregion -->

```python
sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Year:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}
```

### Add Play and Pause Buttons

```python
figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]

custom_colors = {
    'Asia': 'rgb(171, 99, 250)',
    'Europe': 'rgb(230, 99, 250)',
    'Africa': 'rgb(99, 110, 250)',
    'Americas': 'rgb(25, 211, 243)',
    'Oceania': 'rgb(50, 170, 255)'
}
```

#### Fill in Figure with Data and Frames
Now we can put the data from our grid into the figure. Since we are using referenced data from the grid, we use the `.get_column_reference()` method on the grid and supply the name of the column we want via a looping through all the years and continents. First we

Note: If you are using referenced data for a particular parameter, you `MUST` change the parameter name from `name` to `namesrc` to indicate that you are using referenced data from a grid. For instance, `x` becomes `xsrc`, `text` becomes `textsrc`, etc.

```python
col_name_template = '{year}_{continent}_{header}_gapminder_grid'
year = 1952
for continent in continents:
    data_dict = {
        'xsrc': grid.get_column_reference(col_name_template.format(
            year=year, continent=continent, header='lifeExp'
        )),
        'ysrc': grid.get_column_reference(col_name_template.format(
            year=year, continent=continent, header='gdpPercap'
        )),
        'mode': 'markers',
        'textsrc': grid.get_column_reference(col_name_template.format(
            year=year, continent=continent, header='country'
        )),
        'marker': {
            'sizemode': 'area',
            'sizeref': 200000,
            'sizesrc': grid.get_column_reference(col_name_template.format(
                 year=year, continent=continent, header='pop'
            )),
            'color': custom_colors[continent]
        },
        'name': continent
    }
    figure['data'].append(data_dict)
```

<!-- #region -->
### Create Frames
Finally we make our `frames`. Here we are running again through the years and continents, but for each combination we instantiate a frame dictionary of the form:

```
frame = {'data': [], 'name': value-name}
```
We add a dictionary of data to this list and at the end of each loop, we ensure to add the `steps` dictionary to the steps list. At the end, we attatch the `sliders` dictionary to the figure via:

```
figure['layout']['sliders'] = [sliders_dict]
```

and then we plot! Enjoy the Gapminder example!
<!-- #endregion -->

```python
for year in years:
    frame = {'data': [], 'name': str(year)}
    for continent in continents:
        data_dict = {
            'xsrc': grid.get_column_reference(col_name_template.format(
                year=year, continent=continent, header='lifeExp'
            )),
            'ysrc': grid.get_column_reference(col_name_template.format(
                year=year, continent=continent, header='gdpPercap'
            )),
            'mode': 'markers',
            'textsrc': grid.get_column_reference(col_name_template.format(
                year=year, continent=continent, header='country'
                )),
            'marker': {
                'sizemode': 'area',
                'sizeref': 200000,
                'sizesrc': grid.get_column_reference(col_name_template.format(
                    year=year, continent=continent, header='pop'
                )),
                'color': custom_colors[continent]
            },
            'name': continent
        }
        frame['data'].append(data_dict)

    figure['frames'].append(frame)
    slider_step = {'args': [
        [year],
        {'frame': {'duration': 300, 'redraw': False},
         'mode': 'immediate',
       'transition': {'duration': 300}}
     ],
     'label': year,
     'method': 'animate'}
    sliders_dict['steps'].append(slider_step)

figure['layout']['sliders'] = [sliders_dict]
```

### Plot Animation

```python
py.icreate_animations(figure, 'gapminder_example'+str(time.time()))
```

#### Reference
For additional information and attributes for creating bubble charts in Plotly see: https://plot.ly/python/bubble-charts/.
For more documentation on creating animations with Plotly, see https://plot.ly/python/#animations.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'gapminder-example.ipynb', 'python/gapminder-example/', 'Adding Sliders to Animations | plotly',
    'How to make the classic Gapminder Animation using sliders and buttons in Python.',
    title='Adding Sliders to Animations | plotly',
    name='Adding Sliders to Animations',
    language='python',
    page_type='example_index', has_thumbnail='true', thumbnail='thumbnail/gapminder_animation.gif',
    display_as='animations', ipynb= '~notebook_demo/129', order=2)
```

```python

```
