import datetime

import numpy as np
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


def test_eventplot_segments_render():
    fig, ax = plt.subplots()
    ax.eventplot([np.random.randn(20) for _ in range(5)])
    plotly_fig = tls.mpl_to_plotly(fig)
    assert len(plotly_fig.data) == 100


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
    assert len(plotly_fig.data) >= 20


def test_contour_lines_convert():
    """Contour lines used to crash with an ndarray line width."""
    x = np.linspace(-3, 3, 30)
    X, Y = np.meshgrid(x, x)
    fig, ax = plt.subplots()
    ax.contour(X, Y, np.sin(X) * np.cos(Y), 10)
    plotly_fig = tls.mpl_to_plotly(fig)
    assert len(plotly_fig.data) > 0


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
