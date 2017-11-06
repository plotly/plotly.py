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
def shape(color, x0, x1, y0, y1, xref, yref, layer):
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
    num_of_rows = len(df.columns)
    fig = plotly.tools.make_subplots(
        num_of_rows, 1, print_grid=False, horizontal_spacing=SUBPLOT_SPACING,
        vertical_spacing=SUBPLOT_SPACING
    )

    fig['layout'].update(
        dict(shapes=[]),
        showlegend=False,
        annotations=[],
        margin=dict(l=120),
    )

    # add marker symbol
    if num_of_rows <= 3:
        marker_size = 14
    else:
        marker_size = 10
    # marker
    for index in range(num_of_rows):
        fig['data'].append(
            go.Scatter(
                x=df.iloc[index]['markers'],
                y=[0.5],
                marker=dict(
                    size=marker_size,
                    color='rgb(0, 0, 0)',
                    symbol=marker_symbol
                ),
                xaxis='x{}'.format(index + 1),
                yaxis='y{}'.format(index + 1)
            )
        )

    for key in fig['layout'].keys():
        if 'xaxis' in key:
            fig['layout'][key]['showgrid'] = False
            fig['layout'][key]['zeroline'] = False
            fig['layout'][key]['tickwidth'] = 1
        elif 'yaxis' in key:
            fig['layout'][key]['showgrid'] = False
            fig['layout'][key]['zeroline'] = False
            fig['layout'][key]['showticklabels'] = False
            fig['layout'][key]['range'] = [0, 1]

    # ranges
    y0 = 0.35
    y1 = 0.65
    for axis_num in range(num_of_rows):
        fig['layout']['shapes'].append(
            shape(
                BAD_COLOR, 0, df.iloc[axis_num]['ranges'][0], y0, y1,
                'x{}'.format(axis_num + 1),
                'y{}'.format(axis_num + 1),
                'below'
            )
        )
        fig['layout']['shapes'].append(
            shape(
                OK_COLOR, df.iloc[axis_num]['ranges'][0],
                df.iloc[axis_num]['ranges'][1], y0, y1,
                'x{}'.format(axis_num + 1),
                'y{}'.format(axis_num + 1),
                'below'
            )
        )
        fig['layout']['shapes'].append(
            shape(
                GOOD_COLOR, df.iloc[axis_num]['ranges'][1],
                df.iloc[axis_num]['ranges'][2], y0, y1,
                'x{}'.format(axis_num + 1),
                'y{}'.format(axis_num + 1),
                'below'
            )
        )

    # measures
    y0 = 0.45
    y1 = 0.55
    for axis_num in range(num_of_rows):
        darkblue_len = df.iloc[axis_num]['measures'][0]
        lightblue_len = df.iloc[axis_num]['measures'][1]
        fig['layout']['shapes'].append(
            shape(
                DARK_BLUE, 0, darkblue_len, y0, y1,
                'x{}'.format(axis_num + 1),
                'y{}'.format(axis_num + 1),
                'below'
            )
        )
        fig['layout']['shapes'].append(
                shape(
                    LIGHT_BLUE, darkblue_len, lightblue_len, y0, y1,
                    'x{}'.format(axis_num + 1),
                    'y{}'.format(axis_num + 1),
                    'below'
                )
        )

    # labels
    fig['layout']['annotations'] = []
    for k in range(num_of_rows):
        title = df.iloc[k]['title']
        subtitle = df.iloc[k]['subtitle']

        label = '<b>{}</b><br>{}'.format(title, subtitle)
        annot = utils.annotation_dict_for_label(
            label, k + 1, num_of_rows, SUBPLOT_SPACING, 'row', True, False
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

    # check for all keys
    #for df_keys in list(df.columns):
    if any(key not in VALID_KEYS for key in df.columns):
        raise exceptions.PlotlyError(
            "The valid keys you need are"
        )
        #utils.list_of_options

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
