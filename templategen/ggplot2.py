import plotly.graph_objs as go
from templategen.utils import set_all_colorscales, set_all_colorbars

from .utils.colors import colors


def generate_ggplot2_template():
    # Initialize template
    # -------------------
    template = go.layout.Template()

    # Define colors
    # -------------
    # Based on theme_gray from
    # https://github.com/tidyverse/ggplot2/blob/master/R/theme-defaults.r

    axis_ticks_clr = colors['gray20']
    axis_text_clr = colors['gray30']
    panel_background_clr = colors['gray93']
    panel_grid_clr = 'white'
    zerolinecolor = 'white'
    plot_background_clr = 'white'
    paper_clr = "white"
    strip_clr = colors['gray85']

    # Set global font color
    template.layout.font.color = axis_text_clr

    # Set background colors
    template.layout.paper_bgcolor = paper_clr
    template.layout.plot_bgcolor = panel_background_clr
    template.layout.polar.bgcolor = panel_background_clr
    template.layout.ternary.bgcolor = panel_background_clr

    # Hue cycle for 3 categories
    template.layout.colorway = ['#F8766D', '#00BA38', '#619CFF']

    # Set colorscale
    # Colors picked using colorpicker from
    # https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html
    colorscale = [[0, 'rgb(20,44,66)'], [1, 'rgb(90,179,244)']]

    set_all_colorscales(template, colorscale)

    # Set colorbar
    # Note the light inward ticks in
    # https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html
    colorbar = dict(outlinewidth=0,
                    tickcolor=panel_background_clr,
                    ticks='inside',
                    len=0.2,
                    ticklen=6)

    set_all_colorbars(template, colorbar)

    # Common axis properties
    axis = dict(showgrid=True,
                gridcolor=panel_grid_clr,
                linecolor=panel_grid_clr,
                tickcolor=axis_ticks_clr,
                ticks="outside")

    cartesian_axis = dict(axis, zerolinecolor=zerolinecolor)

    # Cartesian
    template.layout.xaxis = cartesian_axis
    template.layout.yaxis = cartesian_axis

    # 3D
    axis_3d = dict(cartesian_axis, backgroundcolor=panel_background_clr,
                   showbackground=True)
    template.layout.scene.xaxis = axis_3d
    template.layout.scene.yaxis = axis_3d
    template.layout.scene.zaxis = axis_3d

    # Ternary
    template.layout.ternary.aaxis = axis
    template.layout.ternary.baxis = axis
    template.layout.ternary.caxis = axis

    # Polar
    template.layout.polar.angularaxis = axis
    template.layout.polar.radialaxis = axis

    # Carpet
    carpet_axis = dict(
        gridcolor=panel_grid_clr,
        linecolor=panel_grid_clr,
        startlinecolor=axis_ticks_clr,
        endlinecolor=axis_ticks_clr,
        minorgridcolor=panel_grid_clr)

    template.data.carpet = [{
        'aaxis': carpet_axis,
        'baxis': carpet_axis}]

    # Shape defaults
    # semi-transparent black and no outline
    template.layout.shapedefaults = dict(fillcolor='black',
                                         line={'width': 0},
                                         opacity=0.3)

    # Annotation defaults
    # Remove arrow head and make line thinner
    template.layout.annotationdefaults.arrowhead = 0
    template.layout.annotationdefaults.arrowwidth = 1

    # Geo
    template.layout.geo.landcolor = panel_background_clr
    template.layout.geo.subunitcolor = 'white'
    template.layout.geo.showland = True
    template.layout.geo.showlakes = True
    template.layout.geo.lakecolor = 'white'

    # Table
    template.data.table = [{'header': {'fill': {'color': strip_clr},
                                       'line': {'color': panel_grid_clr}},
                            'cells': {'fill': {'color': panel_background_clr},
                                      'line': {'color': panel_grid_clr}}}]

    return template

