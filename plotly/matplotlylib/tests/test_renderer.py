import plotly.tools as tls

from . import plt

def test_lines_markers_legend_plot():
    x = [0, 1]
    y = [0, 1]
    label = "label"
    plt.figure()
    plt.plot(x, y, "o-", label=label)
    plt.legend()

    plotly_fig = tls.mpl_to_plotly(plt.gcf())

    assert plotly_fig.data[0].mode == "lines+markers"
    assert plotly_fig.data[0].x == tuple(x)
    assert plotly_fig.data[0].y == tuple(y)
    assert plotly_fig.data[0].name == "label"
