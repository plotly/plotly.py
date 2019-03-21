import json as _json

from chart_studio.grid_objs import Column
from plotly import utils
from plotly.tests.test_optional.test_utils.test_utils import numeric_list, \
    mixed_list, np_list


def test_column_json_encoding():
    columns = [
        Column(numeric_list, 'col 1'),
        Column(mixed_list, 'col 2'),
        Column(np_list, 'col 3')
    ]
    json_columns = _json.dumps(
        columns, cls=utils.PlotlyJSONEncoder, sort_keys=True
    )
    assert('[{"data": [1, 2, 3], "name": "col 1"}, '
           '{"data": [1, "A", "2014-01-05", '
           '"2014-01-05 01:01:01", '
           '"2014-01-05 01:01:01.000001"], '
           '"name": "col 2"}, '
           '{"data": [1, 2, 3, null, null, null, '
           '"2014-01-05"], "name": "col 3"}]' == json_columns)