### Creating a grid with `grid_objs`

```python
from plotly.grid_objs import Column, Grid

column_1 = Column([1, 2, 3], 'column 1')

column_2 = Column(['a', 'b', datetime.datetime.now()], 'column 2')

grid = Grid(column_1, column_2)

unique_url = grid.upload(filename, world_readable=True)
```

### Updating grids

```python
from plotly.grid_objs import Row

row = Row({'column 1': 4, 'column 2': 5})

grid = Grid(c1, c2)
grid.upload()
grid.append_row(row) # currently supported


# or, download the grid and append a row
grid = py.get_grid(filename) # currently unsupported
grid.append_row(row)


# or, download a "preview" of the grid and append a row
# (not all of the data would be downloaded, just enough to get the file_id
#  and a few rows for inspection, like pandas's `head`)
grid = py.get_grid(filename, preview=True) # currently unsupported
grid.append_row(row)


# or, if you don't want to download and you don't have the grid handy
py.append_row(row, filename='experimental data') # currently unsupported.
                                                 # behind the scenes, this will:
                                                 # - make a get request to get the file_id
                                                 # - make a post

py.append_row(row, file_id='chris/34') # currently supported

py.append_row(row, grid_url='https://plot.ly/~chris/34') # currently supported
```

### On overwriting and duplicate file names

Overwriting currently isn't possible. For now,
```python
>> grid.upload('my grid')
"PlotlyFileException: Yikes, a file already exists with this filename."
"You can delete that file with:"
"> py.delete('my grid')"
"Warning: If any graphs were made from this grid, the data in those graphs"
"will also be lost. If you make a new grid after you delete with the same filename, "
"the new grid's URL will also be different."
"That's confusing and you're probably not having a good time.""
"Questions? chris@plot.ly"
```

In the near future:
```python
# Updates the data, but not the column ids, of the grid. Referenced plots don't break.
# Behind the scenes, this:
# 1 - Makes a `GET` request to retrieve a {column_name: column_id} hash
# 2 - Makes a `PUT` request to update the data of the columns
>> grid.upload('my grid') # overwrite defaults to True

# Or, recieve an exception with:
>> grid.upload('my grid', overwrite=False)
"PLotlyFileException: Yikes! ..."
```

### Appearance and Access

```python
>> print Column([1,2,3], 'column 1')
<Column "column 1": [1, 2, 3]>
```

```python
>> print Grid(col1, col2)
<Grid: [<Column "column 1": [1, 2, 3]>, <Column "column 2": ["a", "b", "c"]>]>
```

```python
>> grid = Grid(col1, col2)
>> print grid[0]
<Column "column 1": [1, 2, 3]>
```

```python
>> grid = Grid(col1, col2)
>> print grid.get_column('column 1')
<Column "column 1": [1, 2, 3]>
```

### Creating a graph from a grid

```python
>> from plotly.grid_objs import Grid
>> grid = Grid(column_1, column_2)
>> grid.upload(grid, 'experimental data')

>> fig_data = [Scatter(xsrc=grid[0], ysrc=grid[0])]
>> print Scatter(xsrc=grid[0], ysrc=grid[1])
[{"xsrc": "chris/8:3dkb", "ysrc": "chris/8:cbk8", "type": "scatter"}]
>> py.plot(fig_data)
```


### Errors
```python
>> grid = Grid(column_1, column_2)
>> trace = Scatter(x=grid[0], y=grid[1])
"PlotlyGridException: Grid must be uploaded to Plotly before figures can be created."
"Call `py.upload_grid(grid)`"
```

```python
>> col1 = Column([1,2,3], 'column 1')
>> col1.data = [10, 20, 30]
>> col1.name = 'new column name'
>> Grid(col1).upload('my grid')
>> col1.name = 'update the column name again'
"PlotlyGridException: Cannot update the grid after it has been uploaded to Plotly"
```

```python
>> col1 = Column([], 'my column name')
>> col2 = Column([], 'my column name')
>> Grid(col1, col2)
"PlotlyGridException: Grid can't have duplicate column names"
```

```python
>> grid.append_row(Row({'column 1': 1}))
"PlotlyGridException: Missing column entries, partial row update is not supported."
"Supply data for 'column 2' and try again."
```

Type checking boiler plate
```python
>> Column({'a': 'b'}, 'col1')
"PlotlyColumnException: Data argument must be type list or tuple"
```

```python
>> Column([{'a': 'b'}], 'col1')
"PlotlyColumnException: Data values must be a string, a number, or a datetime"
```
