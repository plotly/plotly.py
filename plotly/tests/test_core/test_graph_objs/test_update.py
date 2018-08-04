from __future__ import absolute_import
from unittest import skip

import plotly.graph_objs as go
from plotly.graph_objs import Data, Figure, Layout, Line, Scatter, scatter, XAxis
from plotly.tests.utils import strip_dict_params

from unittest import TestCase


class TestUpdateMethod(TestCase):
    def setUp(self):
        print('Setup!')

    def test_update_dict(self):
        title = 'this'
        fig = Figure()
        fig.update(layout=Layout(title=title))
        assert fig == Figure(layout=Layout(title=title))
        fig['layout'].update(xaxis=XAxis())
        assert fig == Figure(layout=Layout(title=title, xaxis=XAxis()))


    def test_update_list(self):
        trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
        trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
        fig = Figure([trace1, trace2])
        update = dict(x=[2, 3, 4], y=[1, 2, 3])
        fig.data[0].update(update)
        fig.data[1].update(update)

        d1, d2 = strip_dict_params(fig.data[0], Scatter(x=[2, 3, 4], y=[1, 2, 3]))
        assert d1 == d2
        d1, d2 = strip_dict_params(fig.data[1], Scatter(x=[2, 3, 4], y=[1, 2, 3]))
        assert d1 == d2


    def test_update_dict_empty(self):
        trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
        trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
        fig = Figure([trace1, trace2])
        fig.update({})
        d1, d2 = strip_dict_params(fig.data[0], Scatter(x=[1, 2, 3], y=[2, 1, 2]))
        assert d1 == d2
        d1, d2 = strip_dict_params(fig.data[1], Scatter(x=[1, 2, 3], y=[3, 2, 1]))
        assert d1 == d2


    def test_update_list_empty(self):
        trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
        trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
        fig = Figure([trace1, trace2])
        fig.update([])
        d1, d2 = strip_dict_params(fig.data[0], Scatter(x=[1, 2, 3], y=[2, 1, 2]))
        assert d1 == d2
        d1, d2 = strip_dict_params(fig.data[1], Scatter(x=[1, 2, 3], y=[3, 2, 1]))
        assert d1 == d2


    @skip('See https://github.com/plotly/python-api/issues/291')
    def test_update_list_make_copies_false(self):
        trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
        trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
        data = Data([trace1, trace2])
        update = dict(x=[2, 3, 4], y=[1, 2, 3], line=Line())
        data.update(update, make_copies=False)
        assert data[0]['line'] is data[1]['line']

    def test_update_uninitialized_list_with_list(self):
        """
        If the original list is undefined, the updated list should be
        accepted in full.

        See GH1072
        """
        layout = go.Layout()
        layout.update(annotations=[
            go.layout.Annotation(text='one'),
            go.layout.Annotation(text='two'),
        ])

        expected = {'annotations': [{'text': 'one'}, {'text': 'two'}]}

        self.assertEqual(len(layout.annotations), 2)
        self.assertEqual(layout.to_plotly_json(), expected)

    def test_update_initialized_empty_list_with_list(self):
        """
        If the original list is empty, treat is just as if it's undefined.
        This is a change in behavior from version 2
        (where the input list would just be completly ignored), because
        in version 3 the difference between an uninitialized and empty list
        is not obvious to the user.
        """
        layout = go.Layout(annotations=[])
        layout.update(annotations=[
            go.layout.Annotation(text='one'),
            go.layout.Annotation(text='two'),
        ])

        expected = {'annotations': [{'text': 'one'}, {'text': 'two'}]}

        self.assertEqual(len(layout.annotations), 2)
        self.assertEqual(layout.to_plotly_json(), expected)

    def test_update_initialized_nonempty_list_with_dict(self):
        """
        If the original list is defined, a dict from
        index numbers to property dicts may be used to update select
        elements of the existing list
        """
        layout = go.Layout(annotations=[
            go.layout.Annotation(text='one'),
            go.layout.Annotation(text='two'),
        ])

        layout.update(annotations={1: go.layout.Annotation(width=30)})

        expected = {'annotations': [{'text': 'one'},
                                    {'text': 'two', 'width': 30}]}

        self.assertEqual(len(layout.annotations), 2)
        self.assertEqual(layout.to_plotly_json(), expected)
