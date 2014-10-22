import json

from plotly.grid_objs.grid_objs import Column


class ColumnJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Column):
            return {'name': obj.name, 'data': obj.data}
        else:
            return json.JSONEncoder.default(self, obj)
