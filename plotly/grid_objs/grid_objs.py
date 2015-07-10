"""
grid_objs
=========

"""
from __future__ import absolute_import

import json
from collections import MutableSequence

from plotly import exceptions, utils

__all__ = None


class Column(object):
    """
    Columns make up Plotly Grids and can be the source of
    data for Plotly Graphs.
    They have a name and an array of data.
    They can be uploaded to Plotly with the `plotly.plotly.grid_ops`
    class.

    Usage example 1: Upload a set of columns as a grid to Plotly
    ```
    from plotly.grid_objs import Grid, Column
    import plotly.plotly as py
    column_1 = Column([1, 2, 3], 'time')
    column_2 = Column([4, 2, 5], 'voltage')
    grid = Grid([column_1, column_2])
    py.grid_ops.upload(grid, 'time vs voltage')
    ```

    Usage example 2: Make a graph based with data that is sourced
                     from a newly uploaded Plotly columns
    ```
    import plotly.plotly as py
    from plotly.grid_objs import Grid, Column
    from plotly.graph_objs import Scatter
    # Upload a grid
    column_1 = Column([1, 2, 3], 'time')
    column_2 = Column([4, 2, 5], 'voltage')
    grid = Grid([column_1, column_2])
    py.grid_ops.upload(grid, 'time vs voltage')

    # Build a Plotly graph object sourced from the
    # grid's columns
    trace = Scatter(xsrc=grid[0], ysrc=grid[1])
    py.plot([trace], filename='graph from grid')
    ```
    """
    def __init__(self, data, name):
        """
        Initialize a Plotly column with `data` and `name`.
        `data` is an array of strings, numbers, or dates.
        `name` is the name of the column as it will apppear
               in the Plotly grid. Names must be unique to a grid.
        """

        # TODO: data type checking
        self.data = data
        # TODO: name type checking
        self.name = name

        self.id = ''

    def __str__(self):
        max_chars = 10
        jdata = json.dumps(self.data, cls=utils.PlotlyJSONEncoder)
        if len(jdata) > max_chars:
            data_string = jdata[:max_chars] + "...]"
        else:
            data_string = jdata
        string = '<name="{name}", data={data_string}, id={id}>'
        return string.format(name=self.name, data=data_string, id=self.id)

    def __repr__(self):
        return 'Column("{0}", {1})'.format(self.data, self.name)

    def to_plotly_json(self):
        return {'name': self.name, 'data': self.data}


class Grid(MutableSequence):
    """
    Grid is Plotly's Python representation of Plotly Grids.
    Plotly Grids are tabular data made up of columns. They can be
    uploaded, appended to, and can source the data for Plotly
    graphs.

    A plotly.grid_objs.Grid object is essentially a list.

    Usage example 1: Upload a set of columns as a grid to Plotly
    ```
    from plotly.grid_objs import Grid, Column
    import plotly.plotly as py
    column_1 = Column([1, 2, 3], 'time')
    column_2 = Column([4, 2, 5], 'voltage')
    grid = Grid([column_1, column_2])
    py.grid_ops.upload(grid, 'time vs voltage')
    ```

    Usage example 2: Make a graph based with data that is sourced
                     from a newly uploaded Plotly columns
    ```
    import plotly.plotly as py
    from plotly.grid_objs import Grid, Column
    from plotly.graph_objs import Scatter
    # Upload a grid
    column_1 = Column([1, 2, 3], 'time')
    column_2 = Column([4, 2, 5], 'voltage')
    grid = Grid([column_1, column_2])
    py.grid_ops.upload(grid, 'time vs voltage')

    # Build a Plotly graph object sourced from the
    # grid's columns
    trace = Scatter(xsrc=grid[0], ysrc=grid[1])
    py.plot([trace], filename='graph from grid')
    ```
    """
    def __init__(self, iterable_of_columns):
        """
        Initialize a grid with an iterable of
        `plotly.grid_objs.Column objects

        Usage example:
        ```
        column_1 = Column([1, 2, 3], 'time')
        column_2 = Column([4, 2, 5], 'voltage')
        grid = Grid([column_1, column_2])
        ```
        """

        # TODO: verify that columns are actually columns

        column_names = [column.name for column in iterable_of_columns]
        duplicate_name = utils.get_first_duplicate(column_names)
        if duplicate_name:
            err = exceptions.NON_UNIQUE_COLUMN_MESSAGE.format(duplicate_name)
            raise exceptions.InputError(err)

        self._columns = list(iterable_of_columns)
        self.id = ''

    def __repr__(self):
        return self._columns.__repr__()

    def __getitem__(self, index):
        return self._columns[index]

    def __setitem__(self, index, column):
        self._validate_insertion(column)
        return self._columns.__setitem__(index, column)

    def __delitem__(self, index):
        del self._columns[index]

    def __len__(self):
        return len(self._columns)

    def insert(self, index, column):
        self._validate_insertion(column)
        self._columns.insert(index, column)

    def _validate_insertion(self, column):
        """
        Raise an error if we're gonna add a duplicate column name
        """
        existing_column_names = [col.name for col in self._columns]
        if column.name in existing_column_names:
            err = exceptions.NON_UNIQUE_COLUMN_MESSAGE.format(column.name)
            raise exceptions.InputError(err)

    def _to_plotly_grid_json(self):
        grid_json = {'cols': {}}
        for column_index, column in enumerate(self):
            grid_json['cols'][column.name] = {
                'data': column.data,
                'order': column_index
            }
        return grid_json

    def get_column(self, column_name):
        """ Return the first column with name `column_name`.
        If no column with `column_name` exists in this grid, return None.
        """
        for column in self._columns:
            if column.name == column_name:
                return column
