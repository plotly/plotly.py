"""
grid_objs
=========

"""
from __future__ import absolute_import

from collections import MutableSequence

from requests.compat import json as _json

from plotly import exceptions, optional_imports, utils

pd = optional_imports.get_module('pandas')

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
        jdata = _json.dumps(self.data, cls=utils.PlotlyJSONEncoder)
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
    def __init__(self, columns_or_json, fid=None):
        """
        Initialize a grid with an iterable of `plotly.grid_objs.Column`
        objects or a json/dict describing a grid. See second usage example
        below for the necessary structure of the dict.

        :param (str|bool) fid: should not be accessible to users. Default
            is 'None' but if a grid is retrieved via `py.get_grid()` then the
            retrieved grid response will contain the fid which will be
            necessary to set `self.id` and `self._columns.id` below.

        Example from iterable of columns:
        ```
        column_1 = Column([1, 2, 3], 'time')
        column_2 = Column([4, 2, 5], 'voltage')
        grid = Grid([column_1, column_2])
        ```
        Example from json grid
        ```
        grid_json = {
            'cols': {
                'time': {'data': [1, 2, 3], 'order': 0, 'uid': '4cd7fc'},
                'voltage': {'data': [4, 2, 5], 'order': 1, 'uid': u'2744be'}
            }
        }
        grid = Grid(grid_json)
        ```
        """
        # TODO: verify that columns are actually columns
        if pd and isinstance(columns_or_json, pd.DataFrame):
            duplicate_name = utils.get_first_duplicate(columns_or_json.columns)
            if duplicate_name:
                err = exceptions.NON_UNIQUE_COLUMN_MESSAGE.format(duplicate_name)
                raise exceptions.InputError(err)

            # create columns from dataframe
            all_columns = []
            for name in columns_or_json.columns:
                all_columns.append(Column(columns_or_json[name].tolist(), name))
            self._columns = all_columns
            self.id = ''

        elif isinstance(columns_or_json, dict):
            # check that fid is entered
            if fid is None:
                raise exceptions.PlotlyError(
                    "If you are manually converting a raw json/dict grid "
                    "into a Grid instance, you must ensure that 'fid' is "
                    "set to your file ID. This looks like 'username:187'."
                )

            self.id = fid

            # check if 'cols' is a root key
            if 'cols' not in columns_or_json:
                raise exceptions.PlotlyError(
                    "'cols' must be a root key in your json grid."
                )

            # check if 'data', 'order' and 'uid' are not in columns
            grid_col_keys = ['data', 'order', 'uid']

            for column_name in columns_or_json['cols']:
                for key in grid_col_keys:
                    if key not in columns_or_json['cols'][column_name]:
                        raise exceptions.PlotlyError(
                            "Each column name of your dictionary must have "
                            "'data', 'order' and 'uid' as keys."
                        )
            # collect and sort all orders in case orders do not start
            # at zero or there are jump discontinuities between them
            all_orders = []
            for column_name in columns_or_json['cols'].keys():
                all_orders.append(columns_or_json['cols'][column_name]['order'])
            all_orders.sort()

            # put columns in order in a list
            ordered_columns = []
            for order in all_orders:
                for column_name in columns_or_json['cols'].keys():
                    if columns_or_json['cols'][column_name]['order'] == order:
                        break

                ordered_columns.append(Column(
                    columns_or_json['cols'][column_name]['data'],
                    column_name)
                )
            self._columns = ordered_columns

            # fill in column_ids
            for column in self:
                column.id = self.id + ':' + columns_or_json['cols'][column.name]['uid']

        else:
            column_names = [column.name for column in columns_or_json]
            duplicate_name = utils.get_first_duplicate(column_names)
            if duplicate_name:
                err = exceptions.NON_UNIQUE_COLUMN_MESSAGE.format(duplicate_name)
                raise exceptions.InputError(err)

            self._columns = list(columns_or_json)
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

    def get_column_reference(self, column_name):
        """
        Returns the column reference of given column in the grid by its name.

        Raises an error if the column name is not in the grid. Otherwise,
        returns the fid:uid pair, which may be the empty string.
        """
        column_id = None
        for column in self._columns:
            if column.name == column_name:
                column_id = column.id
                break

        if column_id is None:
            col_names = []
            for column in self._columns:
                col_names.append(column.name)
            raise exceptions.PlotlyError(
                "Whoops, that column name doesn't match any of the column "
                "names in your grid. You must pick from {cols}".format(cols=col_names)
            )
        return column_id
