## Spec for Report class

#### Basic idea and usage

After importing plotly, a Report object is created behind-the-scenes.
There is only one report object per Python session.
Grids and plots returned from plot.ly are automatically appended to the report object during the Python session, 
so that when you create a report:

```python
import plotly
rp = plotly.report
```

It is pre-loaded with a list of plots, grids, and widget boxes that you've created during your session. Something like

```python
rp.save()
```

Would then compile and save the report to a local html file.

#### Item class

Reports would be structured as a list of Item objects.
Text, Plot, or Grid objects would subclass from an Item class.

Item objects would have these methods and attributes:

* inline -- True or False. Defaults to false. >=2 sequential Items in report with inline=True will display inline.
* to_html() -- Returns the Item's representation as an html string, including container div.
* serialize() -- Returns the Item's representation as a dict.

#### Text class

Methods / attributes:

* markdown -- True or False. Defaults to False. Used by to_html() to convert content to html.
* content -- plain text, html, or markdown string of content. 
* type (optional) -- for the html or markdown noob, adds css class to parent div for styling and parent html tags on to_html(). 
* possible types: caption, latex, paragraph, title, subtitle.

Usage examples:

```python
t1 = Text( 'Hello, world', type='title' ) # plain text with type
t2 = Text( '# Hello, world', markdown=True ) # markdown
t3 = Text( '<table>...</table>' ) # html
```

#### Grid class

Methods / attributes:

* max_rows -- maximum number of rows to display

Usage examples:

```python
g1 = Grid( 234 ) # fid of user's grid
g2 = Grid( 'https://plot.ly/~jackp/1724', inline=True ) URL of user's grid
g3 = Grid( ('msunds',34), inline=True ) tuple for another user's grid, placed next to g2
```

#### Plot class

Methods / attributes:

* None?

Usage examples:

```python
p1 = Plot( 234 ) # fid of user's plot
p2 = Plot( 'https://plot.ly/~jackp/1724', inline=True ) URL of user's plot
p3 = Plot( ('msunds',34), inline=True ) tuple for another user's plot, placed next to p2
```

## Serialization structure

In order to save reports, some serialization structure will be needed. Here's a suggestion:

```python
{
    name: 'my report',
    items: [
        { class: 'text', content: '## Subsection', markdown=True },
        { class: 'grid', inline: True, fid: 123, username: 'alex' },
        { class: 'plot', inline: True, fid: 234, username: 'alex' },
        { class: 'text', content: 'Hello, hello', type='caption' },
    ]
}
```

## Report class methods

#### Subclass from Python list
Subclass from lists so user can get all the list behavior they would expect from a list-like object? pop(), splicing, copying...

#### rp.print()
Prints the current report structure. 
What's the most helpful way to give the user a quick view of their report structure and item order?
Points to consider:
* How do we show items share the same vertical level (ie a grid (html table) and plot side-by-side)
* Do we limit text to ~50 chars with ellipses?
* Show indices for help with splicing out items?

```python
[0] Text: '# Report Title' (BLOCK1)
[1] Plot: https://plot.ly/~jackp/1 (BLOCK2)
[2] Grid: https://plot.ly/~jackp/2 (BLOCK2)
[3] Text: 'Lorem ipsum dolor sit amet, cons...' (BLOCK3)
```
Where BLOCK-N specifies vertical placement.

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

