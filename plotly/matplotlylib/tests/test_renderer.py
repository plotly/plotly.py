import plotly.tools as tls

from . import plt


def test_axis_mirror_with_spines_and_ticks():
    """Test that mirror=True when both spines and ticks are visible on both sides."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    # Show all spines
    ax.spines["top"].set_visible(True)
    ax.spines["bottom"].set_visible(True)
    ax.spines["left"].set_visible(True)
    ax.spines["right"].set_visible(True)

    # Show ticks on all sides
    ax.tick_params(top=True, bottom=True, left=True, right=True)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.mirror == "ticks"
    assert plotly_fig.layout.yaxis.mirror == "ticks"


def test_axis_mirror_with_ticks_only():
    """Test that mirror=False when spines are not visible on both sides."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    # Hide opposite spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Show ticks on all sides
    ax.tick_params(top=True, bottom=True, left=True, right=True)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.mirror == False
    assert plotly_fig.layout.yaxis.mirror == False


def test_axis_mirror_false_with_one_sided_ticks():
    """Test that mirror=True when ticks are only on one side but spines are
    visible on both sides."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    # Default matplotlib behavior - ticks only on bottom and left
    ax.tick_params(top=False, bottom=True, left=True, right=False)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.mirror == True
    assert plotly_fig.layout.yaxis.mirror == True


def test_axis_mirror_mixed_configurations():
    """Test different configurations for x and y axes."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    # X-axis: spines and ticks on both sides (mirror="ticks")
    ax.spines["top"].set_visible(True)
    ax.spines["bottom"].set_visible(True)
    ax.tick_params(top=True, bottom=True)

    # Y-axis: spine only on one side (mirror=False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(True)
    ax.tick_params(left=True, right=True)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.mirror == "ticks"
    assert plotly_fig.layout.yaxis.mirror == False
