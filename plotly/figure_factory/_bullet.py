from __future__ import absolute_import

import math

from plotly import colors, exceptions, optional_imports
from plotly.figure_factory import utils

import plotly
import plotly.graph_objs as go

pd = optional_imports.get_module('pandas')

VALID_KEYS = ['title', 'subtitle', 'ranges', 'measures', 'markers']


def _bullet(df, as_rows, marker_size, marker_symbol, range_colors,
            measure_colors, subplot_spacing):
    num_of_lanes = len(df)
    num_of_rows = num_of_lanes if as_rows else 1
    num_of_cols = 1 if as_rows else num_of_lanes
    if not subplot_spacing:
        subplot_spacing = 1./num_of_lanes
    fig = plotly.tools.make_subplots(
        num_of_rows, num_of_cols, print_grid=False,
        horizontal_spacing=subplot_spacing,
        vertical_spacing=subplot_spacing
    )

    # layout
    fig['layout'].update(
        dict(shapes=[]),
        showlegend=False,
        barmode='stack',
        margin=dict(l=120 if as_rows else 80),
    )

    if as_rows:
        width_axis = 'yaxis'
        length_axis = 'xaxis'
    else:
        width_axis = 'xaxis'
        length_axis = 'yaxis'

    for key in fig['layout'].keys():
        if 'axis' in key:
            fig['layout'][key]['showgrid'] = False
            fig['layout'][key]['zeroline'] = False
        if length_axis in key:
            fig['layout'][key]['tickwidth'] = 1
        if width_axis in key:
            fig['layout'][key]['showticklabels'] = False
            fig['layout'][key]['range'] = [0, 1]

    # narrow domain if 1 bar
    if num_of_lanes <= 1:
        fig['layout'][width_axis + '1']['domain'] = [0.4, 0.6]

    # marker symbol size
    if not marker_size:
        if num_of_lanes <= 4:
            marker_size = 18
        else:
            marker_size = 8

    if not range_colors:
        range_colors = ['rgb(200, 200, 200)', 'rgb(245, 245, 245)']
    if not measure_colors:
        measure_colors = ['rgb(31, 119, 180)', 'rgb(176, 196, 221)']

    for row in range(num_of_lanes):
        # ranges bars
        for idx in range(len(df.iloc[row]['ranges'])):
            inter_colors = colors.n_colors(
                range_colors[0], range_colors[1],
                len(df.iloc[row]['ranges']), 'rgb'
            )
            x = [sorted(df.iloc[row]['ranges'])[-1 - idx]] if as_rows else [0]
            y = [0] if as_rows else [sorted(df.iloc[row]['ranges'])[-1 - idx]]
            bar = go.Bar(
                x=x,
                y=y,
                marker=dict(
                    color=inter_colors[-1 - idx]
                ),
                name='ranges',
                hoverinfo='x' if as_rows else 'y',
                orientation='h' if as_rows else 'v',
                width=2,
                base=0,
                xaxis='x{}'.format(row + 1),
                yaxis='y{}'.format(row + 1)
            )
            fig['data'].append(bar)

        # measures bars
        for idx in range(len(df.iloc[row]['measures'])):
            inter_colors = colors.n_colors(
                measure_colors[0], measure_colors[1],
                len(df.iloc[row]['measures']), 'rgb'
            )
            x = ([sorted(df.iloc[row]['measures'])[-1 - idx]] if as_rows
                 else [0.5])
            y = ([0.5] if as_rows
                 else [sorted(df.iloc[row]['measures'])[-1 - idx]])
            bar = go.Bar(
                x=x,
                y=y,
                marker=dict(
                    color=inter_colors[-1 - idx]
                ),
                name='measures',
                hoverinfo='x' if as_rows else 'y',
                orientation='h' if as_rows else 'v',
                width=0.4,
                base=0,
                xaxis='x{}'.format(row + 1),
                yaxis='y{}'.format(row + 1)
            )
            fig['data'].append(bar)

        # markers
        x = df.iloc[row]['markers'] if as_rows else [0.5]
        y = [0.5] if as_rows else df.iloc[row]['markers']
        markers = go.Scatter(
            x=x,
            y=y,
            marker=dict(
                color='rgb(0, 0, 0)',
                symbol=marker_symbol,
                size=marker_size
            ),
            name='markers',
            hoverinfo='x' if as_rows else 'y',
            xaxis='x{}'.format(row + 1),
            yaxis='y{}'.format(row + 1)
        )
        fig['data'].append(markers)

        # labels
        title = df.iloc[row]['title']
        if 'subtitle' in df:
            subtitle = '<br>{}'.format(df.iloc[row]['subtitle'])
        else:
            subtitle = ''
        label = '<b>{}</b>'.format(title) + subtitle
        annot = utils.annotation_dict_for_label(
            label,
            (num_of_lanes - row if as_rows else row + 1),
            num_of_lanes, subplot_spacing,
            'row' if as_rows else 'col',
            True if as_rows else False,
            False
        )
        fig['layout']['annotations'].append(annot)

    return fig


