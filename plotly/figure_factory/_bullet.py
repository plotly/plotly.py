from __future__ import absolute_import

import math

from plotly import colors, exceptions, optional_imports
from plotly.figure_factory import utils

import plotly
import plotly.graph_objs as go

pd = optional_imports.get_module('pandas')

VALID_KEYS = ['title', 'subtitle', 'ranges', 'measures', 'markers']


def _bullet(df, markers, measures, ranges, subtitle, title, orientation,
            range_colors, measure_colors, horizontal_spacing,
            vertical_spacing, scatter_options):
    num_of_lanes = len(df)
    num_of_rows = num_of_lanes if orientation == 'h' else 1
    num_of_cols = 1 if orientation == 'h' else num_of_lanes
    if not horizontal_spacing and not vertical_spacing:
        horizontal_spacing = vertical_spacing = 1./num_of_lanes
    fig = plotly.tools.make_subplots(
        num_of_rows, num_of_cols, print_grid=False,
        horizontal_spacing=horizontal_spacing,
        vertical_spacing=vertical_spacing
    )

    # layout
    fig['layout'].update(
        dict(shapes=[]),
        showlegend=False,
        barmode='stack',
        margin=dict(l=120 if orientation == 'h' else 80),
    )

    if orientation == 'h':
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
            x = ([sorted(df.iloc[row]['ranges'])[-1 - idx]] if
                 orientation == 'h' else [0])
            y = ([0] if orientation == 'h' else
                 [sorted(df.iloc[row]['ranges'])[-1 - idx]])
            bar = go.Bar(
                x=x,
                y=y,
                marker=dict(
                    color=inter_colors[-1 - idx]
                ),
                name='ranges',
                hoverinfo='x' if orientation == 'h' else 'y',
                orientation=orientation,
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
            x = ([sorted(df.iloc[row]['measures'])[-1 - idx]] if
                 orientation == 'h' else [0.5])
            y = ([0.5] if orientation == 'h'
                 else [sorted(df.iloc[row]['measures'])[-1 - idx]])
            bar = go.Bar(
                x=x,
                y=y,
                marker=dict(
                    color=inter_colors[-1 - idx]
                ),
                name='measures',
                hoverinfo='x' if orientation == 'h' else 'y',
                orientation=orientation,
                width=0.4,
                base=0,
                xaxis='x{}'.format(row + 1),
                yaxis='y{}'.format(row + 1)
            )
            fig['data'].append(bar)

        # markers
        x = df.iloc[row]['markers'] if orientation == 'h' else [0.5]
        y = [0.5] if orientation == 'h' else df.iloc[row]['markers']
        markers = go.Scatter(
            x=x,
            y=y,
            marker=dict(
                color='rgb(0, 0, 0)',
                symbol=marker_symbol,
                size=marker_size
            ),
            name='markers',
            hoverinfo='x' if orientation == 'h' else 'y',
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
            (num_of_lanes - row if orientation == 'h' else row + 1),
            num_of_lanes,
            vertical_spacing if orientation == 'h' else horizontal_spacing,
            'row' if orientation == 'h' else 'col',
            True if orientation == 'h' else False,
            False
        )
        fig['layout']['annotations'].append(annot)

    return fig


def create_bullet(data, markers=None, measures=None, ranges=None,
                  subtitle=None, title=None, orientation='h',
                  range_colors=None, measure_colors=None, horizontal_spacing=None,
                  vertical_spacing=None, chart_title='Bullet Chart',
                  height=600, width=1000, **scatter_options):
    """
    Returns figure for bullet chart.

    :param (pd.DataFrame | list) data: either a JSON list of dicts or a pandas
        DataFrame. All keys must be one of 'title', 'subtitle', 'ranges',
        'measures', and 'markers'.
    :param (bool) orientation: if 'h', the bars are placed horizontally as
        rows. If 'v' the bars are placed vertically in the chart.
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
    :param (float) horizontal_spacing: see the 'horizontal_spacing' param in
        plotly.tools.make_subplots. Ranges between 0 and 1.
    :param (float) vertical_spacing: see the 'vertical_spacing' param in
        plotly.tools.make_subplots. Ranges between 0 and 1.
    :param (str) title: title of the bullet chart.
    :param (float) height: height of the chart.
    :param (float) width width of the chart.
    """
    # validate df
    if not pd:
        raise exceptions.ImportError(
            "'pandas' must be imported for this figure_factory."
        )

    if isinstance(data, list):
        if not all(isinstance(item, dict) for item in data):
            raise exceptions.PlotlyError(
                'If your data is a list, all entries must be dictionaries.'
            )

    elif not isinstance(data, pd.DataFrame):
        raise exceptions.PlotlyError(
            'You must input a pandas DataFrame or a list of dictionaries.'
        )

    # make DataFrame from data with correct column headers
    col_names = ['title', 'subtitle', 'markers', 'measures', 'ranges']
    if isinstance(data, list):
        df = pd.DataFrame(
            [
                [d[title] for d in data] if title else [''] * len(data),
                [d[subtitle] for d in data] if subtitle else [''] * len(data),
                [d[markers] for d in data] if markers else [[]] * len(data),
                [d[measures] for d in data] if measures else [[]] * len(data),
                [d[ranges] for d in data] if ranges else [[]] * len(data),
            ],
            index=col_names
        )
    elif isinstance(data, pd.DataFrame):
        df = pd.DataFrame(
            [
                data[title].tolist() if title else [''] * len(data),
                data[subtitle].tolist() if subtitle else [''] * len(data),
                data[markers].tolist() if markers else [[]] * len(data),
                data[measures].tolist() if measures else [[]] * len(data),
                data[ranges].tolist() if ranges else [[]] * len(data),
            ],
            index=col_names
        )
    df = pd.DataFrame.transpose(df)

    # make sure ranges, measures, 'markers' are not NAN or NONE
    for needed_key in ['ranges', 'measures', 'markers']:
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

    # scatter options
    default_scatter_options = {
        'marker': {'size': 12,
                   'symbol': 'diamond-tall',
                   'color': 'rgb(0, 0, 0)'}
    }
    if scatter_options == {}:
        scatter_options.update(default_scatter_options)
    else:





    fig = _bullet(
        df, markers, measures, ranges, subtitle, title, orientation,
        range_colors, measure_colors, horizontal_spacing, vertical_spacing,
        scatter_options
    )

    fig['layout'].update(
        title=chart_title,
        height=height,
        width=width,
    )

    return fig
