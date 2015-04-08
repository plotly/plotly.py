import sys
from unittest import TestCase

from plotly.utils import PlotlyJSONEncoder

if sys.version[:3] == '2.6':
    import simplejson as json
else:
    import json


class TestJSONEncoder(TestCase):

    def test_nan_to_null(self):
        array = [1, float('NaN'), float('Inf'), float('-Inf'), 'platypus']
        result = json.dumps(array, cls=PlotlyJSONEncoder)
        expected_result = '[1, null, null, null, "platypus"]'
        self.assertEqual(result, expected_result)
