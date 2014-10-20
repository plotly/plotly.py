
Grid JSON

```python
{
   "cols": {
        "first column": {
            "data": ["a", "b", "c"]
        },
        "second column": {
            "data": [1, 2, 3]
        },
        "third column": {
            "data": [1, 8, 4]
        }
   }
}
```

### Creating a grid with `grid_objs`

```python
from plotly.grid_objs import Column, Grid

column_1 = Column([1, 2, 3], 'column 1')

column_2 = Column(['a', 'b', datetime.datetime.now()], 'column 2')

grid = Grid(column_1, column_2)

unique_url = py.upload_grid(grid, filename='experimental data', world_readable=True)
```

### Updating grids

```
from plotly.grid_objs import Row

row = Row({'column 1': 4, 'column 2': 5})

py.append_row(row, filename='experimental data')
```

```
column = Column([1,2,3], 'column 3')

py.append_column(column, filename='experimental data')
```


### Appearance and Access

```python
>> print Column([1,2,3], 'column 1')
<Column "asdf": [1, 2, 3]>
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
>> print grid['column 1']
<Column "column 1": [1, 2, 3]>
```

### Creating a graph from a grid

```python
grid = Grid(column_1, column_2)
py.upload_grid(grid, filename='experimental data')

fig_data = [Scatter(xsrc=grid['column 1'], ysrc=grid['column 2'])]
py.plot(fig_data)
```

```python
>> grid = Grid(col1, col2)
>> py.upload_grid(grid)
>> print Scatter(xsrc=grid[0], ysrc=grid[1])
{"xsrc": "chris/8:3dkb", "ysrc": "chris/8:cbk8", "type": "scatter"}
```

### Errors
```python
>> grid = Grid(column_1, column_2)
>> trace = Scatter(x=grid[0], y=grid[1])
PlotlyGridException: Grid must be uploaded to Plotly before figures can be created.
Call `py.upload_grid(grid)`
```

```python
>> col1 = Column([1,2,3], 'column 1')
>> col1.data = [10, 20, 30]
>> col1.name = 'new column name'
>> py.upload_grid(Grid(col1))
>> col1.name = 'update the column name again'
PlotlyGridException: Cannot update the grid after it has been uploaded to Plotly
```

```python
>> col1 = Column([], 'my column name')
>> col2 = Column([], 'my column name')
>> Grid(col1, col2)
PlotlyGridException: Grid can't have duplicate column names
```

```python
>> py.append_row(Row({'column 1': 1}))
PlotlyGridException: Missing column entries, partial row update is not supported.
Supply data for 'column 2' and try again.
```


Type checking boiler plate
```python
>> Column({'a': 'b'}, 'col1')
PlotlyColumnException: Data argument must be type list or tuple
```

```python
>> Column([{'a': 'b'}], 'col1')
PlotlyColumnException: Data values must be a string, a number, or a datetime
```


### Help

```python

```
