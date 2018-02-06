#
# Note that the following themes used values from the matplotlib style library
# (https://github.com/matplotlib/matplotlib/tree/master/lib/matplotlib/mpl-data/stylelib):
#
# - ggplot
# - fivethirtyeight
# - seaborn
#

from . import graph_objs as go
from .graph_objs_tools import Cycler


def ggplot_theme():
    axis = dict(showgrid=True, gridcolor="#cbcbcb",
                linewidth=1.0, linecolor="#f0f0f0",
                ticklen=0.0, tickcolor="#555555", ticks="outside",
                titlefont={"size": 12, "color": "#555555"})
    layout = go.Layout(dict(
        plot_bgcolor="E5E5E5", paper_bgcolor="white",
        font={"size": 10}, xaxis=axis, yaxis=axis, titlefont={"size": 14}
    ))
    marker_color = Cycler(["#E24A33", "#348ABD", "#988ED5", "#777777",
                           "#FBC15E", "#8EBA42", "#FFB5B8"])
    global_trace = dict(marker={
        "color": marker_color,
        "line": {"width": 0.5, "color": "#348ABD"}
    })
    return go.PlotlyTheme(global_trace=global_trace, layout=layout)


def fivethirtyeight_theme():
    scatter = go.Scatter(line={"width": 4})
    axis = dict(showgrid=True, gridcolor="#cbcbcb",
                linewidth=1.0, linecolor="#f0f0f0",
                ticklen=0.0, tickcolor="#555555", ticks="outside",
                titlefont=dict(size=12, color="#555555"))
    layout = go.Layout(
        plot_bgcolor="#f0f0f0",
        paper_bgcolor="#f0f0f0",
        font=dict(size=14),
        xaxis=axis,
        yaxis=axis,
        legend=dict(borderwidth=1.0, bgcolor="f0f0f0", bordercolor="f0f0f0"),
        titlefont={"size": 14})
    colors = ["#008fd5", "#fc4f30", "#e5ae38", "#6d904f",
              "#8b8b8b", "#810f7c"]
    global_trace = dict(marker={"color": Cycler(colors)})
    return go.PlotlyTheme(
        global_trace=global_trace, layout=layout, scatter=scatter
    )


def seaborn_theme():
    heatmap = go.Heatmap(colorscale="Greys")
    scatter = go.Scatter(
        marker=dict(size=9, line={"width": 0}),
        line={"width": 1.75}
    )
    axis = dict(showgrid=True, gridcolor="white",
                linewidth=1.0, linecolor="white",
                ticklen=0.0, tickcolor="#555555", ticks="outside",
                tickfont=dict(size=10),
                titlefont=dict(size=12, color="#555555"))
    # TODO: major vs minor ticks...
    layout = go.Layout(
        plot_bgcolor="EAEAF2",
        paper_bgcolor="white",
        width=800,
        height=550,
        font=dict(family="Arial", size=14, color=0.15),
        xaxis=axis,
        yaxis=axis,
        legend=dict(font=dict(size=10),
                    bgcolor="white", bordercolor="white"),
        titlefont=dict(size=14))
    colors = ["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974", "#64B5CD"]
    global_trace = {"marker": {"color": Cycler(colors)}}
    return go.PlotlyTheme(
        global_trace=global_trace, layout=layout, scatter=scatter,
        heatmap=heatmap
    )


def tomorrow_night_eighties_theme():
    bgcolor = "#2d2d2d"  # Background
    grid_color = "#515151"  # Selection
    label_color = "#cccccc"  # Comment
    colors = ["#cc99cc", "#66cccc", "#f2777a", "#ffcc66",
              "#99cc99", "#f99157", "#6699cc"]

    axis = dict(showgrid=True, gridcolor=grid_color, gridwidth=0.35,
                linecolor=grid_color,
                titlefont=dict(color=label_color, size=14),
                linewidth=1.2, tickcolor=label_color)

    layout = go.Layout(
        plot_bgcolor=bgcolor,
        paper_bgcolor=bgcolor,
        xaxis=axis,
        yaxis=axis,
        font=dict(size=10, color=label_color),
        titlefont=dict(size=14),
        margin=dict(l=65, r=65, t=65, b=65)
    )

    global_trace = {"marker": {"color": Cycler(colors)}}
    return go.PlotlyTheme(global_trace=global_trace, layout=layout)


THEMES = {
    "ggplot": ggplot_theme(),
    "tomorrow_night_eighties": tomorrow_night_eighties_theme(),
    "seaborn": seaborn_theme(),
    "fivethirtyeight": fivethirtyeight_theme(),
}
