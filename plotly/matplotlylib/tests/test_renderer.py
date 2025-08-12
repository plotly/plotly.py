import matplotlib.pyplot as plt
import plotly.tools as tls


def test_native_legend_enabled_when_matplotlib_legend_present():
    """Test that when matplotlib legend is present, Plotly uses native legend."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], label="Line 1")
    ax.plot([0, 1], [1, 0], label="Line 2")
    ax.legend()

    plotly_fig = tls.mpl_to_plotly(fig)

    # Should enable native legend
    assert plotly_fig.layout.showlegend == True
    # Should have 2 traces with names
    assert len(plotly_fig.data) == 2
    assert plotly_fig.data[0].name == "Line 1"
    assert plotly_fig.data[1].name == "Line 2"


def test_no_fake_legend_shapes_with_native_legend():
    """Test that fake legend shapes are not created when using native legend."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], "o-", label="Data with markers")
    ax.legend()

    plotly_fig = tls.mpl_to_plotly(fig)

    # Should use native legend
    assert plotly_fig.layout.showlegend == True
    # Should not create fake legend elements
    assert len(plotly_fig.layout.shapes) == 0
    assert len(plotly_fig.layout.annotations) == 0


def test_legend_disabled_when_no_matplotlib_legend():
    """Test that legend is not enabled when no matplotlib legend is present."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], label="Line 1")  # Has label but no legend() call

    plotly_fig = tls.mpl_to_plotly(fig)

    # Should not have showlegend explicitly set to True
    # (Plotly's default behavior when no legend elements exist)
    assert (
        not hasattr(plotly_fig.layout, "showlegend")
        or plotly_fig.layout.showlegend != True
    )


def test_legend_disabled_when_matplotlib_legend_not_visible():
    """Test that legend is not enabled when no matplotlib legend is not visible."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], label="Line 1")
    legend = ax.legend()
    legend.set_visible(False)  # Hide the legend

    plotly_fig = tls.mpl_to_plotly(fig)

    # Should not enable legend when matplotlib legend is hidden
    assert (
        not hasattr(plotly_fig.layout, "showlegend")
        or plotly_fig.layout.showlegend != True
    )


def test_multiple_traces_native_legend():
    """Test native legend works with multiple traces of different types."""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 0], "-", label="Line")
    ax.plot([0, 1, 2], [1, 0, 1], "o", label="Markers")
    ax.plot([0, 1, 2], [0.5, 0.5, 0.5], "s-", label="Line+Markers")
    ax.legend()

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.showlegend == True
    assert len(plotly_fig.data) == 3
    assert plotly_fig.data[0].name == "Line"
    assert plotly_fig.data[1].name == "Markers"
    assert plotly_fig.data[2].name == "Line+Markers"
    # Verify modes are correct
    assert plotly_fig.data[0].mode == "lines"
    assert plotly_fig.data[1].mode == "markers"
    assert plotly_fig.data[2].mode == "lines+markers"



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
