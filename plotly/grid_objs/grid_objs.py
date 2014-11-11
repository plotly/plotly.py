"""
grid_objs
=========

"""
from __future__ import absolute_import


import json
from collections import MutableSequence
from plotly import exceptions
from plotly import utils

__all__ = None

class Column(object):
    def __init__(self, data, name):
        # TODO: data type checking
        self.data = data
        # TODO: name type checking
        self.name = name

        self.id = ''

    def __str__(self):
        max_chars = 10
        jdata = json.dumps(self.data, cls=utils._plotlyJSONEncoder)
        if len(jdata) > max_chars:
            data_string = jdata[:max_chars] + "...]"
        else:
            data_string = jdata
        string = '<name="{name}", data={data_string}, id={id}>'
        return string.format(name=self.name, data=data_string, id=self.id)

    def __repr__(self):
        return 'Column("{}", {})'.format(self.data, self.name)

    def to_json(self):
        return {'name': self.name, 'data': self.data}


class Grid(MutableSequence):
    def __init__(self, iterable_of_columns):
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

