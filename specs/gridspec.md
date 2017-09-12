### Creating a grid with `grid_objs`

```python
from plotly.grid_objs import Column, Grid

column_1 = Column([1, 2, 3], 'column 1')

column_2 = Column(['a', 'b', datetime.datetime.now()], 'column 2')

grid = Grid(column_1, column_2)

unique_url = py.grid_ops.upload(grid, filename, world_readable=True)
```

### Updating grids

Grids are identified with either `grid` or `grid_url`, or `filename`
`filename` will be unsupported in this version
```python

rows = [[1, 'a'], [2, 'b']]

grid = Grid(c1, c2)

py.grid_ops.upload(grid, 'my file')

# We recommend this call signature, since `row` gets appended to the grid
py.grid_ops.append_rows(rows, grid=grid)

# But, these all do the same thing
py.grid_ops.append_rows(rows, grid_url="https://plot.ly/~chris/3") #shortcut
py.grid_ops.append_rows(rows, filename='my file') # currently unsupported.
                                            # will do a get request behind
                                            # the scenes to get the grid_id
```

Similarly for appending columns:
```python
from plotly.grid_objs import Column

new_col = Column([1,2,3], 'new col name')

# these are equivalent
py.grid_ops.append_columns([new_col], grid_url='https://plot.ly/~chris/3')
py.grid_ops.append_columns([new_col], filename='my file') # Currently unsupported

# this, too:
grid = Grid(Column([1,2,3], 'first column name'))
py.grid_ops.upload(grid, 'my file')

py.grid_ops.append_columns([new_col], grid=grid) # also implicitly adds new_col to grid

grid[0].name # 'first column name'
grid[1].name # 'new col name'
```


### On overwriting and duplicate file names and deletion

Overwriting currently isn't possible. For now,
```python
>> py.grid_ops.upload(grid, 'my grid')
"PlotlyFileException: Yikes, a file already exists with this filename."
"You can delete that file with:"
"> py.grid_ops.delete('my grid')"
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
>> py.grid_ops.upload('my grid') # overwrite defaults to True

# Or, recieve an exception with:
>> py.grid_ops.upload(grid, 'my grid', overwrite=False)
"PLotlyFileException: Yikes! ..."
```

Deleting:

```
# throw good errors if none or more than 1 were specified
py.grid_ops.delete(filename=None, grid_url=None, grid=None, grid_id=None)
```

In the future, once we can delete Plots and Folders

```
py.file_ops.delete(file_path=None, fid=None, url=None)
```


### Appearance and Access

```python
>> print(Column([1,2,3], 'column 1'))
<Column "column 1": [1, 2, 3]>
```

```python
>> print(Grid(col1, col2))
<Grid: [<Column "column 1": [1, 2, 3]>, <Column "column 2": ["a", "b", "c"]>]>
```

```python
>> grid = Grid(col1, col2)
>> print(grid[0])
<Column "column 1": [1, 2, 3]>
```

```python
>> grid = Grid(col1, col2)
>> print(grid.get_column('column 1'))
<Column "column 1": [1, 2, 3]>
```

### Creating a graph from a grid

If you have the grid
```python
>> from plotly.grid_objs import Grid
>> grid = Grid(column_1, column_2)
>> grid.upload(grid, 'experimental data')

>> fig_data = [Scatter(xsrc=grid[0], ysrc=grid[0])]
>> print(Scatter(xsrc=grid[0], ysrc=grid[1]))
[{"xsrc": "chris/8:3dkb", "ysrc": "chris/8:cbk8", "type": "scatter"}]
>> py.plot(fig_data)

>> Scatter(x=[1,2,3], y=[2,1,2])
"High five!"
>> Scatter(xsrc=[1,2,3], ysrc=[2,1,2])
"PlotlyTypeException: xrc and ysrc must be type string or plotly.grid_obj.Column"
>> Scatter(xsrc=Column('myCol', [1,2,3]), ysrc=Column('otherCol', [2,1,2]))
"PlotlyFileException: you must upload a grid before you can reference it in plots"
>> Scatter(xsrc=localGrid[0], ysrc=localGrid[1])
"PlotlyFileException: you must upload a grid before you can reference it in plots"
>>  Scatter(x=grid[0], y=grid[1])
"PlotlyTypeException: Yikes, column objects aren't currently supported here."
"x must be an array of strings, numbers, or datetimes."
>> print(Scatter(xsrc=grid[0], yscr=grid[1]))
{"xsrc": "chris/3:3dfbk", "ysrc": "chris/3:dk3c"}
```

Otherwise, download the grid (Not currently supported)
```
>> grid = grid_ops.get(filename=None, grid_id=None, grid_url=None)
```

(Download should use same endpoint as `grid_url.json`, e.g. [https://plot.ly/~chris/142.json](https://plot.ly/~chris/142.json))

### Errors
```python
>> grid = Grid(column_1, column_2)
>> trace = Scatter(x=grid[0], y=grid[1])
"PlotlyGridException: Grid must be uploaded to Plotly before figures can be created."
"Call `py.grid_ops.upload(grid)`"
```

```python
>> col1 = Column([], 'my column name')
>> col2 = Column([], 'my column name')
>> Grid(col1, col2)
"PlotlyGridException: Grid can't have duplicate column names"
```

```python
>> py.grid_ops.append_row(Row({'column 1': 1}), grid=grid)
"PlotlyGridException: Missing column entries, partial row update is not supported."
"Supply data for 'column 2' and try again."
```

Type checking boiler plate
```python
>> Column({'a': 'b'}, 'col1')
"PlotlyColumnException: Data argument must be an array of numbers, strings, Nones, or datetimes"
```

```python
>> Column([{'a': 'b'}], 'col1')
"PlotlyColumnException: Data values must be an array string, a number, Nones, or a datetime"
```

### Exceptions from Requests
A `PlotlyRequestError` that prints a useful error message from the server:
1. Print `response.detail` if provided (Plotly error message)
2. Otherwise, print `response.body` if the response is plain-text
3. Otherwise, print the original `requests.expceptions.HTTPError` error message.

Also, store the status code.


### Adding metadata to grids

```python
c1 = Column('first column', [1, 2, 3, 4])
grid = Grid([c1])
meta = {"settings":{"scope1":{"model":"Unicorn Finder","voltage":4}}}
py.grid_ops.upload(
    grid,
    unique_filename,
    meta=meta,
    auto_open=False)
```

```python
# First, create a grid
c1 = Column('first column', [1, 2, 3, 4])
grid = Grid([c1])
grid_url = py.grid_ops.upload(grid, unique_filename, auto_open=False)

# Add some Metadata to that grid
meta = {"settings": {"scope1": {"model": "Unicorn Finder", "voltage": 4}}}
meta_url = py.meta_ops.upload(
    meta,
    grid_url=grid_url)
```

### Plotly File system

```python

>> py.file_ops.mkdirs('new folder in root')

>> py.file_ops.mkdirs('make/each/of/these/folders')
```

Note that this is like `mkdir -p`. `mkdirs` is a Java convention.
We could also use our own, like:

- `py.file_ops.create_folders('new/folders')`
- `py.file_ops.new_folders('new/folders')`

These commands will:
- return status codes: `200` if nothing created, `201` if created
- raise exception if a file or folder already exists with that path


In the future, once we can delete Plots and Folders

```
py.file_ops.delete(file_path=None, fid=None, url=None)
```

Or, if we want to keep unix convention (do we?)
```
py.file_ops.rm(file_path=None, fid=None, url=None)
```
