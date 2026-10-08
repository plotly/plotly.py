import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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


def test_drawstyle_maps_to_line_shape():
    cases = {
        "steps-pre": "vh",
        "steps": "vh",
        "steps-post": "hv",
        "steps-mid": "hvh",
    }
    for drawstyle, shape in cases.items():
        fig, ax = plt.subplots()
        ax.plot([0, 1, 2], [0, 1, 0], drawstyle=drawstyle)

        plotly_fig = tls.mpl_to_plotly(fig)

        assert plotly_fig.data[0].line.shape == shape


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


def test_axis_showline_tied_to_main_spine():
    """Test that showline follows the main-side spine (bottom for x, left for y)."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    # Hide the mirror-side spines only
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.showline == True
    assert plotly_fig.layout.yaxis.showline == True


def test_axis_showline_hidden_when_main_spine_hidden():
    """Test that showline is False when the main-side spine is hidden."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    # Hide the main-side spines but keep the mirror-side ones
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.showline == False
    assert plotly_fig.layout.yaxis.showline == False


def test_ticks_hidden_when_mpl_main_ticks_hidden():
    """Test that tick markers are hidden when the mpl main-side ticks are hidden."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    ax.tick_params(top=False, bottom=False, left=False, right=False)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.ticks == ""
    assert plotly_fig.layout.yaxis.ticks == ""


def test_twinx_axis_position_and_ticks():
    """Test that twinx secondary y-axis is on the right with visible ticks and title."""
    fig, ax1 = plt.subplots()
    ax1.plot([0, 1, 2], [0, 1, 4])
    ax1.set_ylabel("left axis")
    ax2 = ax1.twinx()
    ax2.plot([0, 1, 2], [10, 5, 2])
    ax2.set_ylabel("right axis")

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.yaxis.side == "left"
    assert plotly_fig.layout.yaxis.title.text == "left axis"
    assert plotly_fig.layout.yaxis.ticks == "inside"

    assert plotly_fig.layout.yaxis2.side == "right"
    assert plotly_fig.layout.yaxis2.title.text == "right axis"
    assert plotly_fig.layout.yaxis2.ticks == "inside"
    assert plotly_fig.layout.yaxis2.overlaying == "y"
    assert plotly_fig.layout.xaxis2.overlaying == "x"
    assert plotly_fig.layout.xaxis2.visible is False
    assert len(plotly_fig.data) == 2


def test_twiny_axis_position_and_ticks():
    """Test that twiny secondary x-axis is on the top with visible ticks and title."""
    fig, ax1 = plt.subplots()
    ax1.plot([0, 1, 2], [0, 1, 4])
    ax1.set_xlabel("bottom axis")
    ax2 = ax1.twiny()
    ax2.plot([10, 5, 2], [0, 1, 4])
    ax2.set_xlabel("top axis")

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.side == "bottom"
    assert plotly_fig.layout.xaxis.title.text == "bottom axis"
    assert plotly_fig.layout.xaxis.ticks == "inside"

    assert plotly_fig.layout.xaxis2.side == "top"
    assert plotly_fig.layout.xaxis2.title.text == "top axis"
    assert plotly_fig.layout.xaxis2.ticks == "inside"
    assert plotly_fig.layout.xaxis2.overlaying == "x"
    assert plotly_fig.layout.yaxis2.overlaying == "y"
    assert plotly_fig.layout.yaxis2.visible is False
    assert len(plotly_fig.data) == 2


def test_right_axis_ticks_hidden_when_mpl_right_ticks_hidden():
    """Test that ticks are hidden on a right-side axis when right ticks are hidden in matplotlib."""
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax2.tick_params(right=False)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.yaxis2.side == "right"
    assert plotly_fig.layout.yaxis2.ticks == ""


def test_sharex_stacked_lines_in_correct_subplots():
    """Test that vertically stacked subplots with sharex=True place lines in separate subplots."""
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot([1, 2, 3], [4, 5, 6])
    ax2.plot([1, 2, 3], [10, 20, 30])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert len(plotly_fig.data) == 2
    # First line belongs to the top subplot
    assert plotly_fig.data[0].yaxis in (None, "y", "y1")
    # Second line belongs to the bottom subplot
    assert plotly_fig.data[1].yaxis == "y2"

    # Distinct non-overlapping vertical domains (top above bottom)
    assert plotly_fig.layout.yaxis.domain[0] > plotly_fig.layout.yaxis2.domain[1]

    # The bottom subplot must not overlay the top subplot
    assert plotly_fig.layout.yaxis2.overlaying is None
    assert plotly_fig.layout.xaxis2.overlaying is None


def test_violinplot_bodies_are_filled_polygons():
    fig, ax = plt.subplots()
    ax.violinplot(np.random.randn(100, 3))
    plotly_fig = tls.mpl_to_plotly(fig)
    bodies = [t for t in plotly_fig.data if t.fill == "toself" and len(t.x) > 100]
    assert len(bodies) >= 3


def test_pcolor_rectangles_render():
    x = np.linspace(-3, 3, 10)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.pcolor(X, Y, np.sin(X) * np.cos(Y))
    plotly_fig = tls.mpl_to_plotly(fig)
    assert len(plotly_fig.data) == 100
    assert all(len(t.x) >= 4 for t in plotly_fig.data)


def test_boxplot_converts_with_none_marker_facecolor():
    """Boxplot outlier markers use facecolor 'none', which plotly rejects."""
    fig, ax = plt.subplots()
    ax.boxplot(np.random.randn(100, 4))

    plotly_fig = tls.mpl_to_plotly(fig)

    assert len(plotly_fig.data) > 0


def test_line_with_none_color_converts():
    """Lines with color='none' use the string 'none' for the line color,
    which plotly rejects; it must be exported as a transparent line."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], color="none")

    plotly_fig = tls.mpl_to_plotly(fig)

    assert len(plotly_fig.data) == 1
    assert plotly_fig.data[0].line.color == "rgba(0,0,0,0)"


