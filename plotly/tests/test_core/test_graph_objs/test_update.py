from __future__ import absolute_import
from unittest import skip, TestCase

from plotly.graph_objs import Data, Figure, Layout, Line, Scatter, XAxis, attr
from plotly.exceptions import PlotlyDictKeyError


def test_update_dict():
    title = 'this'
    fig = Figure()
    fig.update(layout=Layout(title=title))
    assert fig == Figure(layout=Layout(title=title))
    fig['layout'].update(xaxis=XAxis())
    assert fig == Figure(layout=Layout(title=title, xaxis=XAxis()))


class TestMagicUpdates(TestCase):
    def test_update_magic_kwargs(self):
        have = Scatter(y=[1, 2, 3, 4])
        have.update(
            opacity=0.9, line_width=10,
            hoverinfo_font_family="Times",
            marker_colorbar_tickfont_size=10
        )
        want = Scatter({
            "y": [1, 2, 3, 4],
            "opacity": 0.9,
            "line": {"width": 10},
            "hoverinfo": {"font": {"family": "Times"}},
            "marker": {"colorbar": {"tickfont": {"size": 10}}},
        })
        assert have == want

        have2 = (Scatter(y=[1, 2, 3, 4])
            .update(
                opacity=0.9, line_width=10,
                hoverinfo_font_family="Times",
                marker_colorbar_tickfont_size=10
            )
        )
        assert have2 == want

    def test_update_magic_and_attr(self):
        have = Scatter()
        have.update(marker=attr(color="red", line_width=4))
        want = Scatter({
            "marker": {"color": "red", "line": {"width": 4}}
        })
        assert have == want

    def test_cant_update_invalid_attribute(self):
        have = Scatter()
        with self.assertRaises(PlotlyDictKeyError):
            have.update(marker_line_fuzz=42)


def test_update_list():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    data = Data([trace1, trace2])
    update = dict(x=[2, 3, 4], y=[1, 2, 3])
    data.update(update)
    assert data[0] == Scatter(x=[2, 3, 4], y=[1, 2, 3])
    assert data[1] == Scatter(x=[2, 3, 4], y=[1, 2, 3])


def test_update_dict_empty():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    data = Data([trace1, trace2])
    data.update({})
    print(data.to_string())
    assert data[0] == Scatter(x=[1, 2, 3], y=[2, 1, 2])
    assert data[1] == Scatter(x=[1, 2, 3], y=[3, 2, 1])


def test_update_list_empty():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    data = Data([trace1, trace2])
    data.update([])
    print(data.to_string())
    assert data[0] == Scatter(x=[1, 2, 3], y=[2, 1, 2])
    assert data[1] == Scatter(x=[1, 2, 3], y=[3, 2, 1])


@skip('See https://github.com/plotly/python-api/issues/291')
def test_update_list_make_copies_false():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    data = Data([trace1, trace2])
    update = dict(x=[2, 3, 4], y=[1, 2, 3], line=Line())
    data.update(update, make_copies=False)
    assert data[0]['line'] is data[1]['line']


def test_update_list_make_copies_true():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    data = Data([trace1, trace2])
    update = dict(x=[2, 3, 4], y=[1, 2, 3], line=Line())
    data.update(update, make_copies=True)
    assert data[0]['line'] is not data[1]['line']
