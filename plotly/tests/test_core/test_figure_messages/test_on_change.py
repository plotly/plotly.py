import sys
from unittest import TestCase
from nose.tools import raises

import plotly.graph_objs as go

if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


class TestOnChangeCallbacks(TestCase):
    def setUp(self):
        # Construct initial scatter object
        self.figure = go.Figure(data=[
            go.Scatter(y=[3, 2, 1], marker={'color': 'green'}),
            go.Bar(y=[3, 2, 1, 0, -1], marker={'opacity': 0.5})],
                                layout={
                                    'xaxis': {'range': [-1, 4]},
                                    'width': 1000},
                                frames=[go.Frame(
                                    layout={'yaxis':
                                            {'title': 'f1'}})])

    # on_change validation
    # --------------------
    @raises(ValueError)
    def test_raise_if_no_figure(self):
        scatt = go.Scatter()
        fn = MagicMock()
        scatt.on_change(fn, 'x')

    @raises(ValueError)
    def test_raise_on_frame_hierarchy(self):
        fn = MagicMock()
        self.figure.frames[0].layout.xaxis.on_change(fn, 'range')

    @raises(ValueError)
    def test_validate_property_path_nested(self):
        fn = MagicMock()
        self.figure.layout.xaxis.on_change(fn, 'bogus')

    @raises(ValueError)
    def test_validate_property_path_nested(self):
        fn = MagicMock()
        self.figure.layout.on_change(fn, 'xaxis.titlefont.bogus')

    # Python triggered changes
    # ------------------------
    def test_single_prop_callback_on_assignment(self):
        # Install callbacks on 'x', and 'y' property of first trace
        fn_x = MagicMock()
        fn_y = MagicMock()
        self.figure.data[0].on_change(fn_x, 'x')
        self.figure.data[0].on_change(fn_y, 'y')

        # Setting x and y on second trace does not trigger callback
        self.figure.data[1].x = [1, 2, 3]
        self.figure.data[1].y = [1, 2, 3]

        self.assertFalse(fn_x.called)
        self.assertFalse(fn_y.called)

        # Set x on first trace
        self.figure.data[0].x = [10, 20, 30]
        fn_x.assert_called_once_with(self.figure.data[0], (10, 20, 30))
        self.assertFalse(fn_y.called)

        # Set y on first trace
        self.figure.data[0].y = [11, 22, 33]
        fn_y.assert_called_once_with(self.figure.data[0], (11, 22, 33))

    def test_multi_prop_callback_on_assignment_trace(self):
        # Register callback if either 'x' or 'y' changes on first trace
        fn = MagicMock()
        self.figure.data[0].on_change(fn, 'x', 'y')

        # Perform assignment on one of the properties
        self.figure.data[0].x = [11, 22, 33]

        # Check function called once with new value of x and old value of y
        fn.assert_called_once_with(self.figure.data[0],
                                   (11, 22, 33),
                                   (3, 2, 1))

    def test_multi_prop_callback_on_assignment_layout(self):
        fn_range = MagicMock()

        # Register callback if either axis range is changed. Both tuple and
        # dot syntax are supported for nested properties
        self.figure.layout.on_change(fn_range,
                                     ('xaxis', 'range'),
                                     'yaxis.range')

        self.figure.layout.xaxis.range = [-10, 10]
        fn_range.assert_called_once_with(self.figure.layout, (-10, 10), None)

    def test_multi_prop_callback_on_assignment_layout_nested(self):
        fn_titlefont = MagicMock()
        fn_xaxis = MagicMock()
        fn_layout = MagicMock()

        # Register callback on change to family property under titlefont
        self.figure.layout.xaxis.titlefont.on_change(fn_titlefont,
                                                     'family')

        # Register callback on the range and titlefont.family properties
        # under xaxis
        self.figure.layout.xaxis.on_change(fn_xaxis,
                                           'range',
                                           'titlefont.family')

        # Register callback on xaxis object itself
        self.figure.layout.on_change(fn_layout, 'xaxis')

        # Assign a new xaxis range and titlefont.family
        self.figure.layout.xaxis.titlefont.family = 'courier'

        # Check that all callbacks were executed once
        fn_titlefont.assert_called_once_with(
            self.figure.layout.xaxis.titlefont,
            'courier')

        fn_xaxis.assert_called_once_with(
            self.figure.layout.xaxis,
            (-1, 4),
            'courier')

        fn_layout.assert_called_once_with(
            self.figure.layout,
            go.layout.XAxis(range=(-1, 4), titlefont={'family': 'courier'}))

    def test_prop_callback_nested_arrays(self):

        # Initialize updatemenus and buttons
        self.figure.layout.updatemenus = [{}, {}, {}]
        self.figure.layout.updatemenus[2].buttons = [{}, {}]
        self.figure.layout.updatemenus[2].buttons[1].label = 'button 1'
        self.figure.layout.updatemenus[2].buttons[1].method = 'relayout'

        # Register method callback
        fn_button = MagicMock()
        fn_layout = MagicMock()

        self.figure.layout.updatemenus[2].buttons[1].on_change(
            fn_button, 'method')

        self.figure.layout.on_change(
            fn_layout, 'updatemenus[2].buttons[1].method')

        # Update button method
        self.figure.layout.updatemenus[2].buttons[1].method = 'restyle'

        # Check that both callbacks are called once
        fn_button.assert_called_once_with(
            self.figure.layout.updatemenus[2].buttons[1], 'restyle')

        fn_layout.assert_called_once_with(self.figure.layout, 'restyle')

    def test_callback_on_update(self):
        fn_range = MagicMock()
        self.figure.layout.on_change(fn_range,
                                     'xaxis.range',
                                     'yaxis.range')

        self.figure.update({'layout': {'yaxis': {'range': [11, 22]}}})
        fn_range.assert_called_once_with(self.figure.layout,
                                         (-1, 4),
                                         (11, 22))

    def test_callback_on_update_single_call(self):
        fn_range = MagicMock()
        self.figure.layout.on_change(fn_range,
                                     'xaxis.range',
                                     'yaxis.range',
                                     'width')

        self.figure.update({'layout': {
            'xaxis': {'range': [-10, 10]},
            'yaxis': {'range': [11, 22]}}})

        # Even though both properties changed, callback should be called
        # only once with the new value of both properties
        fn_range.assert_called_once_with(self.figure.layout,
                                         (-10, 10),
                                         (11, 22),
                                         1000)

    def test_callback_on_batch_update(self):
        fn_range = MagicMock()
        self.figure.layout.on_change(fn_range,
                                     'xaxis.range',
                                     'yaxis.range',
                                     'width')

        with self.figure.batch_update():
            self.figure.layout.xaxis.range = [-10, 10]
            self.figure.layout.width = 500
            # Check fn not called before context exits
            self.assertFalse(fn_range.called)

        fn_range.assert_called_once_with(self.figure.layout,
                                         (-10, 10),
                                         None,
                                         500)

    def test_callback_on_batch_animate(self):
        fn_range = MagicMock()
        self.figure.layout.on_change(fn_range,
                                     'xaxis.range',
                                     'yaxis.range',
                                     'width')

        with self.figure.batch_animate():
            self.figure['layout.xaxis.range'] = [-10, 10]
            self.figure[('layout', 'yaxis', 'range')] = (11, 22)
            # Check fn not called before context exits
            self.assertFalse(fn_range.called)

        fn_range.assert_called_once_with(self.figure.layout,
                                         (-10, 10),
                                         (11, 22),
                                         1000)

    def test_callback_on_plotly_relayout(self):
        fn_range = MagicMock()
        self.figure.layout.on_change(fn_range,
                                     'xaxis.range',
                                     'yaxis.range',
                                     'width')

        self.figure.plotly_relayout(
            relayout_data={'xaxis.range': [-10, 10],
                           'yaxis.range': [11, 22]})

        fn_range.assert_called_once_with(self.figure.layout,
                                         (-10, 10),
                                         (11, 22),
                                         1000)

    def test_callback_on_plotly_restyle(self):
        # Register callback if either 'x' or 'y' changes on first trace
        fn = MagicMock()
        self.figure.data[0].on_change(fn, 'x', 'y')

        # Perform assignment on one of pthe properties
        self.figure.plotly_restyle({'x': [[11, 22, 33],
                                          [1, 11, 111]]},
                                   trace_indexes=[0, 1])

        # Check function called once with new value of x and old value of y
        fn.assert_called_once_with(self.figure.data[0],
                                   (11, 22, 33),
                                   (3, 2, 1))

    def test_callback_on_plotly_update(self):
        fn_range = MagicMock()
        self.figure.layout.on_change(fn_range,
                                     'xaxis.range',
                                     'yaxis.range',
                                     'width')

        self.figure.plotly_update(
            restyle_data={'marker.color': 'blue'},
            relayout_data={'xaxis.range': [-10, 10],
                           'yaxis.range': [11, 22]})

        fn_range.assert_called_once_with(self.figure.layout,
                                         (-10, 10),
                                         (11, 22),
                                         1000)
