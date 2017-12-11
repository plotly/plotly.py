from __future__ import absolute_import

from plotly import exceptions, optional_imports
from plotly.figure_factory import utils

import plotly
import plotly.graph_objs as go

import numpy as np
pd = optional_imports.get_module('pandas')

VALID_CHART_TYPES = ('name', 'bullet', 'line', 'avg', 'bar')


def create_sparkline(df, chart_types=VALID_CHART_TYPES,
                     colors=('rgb(181,221,232)', 'rgb(62,151,169)'),
                     column_width=None, show_titles=False, textalign='center',
                     horizontal_spacing=0.0, vertical_spacing=0.0,
                     alternate_row_color=True,
                     lane_colors=('rgba(249, 247, 244, 1.0)',
                                  'rgba(255, 253, 250, 1.0)'),
                     scatter_options=None, **layout_options):
    """
    Returns figure for sparkline.

    :param (pd.DataFrame | list | tuple) df: either a list/tuple of
        dictionaries or a pandas DataFrame.
    :param (list|tuple) chart_types: a sequence of any combination of valid
        chart types. The valid chart types are 'name', 'bullet', 'line', 'avg'
        and 'bar'
    :param (list|tuple) colors: a sequence of exactly 2 colors which are used
        to color the charts. Set the first color to your ___ color and the
        second color as your ___
        Default = ('rgb(181,221,232)', 'rgb(62,151,169)')
    :param (list) column_width: Specify a list that contains numbers where
        the amount of numbers in the list is equal to `chart_types`. Call
        `help(plotly.tools.make_subplots)` for more info on this subplot param
    :param (bool) show_titles: determines if title of chart type is displayed
        above their respective column
    :param (str) textalign: aligns name and avg cells. Use either 'center',
        'left', or 'right'. Default='center'.
    :param (float) horizontal_spacing: Space between subplot columns.
        Applied to all columns
    :param (float) vertical_spacing: Space between subplot rows.
        Applied to all rows
    :param (float) alternate_row_color: set to True to enable the alternate
        row coloring of the chart. Uses the colors from param 'lane_colors'
    :param (list) lane_colors: a list/tuple of two colors that are used to
        alternately color the rows of the chart.
    :param (dict) scatter_options: describes attributes for the scatter point
        in each bullet chart such as name and marker size. Call
        help(plotly.graph_objs.Scatter) for more information on valid params.
    :param layout_options: describes attributes for the layout of the figure
        such as title, height and width. Call help(plotly.graph_objs.Layout)
        for more information on valid params
    """
    # validate dataframe
    if not pd:
        raise exceptions.ImportError(
            "'pandas' must be installed for this figure factory."
        )

    elif not isinstance(df, pd.DataFrame):
        raise exceptions.PlotlyError(
            'df must be a pandas DataFrame'
        )

    # validate list/tuple of colors
    if not utils.is_sequence(colors):
        raise exceptions.PlotlyError(
            'colors must be a list/tuple'
        )

    if len(colors) < 2:
        raise exceptions.PlotlyError(
            'colors must be a list/tuple with 2 colors inside'
        )
    plotly.colors.validate_colors(colors)

    num_of_chart_types = len(chart_types)
    # narrow columns that are 'name' or 'avg'
    narrow_cols = ['name', 'avg']
    narrow_idxs = []
    for i, chart in enumerate(chart_types):
        if chart in narrow_cols:
            narrow_idxs.append(i)

    if not column_width:
        column_width = [3.0] * num_of_chart_types
        for idx in narrow_idxs:
            column_width[idx] = 1.0

    fig = plotly.tools.make_subplots(
        len(df.columns), num_of_chart_types, print_grid=False,
        shared_xaxes=False, shared_yaxes=False,
        horizontal_spacing=horizontal_spacing,
        vertical_spacing=vertical_spacing, column_width=column_width
    )

    # layout options
    fig['layout'].update(
        title='',
        annotations=[],
        showlegend=False
    )

    # update layout
    fig['layout'].update(layout_options)

    for key in fig['layout'].keys():
        if 'axis' in key:
            fig['layout'][key].update(
                showgrid=False,
                zeroline=False,
                showticklabels=False
            )

    # text alignment
    xanchor = textalign
    if textalign == 'left':
        x = 0
    elif textalign == 'center':
        x = 0.5
    elif textalign == 'right':
        x = 1
    else:
        raise exceptions.PlotlyError(
            'textalign must be left, center or right'
        )

    # scatter options
    default_scatter = {
        'mode': 'markers',
        'marker': {'size': 9,
                   'symbol': 'diamond-tall',
                   'color': colors[1]}
    }

    if not scatter_options:
        scatter_options = {}

    if scatter_options == {}:
        scatter_options.update(default_scatter)
    else:
        # add default options to scatter_options if they are not present
        for k in default_scatter['marker']:
            if k not in scatter_options['marker']:
                scatter_options['marker'][k] = default_scatter['marker'][k]

    # create and insert charts
    for j, key in enumerate(df):
        for c, chart in enumerate(chart_types):
            mean = np.mean(df[key])
            rounded_mean = round(mean, 2)
            if chart == 'name':
                fig['layout']['annotations'].append(
                    dict(
                        x=x,
                        y=0.5,
                        xref='x{}'.format(j * num_of_chart_types + c + 1),
                        yref='y{}'.format(j * num_of_chart_types + c + 1),
                        xanchor=xanchor,
                        text=key,
                        showarrow=False,
                        font=dict(size=12),
                    )
                )
                empty_data = go.Bar(
                    x=[0],
                    y=[0],
                    visible=False
                )
                if alternate_row_color:
                    bkgcolor = go.Scatter(
                        x=[0, 1],
                        y=[1.2, 1.2],
                        fill='tozeroy',
                        mode='line',
                        hoverinfo='none',
                        line=dict(
                            color=(lane_colors[0] if (j + 1) % 2 == 0
                                   else lane_colors[1]),
                            width=0
                        ),
                    )
                    fig.append_trace(bkgcolor, j + 1, c + 1)
                fig.append_trace(empty_data, j + 1, c + 1)

            elif chart == 'bullet':
                bullet_range = go.Bar(
                    x=[rounded_mean],
                    y=[0.5],
                    marker=dict(
                        color=colors[0]
                    ),
                    hoverinfo='x',
                    orientation='h',
                    width=0.5
                )

                bullet_measure = go.Bar(
                    x=[list(df[key])[-1]],
                    y=[0.5],
                    marker=dict(
                        color=colors[1]
                    ),
                    hoverinfo='x',
                    orientation='h',
                    width=0.14,
                    offset=-0.07
                )

                bullet_pt = go.Scatter(
                    x=[max(df[key])],
                    y=[0.5],
                    hoverinfo='x',
                    **scatter_options
                )

                range_e = max(df[key]) + 0.5 * rounded_mean
                if alternate_row_color:
                    bkgcolor = go.Scatter(
                        x=[0, range_e],
                        y=[1, 1],
                        fill='tozeroy',
                        mode='lines',
                        hoverinfo='none',
                        line=dict(
                            color=(lane_colors[0] if (j + 1) % 2 == 0
                                   else lane_colors[1]),
                            width=0
                        ),
                    )

                    fig.append_trace(bkgcolor, j + 1, c + 1)
                fig.append_trace(bullet_range, j + 1, c + 1)
                fig.append_trace(bullet_measure, j + 1, c + 1)
                fig.append_trace(bullet_pt, j + 1, c + 1)

                fig['layout']['xaxis{}'.format(
                    j * num_of_chart_types + (c + 1)
                )]['range'] = [0, range_e]
                fig['layout']['yaxis{}'.format(
                    j * num_of_chart_types + (c + 1)
                )]['range'] = [0, 1]
            elif chart == 'line':
                trace_line = go.Scatter(
                    x=range(len(df[key])),
                    y=df[key].tolist(),
                    mode='lines',
                    marker=dict(
                        color=colors[0]
                    )
                )
                fig.append_trace(trace_line, j + 1, c + 1)

                trace_line_pt = go.Scatter(
                    x=[len(df[key]) - 1],
                    y=[list(df[key])[-1]],
                    mode='markers',
                    marker=dict(
                        color=colors[1]
                    ),
                    **scatter_options
                )

                if alternate_row_color:
                    bkgcolor = go.Scatter(
                        x=[0, len(df[key])],
                        y=[2 * max(df[key].tolist())] * 2,
                        fill='tozeroy',
                        mode='lines',
                        hoverinfo='none',
                        line=dict(
                            color=(lane_colors[0] if (j + 1) % 2 == 0
                                   else lane_colors[1]),
                            width=0
                        ),
                    )
                    fig.append_trace(bkgcolor, j + 1, c + 1)
                fig.append_trace(trace_line_pt, j + 1, c + 1)

                fig['layout']['yaxis{}'.format(
                    j * num_of_chart_types + (c + 1)
                )]['range'] = [0, 2 * max(df[key].tolist())]
            elif chart == 'avg':
                fig['layout']['annotations'].append(
                    dict(
                        xref='x{}'.format(j * num_of_chart_types + c + 1),
                        yref='y{}'.format(j * num_of_chart_types + c + 1),
                        x=x,
                        y=0.5,
                        xanchor=xanchor,
                        text='{}'.format(rounded_mean),
                        showarrow=False,
                        font=dict(size=12),
                    )
                )
                empty_data = go.Bar(
                    x=[0],
                    y=[0],
                    visible=False
                )

                if alternate_row_color:
                    bkgcolor = go.Scatter(
                        x=[0, 2],
                        y=[1.2, 1.2],
                        fill='tozeroy',
                        mode='line',
                        hoverinfo='none',
                        line=dict(
                            color=(lane_colors[0] if (j + 1) % 2 == 0
                                   else lane_colors[1]),
                            width=0
                        ),
                    )
                    fig.append_trace(bkgcolor, j + 1, c + 1)
                fig.append_trace(empty_data, j + 1, c + 1)
            elif chart == 'bar':
                trace_bar = go.Bar(
                    x=range(len(df[key])),
                    y=df[key].tolist(),
                    marker=dict(
                        color=[colors[0] for _ in
                               range(len(df[key]) - 1)] + [colors[1]]
                    )
                )

                if alternate_row_color:
                    bkgcolor = go.Scatter(
                        x=[-1, len(df[key])],
                        y=[2 * max(df[key].tolist())] * 2,
                        fill='tozeroy',
                        mode='lines',
                        hoverinfo='none',
                        line=dict(
                            color=(lane_colors[0] if (j + 1) % 2 == 0
                                   else lane_colors[1]),
                            width=0
                        ),
                    )
                    fig.append_trace(bkgcolor, j + 1, c + 1)
                fig.append_trace(trace_bar, j + 1, c + 1)

                fig['layout']['yaxis{}'.format(
                    j * num_of_chart_types + (c + 1)
                )]['range'] = [0, 2 * max(df[key].tolist())]
            else:
                raise exceptions.PlotlyError(
                    'Your chart type must be a list and may only contain any '
                    'combination of the keys {}'.format(
                        utils.list_of_options(
                            VALID_CHART_TYPES, 'or')
                    )
                )
            for x_y in ['xaxis', 'yaxis']:
                fig['layout']['{}{}'.format(
                    x_y, j * num_of_chart_types + (c + 1)
                )]['fixedrange'] = True

    # show titles
    if show_titles:
        for k, header in enumerate(chart_types):
            label = utils.annotation_dict_for_label(
                header, k + 1, 5, subplot_spacing=0, row_col='col',
                flipped=False, column_width=column_width
            )
            fig['layout']['annotations'].append(label)

    # narrow columns with 'name' or 'avg' chart type
    for j in range(len(df.columns)):
        for idx in narrow_idxs:
            for axis in ['xaxis', 'yaxis']:
                fig['layout']['{}{}'.format(
                    axis, j * num_of_chart_types + idx + 1
                )]['range'] = [0, 1]

    return fig
