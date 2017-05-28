## Spec for Report class

#### Basic idea and usage

After importing plotly, a Report object is created behind-the-scenes.
There is only one report object per Python session.
Plots returned from plot.ly are automatically appended to the report object during the Python session, 
so that when you create a report:

```python
import plotly
rp = plotly.report
```

It is pre-loaded with a list of plots and widget boxes that you've created during your session. Something like

```python
rp.save()
```

Would then compile and save the report to a local html file.

#### Item class

Reports would be structured as a list of Item objects.
Text, Plot, or Table objects would subclass from an Item class.

Item objects would have these methods and attributes:

* inline -- True or False. Defaults to false. 2 sequential Items in report with inline=True will display inline. Start with max. allowance of 2 inline items.
** Uses bootstraps 1-12 grid layout for fluid horizontal layout. Defaults to 3 for Table and vertical WidgetBox objects and 9 for plots. Coud add a "layout" attribute in the future for further control of this.
* to_html() -- Returns the Item's representation as an html string, including container div.
* to_json() -- Returns the Item's representation as a dict.

#### Text class

###### Methods / attributes:

* markdown -- True or False. Defaults to False. Used by to_html() to convert content to html.
* content -- plain text, html, or markdown string of content. 
* type (optional) -- for the html or markdown noob, adds css class to parent div for styling and parent html tags on to_html(). 
* possible types: caption, latex, paragraph, title, subtitle.

###### Usage examples:

```python
t1 = Text( 'Hello, world', type='title' ) # plain text with type
t2 = Text( '# Hello, world', markdown=True ) # markdown
t3 = Text( '<table>...</table>' ) # html
```

#### Table class

###### Methods / attributes:

* max_rows -- maximum number of rows to display
* max_cols -- maximum number of columns to display

###### Usage examples:

```python
tb1 = Table( pd, title="Q1 earnings" ) # pandas dataframe, optional title kwarg (=HTML caption)
tb2 = Table( '1,2,3\n4,5,6\n7,8,9' ) # csv string
tb3 = Table( [ [1,2,3], [4,5,6], [7,8,9] ] ) # list of lists
tb4 = Table( fig ) # plotly figure object
tb5 = Table( data ) # plotly data object

# vvv When Plotly grid's support GET requests, could read grids into Table objects
tb1 = Table( 234 ) # fid of user's grid
tb2 = Table( 'https://plot.ly/~jackp/1724', inline=True ) URL of user's grid
tb3 = Table( ('msunds',34), inline=True ) tuple for another user's grid, placed next to g2
```

#### Plot class

###### Methods / attributes:

* format = 'pdf' | 'png' | 'interactive'

###### Usage examples:

```python
p1 = Plot( 234 ) # fid of user's plot
p2 = Plot( 'https://plot.ly/~jackp/1724', inline=True, format='pdf' ) URL of user's plot
p3 = Plot( ('msunds',34), inline=True ) tuple for another user's plot, placed next to p2
```

## Serialization structure

In order to save reports, some serialization structure will be needed. Here's a suggestion:

```python
[
    { class: 'text', content: 'Title', type='caption' },
    { class: 'text', content: '## Subsection', markdown=True },
    { class: 'table', position: 'inline', content: '[[1,2,3],[4,5,6],[7,8,9]]' }, 
    { class: 'plot', position: 'inline', fid: 234, username: 'alex' },
    { class: 'text', content: 'Hello, hello', type='caption' },
    { class: 'table', fid: 123, username: 'alex' }, # table uses fid and username if grid
]
```

## Report class methods

#### Subclass from Python list
Subclass from lists so user can get all the list behavior they would expect from a list-like object? pop(), splicing, copying...

#### rp.prettyprint()
Idea: print the current report structure in a way that's understandable at-a-glance. 
What's the most helpful way to give the user a quick view of their report structure and item order?
Points to consider:
* How do we show items share the same vertical level (ie a grid (html table) and plot side-by-side)
* Do we limit text to ~50 chars with ellipses?
* Show indices for help with splicing out items?

```python
[0] Text: '# Report Title' (ROW1)
[1] Plot: https://plot.ly/~jackp/1 (ROW2)
[2] Grid: https://plot.ly/~jackp/2 (ROW2)
[3] Text: 'Lorem ipsum dolor sit amet, cons...' (ROW3)
```
Where ROW-N specifies vertical placement.

#### rp.append()

Accepts any Item object or list of Item objects:

```python
>>> t = Text( '## Subsection title' );
>>> rp.append( t )
1 Text object added to report.
```

#### rp.clear()

Clears all items from report

#### rp.save()

Writes report to flat html file.

optional kwargs:

```python
rp.save( plot_format = 'pdf') # converts all plots to pdf or png
rp.save( path = 'Desktop' ) # absolute or relative path for saving
```

