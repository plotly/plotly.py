import plotly.tools as tls

from . import plt

def test_plot_bgcolor_defaults_to_white():
    plt.figure()
    plt.plot([0, 1], [0, 1])

    plotly_fig = tls.mpl_to_plotly(plt.gcf())

    assert plotly_fig.layout.template.layout.plot_bgcolor == "white"
