import plotly.tools as tls

from . import plt


def test_non_arithmetic_progression_xtickvals():
    xticks = [0.01, 0.53, 0.75]
    plt.figure()
    plt.plot([0, 1], [0, 1])
    plt.xticks(xticks)

    plotly_fig = tls.mpl_to_plotly(plt.gcf())

    assert plotly_fig.layout.xaxis.tickvals == tuple(xticks)


def test_non_arithmetic_progression_xticktext():
    xtickvals = [0.01, 0.53, 0.75]
    xticktext = ["Baseline", "param = 1", "param = 2"]
    plt.figure()
    plt.plot([0, 1], [0, 1])
    plt.xticks(xtickvals, xticktext)

    plotly_fig = tls.mpl_to_plotly(plt.gcf())

    assert plotly_fig.layout.xaxis.tickvals == tuple(xtickvals)
    assert plotly_fig.layout.xaxis.ticktext == tuple(xticktext)
