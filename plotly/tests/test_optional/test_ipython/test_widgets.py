import six
from unittest import TestCase

version = six.sys.version_info[:2]  # need this for conditional testing

# unittest `skip` not supported in 2.6 and IPython not supported in 2.6/3.2
if version < (2, 7) or (2, 7) < version < (3, 3):
    pass
else:
    from plotly.widgets import GraphWidget


    class TestWidgets(TestCase):

        def test_instantiate_graph_widget(self):
            widget = GraphWidget
