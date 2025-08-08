import plotly.tools as tls

from . import plt

def test_axis_linecolor_defaults_to_black():
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.linecolor == "black"
    assert plotly_fig.layout.yaxis.linecolor == "black"