def test_line_with_rgba_color_converts():
    """Line colors that carry their own alpha (rgba tuple or 8-digit hex)
    export as rgba strings."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], color=(1.0, 0.0, 0.0, 0.5))
    ax.plot([0, 1], [1, 0], color="#0000FF80")

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.data[0].line.color == "rgba(255, 0, 0, 0.5)"
    assert plotly_fig.data[1].line.color == "rgba(0, 0, 255, 0.5019607843137255)"


def test_line_rgba_color_with_separate_alpha_converts():
    """An explicit alpha overrides the alpha carried by the line color."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], color=(1.0, 0.0, 0.0, 0.2), alpha=0.5)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.data[0].line.color == "rgba(255, 0, 0, 0.5)"


def test_transparent_text_colors_export():
    """Text, title, and axis labels with color 'none' export transparent
    fonts."""
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, "text", color="none")
    ax.set_title("title", color="none")
    ax.set_xlabel("xlabel", color="none")
    ax.set_ylabel("ylabel", color="none")

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.annotations[0].font.color == "rgba(0,0,0,0)"
    assert plotly_fig.layout.title.font.color == "rgba(0,0,0,0)"
    assert plotly_fig.layout.xaxis.title.font.color == "rgba(0,0,0,0)"
    assert plotly_fig.layout.yaxis.title.font.color == "rgba(0,0,0,0)"


def test_export_color_maps_colors():
    """_export_color maps matplotlib color strings to plotly colors, keeping
    or overriding the alpha as requested."""
    from plotly.matplotlylib.mpltools import _export_color

    expected_mappings = {
        (None, None): None,
        ("none", None): "rgba(0,0,0,0)",
        ("#FF0000", None): "#FF0000",
        ("#FF0000", 1): "rgba(255, 0, 0, 1)",
        ("#FF0000", 0.5): "rgba(255, 0, 0, 0.5)",
        ("rgba(255, 0, 0, 0.2)", None): "rgba(255, 0, 0, 0.2)",
        ("rgba(255, 0, 0, 0.2)", 1): "rgba(255, 0, 0, 0.2)",
        ("rgba(255, 0, 0, 0.2)", 0.5): "rgba(255, 0, 0, 0.5)",
        ("rgb(255, 0, 0)", None): "rgb(255, 0, 0)",
        ("rgb(255, 0, 0)", 0.5): "rgba(255, 0, 0, 0.5)",
        ((1.0, 0.0, 0.0, 0.5), None): "rgba(255, 0, 0, 0.5)",
        ((0.0, 1.0, 0.0, 1.0), None): "#00FF00",
    }
    for (color, opacity), expected in expected_mappings.items():
        result = _export_color(color, opacity)
        assert result == expected, (
            f"Input {color!r} with opacity {opacity!r} produced {result!r}, "
            f"expected {expected!r}"
        )

    assert _export_color(["#FF0000", "none"]) == ["#FF0000", "rgba(0,0,0,0)"]
    assert _export_color(["rgba(255, 0, 0, 0.2)"], 0.5) == ["rgba(255, 0, 0, 0.5)"]


