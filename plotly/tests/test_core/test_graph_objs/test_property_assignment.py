from unittest import TestCase
import plotly.graph_objs as go

from plotly.tests.utils import strip_dict_params


class TestAssignmentPrimitive(TestCase):

    def setUp(self):
        # Construct initial scatter object
        self.scatter = go.Scatter(name='scatter A')

        # Assert initial state
        d1, d2 = strip_dict_params(
            self.scatter,
            {'type': 'scatter',
             'name': 'scatter A'}
        )
        assert d1 == d2

        # Construct expected results
        self.expected_toplevel = {
            'type': 'scatter',
            'name': 'scatter A',
            'fillcolor': 'green'}

        self.expected_nested = {
            'type': 'scatter',
            'name': 'scatter A',
            'marker': {'colorbar': {'titlefont':
                                    {'family': 'courier'}}}}

    def test_toplevel_attr(self):
        assert self.scatter.fillcolor is None
        self.scatter.fillcolor = 'green'
        assert self.scatter.fillcolor == 'green'

        d1, d2 = strip_dict_params(self.scatter, self.expected_toplevel)
        assert d1 == d2

    def test_toplevel_item(self):
        assert self.scatter['fillcolor'] is None
        self.scatter['fillcolor'] = 'green'
        assert self.scatter['fillcolor'] == 'green'

        d1, d2 = strip_dict_params(self.scatter, self.expected_toplevel)
        assert d1 == d2

    def test_nested_attr(self):
        assert self.scatter.marker.colorbar.titlefont.family is None
        self.scatter.marker.colorbar.titlefont.family = 'courier'
        assert self.scatter.marker.colorbar.titlefont.family == 'courier'
        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_item(self):
        assert (self.scatter['marker']['colorbar']['titlefont']['family']
                is None)
        self.scatter['marker']['colorbar']['titlefont']['family'] = 'courier'
        assert (self.scatter['marker']['colorbar']['titlefont']['family']
                == 'courier')
        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_item_dots(self):
        assert self.scatter['marker.colorbar.titlefont.family'] is None
        self.scatter['marker.colorbar.titlefont.family'] = 'courier'
        assert self.scatter['marker.colorbar.titlefont.family'] == 'courier'
        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_item_tuple(self):
        assert self.scatter['marker.colorbar.titlefont.family'] is None
        self.scatter[('marker', 'colorbar', 'titlefont', 'family')] = 'courier'
        assert (self.scatter[('marker', 'colorbar', 'titlefont', 'family')]
                == 'courier')
        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_update(self):
        self.scatter.update(
            marker={'colorbar': {'titlefont': {'family': 'courier'}}})
        assert (self.scatter[('marker', 'colorbar', 'titlefont', 'family')]
                == 'courier')
        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2


