"""
grid_objs
=========

"""

import json


class Column():
    def __init__(self, name, data):
        # TODO: data type checking
        self.data = data
        # TODO: name type checking
        self.name = name

        self.uid = ''

    def __repr__(self):
        jdata = json.dumps(self.data)
        return '<Column "{name}": {data}{ellipses}>'.format(
            name=self.name,
            data=jdata[0:10],
            ellipses='...]' if len(jdata) > 10 else '')


class Grid(list):
    def __init__(self, columns):
        # TODO: column type checking
        column_names = [column.name for column in columns]
        if (len(column_names) > len(set(column_names))):
            # TODO: Descriptive exception
            raise Exception('Duplicate column names')

        return super(Grid, self).__init__(columns)