def test_scatter_with_multiple_colors_converts():
    """Scatter markers with per-point colors export a list of marker colors."""
    fig, ax = plt.subplots()
    ax.scatter([0, 1, 2], [0, 1, 2], c=["red", "green", "blue"])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.data[0].mode == "markers"
    assert plotly_fig.data[0].marker.color == (
        "rgba(255,0,0,1.0)",
        "rgba(0,128,0,1.0)",
        "rgba(0,0,255,1.0)",
    )


def test_eventplot_segments_render():
    fig, ax = plt.subplots()
    ax.eventplot([np.random.randn(20) for _ in range(5)])
    plotly_fig = tls.mpl_to_plotly(fig)
    # Each of the 5 event rows is a line collection whose 20 segments are grouped
    assert len(plotly_fig.data) == 5
    assert all(t.x.count(None) == 19 for t in plotly_fig.data)


def test_stackplot_areas_render():
    x = np.arange(10)
    fig, ax = plt.subplots()
    ax.stackplot(x, np.random.rand(10), np.random.rand(10), np.random.rand(10))
    plotly_fig = tls.mpl_to_plotly(fig)
    assert len(plotly_fig.data) >= 3


def test_fill_between_renders():
    x = np.linspace(0, 2 * np.pi, 50)
    fig, ax = plt.subplots()
    ax.fill_between(x, np.sin(x), np.cos(x))
    plotly_fig = tls.mpl_to_plotly(fig)
    assert len(plotly_fig.data) >= 1


def test_collection_alpha():
    """Collection alpha is baked into the facecolor rgba by matplotlib. if
    fillcolor has an alpha channel, the opacity field should not be set."""
    x = np.linspace(0, 2 * np.pi, 50)
    fig, ax = plt.subplots()
    ax.fill_between(x, np.sin(x), np.cos(x), color="red", alpha=0.4)
    plotly_fig = tls.mpl_to_plotly(fig)
    trace = plotly_fig.data[0]
    assert trace.fillcolor == "rgba(255,0,0,0.4)"
    assert trace.opacity is None


def test_violin_body_default_alpha():
    """Violin bodies default to alpha=0.3 in matplotlib, which is
    embedded in their facecolor rgba. If the alpha channel in fillcolor
    is set, the opacity field should not be set."""
    fig, ax = plt.subplots()
    ax.violinplot(np.random.randn(100, 3))
    plotly_fig = tls.mpl_to_plotly(fig)
    bodies = [
        t
        for t in plotly_fig.data
        if t.fill == "toself" and t.fillcolor == "rgba(31,119,180,0.3)"
    ]
    assert len(bodies) >= 3
    assert all(t.opacity is None for t in bodies)


def test_stem_plot_renders():
    x = np.linspace(0, 2 * np.pi, 20)
    fig, ax = plt.subplots()
    ax.stem(x, np.sin(x))
    plotly_fig = tls.mpl_to_plotly(fig)
    # The 20 vertical stem lines are grouped into a single line trace with 19 None separators
    stem_lines = [
        t for t in plotly_fig.data if t.mode == "lines" and t.x.count(None) == 19
    ]
    assert len(stem_lines) == 1


def test_contour_lines_convert():
    """Contour lines must render as lines, not filled polygons."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.contour(X, Y, np.sin(X) * np.cos(Y), 10)
    plotly_fig = tls.mpl_to_plotly(fig)
    assert len(plotly_fig.data) > 0
    assert all(t.fill is None for t in plotly_fig.data)
    assert all(t.mode == "lines" for t in plotly_fig.data)


def test_contourf_bands_render():
    """Contourf bands (multi-subpath collections) must render as fills."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.contourf(X, Y, np.sin(X) * np.cos(Y), 10)
    plotly_fig = tls.mpl_to_plotly(fig)
    filled = [t for t in plotly_fig.data if t.fill == "toself"]
    assert len(filled) > 0