class TestAssignmentCompound(TestCase):

    def setUp(self):
        # Construct initial scatter object
        self.scatter = go.Scatter(name='scatter A')

        # Assert initial state
        d1, d2 = strip_dict_params(
            self.scatter,
            {'type': 'scatter',
             'name': 'scatter A'}
        )
        assert d1 == d2

        # Construct expected results
        self.expected_toplevel = {
            'type': 'scatter',
            'name': 'scatter A',
            'marker': {'color': 'yellow',
                       'size': 10}}

        self.expected_nested = {
            'type': 'scatter',
            'name': 'scatter A',
            'marker': {'colorbar': {
                'bgcolor': 'yellow',
                'thickness': 5}}}

    def test_toplevel_obj(self):
        d1, d2 = strip_dict_params(self.scatter.marker, {})
        assert d1 == d2
        self.scatter.marker = go.scatter.Marker(color='yellow', size=10)

        assert isinstance(self.scatter.marker, go.scatter.Marker)
        d1, d2 = strip_dict_params(self.scatter.marker,
                                   self.expected_toplevel['marker'])
        assert d1 == d2

        d1, d2 = strip_dict_params(self.scatter, self.expected_toplevel)
        assert d1 == d2

    def test_toplevel_dict(self):
        d1, d2 = strip_dict_params(self.scatter['marker'], {})
        assert d1 == d2
        self.scatter['marker'] = dict(color='yellow', size=10)

        assert isinstance(self.scatter['marker'], go.scatter.Marker)
        d1, d2 = strip_dict_params(self.scatter.marker,
                                   self.expected_toplevel['marker'])
        assert d1 == d2

        d1, d2 = strip_dict_params(self.scatter, self.expected_toplevel)
        assert d1 == d2

    def test_nested_obj(self):
        d1, d2 = strip_dict_params(self.scatter.marker.colorbar, {})
        assert d1 == d2
        self.scatter.marker.colorbar = go.scatter.marker.ColorBar(
            bgcolor='yellow', thickness=5)

        assert isinstance(self.scatter.marker.colorbar,
                          go.scatter.marker.ColorBar)
        d1, d2 = strip_dict_params(self.scatter.marker.colorbar,
                                   self.expected_nested['marker']['colorbar'])
        assert d1 == d2

        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_dict(self):
        d1, d2 = strip_dict_params(self.scatter['marker']['colorbar'], {})
        assert d1 == d2
        self.scatter['marker']['colorbar'] = dict(
            bgcolor='yellow', thickness=5)

        assert isinstance(self.scatter['marker']['colorbar'],
                          go.scatter.marker.ColorBar)
        d1, d2 = strip_dict_params(self.scatter['marker']['colorbar'],
                                   self.expected_nested['marker']['colorbar'])
        assert d1 == d2

        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_dict_dot(self):
        d1, d2 = strip_dict_params(self.scatter.marker.colorbar, {})
        assert d1 == d2
        self.scatter['marker.colorbar'] = dict(
            bgcolor='yellow', thickness=5)

        assert isinstance(self.scatter['marker.colorbar'],
                          go.scatter.marker.ColorBar)
        d1, d2 = strip_dict_params(self.scatter['marker.colorbar'],
                                   self.expected_nested['marker']['colorbar'])
        assert d1 == d2

        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_dict_tuple(self):
        d1, d2 = strip_dict_params(self.scatter[('marker', 'colorbar')], {})
        assert d1 == d2
        self.scatter[('marker', 'colorbar')] = dict(
            bgcolor='yellow', thickness=5)

        assert isinstance(self.scatter[('marker', 'colorbar')],
                          go.scatter.marker.ColorBar)
        d1, d2 = strip_dict_params(self.scatter[('marker', 'colorbar')],
                                   self.expected_nested['marker']['colorbar'])
        assert d1 == d2

        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_update_obj(self):

        self.scatter.update(
            marker={'colorbar':
                    go.scatter.marker.ColorBar(bgcolor='yellow',
                                               thickness=5)})

        assert isinstance(self.scatter['marker']['colorbar'],
                          go.scatter.marker.ColorBar)
        d1, d2 = strip_dict_params(self.scatter['marker']['colorbar'],
                                   self.expected_nested['marker']['colorbar'])
        assert d1 == d2

        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2

    def test_nested_update_dict(self):

        self.scatter.update(
            marker={'colorbar': dict(bgcolor='yellow', thickness=5)})

        assert isinstance(self.scatter['marker']['colorbar'],
                          go.scatter.marker.ColorBar)
        d1, d2 = strip_dict_params(self.scatter['marker']['colorbar'],
                                   self.expected_nested['marker']['colorbar'])
        assert d1 == d2

        d1, d2 = strip_dict_params(self.scatter, self.expected_nested)
        assert d1 == d2


class TestAssignmnetNone(TestCase):

    def test_toplevel(self):
        # Initialize scatter
        scatter = go.Scatter(name='scatter A',
                             y=[3, 2, 4],
                             marker={
                                 'colorbar': {'titlefont':
                                              {'family': 'courier'}}})
        expected = {
            'type': 'scatter',
            'name': 'scatter A',
            'y': [3, 2, 4],
            'marker': {'colorbar': {'titlefont':
                                    {'family': 'courier'}}}}

        d1, d2 = strip_dict_params(scatter, expected)
        assert d1 == d2

        # Set property not defined to None
        scatter.x = None
        d1, d2 = strip_dict_params(scatter, expected)
        assert d1 == d2

        scatter['line.width'] = None
        d1, d2 = strip_dict_params(scatter, expected)
        assert d1 == d2

        # Set defined property to None
        scatter.y = None
        expected.pop('y')
        d1, d2 = strip_dict_params(scatter, expected)
        assert d1 == d2

        # Set compound properties to None
        scatter[('marker', 'colorbar', 'titlefont')] = None
        expected['marker']['colorbar'].pop('titlefont')
        d1, d2 = strip_dict_params(scatter, expected)
        assert d1 == d2

        scatter.marker = None
        expected.pop('marker')
        d1, d2 = strip_dict_params(scatter, expected)
        assert d1 == d2