def create_bullet(df, as_rows=True, marker_size=16,
                  marker_symbol='diamond-tall', range_colors=None,
                  measure_colors=None, subplot_spacing=None,
                  title='Bullet Chart', height=600, width=1000):
    """
    Returns figure for bullet chart.

    :param (pd.DataFrame | list) df: either a JSON list of dicts or a pandas
        DataFrame. All keys must be one of 'title', 'subtitle', 'ranges',
        'measures', and 'markers'.
    :param (bool) as_rows: if True, the bars are placed horizontally as rows.
        If False, the bars are placed vertically in the chart.
    :param (int) marker_size: sets the size of the markers in the chart.
    :param (str | int) marker_symbol: the symbol of the markers in the chart.
        Default='diamond-tall'
    :param (list) range_colors: a list of two colors between which all
        the rectangles for the range are drawn. These rectangles are meant to
        be qualitative indicators against which the marker and measure bars
        are compared.
        Default=['rgb(198, 198, 198)', 'rgb(248, 248, 248)']
    :param (list) measure_colors: a list of two colors which is used to color
        the thin quantitative bars in the bullet chart.
        Default=['rgb(31, 119, 180)', 'rgb(176, 196, 221)']
    :param (float) subplot_spacing: set the distance between each bar chart.
        If not specified an automatic spacing is assigned based on the number
        of bars to be plotted.
    :param (str) title: title of the bullet chart.
    :param (float) height: height of the chart.
    :param (float) width width of the chart.
    """
    # validate df
    if not pd:
        raise exceptions.ImportError(
            "'pandas' must be imported for this figure_factory."
        )

    if isinstance(df, list):
        if not all(isinstance(item, dict) for item in df):
            raise exceptions.PlotlyError(
                'If your data is a list, all entries must be dictionaries.'
            )
        df = pd.DataFrame(df)

    elif not isinstance(df, pd.DataFrame):
        raise exceptions.PlotlyError(
            'You must input a pandas DataFrame or a list of dictionaries.'
        )

    # check for valid keys
    if any(key not in VALID_KEYS for key in df.columns):
        raise exceptions.PlotlyError(
            'Your headers/dict keys must be either {}'.format(
                utils.list_of_options(VALID_KEYS, 'or')
            )
        )

    # add necessary columns if missing
    for key in VALID_KEYS:
        if key not in df:
            if key in ['title', 'subtitle']:
                element = ''
            else:
                element = []
            df[key] = [element for _ in range(len(df))]

    # make sure ranges and measures are not NAN or NONE
    for needed_key in ['ranges', 'measures']:
        for idx, r in enumerate(df[needed_key]):
            try:
                r_is_nan = math.isnan(r)
                if r_is_nan or r is None:
                    df[needed_key][idx] = []
            except TypeError:
                pass

    # validate custom colors
    for colors_list in [range_colors, measure_colors]:
        if colors_list:
            if len(colors_list) != 2:
                raise exceptions.PlotlyError(
                    "Both 'range_colors' or 'measure_colors' must be a list "
                    "of two valid colors."
                )
            colors.validate_colors(colors_list)
            colors_list = colors.convert_colors_to_same_type(colors_list,
                                                             'rgb')[0]

    fig = _bullet(
        df, as_rows, marker_size, marker_symbol, range_colors, measure_colors,
        subplot_spacing
    )

    fig['layout'].update(
        title=title,
        height=height,
        width=width,
    )

    return fig
