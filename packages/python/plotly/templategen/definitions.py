from plotly.graph_objs.layout import Template
from templategen.utils import initialize_template
from .utils.colors import colors
import colorcet as cc
import plotly.express as px

# dict of template builder functions
# This way we can loop over definitions in __init__.py
builders = {}


def ggplot2():
    # Define colors
    # -------------
    # Based on theme_gray from
    # https://github.com/tidyverse/ggplot2/blob/master/R/theme-defaults.r

    # Set colorscale
    # Colors picked using colorpicker from
    # https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html
    colorscale = [[0, "rgb(20,44,66)"], [1, "rgb(90,179,244)"]]

    # Hue cycle for 5 categories
    colorway = ["#F8766D", "#A3A500", "#00BF7D", "#00B0F6", "#E76BF3"]

    # Set colorbar_common
    # Note the light inward ticks in
    # https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html
    colorbar_common = dict(
        outlinewidth=0, tickcolor=colors["gray93"], ticks="inside", ticklen=6
    )

    # Common axis common properties
    axis_common = dict(
        showgrid=True,
        gridcolor="white",
        linecolor="white",
        tickcolor=colors["gray20"],
        ticks="outside",
        title=dict(standoff=15),
    )

    # semi-transparent black and no outline
    shape_defaults = dict(fillcolor="black", line={"width": 0}, opacity=0.3)

    # Remove arrow head and make line thinner
    annotation_defaults = {"arrowhead": 0, "arrowwidth": 1}

    template = initialize_template(
        paper_clr="white",
        font_clr=colors["gray20"],
        panel_background_clr=colors["gray93"],
        panel_grid_clr="white",
        axis_ticks_clr=colors["gray20"],
        zerolinecolor_clr="white",
        table_cell_clr=colors["gray93"],
        table_header_clr=colors["gray85"],
        table_line_clr="white",
        colorway=colorway,
        colorbar_common=colorbar_common,
        colorscale=colorscale,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults,
    )

    # Increase grid width for 3d plots
    template.layout.scene.xaxis.gridwidth = 2
    template.layout.scene.yaxis.gridwidth = 2
    template.layout.scene.zaxis.gridwidth = 2

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    return template


builders["ggplot2"] = ggplot2


def simple_white():
    # Set colorbar_common
    colorbar_common = dict(outlinewidth=1, tickcolor=colors["gray14"], ticks="outside")

    # Common axis common properties
    axis_common = dict(
        showgrid=False,
        gridcolor=colors["gray91"],
        linecolor=colors["gray14"],
        ticks="outside",
        showline=True,
        title=dict(standoff=15),
    )
    # semi-transparent black and no outline
    shape_defaults = dict(fillcolor="black", line={"width": 0}, opacity=0.3)

    # Remove arrow head and make line thinner
    annotation_defaults = {"arrowhead": 0, "arrowwidth": 1}

    template = initialize_template(
        paper_clr="white",
        font_clr=colors["gray14"],
        panel_background_clr="white",
        panel_grid_clr="white",
        axis_ticks_clr=colors["gray14"],
        zerolinecolor_clr=colors["gray14"],
        table_cell_clr=colors["gray93"],
        table_header_clr=colors["gray85"],
        table_line_clr="white",
        colorway=px.colors.qualitative.D3,
        colorbar_common=colorbar_common,
        colorscale=px.colors.sequential.Viridis,
        colorscale_diverging=px.colors.diverging.RdBu,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults,
    )

    # Left align title
    template.layout.title.x = 0.05

    # Increase grid width for 3d plots
    opts = dict(gridwidth=2, gridcolor=colors["gray91"], zeroline=False)
    template.layout.scene.xaxis.update(opts)
    template.layout.scene.yaxis.update(opts)
    template.layout.scene.zaxis.update(opts)

    # Darken ternary
    opts = dict(linecolor=colors["gray14"], gridcolor=colors["gray91"])
    template.layout.ternary.aaxis.update(opts)
    template.layout.ternary.baxis.update(opts)
    template.layout.ternary.caxis.update(opts)

    # Remove lines through the origin
    template.layout.xaxis.update(zeroline=False)
    template.layout.yaxis.update(zeroline=False)

    # Separate histogram bins wit ha white line
    opts = {"marker": {"line": {"width": 0.6, "color": "white"}}}
    template.data.histogram = [opts]

    # Mapbox light style
    template.layout.mapbox.style = "light"

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]
    return template


