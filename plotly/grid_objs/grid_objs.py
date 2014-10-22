"""
grid_objs
=========

"""

import json
from collections import MutableSequence


class Column():
    def __init__(self, name, data):
        # TODO: data type checking
        self.data = data
        # TODO: name type checking
        self.name = name

        self.id = ''

    def __repr__(self):
        jdata = json.dumps(self.data)
        return '<Column "{name}": {data}{ellipses}>'.format(
            name=self.name,
            data=jdata[0:10],
            ellipses='...]' if len(jdata) > 20 else '')


class Grid(MutableSequence):
    def __init__(self, iterable_of_columns):
        column_names = [column.name for column in iterable_of_columns]
        if (len(column_names) > len(set(column_names))):
            # TODO: Descriptive exception
            raise Exception('duplicate!')
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
            # TODO: Descriptive exception
            raise Exception('duplicate')

    def get_column(self, column_name):
        return next(column for column in self._columns if column.name==column_name)