def test_filled_path_collection_date_xaxis():
    """Filled path collections with date x-values must export date strings,
    not raw matplotlib date numbers."""
    dates = [
        datetime.datetime(2023, 1, 1) + datetime.timedelta(days=i) for i in range(10)
    ]
    fig, ax = plt.subplots()
    ax.fill_between(dates, np.sin(np.arange(10)), np.cos(np.arange(10)))
    plotly_fig = tls.mpl_to_plotly(fig)
    filled = [t for t in plotly_fig.data if t.fill == "toself"]
    assert len(filled) >= 1
    assert all(isinstance(x, str) for x in filled[0].x)


def test_background_colors_from_matplotlib_defaults():
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.plot_bgcolor == "#FFFFFF"
    assert plotly_fig.layout.paper_bgcolor == "#FFFFFF"


def test_custom_background_colors_are_preserved():
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("lightyellow")
    ax.set_facecolor("lightgray")
    ax.plot([0, 1], [0, 1])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.plot_bgcolor == "#D3D3D3"
    assert plotly_fig.layout.paper_bgcolor == "#FFFFE0"


def test_semitransparent_axes_background_preserved():
    """Axes backgrounds with alpha export as mpl-style rgba strings, which
    must be passed through as-is, not re-parsed by export_color."""
    fig, ax = plt.subplots()
    ax.set_facecolor((0.1, 0.2, 0.3, 0.4))
    ax.plot([0, 1], [0, 1])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.plot_bgcolor == "rgba(26, 51, 76, 0.4)"


def test_histogram_converts():
    """Histograms must convert without error and keep bargap in plotly's
    valid [0, 1] range; get_bar_gap can return a gap with floating point
    noise for touching bars, which plotly rejects."""
    # Seed 0 makes the first gap slightly negative (-4.4e-16)
    rng = np.random.RandomState(0)
    fig, ax = plt.subplots()
    ax.hist(rng.randn(10000), 30)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert len(plotly_fig.data) == 1
    assert plotly_fig.layout.bargap == 0


def test_line_color_is_valid_plotly_color():
    """Converted line colors are valid plotly color strings: plotly rejects
    a space between 'rgba' and the opening parenthesis."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], color="red")

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.data[0].line.color == "rgba(255, 0, 0, 1)"


def test_non_arithmetic_progression_xtickvals():
    xticks = [0.01, 0.53, 0.75]
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.set_xticks(xticks)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickvals == tuple(xticks)


def test_non_arithmetic_progression_yticks():
    yticks = [0.01, 0.53, 0.75]
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.set_yticks(yticks)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.yaxis.tickvals == tuple(yticks)


def test_non_arithmetic_progression_xticktext():
    xtickvals = [0.01, 0.53, 0.75]
    xticktext = ["Baseline", "param = 1", "param = 2"]
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.set_xticks(xtickvals, xticktext)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickvals == tuple(xtickvals)
    assert plotly_fig.layout.xaxis.ticktext == tuple(xticktext)


def test_fixed_formatter_ticktext():
    import matplotlib.ticker as ticker

    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.xaxis.set_major_locator(ticker.FixedLocator([0.01, 0.53, 0.75]))
    ax.xaxis.set_major_formatter(
        ticker.FixedFormatter(["Baseline", "param = 1", "param = 2"])
    )

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickvals == (0.01, 0.53, 0.75)
    assert plotly_fig.layout.xaxis.ticktext == ("Baseline", "param = 1", "param = 2")


def test_no_legend_entries_for_internal_mpl_labels():
    """mpl internal labels (_nolegend_, _childN) must not become legend entries."""
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 0, 1], "b", [0, 1, 2, 3], [1, 0, 1, 0], "r--")

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.showlegend == False
    assert all(t.name is None for t in plotly_fig.data)


def test_unlabeled_traces_hidden_from_legend_when_figure_has_legend():
    """Traces without labels must have showlegend=False when a figure has a legend."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], label="Labeled line")
    ax.plot([0, 1], [1, 0])  # Unlabeled line
    ax.legend()

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.showlegend == True
    assert len(plotly_fig.data) == 2
    assert plotly_fig.data[0].name == "Labeled line"
    assert plotly_fig.data[0].showlegend is not False
    assert plotly_fig.data[1].name is None
    assert plotly_fig.data[1].showlegend is False


def test_custom_date_xtickvals_are_converted():
    """Custom tick values on a date axis must be converted to date strings,
    not left as raw matplotlib date numbers or datetime objects."""
    dates = [datetime.datetime(2023, 1, i) for i in range(1, 11)]
    fig, ax = plt.subplots()
    ax.plot(dates, np.random.rand(10))
    ax.set_xticks(dates[::3])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickvals == (
        "2023-01-01 00:00:00",
        "2023-01-04 00:00:00",
        "2023-01-07 00:00:00",
        "2023-01-10 00:00:00",
    )