builders["simple_white"] = simple_white


def seaborn():
    # Define colors
    # -------------
    # Set colorscale
    # N = len(sns.cm.rocket.colors)
    # [[i/(N-1), f'rgb({int(r*255)},{int(g*255)},{int(b*255)})']
    #  for i, (r,g,b) in enumerate(sns.cm.rocket.colors)
    #  if i % 16 == 0 or i == 255]
    colorscale = [
        [0.0, "rgb(2,4,25)"],
        [0.06274509803921569, "rgb(24,15,41)"],
        [0.12549019607843137, "rgb(47,23,57)"],
        [0.18823529411764706, "rgb(71,28,72)"],
        [0.25098039215686274, "rgb(97,30,82)"],
        [0.3137254901960784, "rgb(123,30,89)"],
        [0.3764705882352941, "rgb(150,27,91)"],
        [0.4392156862745098, "rgb(177,22,88)"],
        [0.5019607843137255, "rgb(203,26,79)"],
        [0.5647058823529412, "rgb(223,47,67)"],
        [0.6274509803921569, "rgb(236,76,61)"],
        [0.6901960784313725, "rgb(242,107,73)"],
        [0.7529411764705882, "rgb(244,135,95)"],
        [0.8156862745098039, "rgb(245,162,122)"],
        [0.8784313725490196, "rgb(246,188,153)"],
        [0.9411764705882353, "rgb(247,212,187)"],
        [1.0, "rgb(250,234,220)"],
    ]

    # Hue cycle for 3 categories
    #
    # Created with:
    # import seaborn as sns
    # sns.set()
    # [f'rgb({int(r*255)},{int(g*255)},{int(b*255)})'
    #  for r, g, b in sns.color_palette()]
    colorway = [
        "rgb(76,114,176)",
        "rgb(221,132,82)",
        "rgb(85,168,104)",
        "rgb(196,78,82)",
        "rgb(129,114,179)",
        "rgb(147,120,96)",
        "rgb(218,139,195)",
        "rgb(140,140,140)",
        "rgb(204,185,116)",
        "rgb(100,181,205)",
    ]

    # Set colorbar_common
    # Note the light inward ticks in
    # https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html
    colorbar_common = dict(
        outlinewidth=0,
        tickcolor=colors["gray14"],
        ticks="outside",
        tickwidth=2,
        ticklen=8,
    )

    # Common axis common properties
    axis_common = dict(
        showgrid=True,
        gridcolor="white",
        linecolor="white",
        ticks="",
        title=dict(standoff=15),
    )

    # semi-transparent black and no outline
    annotation_clr = "rgb(67,103,167)"
    shape_defaults = dict(fillcolor=annotation_clr, line={"width": 0}, opacity=0.5)

    # Remove arrow head and make line thinner
    annotation_defaults = {"arrowcolor": annotation_clr}

    template = initialize_template(
        paper_clr="white",
        font_clr=colors["gray14"],
        panel_background_clr="rgb(234,234,242)",
        panel_grid_clr="white",
        axis_ticks_clr=colors["gray14"],
        zerolinecolor_clr="white",
        table_cell_clr="rgb(231,231,240)",
        table_header_clr="rgb(183,183,191)",
        table_line_clr="white",
        colorway=colorway,
        colorbar_common=colorbar_common,
        colorscale=colorscale,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults,
    )

    # Increase grid width for 3d plots
    template.layout.scene.xaxis.gridwidth = 2
    template.layout.scene.yaxis.gridwidth = 2
    template.layout.scene.zaxis.gridwidth = 2

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]
    return template


builders["seaborn"] = seaborn


