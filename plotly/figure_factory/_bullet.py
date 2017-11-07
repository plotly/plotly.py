from __future__ import absolute_import

import math

from plotly import colors, exceptions, optional_imports
from plotly.figure_factory import utils

import plotly
import plotly.graph_objs as go

pd = optional_imports.get_module('pandas')

SUBPLOT_SPACING = 0.015
VALID_KEYS = ['title', 'subtitle', 'ranges', 'measures', 'markers']


# add shapes
def rectangle(color, x0, x1, y0, y1, xref, yref, layer):
    return {
        'fillcolor': color,
        'line': {'width': 0},
        'opacity': 1,
        'type': 'rect',
        'x0': x0,
        'x1':  x1,
        'xref':  xref,
        'y0': y0,
        'y1': y1,
        'yref': yref,
        'layer': layer
    }


def _bullet(df, as_rows, marker_size, marker_symbol, range_colors,
            measure_colors):
    num_of_lanes = len(df)
    num_of_rows = num_of_lanes if as_rows else 1
    num_of_cols = 1 if as_rows else num_of_lanes
    fig = plotly.tools.make_subplots(
        num_of_rows, num_of_cols, print_grid=False,
        horizontal_spacing=SUBPLOT_SPACING,
        vertical_spacing=SUBPLOT_SPACING
    )

    # layout
    fig['layout'].update(
        dict(shapes=[]),
        showlegend=False,
        annotations=[],
        margin=dict(l=120 if as_rows else 80),
    )

    if as_rows:
        length_axis = 'xaxis'
        width_axis = 'yaxis'
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

    # marker symbol size
    if not marker_size:
        if num_of_lanes <= 3:
            marker_size = 18
        else:
            marker_size = 12
    for idx in range(num_of_lanes):
        # marker
        x = df.iloc[idx]['markers'] if as_rows else [0.5]
        y = [0.5] if as_rows else df.iloc[idx]['markers']
        fig['data'].append(
            go.Scatter(
                x=x,
                y=y,
                marker=dict(
                    size=marker_size,
                    color='rgb(0, 0, 0)',
                    symbol=marker_symbol
                ),
                xaxis='x{}'.format(idx + 1),
                yaxis='y{}'.format(idx + 1)
            )
        )

        # ranges
        y0_ranges = 0.35
        y1_ranges = 0.65
        if not range_colors:
            range_colors = ['rgb(200, 200, 200)', 'rgb(245, 245, 245)']
        ranges_len = len(df.iloc[idx]['ranges'])
        if ranges_len <= 1:
            inter_colors = [range_colors[0]]
        else:
            inter_colors = colors.n_colors(
                range_colors[0], range_colors[1], ranges_len, 'rgb'
            )
        for range_idx in range(ranges_len):
            color = inter_colors[range_idx]
            if range_idx == 0:
                start_range = 0
            else:
                start_range = df.iloc[idx]['ranges'][range_idx - 1]
            end_range = df.iloc[idx]['ranges'][range_idx]

            x0 = start_range if as_rows else y0_ranges
            x1 = end_range if as_rows else y1_ranges
            y0 = y0_ranges if as_rows else start_range
            y1 = y1_ranges if as_rows else end_range
            fig['layout']['shapes'].append(
                rectangle(
                    color, x0, x1, y0, y1,
                    'x{}'.format(idx + 1),
                    'y{}'.format(idx + 1),
                    'below'
                )
            )

        # measures
        y0_measures = 0.45
        y1_measures = 0.55
        if not measure_colors:
            measure_colors = ['rgb(31, 119, 180)', 'rgb(176, 196, 221)']
        measures_len = len(df.iloc[idx]['measures'])
        if measures_len <= 1:
            inter_colors = [measure_colors[0]]
        else:
            inter_colors = colors.n_colors(
                measure_colors[0], measure_colors[1], measures_len, 'rgb'
            )
        for range_idx in range(measures_len):
            color = inter_colors[range_idx]
            if range_idx == 0:
                start_range = 0
            else:
                start_range = df.iloc[idx]['measures'][range_idx - 1]
            end_range = df.iloc[idx]['measures'][range_idx]

            x0 = start_range if as_rows else y0_measures
            x1 = end_range if as_rows else y1_measures
            y0 = y0_measures if as_rows else start_range
            y1 = y1_measures if as_rows else end_range
            fig['layout']['shapes'].append(
                rectangle(
                    color, x0, x1, y0, y1,
                    'x{}'.format(idx + 1),
                    'y{}'.format(idx + 1),
                    'below'
                )
            )

        # labels
        title = df.iloc[idx]['title']
        if 'subtitle' in df:
            subtitle = '<br>{}'.format(df.iloc[idx]['subtitle'])
        else:
            subtitle = ''
        label = '<b>{}</b>'.format(title) + subtitle
        annot = utils.annotation_dict_for_label(
            label, num_of_lanes - idx, num_of_lanes, SUBPLOT_SPACING,
            'row' if as_rows else 'col',
            True if as_rows else False,
            False
        )
        fig['layout']['annotations'].append(annot)

    return fig


def create_bullet(df, as_rows=True, marker_size=16,
                  marker_symbol='diamond-tall', range_colors=None,
                  measure_colors=None, title='Bullet Chart', height=600,
                  width=1000):
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
                "If your data is a list, all entries must be dictionaries."
            )
        df = pd.DataFrame(df)

    elif not isinstance(df, pd.DataFrame):
        raise exceptions.PlotlyError(
            "You must input a pandas DataFrame or a list of dictionaries."
        )

    # check for valid keys
    if any(key not in VALID_KEYS for key in df.columns):
        raise exceptions.PlotlyError(
            "Your headers/dict keys must be either {}".format(
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
        df, as_rows, marker_size, marker_symbol, range_colors, measure_colors
    )

    fig['layout'].update(
        title=title,
        height=height,
        width=width,
    )

    return fig
