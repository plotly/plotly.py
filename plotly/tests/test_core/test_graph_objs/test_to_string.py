from __future__ import absolute_import

from plotly.graph_objs import Contour, Data, Figure, Layout, Margin, Scatter


def test_to_string():
    fig = Figure(
        data=Data([
            Scatter(
                x=[1, 2, 3, 4],
                y=[10, 15, 13, 17]
            ),
            Scatter(
                x=[1, 2, 3, 4],
                y=[16, 5, 11, 9]
            )
        ]),
        layout=Layout(
            autosize=False,
            width=500,
            height=500,
            margin=Margin(
                l=65,
                r=50,
                b=65,
                t=65
            )
        )
    )
    fig_string = fig.to_string(pretty=False)
    comp_string = ('Figure(\n'
                   '    data=Data([\n'
                   '        Scatter(\n'
                   '            x=[1, 2, 3, 4],\n'
                   '            y=[10, 15, 13, 17]\n'
                   '        ),\n'
                   '        Scatter(\n'
                   '            x=[1, 2, 3, 4],\n'
                   '            y=[16, 5, 11, 9]\n'
                   '        )\n'
                   '    ]),\n'
                   '    layout=Layout(\n'
                   '        autosize=False,\n'
                   '        height=500,\n'
                   '        margin=Margin(\n'
                   '            r=50,\n'
                   '            t=65,\n'
                   '            b=65,\n'
                   '            l=65\n'
                   '        ),\n'
                   '        width=500\n'
                   '    )\n'
                   ')')
    assert fig_string == comp_string


def test_nested_list():
    z = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
          13, 14, 15, 16, 17, 18, 19, 20, 21]]
    print(Contour(z=z).to_string())