def test_uneven_custom_date_xtickvals_are_converted():
    """Unevenly spaced custom date ticks must be converted to date strings."""
    dates = [datetime.datetime(2023, 1, i) for i in range(1, 11)]
    ticks = [datetime.datetime(2023, 1, i) for i in [1, 3, 6, 10]]
    fig, ax = plt.subplots()
    ax.plot(dates, np.random.rand(10))
    ax.set_xticks(ticks)

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickvals == (
        "2023-01-01 00:00:00",
        "2023-01-03 00:00:00",
        "2023-01-06 00:00:00",
        "2023-01-10 00:00:00",
    )


def test_custom_date_xtickvals_given_as_numbers_are_converted():
    """Custom date ticks given as matplotlib date numbers must be converted
    to date strings."""
    import matplotlib.dates as mdates

    dates = [datetime.datetime(2023, 1, i) for i in range(1, 11)]
    fig, ax = plt.subplots()
    ax.plot(dates, np.random.rand(10))
    ax.set_xticks([mdates.date2num(d) for d in dates[::3]])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickvals == (
        "2023-01-01 00:00:00",
        "2023-01-04 00:00:00",
        "2023-01-07 00:00:00",
        "2023-01-10 00:00:00",
    )


def test_tick_label_color_exports():
    """Tick label colors are exported to the plotly tickfont."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickfont.color == "#000000"


def test_dark_tick_label_color_exports():
    """Dark-background tick label colors are exported to the plotly
    tickfont."""
    with plt.style.context("dark_background"):
        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1])

        plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickfont.color == "#FFFFFF"


def test_transparent_tick_label_color_exports():
    """Transparent tick label colors ('none') export as transparent rgba."""
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.tick_params(labelcolor="none")

    plotly_fig = tls.mpl_to_plotly(fig)

    assert plotly_fig.layout.xaxis.tickfont.color == "rgba(0,0,0,0)"
    assert plotly_fig.layout.yaxis.tickfont.color == "rgba(0,0,0,0)"


def test_contour_rings_are_closed():
    """Closed contour loops (Z codes) must close in plotly, not leave a gap."""
    x = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.contour(X, Y, X**2 + Y**2, levels=[1, 4])
    plotly_fig = tls.mpl_to_plotly(fig)

    assert len(plotly_fig.data) == 2
    assert plotly_fig.data[0].x[0] == plotly_fig.data[0].x[-1]
    assert plotly_fig.data[0].y[0] == plotly_fig.data[0].y[-1]
    assert plotly_fig.data[1].x[0] == plotly_fig.data[1].x[-1]
    assert plotly_fig.data[1].y[0] == plotly_fig.data[1].y[-1]


def test_disjoint_contour_subpaths_are_separated_by_none():
    """Disjoint subpaths of one contour level are drawn in a single trace,
    separated by None so plotly does not connect them."""
    x = np.linspace(-3, 3, 61)
    X, Y = np.meshgrid(x, x)
    # two separate bumps: the 0.5 level is two disjoint rings in one path
    Z = np.exp(-((X + 1.5) ** 2 + Y**2)) + np.exp(-((X - 1.5) ** 2 + Y**2))
    fig, ax = plt.subplots()
    ax.contour(X, Y, Z, levels=[0.5])
    plotly_fig = tls.mpl_to_plotly(fig)

    assert len(plotly_fig.data) == 1
    xs = list(plotly_fig.data[0].x)
    ys = list(plotly_fig.data[0].y)
    x_gaps = [i for i, v in enumerate(xs) if v is None]
    y_gaps = [i for i, v in enumerate(ys) if v is None]
    assert len(x_gaps) == 1
    assert x_gaps == y_gaps

    gap = x_gaps[0]
    rings = [(xs[:gap], ys[:gap]), (xs[gap + 1 :], ys[gap + 1 :])]
    for ring_x, ring_y in rings:
        assert len(ring_x) > 2
        # each ring is closed
        assert ring_x[0] == ring_x[-1]
        assert ring_y[0] == ring_y[-1]
    # one ring around each bump, so no segment bridges the two
    left, right = sorted(rings, key=lambda ring: ring[0][0])
    assert max(left[0]) < 0
    assert min(right[0]) > 0


def test_line_collection_date_xaxis():
    """Line collections with date x-values must export date strings,
    not raw matplotlib date numbers."""
    dates = [
        datetime.datetime(2023, 1, 1) + datetime.timedelta(days=i) for i in range(10)
    ]
    y = np.linspace(0, 10, 10)
    X, Y = np.meshgrid(mdates.date2num(dates), y)
    fig, ax = plt.subplots()
    ax.xaxis_date()
    ax.contour(X, Y, np.sin(X) * np.cos(Y), 5)
    plotly_fig = tls.mpl_to_plotly(fig)
    lines = [t for t in plotly_fig.data if t.mode == "lines"]
    assert len(lines) >= 1
    assert any(isinstance(x, str) for t in lines for x in t.x)
    assert all(x is None or isinstance(x, str) for t in lines for x in t.x)


def test_contour_line_dash_styles():
    """Each contour level keeps its matplotlib dash pattern, exported as a
    px dash list (matplotlib's pattern is already scaled by line width)."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.contour(
        X,
        Y,
        np.sin(X) * np.cos(Y),
        levels=[-0.5, -0.25, 0.25, 0.5],
        colors="k",
        linewidths=1.5,
        linestyles=["dashed", "solid", "dotted", (0, (5, 2, 1, 2))],
    )
    plotly_fig = tls.mpl_to_plotly(fig)

    assert [t.line.dash for t in plotly_fig.data] == [
        "5.55px,2.4px",
        "solid",
        "1.5px,2.475px",
        "7.5px,3px,1.5px,3px",
    ]


