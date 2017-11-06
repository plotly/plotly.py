from __future__ import absolute_import

from plotly import exceptions, optional_imports
from plotly.figure_factory import utils

import plotly
import plotly.graph_objs as go

from numbers import Number
import pandas as pd

pd = optional_imports.get_module('pandas')

DARK_BLUE = 'rgb(31, 119, 180)'
LIGHT_BLUE = 'rgb(176, 196, 221)'
BAD_COLOR ='rgb(204, 204, 204)'
OK_COLOR = 'rgb(221, 221, 221)'
GOOD_COLOR = 'rgb(238, 238, 238)'
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


def _bullet_rows(df, marker_symbol):
    num_of_rows = len(df)
    fig = plotly.tools.make_subplots(
        num_of_rows, 1, print_grid=False, horizontal_spacing=SUBPLOT_SPACING,
        vertical_spacing=SUBPLOT_SPACING
    )

    # layout
    fig['layout'].update(
        dict(shapes=[]),
        showlegend=False,
        annotations=[],
        margin=dict(l=120),
    )

    for key in fig['layout'].keys():
        if 'axis' in key:
            fig['layout'][key]['showgrid'] = False
            fig['layout'][key]['zeroline'] = False
        if 'xaxis' in key:
            fig['layout'][key]['tickwidth'] = 1
        if 'yaxis' in key:
            fig['layout'][key]['showticklabels'] = False
            fig['layout'][key]['range'] = [0, 1]

    # marker symbol size
    if num_of_rows <= 3:
        marker_size = 14
    else:
        marker_size = 10
    for idx in range(num_of_rows):
        # marker
        fig['data'].append(
            go.Scatter(
                x=df.iloc[idx]['markers'],
                y=[0.5],
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
        ranges_len = len(df.iloc[idx]['ranges'])
        color_incr = 36.0 / max(1, ranges_len - 1)
        for range_idx in range(ranges_len):
            rgb_val = 198 + range_idx * color_incr
            grey_color = 'rgb(' + 3 * '{},'.format(rgb_val)  + ')'
            if range_idx == 0:
                start_range = 0
            else:
                start_range = df.iloc[idx]['ranges'][range_idx - 1]
            end_range = df.iloc[idx]['ranges'][range_idx]
            fig['layout']['shapes'].append(
                rectangle(
                    grey_color, start_range, end_range, y0_ranges, y1_ranges,
                    'x{}'.format(idx + 1),
                    'y{}'.format(idx + 1),
                    'below'
                )
            )

        # measures
        y0_measures = 0.45
        y1_measures = 0.55
        darkblue_len = df.iloc[idx]['measures'][0]
        lightblue_len = df.iloc[idx]['measures'][1]
        fig['layout']['shapes'].append(
            rectangle(
                DARK_BLUE, 0, darkblue_len, y0_measures, y1_measures,
                'x{}'.format(idx + 1),
                'y{}'.format(idx + 1),
                'below'
            )
        )
        fig['layout']['shapes'].append(
                rectangle(
                    LIGHT_BLUE, darkblue_len, lightblue_len,
                    y0_measures, y1_measures,
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
            label, num_of_rows - idx, num_of_rows, SUBPLOT_SPACING,
            'row', True, False
        )
        fig['layout']['annotations'].append(annot)
    return fig


def create_bullet(df, as_rows=True, marker_symbol='diamond-tall',
                  title='Bullet Chart', height=600, width=1000):
    """
    Returns figure for bullet chart.

    :param (pd.DataFrame | list) df: either a JSON list of dicts or a pandas
        DataFrame. Must contain the keys 'title', 'subtitle', 'ranges',
        'measures', and 'markers'.
    :param (str) title: title of the bullet chart.
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

    if as_rows:
        fig = _bullet_rows(df, marker_symbol)
    else:
        fig = _bullet_cols()

    fig['layout'].update(
        title=title,
        height=height,
        width=width,
    )

    return fig