# https://brand.plot.ly/
plotly_clrs = {
    "Rhino Light 4": "#f2f5fa",
    "Rhino Light 3": "#F3F6FA",
    "Rhino Light 2": "#EBF0F8",
    "Rhino Light 1": "#DFE8F3",
    "Rhino Medium 2": "#C8D4E3",
    "Rhino Medium 1": "#A2B1C6",
    "Rhino Dark": "#506784",
    "Rhino Core": "#2a3f5f",
    "Dodger": "#119DFF",
    "Dodger Shade": "#0D76BF",
    "Aqua": "#09ffff",
    "Aqua Shade": "#19d3f3",
    "Lavender": "#e763fa",
    "Lavender Shade": "#ab63fa",
    "Cornflower": "#636efa",
    "Emerald": "#00cc96",
    "Sienna": "#EF553B",
}

# ## Add interpolated theme colors
#
# Interpolate from Rhino Dark to 0.5 of the way toward Black
# https://meyerweb.com/eric/tools/color-blend/#506784:000000:1:hex
plotly_clrs["Rhino Darker"] = "#283442"

# https://meyerweb.com/eric/tools/color-blend/#DFE8F3:EBF0F8:1:hex
plotly_clrs["Rhino Light 1.5"] = "#E5ECF6"

# Perceptually uniform colorscale that matches brand colors really well.
# Trim the upper and lower ends so that it doesn't go so close to black and
# white.  This makes the scale more visible on both white and black
# backgrounds
bmw_subset = cc.b_linear_bmw_5_95_c86[50:230]
linear_bmw_5_95_c86_n256 = [
    [i / (len(bmw_subset) - 1), clr]
    for i, clr in enumerate(bmw_subset)
    if i % 16 == 0 or i == (len(bmw_subset) - 1)
]


# Plasma colorscale
# -----------------
# Get this from plotly_express logic after integration
plasma_colors = [
    "#0d0887",
    "#46039f",
    "#7201a8",
    "#9c179e",
    "#bd3786",
    "#d8576b",
    "#ed7953",
    "#fb9f3a",
    "#fdca26",
    "#f0f921",
]

plasma = [
    [(1.0 * i) / (1.0 * (len(plasma_colors) - 1)), x]
    for i, x in enumerate(plasma_colors)
]

jupyterlab_output_clr = "rgb(17,17,17)"

plotly_diverging = [
    [0, "#8e0152"],
    [0.1, "#c51b7d"],
    [0.2, "#de77ae"],
    [0.3, "#f1b6da"],
    [0.4, "#fde0ef"],
    [0.5, "#f7f7f7"],
    [0.6, "#e6f5d0"],
    [0.7, "#b8e186"],
    [0.8, "#7fbc41"],
    [0.9, "#4d9221"],
    [1, "#276419"],
]

plotly_colorway = [
    plotly_clrs["Cornflower"],
    plotly_clrs["Sienna"],
    plotly_clrs["Emerald"],
    plotly_clrs["Lavender Shade"],
    "#FFA15A",
    plotly_clrs["Aqua Shade"],
    "#FF6692",
    "#B6E880",
    "#FF97FF",
    "#FECB52",
]


def plotly():
    # Define colors
    # -------------
    colorscale = plasma

    # Set colorbar_common
    colorbar_common = dict(outlinewidth=0, ticks="")

    # Common axis common properties
    axis_common = dict(
        gridcolor="white", linecolor="white", ticks="", title=dict(standoff=15),
    )

    # Near black line color, no fill
    annotation_clr = plotly_clrs["Rhino Core"]
    shape_defaults = dict(line_color=annotation_clr)

    # Remove arrow head and make line thinner
    annotation_defaults = {
        "arrowcolor": annotation_clr,
        "arrowhead": 0,
        "arrowwidth": 1,
    }

    template = initialize_template(
        paper_clr="white",
        font_clr=plotly_clrs["Rhino Core"],
        panel_background_clr=plotly_clrs["Rhino Light 1.5"],
        panel_grid_clr="white",
        axis_ticks_clr=plotly_clrs["Rhino Core"],
        zerolinecolor_clr="white",
        table_cell_clr=plotly_clrs["Rhino Light 2"],
        table_header_clr=plotly_clrs["Rhino Medium 2"],
        table_line_clr="white",
        colorway=plotly_colorway,
        colorbar_common=colorbar_common,
        colorscale=colorscale,
        colorscale_diverging=plotly_diverging,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults,
    )

    # Left align title
    template.layout.title.x = 0.05

    # Increase grid width for 3d plots
    template.layout.scene.xaxis.gridwidth = 2
    template.layout.scene.yaxis.gridwidth = 2
    template.layout.scene.zaxis.gridwidth = 2

    # Increase width of cartesian zero lines
    template.layout.xaxis.zerolinewidth = 2
    template.layout.yaxis.zerolinewidth = 2

    # Mapbox light style
    template.layout.mapbox.style = "light"

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    # Set table header font color to white
    return template


