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
    description: How to make tables in Python with Plotly's Figure Factory.
    display_as: basic
    language: python
    layout: base
    name: Figure Factory Tables
    order: 15
    permalink: python/figure-factory-table/
    redirect_from:
    - python/figure-factory/table/
    - python/v3/figure-factory/table/
    thumbnail: thumbnail/table.gif
---

Tables can be created using a [`table` trace type](/python/table/), or by using a [figure factory](/python/figure-factories/) as detailed in this page.

#### Simple Table

```python
import plotly.figure_factory as ff

data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2005, 295500000],
               ['Canada', 2005, 32310000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]

fig = ff.create_table(data_matrix)
fig.show()
```

#### Add Links

```python
import plotly.figure_factory as ff

data_matrix = [['User', 'Language', 'Chart Type', '# of Views'],
               ['<a href="https://plotly.com/~empet/folder/home">empet</a>',
                '<a href="https://plotly.com/python/">Python</a>',
                '<a href="https://plotly.com/~empet/8614/">Network Graph</a>',
                298],
               ['<a href="https://plotly.com/~Grondo/folder/home">Grondo</a>',
                '<a href="https://plotly.com/matlab/">Matlab</a>',
                '<a href="https://plotly.com/~Grondo/42/">Subplots</a>',
                356],
               ['<a href="https://plotly.com/~Dreamshot/folder/home">Dreamshot</a>',
                '<a href="https://help.plot.ly/tutorials/">Web App</a>',
                '<a href="https://plotly.com/~Dreamshot/6575/_2014-us-city-populations/">Bubble Map</a>',
                262],
               ['<a href="https://plotly.com/~FiveThirtyEight/folder/home">FiveThirtyEight</a>',
                '<a href="https://help.plot.ly/tutorials/">Web App</a>',
                '<a href="https://plotly.com/~FiveThirtyEight/30/">Scatter</a>',
                692],
               ['<a href="https://plotly.com/~cpsievert/folder/home">cpsievert</a>',
                '<a href="https://plotly.com/r/">R</a>',
                '<a href="https://plotly.com/~cpsievert/1130/">Surface</a>',
                302]]

fig = ff.create_table(data_matrix)
fig.show()
```

### Use LaTeX

```python
import plotly.figure_factory as ff

data_matrix = [['Name', 'Equation'],
               ['Pythagorean Theorem', '$a^{2}+b^{2}=c^{2}$'],
               ['Euler\'s Formula', '$F-E+V=2$'],
               ['The Origin of Complex Numbers', '$i^{2}=-1$'],
               ['Einstein\'s Theory of Relativity', '$E=m c^{2}$']]

fig =  ff.create_table(data_matrix)
fig.show()
```

### Use a Pandas Dataframe

```python
import plotly.figure_factory as ff

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df_sample = df[100:120]

fig =  ff.create_table(df_sample)
fig.show()
```

### Modify Row Height

The default row height is 30 pixels. Set height_constant if you'd like to change the height of each row.


```python
import plotly.figure_factory as ff

data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2005, 295500000],
               ['Canada', 2005, 32310000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]

fig =  ff.create_table(data_matrix, height_constant=20)
fig.show()
```

### Custom Table Colors


```python
import plotly.figure_factory as ff

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df_sample = df[400:410]

colorscale = [[0, '#4d004c'],[.5, '#f2e5ff'],[1, '#ffffff']]

fig =  ff.create_table(df_sample, colorscale=colorscale)

fig.show()
```

### Custom Font Colors

```python
import plotly.figure_factory as ff

text = [['Team', 'Rank'], ['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5], ['F', 6]]

colorscale = [[0, '#272D31'],[.5, '#ffffff'],[1, '#ffffff']]
font=['#FCFCFC', '#00EE00', '#008B00', '#004F00', '#660000', '#CD0000', '#FF3030']

fig = ff.create_table(text, colorscale=colorscale, font_colors=font)
fig.layout.width=250
fig.show()
```

### Change Font Size

```python
import plotly.figure_factory as ff

data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2005, 295500000],
               ['Canada', 2005, 32310000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]

fig = ff.create_table(data_matrix, index=True)

# Make text size larger
for i in range(len(fig.layout.annotations)):
    fig.layout.annotations[i].font.size = 20

fig.show()
```

#### Tables with Graphs

```python
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Add table data
table_data = [['Team', 'Wins', 'Losses', 'Ties'],
              ['Montréal<br>Canadiens', 18, 4, 0],
              ['Dallas Stars', 18, 5, 0],
              ['NY Rangers', 16, 5, 0],
              ['Boston<br>Bruins', 13, 8, 0],
              ['Chicago<br>Blackhawks', 13, 8, 0],
              ['LA Kings', 13, 8, 0],
              ['Ottawa<br>Senators', 12, 5, 0]]
# Initialize a figure with ff.create_table(table_data)
fig = ff.create_table(table_data, height_constant=60)

# Add graph data
teams = ['Montréal Canadiens', 'Dallas Stars', 'NY Rangers',
         'Boston Bruins', 'Chicago Blackhawks', 'LA Kings', 'Ottawa Senators']
GFPG = [3.54, 3.48, 3.0, 3.27, 2.83, 2.45, 3.18]
GAPG = [2.17, 2.57, 2.0, 2.91, 2.57, 2.14, 2.77]
# Make traces for graph
fig.add_trace(go.Scatter(x=teams, y=GFPG,
                    marker=dict(color='#0099ff'),
                    name='Goals For<br>Per Game',
                    xaxis='x2', yaxis='y2'))
fig.add_trace(go.Scatter(x=teams, y=GAPG,
                    marker=dict(color='#404040'),
                    name='Goals Against<br>Per Game',
                    xaxis='x2', yaxis='y2'))

fig.update_layout(
    title_text = '2016 Hockey Stats',
    margin = {'t':50, 'b':100},
    xaxis = {'domain': [0, .5]},
    xaxis2 = {'domain': [0.6, 1.]},
    yaxis2 = {'anchor': 'x2', 'title': 'Goals'}
)

fig.show()
```


```python
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Add table data
table_data = [['Team', 'Wins', 'Losses', 'Ties'],
              ['Montréal<br>Canadiens', 18, 4, 0],
              ['Dallas Stars', 18, 5, 0],
              ['NY Rangers', 16, 5, 0],
              ['Boston<br>Bruins', 13, 8, 0],
              ['Chicago<br>Blackhawks', 13, 8, 0],
              ['Ottawa<br>Senators', 12, 5, 0]]
# Initialize a fig with ff.create_table(table_data)
fig = ff.create_table(table_data, height_constant=60)

# Add graph data
teams = ['Montréal Canadiens', 'Dallas Stars', 'NY Rangers',
         'Boston Bruins', 'Chicago Blackhawks', 'Ottawa Senators']
GFPG = [3.54, 3.48, 3.0, 3.27, 2.83, 3.18]
GAPG = [2.17, 2.57, 2.0, 2.91, 2.57, 2.77]

fig.add_trace(go.Bar(x=teams, y=GFPG, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Goals For<br>Per Game'))

fig.add_trace(go.Bar(x=teams, y=GAPG, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='Goals Against<br>Per Game'))

fig.update_layout(
    title_text = '2016 Hockey Stats',
    height = 800,
    margin = {'t':75, 'l':50},
    yaxis = {'domain': [0, .45]},
    xaxis2 = {'anchor': 'y2'},
    yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'}
)

fig.show()
```


#### Reference

For more info on `ff.create_table()`, see the [full function reference](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_table.html)