class TestAssignCompoundArray(TestCase):

    def setUp(self):
        # Construct initial scatter object
        self.parcoords = go.Parcoords(name='parcoords A')

        # Assert initial state
        d1, d2 = strip_dict_params(
            self.parcoords,
            {'type': 'parcoords',
             'name': 'parcoords A'}
        )
        assert d1 == d2

        # Construct expected results
        self.expected_toplevel = {
            'type': 'parcoords',
            'name': 'parcoords A',
            'dimensions': [
                {'values': [2, 3, 1], 'visible': True},
                {'values': [1, 2, 3], 'label': 'dim1'}]}

        self.layout = go.Layout()

        self.expected_layout1 = {
            'updatemenus': [{},
                            {'font': {'family': 'courier'}}]
        }

        self.expected_layout2 = {
            'updatemenus': [{},
                            {'buttons': [
                                {}, {}, {'method': 'restyle'}]}]
        }

    def test_assign_toplevel_array(self):
        self.assertEqual(self.parcoords.dimensions, ())

        self.parcoords['dimensions'] = [
            go.parcoords.Dimension(values=[2, 3, 1], visible=True),
            dict(values=[1, 2, 3], label='dim1')]

        self.assertEqual(self.parcoords.to_plotly_json(),
                         self.expected_toplevel)

    def test_assign_nested_attr(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]
        self.assertEqual(self.layout['updatemenus'],
                         (go.layout.Updatemenu(), go.layout.Updatemenu()))

        self.layout.updatemenus[1].font.family = 'courier'
        d1, d2 = strip_dict_params(self.layout, self.expected_layout1)
        assert d1 == d2

    def test_assign_double_nested_attr(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout.updatemenus[1].buttons = [{}, {}, {}]

        # Assign
        self.layout.updatemenus[1].buttons[2].method = 'restyle'

        # Check
        self.assertEqual(
            self.layout.updatemenus[1].buttons[2].method,
            'restyle')
        d1, d2 = strip_dict_params(self.layout, self.expected_layout2)
        assert d1 == d2

    def test_assign_double_nested_item(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout['updatemenus'][1]['buttons'] = [{}, {}, {}]

        # Assign
        self.layout['updatemenus'][1]['buttons'][2]['method'] = 'restyle'

        # Check
        self.assertEqual(
            self.layout['updatemenus'][1]['buttons'][2]['method'],
            'restyle'
        )

        d1, d2 = strip_dict_params(self.layout, self.expected_layout2)
        assert d1 == d2

    def test_assign_double_nested_tuple(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout[('updatemenus', 1, 'buttons')] = [{}, {}, {}]

        # Assign
        self.layout[('updatemenus', 1, 'buttons', 2, 'method')] = 'restyle'

        # Check
        self.assertEqual(
            self.layout[('updatemenus', 1, 'buttons', 2, 'method')],
            'restyle')

        d1, d2 = strip_dict_params(self.layout, self.expected_layout2)
        assert d1 == d2

    def test_assign_double_nested_dot(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout['updatemenus'] = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout['updatemenus.1.buttons'] = [{}, {}, {}]

        # Assign
        self.layout['updatemenus[1].buttons[2].method'] = 'restyle'

        # Check
        self.assertEqual(
            self.layout['updatemenus[1].buttons[2].method'],
            'restyle')
        d1, d2 = strip_dict_params(self.layout, self.expected_layout2)
        assert d1 == d2

    def test_assign_double_nested_update_dict(self):

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout.updatemenus[1].buttons = [{}, {}, {}]

        # Update
        self.layout.update(
            updatemenus={1: {'buttons': {2: {'method': 'restyle'}}}})

        # Check
        self.assertEqual(
            self.layout.updatemenus[1].buttons[2].method,
            'restyle')
        d1, d2 = strip_dict_params(self.layout, self.expected_layout2)
        assert d1 == d2

    def test_assign_double_nested_update_array(self):

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout.updatemenus[1].buttons = [{}, {}, {}]

        # Update
        self.layout.update(
            updatemenus=[{}, {'buttons': [{}, {}, {'method': 'restyle'}]}])

        # Check
        self.assertEqual(
            self.layout.updatemenus[1].buttons[2].method,
            'restyle')
        d1, d2 = strip_dict_params(self.layout, self.expected_layout2)
        assert d1 == d2