builders["plotly"] = plotly


def plotly_white():
    # Define colors
    # -------------
    colorscale = plasma

    # Set colorbar_common
    colorbar_common = dict(outlinewidth=0, ticks="")

    # Common axis common properties
    axis_common = dict(
        gridcolor=plotly_clrs["Rhino Light 2"],
        linecolor=plotly_clrs["Rhino Light 2"],
        ticks="",
        title=dict(standoff=15),
    )

    # Near black line color, no fill
    annotation_clr = plotly_clrs["Rhino Core"]
    shape_defaults = dict(line_color=annotation_clr)

    # Remove arrow head and make line thinner
    annotation_defaults = {
        "arrowcolor": annotation_clr,
        "arrowhead": 0,
        "arrowwidth": 1,
    }

    template = initialize_template(
        paper_clr="white",
        font_clr=plotly_clrs["Rhino Core"],
        panel_background_clr="white",
        panel_grid_clr=plotly_clrs["Rhino Medium 2"],
        axis_ticks_clr=plotly_clrs["Rhino Core"],
        zerolinecolor_clr=plotly_clrs["Rhino Light 2"],
        table_cell_clr=plotly_clrs["Rhino Light 2"],
        table_header_clr=plotly_clrs["Rhino Medium 2"],
        table_line_clr="white",
        colorway=plotly_colorway,
        colorbar_common=colorbar_common,
        colorscale=colorscale,
        colorscale_diverging=plotly_diverging,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults,
    )

    # Left align title
    template.layout.title.x = 0.05

    # Increase grid width for 3d plots
    opts = dict(gridwidth=2, gridcolor=plotly_clrs["Rhino Light 1"])
    template.layout.scene.xaxis.update(opts)
    template.layout.scene.yaxis.update(opts)
    template.layout.scene.zaxis.update(opts)

    # Darken ternary
    opts = dict(
        linecolor=plotly_clrs["Rhino Medium 1"], gridcolor=plotly_clrs["Rhino Light 1"]
    )
    template.layout.ternary.aaxis.update(opts)
    template.layout.ternary.baxis.update(opts)
    template.layout.ternary.caxis.update(opts)

    # Increase width of cartesian zero lines
    template.layout.xaxis.zerolinewidth = 2
    template.layout.yaxis.zerolinewidth = 2

    # Mapbox light style
    template.layout.mapbox.style = "light"

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    # Set table header font color to white
    return template


builders["plotly_white"] = plotly_white


