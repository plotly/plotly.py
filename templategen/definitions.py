from templategen.utils import initialize_template
from .utils.colors import colors

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
    colorscale = [[0, 'rgb(20,44,66)'], [1, 'rgb(90,179,244)']]

    # Hue cycle for 3 categories
    colorway = ['#F8766D', '#00BA38', '#619CFF']

    # Set colorbar_common
    # Note the light inward ticks in
    # https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html
    colorbar_common = dict(
        outlinewidth=0,
        tickcolor=colors['gray93'],
        ticks='inside',
        len=0.2,
        ticklen=6)

    # Common axis common properties
    axis_common = dict(
        showgrid=True,
        gridcolor='white',
        linecolor='white',
        tickcolor=colors['gray20'],
        ticks="outside")

    # semi-transparent black and no outline
    shape_defaults = dict(
        fillcolor='black',
        line={'width': 0},
        opacity=0.3)

    # Remove arrow head and make line thinner
    annotation_defaults = {
        'arrowhead': 0,
        'arrowwidth': 1}

    template = initialize_template(
        paper_clr='white',
        font_clr=colors['gray20'],
        panel_background_clr=colors['gray93'],
        panel_grid_clr='white',
        axis_ticks_clr=colors['gray20'],
        zerolinecolor_clr='white',
        table_cell_clr=colors['gray93'],
        table_header_clr=colors['gray85'],
        table_line_clr='white',
        colorway=colorway,
        colorbar_common=colorbar_common,
        colorscale=colorscale,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults
    )

    return template


builders['ggplot2'] = ggplot2


def seaborn():
    # Define colors
    # -------------
    # Based on theme_gray from
    # https://github.com/tidyverse/ggplot2/blob/master/R/theme-defaults.r

    # Set colorscale
    # N = len(sns.cm.rocket.colors)
    # [[i/(N-1), f'rgb({int(r*255)},{int(g*255)},{int(b*255)})']
    #  for i, (r,g,b) in enumerate(sns.cm.rocket.colors)
    #  if i % 16 == 0 or i == 255]
    colorscale = [
        [0.0, 'rgb(2,4,25)'],
        [0.06274509803921569, 'rgb(24,15,41)'],
        [0.12549019607843137, 'rgb(47,23,57)'],
        [0.18823529411764706, 'rgb(71,28,72)'],
        [0.25098039215686274, 'rgb(97,30,82)'],
        [0.3137254901960784, 'rgb(123,30,89)'],
        [0.3764705882352941, 'rgb(150,27,91)'],
        [0.4392156862745098, 'rgb(177,22,88)'],
        [0.5019607843137255, 'rgb(203,26,79)'],
        [0.5647058823529412, 'rgb(223,47,67)'],
        [0.6274509803921569, 'rgb(236,76,61)'],
        [0.6901960784313725, 'rgb(242,107,73)'],
        [0.7529411764705882, 'rgb(244,135,95)'],
        [0.8156862745098039, 'rgb(245,162,122)'],
        [0.8784313725490196, 'rgb(246,188,153)'],
        [0.9411764705882353, 'rgb(247,212,187)'],
        [1.0, 'rgb(250,234,220)']]

    # Hue cycle for 3 categories
    #
    # Created with:
    # import seaborn as sns
    # sns.set()
    # [f'rgb({int(r*255)},{int(g*255)},{int(b*255)})'
    #  for r, g, b in sns.color_palette()]
    colorway = [
        'rgb(76,114,176)',
        'rgb(221,132,82)',
        'rgb(85,168,104)',
        'rgb(196,78,82)',
        'rgb(129,114,179)',
        'rgb(147,120,96)',
        'rgb(218,139,195)',
        'rgb(140,140,140)',
        'rgb(204,185,116)',
        'rgb(100,181,205)']

    # Set colorbar_common
    # Note the light inward ticks in
    # https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html
    colorbar_common = dict(
        outlinewidth=0,
        tickcolor=colors['gray14'],
        ticks='outside',
        tickwidth=2,
        ticklen=8)

    # Common axis common properties
    axis_common = dict(
        showgrid=True,
        gridcolor='white',
        linecolor='white',
        ticks='')

    # semi-transparent black and no outline
    annotation_clr = 'rgb(67,103,167)'
    shape_defaults = dict(
        fillcolor=annotation_clr,
        line={'width': 0},
        opacity=0.5)

    # Remove arrow head and make line thinner
    annotation_defaults = {
        'arrowcolor': annotation_clr}

    template = initialize_template(
        paper_clr='white',
        font_clr=colors['gray14'],
        panel_background_clr='rgb(234,234,242)',
        panel_grid_clr='white',
        axis_ticks_clr=colors['gray14'],
        zerolinecolor_clr='white',
        table_cell_clr='rgb(231,231,240)',
        table_header_clr='rgb(183,183,191)',
        table_line_clr='white',
        colorway=colorway,
        colorbar_common=colorbar_common,
        colorscale=colorscale,
        axis_common=axis_common,
        annotation_defaults=annotation_defaults,
        shape_defaults=shape_defaults
    )

    # Set table header font color to white
    return template


builders['seaborn'] = seaborn
