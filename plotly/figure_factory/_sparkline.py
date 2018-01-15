from __future__ import absolute_import

from plotly import exceptions, optional_imports
from plotly.figure_factory import utils

import plotly
import plotly.graph_objs as go

import numpy as np
pd = optional_imports.get_module('pandas')

VALID_CHART_TYPES = ('label', 'bullet', 'line', 'avg', 'bar', 'area')


def rect(xref, yref, x0, x1, y0, y1, color):
    shape = {
        'layer': 'below',
        'xref': xref,
        'yref': yref,
        'x0': x0,
        'x1': x1,
        'y0': y0,
        'y1': y1,
        'fillcolor': color,
        'line': {'width': 0}
    }
    return shape


VALID_CHART_TYPE_MESSAGE = (
    'Invalid chart type. The valid chart types '
    'are {}'.format(utils.list_of_options(VALID_CHART_TYPES, 'and'))
)


def _sparkline_tidy(df, fig, chart_types, num_of_chart_types, trace_colors_2d,
                    column_width, alternate_row_color, row_colors, xanchor,
                    line_width, align_x, scatter_options, new_marker_color,
                    narrow_idxs, show_titles, row, column, x):
    # create and insert charts
    c_idx = 0
    trace_c_idx = 0
    chart_types_keys = [k for d in chart_types for k in d.keys()]
    for j, rkey in enumerate(df[row].unique()):
        for c, ckey in enumerate(chart_types_keys):
            chart = chart_types[c][ckey]
            data = list(df[(df[row] == rkey) & (df[column] == ckey)][x])

            # update indices
            if c_idx >= len(row_colors):
                c_idx = 0
            r_color = row_colors[c_idx]

            if trace_c_idx >= len(trace_colors_2d):
                trace_c_idx = 0
            dark_color = trace_colors_2d[trace_c_idx][0]
            light_color = trace_colors_2d[trace_c_idx][1]

            if len(data) <= 0:
                if chart in ['label', 'avg']:
                    if chart == 'label':
                        text = rkey
                    else:
                        text = 'nan'
                    fig['layout']['annotations'].append(
                        dict(
                            xref='x{}'.format(j * num_of_chart_types + c + 1),
                            yref='y{}'.format(j * num_of_chart_types + c + 1),
                            x=align_x,
                            y=0.5,
                            xanchor=xanchor,
                            text=text,
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
                    bkg = rect(
                        'x{}'.format(j * num_of_chart_types + c + 1),
                        'y{}'.format(j * num_of_chart_types + c + 1),
                        x0=0, x1=1,
                        y0=-0.1, y1=1.1,
                        color=(
                            r_color
                        )
                    )
                    fig['layout']['shapes'].append(bkg)
                fig.append_trace(empty_data, j + 1, c + 1)
            else:
                mean = np.mean(data)
                rounded_mean = round(mean, 2)
                if chart in ['label', 'avg']:
                    if chart == 'label':
                        text = rkey
                    else:
                        text = '{}'.format(rounded_mean)
                    fig['layout']['annotations'].append(
                        dict(
                            xref='x{}'.format(j * num_of_chart_types + c + 1),
                            yref='y{}'.format(j * num_of_chart_types + c + 1),
                            x=align_x,
                            y=0.5,
                            xanchor=xanchor,
                            text=text,
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
                        bkg = rect(
                            'x{}'.format(j * num_of_chart_types + c + 1),
                            'y{}'.format(j * num_of_chart_types + c + 1),
                            x0=0, x1=1,
                            y0=-0.1, y1=1.1,
                            color=(
                                r_color
                            )
                        )
                        fig['layout']['shapes'].append(bkg)
                    fig.append_trace(empty_data, j + 1, c + 1)

                elif chart == 'bullet':
                    bullet_range = go.Bar(
                        x=[rounded_mean],
                        y=[0.5],
                        marker=dict(
                            color=light_color
                        ),
                        hoverinfo='x',
                        orientation='h',
                        width=0.5
                    )

                    bullet_measure = go.Bar(
                        x=[data[-1]],
                        y=[0.5],
                        marker=dict(
                            color=dark_color
                        ),
                        hoverinfo='x',
                        orientation='h',
                        width=0.14,
                        offset=-0.07
                    )
                    if not new_marker_color:
                        scatter_options['marker']['color'] = dark_color
                    bullet_pt = go.Scatter(
                        x=[max(data)],
                        y=[0.5],
                        hoverinfo='x',
                        **scatter_options
                    )

                    xrange_r = max(data) + 0.5 * rounded_mean
                    if alternate_row_color:
                        bkg = rect(
                            'x{}'.format(j * num_of_chart_types + c + 1),
                            'y{}'.format(j * num_of_chart_types + c + 1),
                            x0=0, x1=xrange_r,
                            y0=0, y1=1,
                            color=(
                                r_color
                            )
                        )
                        fig['layout']['shapes'].append(bkg)
                    fig.append_trace(bullet_range, j + 1, c + 1)
                    fig.append_trace(bullet_measure, j + 1, c + 1)
                    fig.append_trace(bullet_pt, j + 1, c + 1)

                    fig['layout']['xaxis{}'.format(
                        j * num_of_chart_types + (c + 1)
                    )]['range'] = [0, xrange_r]
                    fig['layout']['yaxis{}'.format(
                        j * num_of_chart_types + (c + 1)
                    )]['range'] = [0, 1]
                elif chart in ['line', 'area']:
                    if chart == 'line':
                        trace_line = go.Scatter(
                            x=range(len(data)),
                            y=data,
                            mode='lines',
                            marker=dict(
                                color=dark_color
                            )
                        )
                    else:
                        trace_line = go.Scatter(
                            x=range(len(data)),
                            y=data,
                            mode='lines',
                            fill='tozeroy',
                            fillcolor=light_color,
                            line=dict(width=line_width, color=dark_color)
                        )
                    if not new_marker_color:
                        scatter_options['marker']['color'] = dark_color
                    trace_line_pt = go.Scatter(
                        x=[len(data) - 1],
                        y=[data[-1]],
                        **scatter_options
                    )

                    # invisible pt
                    pt_hidden = go.Scatter(
                        x=[-1],
                        y=[0],
                        hoverinfo='none'
                    )

                    std = np.std(data)
                    x0 = -0.01
                    if np.isnan(std):
                        yrange_top = 1
                        yrange_bottom = 0
                    elif std == 0:
                        extra_space = 0.3 * abs(data[0])
                        yrange_top = data[0] + extra_space
                        yrange_bottom = data[0] - extra_space
                    else:
                        yrange_top = max(data) + 2*std
                        yrange_bottom = min(data) - 2*std
                    if alternate_row_color:
                        bkg = rect(
                            'x{}'.format(j * num_of_chart_types + c + 1),
                            'y{}'.format(j * num_of_chart_types + c + 1),
                            x0=x0, x1=len(data),
                            y0=yrange_bottom, y1=yrange_top,
                            color=(
                                r_color
                            )
                        )
                        fig['layout']['shapes'].append(bkg)
                    fig.append_trace(trace_line, j + 1, c + 1)
                    fig.append_trace(trace_line_pt, j + 1, c + 1)
                    fig.append_trace(pt_hidden, j + 1, c + 1)

                    fig['layout']['yaxis{}'.format(
                        j * num_of_chart_types + (c + 1)
                    )]['range'] = [yrange_bottom, yrange_top]
                    fig['layout']['xaxis{}'.format(
                        j * num_of_chart_types + (c + 1)
                    )]['range'] = [x0, len(data)]
                elif chart == 'bar':
                    std = np.std(data)
                    if std == 0:
                        extra_space = 0.3 * abs(data[0])
                        if data[0] < 0:
                            yrange_top = 0
                            yrange_bottom = (data[0] - extra_space)
                        elif data[0] >= 0:
                            yrange_top = (data[0] + extra_space)
                            yrange_bottom = 0
                    else:
                        yrange_top = max(data) + std
                        yrange_bottom = min(data) - std

                    trace_bar = go.Bar(
                        x=range(len(data)),
                        y=data,
                        marker=dict(
                            color=[light_color for k in
                                   range(len(data) - 1)] + [dark_color]
                        )
                    )

                    if alternate_row_color:
                        bkg = rect(
                            'x{}'.format(j * num_of_chart_types + c + 1),
                            'y{}'.format(j * num_of_chart_types + c + 1),
                            x0=-1, x1=len(data),
                            y0=yrange_bottom, y1=yrange_top,
                            color=(
                                r_color
                            )
                        )
                        fig['layout']['shapes'].append(bkg)
                    fig.append_trace(trace_bar, j + 1, c + 1)

                    fig['layout']['yaxis{}'.format(
                        j * num_of_chart_types + (c + 1)
                    )]['range'] = [yrange_bottom, yrange_top]
                for x_y in ['xaxis', 'yaxis']:
                    fig['layout']['{}{}'.format(
                        x_y, j * num_of_chart_types + (c + 1)
                    )]['fixedrange'] = True

            # show titles
            if show_titles and j == 0:
                label = utils.annotation_dict_for_label(
                    ckey, c + 1, num_of_chart_types, subplot_spacing=0,
                    row_col='col', flipped=False, column_width=column_width
                )
                fig['layout']['annotations'].append(label)

            for idx in narrow_idxs:
                for axis in ['xaxis', 'yaxis']:
                    fig['layout']['{}{}'.format(
                        axis, c * num_of_chart_types + idx + 1
                    )]['range'] = [0, 1]
        c_idx += 1
        trace_c_idx += 1


def _sparkline(df, fig, chart_types, num_of_chart_types, trace_colors_2d,
               column_width, alternate_row_color, row_colors, xanchor,
               line_width, align_x, scatter_options, new_marker_color,
               narrow_idxs, show_titles):
    # create and insert charts
    c_idx = 0
    trace_c_idx = 0
    for j, key in enumerate(df):
        for c, chart in enumerate(chart_types):
            mean = np.mean(df[key])
            rounded_mean = round(mean, 2)
            # update indices
            if c_idx >= len(row_colors):
                c_idx = 0
            r_color = row_colors[c_idx]

            if trace_c_idx >= len(trace_colors_2d):
                trace_c_idx = 0
            dark_color = trace_colors_2d[trace_c_idx][0]
            light_color = trace_colors_2d[trace_c_idx][1]

            if chart == ['label', 'avg']:
                if chart == 'label':
                    text = key
                else:
                    text = '{}'.format(rounded_mean)
                fig['layout']['annotations'].append(
                    dict(
                        x=align_x,
                        y=0.5,
                        xref='x{}'.format(j * num_of_chart_types + c + 1),
                        yref='y{}'.format(j * num_of_chart_types + c + 1),
                        xanchor=xanchor,
                        text=text,
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
                    bkg = rect(
                        'x{}'.format(j * num_of_chart_types + c + 1),
                        'y{}'.format(j * num_of_chart_types + c + 1),
                        x0=-0.1, x1=1.1,
                        y0=-0.1, y1=1.1,
                        color=(
                            r_color
                        )
                    )
                    fig['layout']['shapes'].append(bkg)
                fig.append_trace(empty_data, j + 1, c + 1)

            elif chart == 'bullet':
                bullet_range = go.Bar(
                    x=[rounded_mean],
                    y=[0.5],
                    marker=dict(
                        color=light_color
                    ),
                    hoverinfo='x',
                    orientation='h',
                    width=0.5
                )

                bullet_measure = go.Bar(
                    x=[list(df[key])[-1]],
                    y=[0.5],
                    marker=dict(
                        color=dark_color
                    ),
                    hoverinfo='x',
                    orientation='h',
                    width=0.14,
                    offset=-0.07
                )
                if not new_marker_color:
                    scatter_options['marker']['color'] = dark_color
                bullet_pt = go.Scatter(
                    x=[max(df[key])],
                    y=[0.5],
                    hoverinfo='x',
                    **scatter_options
                )

                xrange_r = max(df[key]) + 0.5 * rounded_mean
                if alternate_row_color:
                    bkg = rect(
                        'x{}'.format(j * num_of_chart_types + c + 1),
                        'y{}'.format(j * num_of_chart_types + c + 1),
                        x0=0, x1=xrange_r,
                        y0=0, y1=1,
                        color=(
                            r_color
                        )
                    )
                    fig['layout']['shapes'].append(bkg)
                fig.append_trace(bullet_range, j + 1, c + 1)
                fig.append_trace(bullet_measure, j + 1, c + 1)
                fig.append_trace(bullet_pt, j + 1, c + 1)

                fig['layout']['xaxis{}'.format(
                    j * num_of_chart_types + (c + 1)
                )]['range'] = [0, xrange_r]
                fig['layout']['yaxis{}'.format(
                    j * num_of_chart_types + (c + 1)
                )]['range'] = [0, 1]

            elif chart in ['line', 'area']:
                if chart == 'line':
                    trace_line = go.Scatter(
                        x=range(len(df[key])),
                        y=df[key].tolist(),
                        mode='lines',
                        marker=dict(
                            color=dark_color
                        )
                    )
                else:
                    trace_line = go.Scatter(
                        x=range(len(df[key])),
                        y=df[key].tolist(),
                        mode='lines',
                        fill='tozeroy',
                        fillcolor=light_color,
                        line=dict(width=line_width, color=dark_color)
                    )
                if not new_marker_color:
                    scatter_options['marker']['color'] = dark_color
                trace_line_pt = go.Scatter(
                    x=[len(df[key]) - 1],
                    y=[df[key].tolist()[-1]],
                    **scatter_options
                )

                std = np.std(df[key])
                if std == 0:
                    extra_space = 0.3 * abs(df[key][0])
                    yrange_top = df[key].tolist()[0] + extra_space
                    yrange_bottom = df[key].tolist()[0] - extra_space
                else:
                    yrange_top = max(df[key].tolist()) + std
                    yrange_bottom = min(df[key].tolist()) - std
                if alternate_row_color:
                    bkg = rect(
                        'x{}'.format(j * num_of_chart_types + c + 1),
                        'y{}'.format(j * num_of_chart_types + c + 1),
                        x0=0, x1=len(df[key]),
                        y0=yrange_bottom, y1=yrange_top,
                        color=(
                            r_color
                        )
                    )
                    fig['layout']['shapes'].append(bkg)
                fig.append_trace(trace_line, j + 1, c + 1)
                fig.append_trace(trace_line_pt, j + 1, c + 1)

                fig['layout']['yaxis{}'.format(
                    j * num_of_chart_types + (c + 1)
                )]['range'] = [yrange_bottom, yrange_top]

            elif chart == 'bar':
                std = np.std(df[key])
                if std == 0:
                    extra_space = 0.3 * abs(df[key][0])
                    if df[key][0] < 0:
                        yrange_top = 0
                        yrange_bottom = (df[key].tolist()[0] - extra_space)
                    elif df[key][0] >= 0:
                        yrange_top = (df[key].tolist()[0] + extra_space)
                        yrange_bottom = 0
                else:
                    yrange_top = max(df[key].tolist()) + std
                    yrange_bottom = min(df[key].tolist()) - std

                trace_bar = go.Bar(
                    x=range(len(df[key])),
                    y=df[key].tolist(),
                    marker=dict(
                        color=[light_color for k in
                               range(len(df[key]) - 1)] + [dark_color]
                    )
                )

                if alternate_row_color:
                    bkg = rect(
                        'x{}'.format(j * num_of_chart_types + c + 1),
                        'y{}'.format(j * num_of_chart_types + c + 1),
                        x0=-1, x1=len(df[key]),
                        y0=yrange_bottom, y1=yrange_top,
                        color=(
                            r_color
                        )
                    )
                    fig['layout']['shapes'].append(bkg)
                fig.append_trace(trace_bar, j + 1, c + 1)

                fig['layout']['yaxis{}'.format(
                    j * num_of_chart_types + (c + 1)
                )]['range'] = [yrange_bottom, yrange_top]
            for x_y in ['xaxis', 'yaxis']:
                fig['layout']['{}{}'.format(
                    x_y, j * num_of_chart_types + (c + 1)
                )]['fixedrange'] = True

            # show titles
            if show_titles and j == 0:
                label = utils.annotation_dict_for_label(
                    chart, c + 1, num_of_chart_types, subplot_spacing=0,
                    row_col='col', flipped=False, column_width=column_width
                )
                fig['layout']['annotations'].append(label)

            for idx in narrow_idxs:
                for axis in ['xaxis', 'yaxis']:
                    fig['layout']['{}{}'.format(
                        axis, c * num_of_chart_types + idx + 1
                    )]['range'] = [0, 1]
        c_idx += 1
        trace_c_idx += 1


def create_sparkline(df, chart_types=None, row=None, column=None,
                     x=None, trace_colors=None, column_width=None,
                     show_titles=False, text_align='center',
                     horizontal_spacing=0.0, vertical_spacing=0.0,
                     alternate_row_color=True,
                     row_colors=('rgb(247, 247, 242)',
                                 'rgb(255, 253, 250)'),
                     line_width=2, scatter_options=None, **layout_options):
    """
    Returns figure for sparkline.

    :param (pd.DataFrame | list | tuple) df: either a list/tuple of
        dictionaries or a pandas DataFrame.
    :param (list|tuple) chart_types: a sequence of any combination of valid
        chart types. The valid chart types are 'label', 'bullet', 'line', 'avg'
        and 'bar'
        Default = ('label', 'bullet', 'line', 'avg', 'bar', 'area')
    :param (list|tuple) trace_colors: a list of colors or a list of lists of
        two colors. Each row uses two colors: a darker one and a lighter one.
        Options:
            - list of 2 colors: first color is dark color for all traces and
              second is light for all traces.
            - 1D list of more than 2 colors: the nth color in the list is the
              nth dark color for the traces and the associated light color is
              just 0.5 times the opacity of the dark color
            - lists of lists: each inner list must have exactly 2 colors in it
              and the first and second color of the nth inner list represent
              the dark and light color for the nth row repsectively
            - list of lists and colors: this is a combination of the previous
              options
        Whenever trace_colors has fewer colors than the number of rows of the
        figure, the colors will repeat from the start of the list
        Default = [['rgb(62,151,169)', 'rgb(181,221,232)']]
    :param (list) column_width: Specify a list that contains numbers where
        the amount of numbers in the list is equal to `chart_types`. Call
        `help(plotly.tools.make_subplots)` for more info on this subplot param
    :param (bool) show_titles: determines if title of chart type is displayed
        above their respective column
    :param (str) text_align: aligns label and avg cells. Use either 'center',
        'left', or 'right'. Default='center'.
    :param (float) horizontal_spacing: Space between subplot columns.
        Applied to all columns
        Default = 0.0
    :param (float) vertical_spacing: Space between subplot rows.
        Applied to all rows
        Default = 0.0
    :param (bool) alternate_row_color: set to True to enable the alternate
        row coloring of the chart. Uses the trace_colors from param 'row_colors'
        Default = True
    :param (list) row_colors: a list/tuple of colors that are used to
        alternately color the rows of the chart. If the number of colors in the
        list is fewer than the number of rows, the active color for the layout
        will be looped back to the first in the list
        Default = ('rgb(247, 247, 242)', 'rgb(255, 253, 250)')
    :param (float) line_width: sets the width of the lines used in 'area' or
        filled area line charts
        Default = 2
    :param (dict) scatter_options: describes attributes for the scatter point
        in each bullet chart such as label and marker size. Call
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

    # validate list/tuple of trace_colors
    if not trace_colors:
        trace_colors = [['rgb(62,151,169)', 'rgb(181,221,232)']]
    if not utils.is_sequence(trace_colors):
        raise exceptions.PlotlyError(
            'trace_colors must be a list/tuple'
        )

    trace_colors_2d = []
    for i, item in enumerate(trace_colors):
        plotly.colors.validate_colors(item)
        if utils.is_sequence(item):
            trace_colors_2d.append(item)
        else:
            # if hex convert to rgb
            if '#' in item:
                tuple_item = plotly.colors.hex_to_rgb(item)
                rgb_item = plotly.colors.label_rgb(tuple_item)
            else:
                rgb_item = item
            light_c = plotly.colors.find_intermediate_color(
                rgb_item, 'rgb(255, 255, 255)', 0.5, colortype='rgb'
            )
            trace_colors_2d.append([rgb_item, light_c])

    # validate chart_types and row, column, x
    if row or column or x:
        if not (row and column and x):
            raise exceptions.PlotlyError(
                "You must set the params 'row', 'column' and 'x' to valid "
                "column names of your dataframe"
            )

        # confirm valid row, column, x values
        for param in [row, column, x]:
            if param not in df:
                raise exceptions.PlotlyError(
                    '{} is not a column name of the dataframe'.format(param)
                )

        if not chart_types:
            chart_types = []
            for j, val in enumerate(df[column].unique()):
                if j == len(VALID_CHART_TYPES):
                    j = 0
                chart_types.append({val: VALID_CHART_TYPES[j]})
                j += 1

        if (not utils.is_sequence(chart_types) and
           not all(isinstance(i, dict) for i in chart_types)):
            raise exceptions.PlotlyError(
                "'chart_types' must be a list/tuple of dictionaries if "
                "'row', 'column', and 'x' are being used"
            )
        chart_types_keys = [k for d in chart_types for k in d.keys()]
        for key in chart_types_keys:
            if key not in df[column].unique():
                raise exceptions.PlotlyError(
                    "All the keys of the dictionaries in 'chart_types' must "
                    "be values in the chosen column. Since your selected "
                    "column is '{}', the available keys {}".format(
                        column,
                        utils.list_of_options(df[column].unique(), 'and')
                    )
                )

        # validate chart types
        chart_vals = [k for d in chart_types for k in d.values()]
        for item in chart_vals:
            if item not in VALID_CHART_TYPES:
                raise exceptions.PlotlyError(VALID_CHART_TYPE_MESSAGE)
    else:
        if not chart_types:
            chart_types = VALID_CHART_TYPES
        for item in chart_types:
            if item not in VALID_CHART_TYPES:
                raise exceptions.PlotlyError(VALID_CHART_TYPE_MESSAGE)

    num_of_chart_types = len(chart_types)
    # narrow columns that are 'label' or 'avg'
    narrow_cols = ['label', 'avg']
    narrow_idxs = []
    if not isinstance(chart_types, dict):
        for i, chart in enumerate(chart_types):
            if chart in narrow_cols:
                narrow_idxs.append(i)
    else:
        for i, chart in enumerate(chart_types):
            if chart in narrow_cols:
                narrow_idxs.append(i)

    if not column_width:
        column_width = [3.0] * num_of_chart_types
        for idx in narrow_idxs:
            column_width[idx] = 1.0

    # text alignment
    xanchor = text_align
    if text_align == 'left':
        align_x = 0
    elif text_align == 'center':
        align_x = 0.5
    elif text_align == 'right':
        align_x = 1
    else:
        raise exceptions.PlotlyError(
            'text_align must be left, center or right'
        )

    # scatter options
    default_scatter = {
        'mode': 'markers',
        'marker': {'size': 8,
                   'symbol': 'diamond-tall'}
    }

    if not scatter_options:
        scatter_options = {}

    if scatter_options == {}:
        scatter_options.update(default_scatter)
    else:
        # add default options to scatter_options if they are not present
        for k in default_scatter['marker']:
            try:
                if k not in scatter_options['marker']:
                    scatter_options['marker'][k] = default_scatter['marker'][k]
            except KeyError:
                scatter_options['marker'] = {}
                scatter_options['marker'][k] = default_scatter['marker'][k]

    if 'marker' in scatter_options and 'color' in scatter_options['marker']:
        new_marker_color = True
    else:
        new_marker_color = False

    # create fig
    if row and column and x:
        fig = plotly.tools.make_subplots(
            len(df[row].unique()), num_of_chart_types, print_grid=False,
            shared_xaxes=False, shared_yaxes=False,
            horizontal_spacing=horizontal_spacing,
            vertical_spacing=vertical_spacing, column_width=column_width
        )
    else:
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
        shapes=[],
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

    if row and column and x:
        _sparkline_tidy(
            df, fig, chart_types, num_of_chart_types, trace_colors_2d,
            column_width, alternate_row_color, row_colors, xanchor,
            line_width, align_x, scatter_options, new_marker_color,
            narrow_idxs, show_titles, row, column, x
        )
    else:
        _sparkline(
            df, fig, chart_types, num_of_chart_types, trace_colors_2d,
            column_width, alternate_row_color, row_colors, xanchor,
            line_width, align_x, scatter_options, new_marker_color,
            narrow_idxs, show_titles
        )

    return fig