def plotly_dark():
    # Define colors
    # -------------
    colorscale = plasma

    # Set colorbar_common
    colorbar_common = dict(outlinewidth=0, ticks="")

    # Common axis common properties
    grid_color = plotly_clrs["Rhino Dark"]
    axis_common = dict(
        gridcolor=grid_color, linecolor=grid_color, ticks="", title=dict(standoff=15),
    )

    # Near white line color, no fill
    annotation_clr = plotly_clrs["Rhino Light 4"]
    shape_defaults = dict(line_color=annotation_clr)

    # Remove arrow head and make line thinner
    annotation_defaults = {
        "arrowcolor": annotation_clr,
        "arrowhead": 0,
        "arrowwidth": 1,
    }

    template = initialize_template(
        paper_clr=jupyterlab_output_clr,
        font_clr=plotly_clrs["Rhino Light 4"],
        panel_background_clr=jupyterlab_output_clr,
        panel_grid_clr=grid_color,
        axis_ticks_clr=plotly_clrs["Rhino Medium 1"],
        zerolinecolor_clr=plotly_clrs["Rhino Medium 2"],
        table_cell_clr=plotly_clrs["Rhino Dark"],
        table_header_clr=plotly_clrs["Rhino Core"],
        table_line_clr=jupyterlab_output_clr,
        colorway=plotly_colorway,
        colorbar_common=colorbar_common,
        colorscale=colorscale,
        colorscale_diverging=plotly_diverging,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults,
    )

    # Left align title
    template.layout.title.x = 0.05

    # Increase grid width for 3d plots
    template.layout.scene.xaxis.gridwidth = 2
    template.layout.scene.yaxis.gridwidth = 2
    template.layout.scene.zaxis.gridwidth = 2

    # Button styling
    template.layout.updatemenudefaults.bgcolor = plotly_clrs["Rhino Dark"]
    template.layout.updatemenudefaults.borderwidth = 0

    # Slider styling
    template.layout.sliderdefaults.bgcolor = "#C8D4E3"
    template.layout.sliderdefaults.borderwidth = 1
    template.layout.sliderdefaults.bordercolor = "rgb(17,17,17)"
    template.layout.sliderdefaults.tickwidth = 0

    # Darken cartesian grid lines a little more
    template.layout.xaxis.gridcolor = plotly_clrs["Rhino Darker"]
    template.layout.yaxis.gridcolor = plotly_clrs["Rhino Darker"]

    # Increase width of cartesian zero lines
    template.layout.xaxis.zerolinecolor = plotly_clrs["Rhino Darker"]
    template.layout.yaxis.zerolinecolor = plotly_clrs["Rhino Darker"]
    template.layout.xaxis.zerolinewidth = 2
    template.layout.yaxis.zerolinewidth = 2

    # Mapbox light style
    template.layout.mapbox.style = "dark"

    # Set marker outline color
    opts = {"marker": {"line": {"color": plotly_clrs["Rhino Darker"]}}}
    template.data.scatter = [opts]
    template.data.scattergl = [opts]

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    # Set table header font color to white
    return template


builders["plotly_dark"] = plotly_dark


def presentation():
    """
    Template that increases the size of text and markers/lines for certain
    trace types
    """

    # Create blank template
    template = Template()
    template.layout.xaxis.title.standoff = 15
    template.layout.yaxis.title.standoff = 15

    # Increase global font size by 1.5x (12->18)
    template.layout.font.size = 18

    # Increase scatter markers and lines by 1.5x
    opts = {"marker": {"size": 9}, "line": {"width": 3}}
    template.data.scatter = [opts]
    template.data.scattergl = [opts]
    template.data.scatter3d = [opts]
    template.data.scatterpolar = [opts]
    template.data.scatterpolargl = [opts]
    template.data.scatterternary = [opts]
    template.data.scattergeo = [opts]

    # Increase default height of table cells
    template.data.table = [{"header": {"height": 36}, "cells": {"height": 30}}]

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    return template


builders["presentation"] = presentation


def xgridoff():
    """
    Template to disable x-grid by default
    """
    # Create blank template
    template = Template()
    template.layout.xaxis.showgrid = False
    template.layout.xaxis.title.standoff = 15
    template.layout.yaxis.title.standoff = 15

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    return template


builders["xgridoff"] = xgridoff


def ygridoff():
    """
    Template to disable y-grid by default
    """
    # Create blank template
    template = Template()
    template.layout.yaxis.showgrid = False

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    return template


builders["ygridoff"] = ygridoff


def gridon():
    """
    Template to enable x and y-grid by default
    """
    # Create blank template
    template = Template()
    template.layout.xaxis.showgrid = True
    template.layout.xaxis.title.standoff = 15
    template.layout.yaxis.showgrid = True
    template.layout.yaxis.title.standoff = 15

    # Automargin for pie chart
    template.data.pie = [{"automargin": True}]

    return template


builders["gridon"] = gridon