def test_contour_line_dash_scales_with_linewidth():
    """matplotlib scales dash patterns by line width; the export follows."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.contour(
        X, Y, np.sin(X) * np.cos(Y), levels=[0.5], linewidths=3, linestyles="dashed"
    )
    plotly_fig = tls.mpl_to_plotly(fig)

    assert len(plotly_fig.data) == 1
    assert plotly_fig.data[0].line.width == 3
    assert plotly_fig.data[0].line.dash == "11.1px,4.8px"


def test_contour_lines_showlegend_false():
    """Contour line traces have showlegend=False so they do not produce legend entries."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.contour(X, Y, np.sin(X) * np.cos(Y), levels=[-0.5, 0.5])
    plotly_fig = tls.mpl_to_plotly(fig)

    assert len(plotly_fig.data) >= 1
    assert all(t.showlegend is False for t in plotly_fig.data)


def test_contour_lines_not_in_legend():
    """Contour lines do not appear in the legend even when a figure legend is present."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], label="Line")
    ax.contour(X, Y, np.sin(X) * np.cos(Y), levels=[-0.5, 0.5])
    ax.legend()
    plotly_fig = tls.mpl_to_plotly(fig)

    contour_traces = [t for t in plotly_fig.data if t.name != "Line"]
    assert len(contour_traces) >= 1
    assert all(t.showlegend is False for t in contour_traces)


def test_consecutive_same_style_lines_grouped_into_one_trace():
    """Consecutive paths with identical styles are grouped into a single trace."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    # 4 contour levels, all black, solid, width 1.5
    ax.contour(
        X,
        Y,
        X**2 + Y**2,
        levels=[1, 2, 3, 4],
        colors="k",
        linestyles="solid",
        linewidths=1.5,
    )
    plotly_fig = tls.mpl_to_plotly(fig)

    # All 4 levels share the same style, so they should be grouped into 1 trace
    assert len(plotly_fig.data) == 1
    trace = plotly_fig.data[0]
    # The trace combines the distinct levels separated by None
    assert trace.x.count(None) >= 3


def test_mixed_style_lines_group_consecutive_matches():
    """Paths are grouped by consecutive matching style (color, width, dash)."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    # 4 levels: 2 negative (dashed by default in mpl), 2 positive (solid by default)
    ax.contour(
        X,
        Y,
        np.sin(X) * np.cos(Y),
        levels=[-0.5, -0.25, 0.25, 0.5],
        colors="k",
        linewidths=1.5,
    )
    plotly_fig = tls.mpl_to_plotly(fig)

    # 2 dashed levels grouped into 1 trace, 2 solid levels grouped into 1 trace -> 2 traces total
    assert len(plotly_fig.data) == 2
    assert plotly_fig.data[0].line.dash != "solid"
    assert plotly_fig.data[1].line.dash == "solid"
