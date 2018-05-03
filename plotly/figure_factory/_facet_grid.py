from __future__ import absolute_import

from plotly import colors, exceptions, optional_imports
from plotly.figure_factory import utils
from plotly.graph_objs import graph_objs
from plotly.tools import make_subplots

import plotly
import plotly.graph_objs as go

import math
import copy
from numbers import Number
import numpy as np
import re

pd = optional_imports.get_module('pandas')

TICK_COLOR = '#969696'
AXIS_TITLE_COLOR = '#0f0f0f'
AXIS_TITLE_SIZE = 12
GRID_COLOR = '#ffffff'
LEGEND_COLOR = '#efefef'
PLOT_BGCOLOR = '#ededed'
ANNOT_RECT_COLOR = '#d0d0d0'
LEGEND_BORDER_WIDTH = 1
LEGEND_ANNOT_X = 1.05
LEGEND_ANNOT_Y = 0.5
MAX_TICKS_PER_AXIS = 5
THRES_FOR_FLIPPED_FACET_TITLES = 10
GRID_WIDTH = 1

X_AND_Y_TRACE_TYPES = ['scatter', 'scattergl', 'line', 'area']
X_OR_Y_TRACE_TYPES = ['histogram', 'bar', 'box', 'bullet', 'text']
VALID_TRACE_TYPES = X_AND_Y_TRACE_TYPES + X_OR_Y_TRACE_TYPES

CUSTOM_LABEL_ERROR = (
    'If you are using a dictionary for custom labels for the facet row/col, '
    'make sure each key in that column of the dataframe is in your facet '
    'labels. The keys you need are {}'
)

BULLET_USING_STRING_DATA_MSG = (
    'Whoops. You are attempting to create a bullet chart out of an array of '
    'data with at least one string in it.\n\nBullet charts in the facet grid '
    'present the mean, standard deviation and maximum value of a 1D dataset. '
    'Since all of these quantities are quantitiative, they can only be '
    'generated from numerical data.'
)

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


def _is_flipped(num):
    if num >= THRES_FOR_FLIPPED_FACET_TITLES:
        flipped = True
    else:
        flipped = False
    return flipped


def _return_label(original_label, facet_labels, facet_var):
    if isinstance(facet_labels, dict):
        label = facet_labels[original_label]
    elif isinstance(facet_labels, str):
        label = '{}: {}'.format(facet_var, original_label)
    else:
        label = original_label
    return label


def _legend_annotation(color_name):
    legend_title = dict(
        textangle=0,
        xanchor='left',
        yanchor='middle',
        x=LEGEND_ANNOT_X,
        y=1.03,
        showarrow=False,
        xref='paper',
        yref='paper',
        text='factor({})'.format(color_name),
        font=dict(
            size=13,
            color='#000000'
        )
    )
    return legend_title


def _annotation_dict(text, lane, num_of_lanes, SUBPLOT_SPACING, row_col='col',
                     flipped=True):
    l = (1 - (num_of_lanes - 1) * SUBPLOT_SPACING) / (num_of_lanes)
    if not flipped:
        xanchor = 'center'
        yanchor = 'middle'
        if row_col == 'col':
            x = (lane - 1) * (l + SUBPLOT_SPACING) + 0.5 * l
            y = 1.03
            textangle = 0
        elif row_col == 'row':
            y = (lane - 1) * (l + SUBPLOT_SPACING) + 0.5 * l
            x = 1.03
            textangle = 90
    else:
        if row_col == 'col':
            xanchor = 'center'
            yanchor = 'bottom'
            x = (lane - 1) * (l + SUBPLOT_SPACING) + 0.5 * l
            y = 1.0
            textangle = 270
        elif row_col == 'row':
            xanchor = 'left'
            yanchor = 'middle'
            y = (lane - 1) * (l + SUBPLOT_SPACING) + 0.5 * l
            x = 1.0
            textangle = 0

    annotation_dict = dict(
        textangle=textangle,
        xanchor=xanchor,
        yanchor=yanchor,
        x=x,
        y=y,
        showarrow=False,
        xref='paper',
        yref='paper',
        text=text,
        font=dict(
            size=13,
            color=AXIS_TITLE_COLOR
        )
    )
    return annotation_dict


def _axis_title_annotation(text, x_or_y_axis):
    if x_or_y_axis == 'x':
        x_pos = 0.5
        y_pos = -0.1
        textangle = 0
    elif x_or_y_axis == 'y':
        x_pos = -0.1
        y_pos = 0.5
        textangle = 270

    if not text:
        text = ''

    annot = {'font': {'color': '#000000', 'size': AXIS_TITLE_SIZE},
             'showarrow': False,
             'text': text,
             'textangle': textangle,
             'x': x_pos,
             'xanchor': 'center',
             'xref': 'paper',
             'y': y_pos,
             'yanchor': 'middle',
             'yref': 'paper'}
    return annot


def _add_shapes_to_fig(fig, annot_rect_color, flipped_rows=False,
                       flipped_cols=False):
    fig['layout']['shapes'] = []
    for key in fig['layout'].keys():
        if 'axis' in key and fig['layout'][key]['domain'] != [0.0, 1.0]:
            shape = {
               'fillcolor': annot_rect_color,
               'layer': 'below',
               'line': {'color': annot_rect_color, 'width': 1},
               'type': 'rect',
               'xref': 'paper',
               'yref': 'paper'
            }

            if 'xaxis' in key:
                shape['x0'] = fig['layout'][key]['domain'][0]
                shape['x1'] = fig['layout'][key]['domain'][1]
                shape['y0'] = 1.005
                shape['y1'] = 1.05

                if flipped_cols:
                    shape['y1'] += 0.5
                fig['layout']['shapes'].append(shape)

            elif 'yaxis' in key:
                shape['x0'] = 1.005
                shape['x1'] = 1.05
                shape['y0'] = fig['layout'][key]['domain'][0]
                shape['y1'] = fig['layout'][key]['domain'][1]

                if flipped_rows:
                    shape['x1'] += 1
                fig['layout']['shapes'].append(shape)


def _make_trace_for_scatter(trace, trace_type, color, **kwargs_marker):
    if trace_type in ['scatter', 'scattergl']:
        trace['mode'] = 'markers'
        trace['marker'] = dict(color=color, **kwargs_marker)
    return trace


def _return_traces_list_for_subplot_cell(trace_type, group, x, y, theme,
                                         trace_dimension,
                                         light_color, dark_color,
                                         marker_color, kwargs_marker,
                                         kwargs_trace):

    mode = None
    traces_for_cell = []
    if trace_type == 'bullet':
        if 'x' in trace_dimension:
            # check if data contains strings
            if any(isinstance(e, str) for e in group[x]):
                raise exceptions.PlotlyError(
                    BULLET_USING_STRING_DATA_MSG
                )
            std = np.std(group[x])
            rounded_mean = round(np.mean(group[x]), 2)
            max_value = max(group[x])
        else:
            # check if data contains strings
            if any(isinstance(e, str) for e in group[y]):
                raise exceptions.PlotlyError(
                    BULLET_USING_STRING_DATA_MSG
                )
            std = np.std(group[y])
            rounded_mean = round(np.mean(group[y]), 2)
            max_value = max(group[y])

        bullet_range_x = std
        bullet_measure_x = rounded_mean
        bullet_pt_x = max_value

        bullet_range = go.Bar(
            x=[bullet_range_x],
            y=[0.5],
            marker=dict(
                color='rgb(230,60,140)',
                line=kwargs_marker['line'],
            ),
            hoverinfo='x',
            orientation='h',
            width=0.5,
            **kwargs_trace
        )

        bullet_measure = go.Bar(
            x=[bullet_measure_x],
            y=[0.5],
            marker=dict(
                color=marker_color,
                line=kwargs_marker['line'],
            ),
            hoverinfo='x',
            orientation='h',
            width=0.14,
            offset=-0.07,
            **kwargs_trace
        )

        bullet_pt = go.Scatter(
            x=[bullet_pt_x],
            y=[0.5],
            hoverinfo='x',
            line=kwargs_marker['line'],
            **kwargs_trace
        )

        traces_for_cell.append(bullet_range)
        traces_for_cell.append(bullet_measure)
        traces_for_cell.append(bullet_pt)

    elif trace_type in ['text']:  # grab from a column
        pass

    elif trace_type in ['scatter', 'scattergl', 'line',
                        'histogram', 'bar', 'box']:
        trace = dict(
            type=trace_type,
            marker=dict(
                color=dark_color,
                line=kwargs_marker['line'],
            ),
            **kwargs_trace
        )

        last_pt = dict(
            type=trace_type,
            marker=dict(
                color=light_color,
            ),
            **kwargs_trace
        )

        if trace_type in ['scatter', 'scattergl']:
            trace['mode'] = 'markers'
            last_pt['mode'] = 'markers'

        elif trace_type == 'line':
            trace['mode'] = 'lines'
            trace['type'] = 'scatter'
            last_pt['mode'] = 'markers'
            last_pt['type'] = 'scatter'

        if trace_dimension == 'x':
            # add x
            trace['x'] = list(group[x]) if len(group[x]) <= 1 else list(group[x])[:-1]
            last_pt['x'] = list(group[x])[-1:]

            #trace['y'] = [None]
            #last_pt['y'] = [None]
        elif trace_dimension == 'y':
            #trace['x'] = [None]
            #last_pt['x'] = [None]

            # add y
            trace['y'] = list(group[y]) if len(group[y]) <= 1 else list(group[y])[:-1]
            last_pt['y'] = list(group[y])[-1:]
        else:  # 'x+y'
            if trace_type in ['scatter', 'scattergl', 'line', 'histogram']:
                # add both x and y
                trace['x'] = list(group[x]) if len(group[x]) <= 1 else list(group[x])[:-1]
                last_pt['x'] = list(group[x])[-1:]

                #trace['y'] = list(group[y]) if len(group[y]) <= 1 else list(group[y])[:-1]
                #last_pt['y'] = list(group[y])[-1:]

            elif trace_type in ['box', 'bar']:
                # add only x
                trace['x'] = list(group[x]) if len(group[x]) <= 1 else list(group[x])[:-1]
                last_pt['x'] = list(group[x])[-1:]

                #trace['y'] = [None]
                #last_pt['y'] = [None]

        traces_for_cell.append(trace)
        traces_for_cell.append(last_pt)

    elif trace_type in ['area']:
        trace = dict(
            x=range(len(group[y])),
            type='scatter',
            mode='lines',
            fill='tozeroy',
            fillcolor=light_color,
            line=dict(
                color=dark_color
            )
        )

        if y:
            trace['y'] = list(group[y]) if len(group[y]) <= 1 else list(group[y])[:-1]
        traces_for_cell.append(trace)

    return traces_for_cell


def _facet_grid_color_categorical(df, x, y, facet_row, facet_col, color_name,
                                  colormap, num_of_rows, num_of_cols,
                                  facet_row_labels, facet_col_labels,
                                  trace_type, flipped_rows, flipped_cols,
                                  show_boxes, SUBPLOT_SPACING, marker_color,
                                  kwargs_trace, kwargs_marker, column_width,
                                  trace_dimension):

    fig = make_subplots(rows=num_of_rows, cols=num_of_cols,
                        shared_xaxes=True, shared_yaxes=True,
                        horizontal_spacing=SUBPLOT_SPACING,
                        vertical_spacing=SUBPLOT_SPACING, print_grid=False,
                        column_width=column_width)

    annotations = []
    if not facet_row and not facet_col:
        color_groups = list(df.groupby(color_name))
        for group in color_groups:
            trace = dict(
                type=trace_type,
                name=group[0],
                marker=dict(
                    color=colormap[group[0]],
                ),
                **kwargs_trace
            )
            if x:
                trace['x'] = group[1][x]
            if y:
                trace['y'] = group[1][y]
            trace = _make_trace_for_scatter(
                trace, trace_type, colormap[group[0]], **kwargs_marker
            )

            fig.append_trace(trace, 1, 1)

    elif (facet_row and not facet_col) or (not facet_row and facet_col):
        groups_by_facet = list(
            df.groupby(facet_row if facet_row else facet_col)
        )
        for j, group in enumerate(groups_by_facet):
            for color_val in df[color_name].unique():
                data_by_color = group[1][group[1][color_name] == color_val]
                trace = dict(
                    type=trace_type,
                    name=color_val,
                    marker=dict(
                        color=colormap[color_val],
                    ),
                    **kwargs_trace
                )
                if x:
                    trace['x'] = data_by_color[x]
                if y:
                    trace['y'] = data_by_color[y]
                trace = _make_trace_for_scatter(
                    trace, trace_type, colormap[color_val], **kwargs_marker
                )

                fig.append_trace(trace,
                                 j + 1 if facet_row else 1,
                                 1 if facet_row else j + 1)

            label = _return_label(
                group[0],
                facet_row_labels if facet_row else facet_col_labels,
                facet_row if facet_row else facet_col
            )

            annotations.append(
                _annotation_dict(
                    label,
                    num_of_rows - j if facet_row else j + 1,
                    num_of_rows if facet_row else num_of_cols,
                    SUBPLOT_SPACING,
                    'row' if facet_row else 'col',
                    flipped_rows)
            )

    elif facet_row and facet_col:
        groups_by_facets = list(df.groupby([facet_row, facet_col]))
        tuple_to_facet_group = {item[0]: item[1] for
                                item in groups_by_facets}

        row_values = df[facet_row].unique()
        col_values = df[facet_col].unique()
        color_vals = df[color_name].unique()
        for row_count, x_val in enumerate(row_values):
            for col_count, y_val in enumerate(col_values):
                try:
                    group = tuple_to_facet_group[(x_val, y_val)]
                except KeyError:
                    group = pd.DataFrame([[None, None, None]],
                                         columns=[x, y, color_name])

                for color_val in color_vals:
                    if group.values.tolist() != [[None, None, None]]:
                        group_filtered = group[group[color_name] == color_val]

                        trace = dict(
                            type=trace_type,
                            name=color_val,
                            marker=dict(
                                color=colormap[color_val],
                            ),
                            **kwargs_trace
                        )
                        new_x = group_filtered[x]
                        new_y = group_filtered[y]
                    else:
                        trace = dict(
                            type=trace_type,
                            name=color_val,
                            marker=dict(
                                color=colormap[color_val],
                            ),
                            showlegend=False,
                            **kwargs_trace
                        )
                        new_x = group[x]
                        new_y = group[y]

                    if x:
                        trace['x'] = new_x
                    if y:
                        trace['y'] = new_y
                    trace = _make_trace_for_scatter(
                        trace, trace_type, colormap[color_val],
                        **kwargs_marker
                    )

                    fig.append_trace(trace, row_count + 1, col_count + 1)
                if row_count == 0:
                    label = _return_label(col_values[col_count],
                                          facet_col_labels, facet_col)
                    annotations.append(
                        _annotation_dict(label, col_count + 1, num_of_cols,
                                         SUBPLOT_SPACING,
                                         row_col='col', flipped=flipped_cols)
                        )
            label = _return_label(row_values[row_count],
                                  facet_row_labels, facet_row)
            annotations.append(
                _annotation_dict(label, num_of_rows - row_count, num_of_rows,
                                 SUBPLOT_SPACING,
                                 row_col='row', flipped=flipped_rows)
            )

    # add annotations
    fig['layout']['annotations'] = annotations

    return fig


def _facet_grid_color_numerical(df, x, y, facet_row, facet_col, color_name,
                                colormap, num_of_rows,
                                num_of_cols, facet_row_labels,
                                facet_col_labels, trace_type,
                                flipped_rows, flipped_cols, show_boxes,
                                SUBPLOT_SPACING, marker_color, kwargs_trace,
                                kwargs_marker, column_width,
                                trace_dimension):

    fig = make_subplots(rows=num_of_rows, cols=num_of_cols,
                        shared_xaxes=True, shared_yaxes=True,
                        horizontal_spacing=SUBPLOT_SPACING,
                        vertical_spacing=SUBPLOT_SPACING, print_grid=False,
                        column_width=column_width)

    annotations = []
    if not facet_row and not facet_col:
        trace = dict(
            type=trace_type,
            marker=dict(
                color=df[color_name],
                colorscale=colormap,
                showscale=True,
            ),
            **kwargs_trace
        )
        if x:
            trace['x'] = df[x]
        if y:
            trace['y'] = df[y]
        trace = _make_trace_for_scatter(
            trace, trace_type, df[color_name], **kwargs_marker
        )

        fig.append_trace(trace, 1, 1)

    if (facet_row and not facet_col) or (not facet_row and facet_col):
        groups_by_facet = list(
            df.groupby(facet_row if facet_row else facet_col)
        )
        for j, group in enumerate(groups_by_facet):
            trace = dict(
                type=trace_type,
                marker=dict(
                    color=df[color_name],
                    colorscale=colormap,
                    showscale=True,
                    colorbar=dict(x=1.15),
                ),
                **kwargs_trace
            )
            if x:
                trace['x'] = group[1][x]
            if y:
                trace['y'] = group[1][y]
            trace = _make_trace_for_scatter(
                trace, trace_type, df[color_name], **kwargs_marker
            )

            fig.append_trace(
                trace,
                j + 1 if facet_row else 1,
                1 if facet_row else j + 1
            )

            labels = facet_row_labels if facet_row else facet_col_labels
            label = _return_label(
                group[0], labels, facet_row if facet_row else facet_col
            )

            annotations.append(
                _annotation_dict(
                    label,
                    num_of_rows - j if facet_row else j + 1,
                    num_of_rows if facet_row else num_of_cols,
                    SUBPLOT_SPACING,
                    'row' if facet_row else 'col',
                    flipped=flipped_rows)
            )

    elif facet_row and facet_col:
        groups_by_facets = list(df.groupby([facet_row, facet_col]))
        tuple_to_facet_group = {item[0]: item[1] for
                                item in groups_by_facets}

        row_values = df[facet_row].unique()
        col_values = df[facet_col].unique()
        for row_count, x_val in enumerate(row_values):
            for col_count, y_val in enumerate(col_values):
                try:
                    group = tuple_to_facet_group[(x_val, y_val)]
                except KeyError:
                    group = pd.DataFrame([[None, None, None]],
                                         columns=[x, y, color_name])

                if group.values.tolist() != [[None, None, None]]:
                    trace = dict(
                        type=trace_type,
                        marker=dict(
                            color=df[color_name],
                            colorscale=colormap,
                            showscale=(row_count == 0),
                            colorbar=dict(x=1.15),
                        ),
                        **kwargs_trace
                    )

                else:
                    trace = dict(
                        type=trace_type,
                        showlegend=False,
                        **kwargs_trace
                    )

                if x:
                    trace['x'] = group[x]
                if y:
                    trace['y'] = group[y]
                trace = _make_trace_for_scatter(
                    trace, trace_type, df[color_name], **kwargs_marker
                )

                fig.append_trace(trace, row_count + 1, col_count + 1)
                if row_count == 0:
                    label = _return_label(col_values[col_count],
                                          facet_col_labels, facet_col)
                    annotations.append(
                        _annotation_dict(label, col_count + 1, num_of_cols,
                                         SUBPLOT_SPACING,
                                         row_col='col', flipped=flipped_cols)
                        )
            label = _return_label(row_values[row_count],
                                  facet_row_labels, facet_row)
            annotations.append(
                _annotation_dict(row_values[row_count],
                                 num_of_rows - row_count, num_of_rows,
                                 SUBPLOT_SPACING,
                                 row_col='row', flipped=flipped_rows)
            )

    # add annotations
    fig['layout']['annotations'] = annotations

    return fig


def _facet_grid(df, x, y, facet_row, facet_col, num_of_rows,
                num_of_cols, facet_row_labels, facet_col_labels,
                trace_type, flipped_rows, flipped_cols, show_boxes,
                SUBPLOT_SPACING, marker_color, kwargs_trace, kwargs_marker,
                row_colors, alternate_row_color, theme, column_width,
                trace_dimension, trace_colors_2d):
    shared_xaxes = shared_yaxes = False
    fig = make_subplots(rows=num_of_rows, cols=num_of_cols,
                        shared_xaxes=shared_xaxes, shared_yaxes=shared_yaxes,
                        horizontal_spacing=SUBPLOT_SPACING,
                        vertical_spacing=SUBPLOT_SPACING, print_grid=False,
                        column_width=column_width)
    annotations = []
    if not facet_row and not facet_col:
        trace = dict(
            type=trace_type,
            marker=dict(
                color=marker_color,
                line=kwargs_marker['line'],
            ),
            **kwargs_trace
        )

        if x:
            trace['x'] = df[x]
        if y:
            trace['y'] = df[y]

        if trace_type in ['scatter', 'scattergl']:
            trace['mode'] = 'markers'
            trace['marker'] = dict(color=marker_color, **kwargs_marker)
        fig.append_trace(trace, 1, 1)

    elif (facet_row and not facet_col) or (not facet_row and facet_col):
        groups_by_facet = list(
            df.groupby(facet_row if facet_row else facet_col)
        )
        for j, group in enumerate(groups_by_facet):
            trace = dict(
                type=trace_type,
                marker=dict(
                    color=marker_color,
                    line=kwargs_marker['line'],
                ),
                **kwargs_trace
            )

            if x:
                trace['x'] = group[1][x]
            if y:
                trace['y'] = group[1][y]
            trace = _make_trace_for_scatter(
                trace, trace_type, marker_color, **kwargs_marker
            )

            fig.append_trace(
                trace,
                j + 1 if facet_row else 1,
                1 if facet_row else j + 1
            )

            label = _return_label(
                group[0],
                facet_row_labels if facet_row else facet_col_labels,
                facet_row if facet_row else facet_col
            )

            annotations.append(
                utils.annotation_dict_for_label(
                    label,
                    num_of_rows - j if facet_row else j + 1,
                    num_of_rows if facet_row else num_of_cols,
                    SUBPLOT_SPACING,
                    'row' if facet_row else 'col',
                    flipped_rows,
                )
            )

    elif facet_row and facet_col:
        groups_by_facets = list(df.groupby([facet_row, facet_col]))
        tuple_to_facet_group = {item[0]: item[1] for
                                item in groups_by_facets}

        row_values = df[facet_row].unique()
        col_values = df[facet_col].unique()

        trace_c_idx = 0
        for row_count, x_val in enumerate(row_values):
            for col_count, y_val in enumerate(col_values):
                try:
                    group = tuple_to_facet_group[(x_val, y_val)]
                except KeyError:
                    group = pd.DataFrame([[None, None]], columns=[x, y])

                # set light and dark colors
                if trace_c_idx >= len(trace_colors_2d):
                    trace_c_idx = 0
                light_color = trace_colors_2d[trace_c_idx][1]
                dark_color = trace_colors_2d[trace_c_idx][0]

                traces_for_cell = _return_traces_list_for_subplot_cell(
                    trace_type, group, x, y, theme, trace_dimension,
                    light_color, dark_color, marker_color, kwargs_marker,
                    kwargs_trace
                )

                # insert traces in subplot cell
                for trace in traces_for_cell:
                    fig.append_trace(trace, row_count + 1, col_count + 1)

                if row_count == 0:
                    label = _return_label(col_values[col_count],
                                          facet_col_labels,
                                          facet_col)
                    annotations.append(
                        utils.annotation_dict_for_label(
                            label, col_count + 1, num_of_cols, SUBPLOT_SPACING,
                            row_col='col', flipped=flipped_cols,
                            column_width=column_width
                        )
                    )

            label = _return_label(row_values[row_count],
                                  facet_row_labels,
                                  facet_row)

            annotations.append(
                utils.annotation_dict_for_label(
                    label, num_of_rows - row_count, num_of_rows,
                    SUBPLOT_SPACING, row_col='row', flipped=flipped_rows
                )
            )
            trace_c_idx += 1

    # add annotations
    fig['layout']['annotations'] = annotations

    return fig


def create_facet_grid(df, x=None, y=None, facet_row=None, facet_col=None,
                      color_name=None, colormap=None, color_is_cat=False,
                      facet_row_labels=None, facet_col_labels=None,
                      height=None, width=None, trace_type='scatter',
                      scales='fixed', dtick_x=None, dtick_y=None,
                      show_boxes=True, ggplot2=False, binsize=1,
                      row_colors=('rgb(247, 247, 242)',
                                  'rgb(255, 253, 250)'),
                      alternate_row_color=True,
                      theme='facet', column_width=None, trace_dimension=None,
                      trace_colors=None, x_margin_factor=0.4,
                      y_margin_factor=0.4, chart_types=None,
                      **kwargs):
    """
    Returns figure for facet grid.

    :param (pd.DataFrame) df: the dataframe of columns for the facet grid.
    :param (str) x: the name of the dataframe column for the x axis data.
    :param (str) y: the name of the dataframe column for the y axis data.
    :param (str) facet_row: the name of the dataframe column that is used to
        facet the grid into row panels.
    :param (str) facet_col: the name of the dataframe column that is used to
        facet the grid into column panels.
    :param (str) color_name: the name of your dataframe column that will
        function as the colormap variable.
    :param (str|list|dict) colormap: the param that determines how the
        color_name column colors the data. If the dataframe contains numeric
        data, then a dictionary of colors will group the data categorically
        while a Plotly Colorscale name or a custom colorscale will treat it
        numerically. To learn more about colors and types of colormap, run
        `help(plotly.colors)`.
    :param (bool) color_is_cat: determines whether a numerical column for the
        colormap will be treated as categorical (True) or sequential (False).
            Default = False.
    :param (str|dict) facet_row_labels: set to either 'name' or a dictionary
        of all the unique values in the faceting row mapped to some text to
        show up in the label annotations. If None, labeling works like usual.
    :param (str|dict) facet_col_labels: set to either 'name' or a dictionary
        of all the values in the faceting row mapped to some text to show up
        in the label annotations. If None, labeling works like usual.
    :param (int) height: the height of the facet grid figure.
    :param (int) width: the width of the facet grid figure.
    :param (str) trace_type: decides the type of plot to appear in the
        facet grid. The options are 'scatter', 'scattergl', 'histogram',
        'bar', and 'box'.
        Default = 'scatter'.
    :param (str) scales: determines if axes have fixed ranges or not. Valid
        settings are 'fixed' (all axes fixed), 'free_x' (x axis free only),
        'free_y' (y axis free only) or 'free' (both axes free).
    :param (float) dtick_x: determines the distance between each tick on the
        x-axis. Default is None which means dtick_x is set automatically.
    :param (float) dtick_y: determines the distance between each tick on the
        y-axis. Default is None which means dtick_y is set automatically.
    :param (bool) show_boxes: draws grey boxes behind the facet titles.
    :param (bool) ggplot2: draws the facet grid in the style of `ggplot2`. See
        http://ggplot2.tidyverse.org/reference/facet_grid.html for reference.
        Default = False
    :param (int) binsize: groups all data into bins of a given length.
    :param (tuple|list) row_colors:
    :param (str) theme: determines the layout style of the plot. The options
        are 'facet' (default) and 'sparklines'.
    :param (list) column_width: Specify a list that contains numbers where
        the amount of numbers in the list is equal to `chart_types`. Call
        `help(plotly.tools.make_subplots)` for more info on this subplot param
    :param (str) trace_dimension: the trace data for plotting the various
        charts. Some charts can only work properly with one variable such as
        bullet or histogram, while scatter and area charts can take 'x' and
        'y' data. The valid options are 'x', 'y' and 'x+y'. If trace_dimension
        is not set, it will automatically set to:
            - 'x' if x=None and y=None OR x='foo' and y='bar'
            - 'x' or 'y' if ONLY one of 'x' or 'y' is set
    :param (list|tuple) trace_colors: a list of colors or a list of lists of
        two colors. Each row in a sparkline chart uses two colors: a darker
        one and a lighter one.
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
    :param (float) x_margin_factor: proportional to how much margin space
        along the x axis there is from the data points to the subplot cell
        border. The x_margin_factor is multiplied by the standard deviation of
        the x-values of the data to yield the actual margin.
        Default = 0.2
    :param (float) y_margin_factor: proportional to how much margin space
        along the y axis there is from the data points to the subplot cell
        border. The y_margin_factor is multiplied by the standard deviation of
        the y-values of the data to yield the actual margin.
        Default = 0.2
    :param (list|tuple) chart_types: a sequence (list/tuple/etc) of valid
        chart names that each column will produce in order from left to right.
    :param (dict) kwargs: a dictionary of scatterplot arguments.

    Examples 1: One Way Faceting
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd

    mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

    fig = ff.create_facet_grid(
        mpg,
        x='displ',
        y='cty',
        facet_col='cyl',
    )
    py.iplot(fig, filename='facet_grid_mpg_one_way_facet')
    ```

    Example 2: Two Way Faceting
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd

    mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

    fig = ff.create_facet_grid(
        mpg,
        x='displ',
        y='cty',
        facet_row='drv',
        facet_col='cyl',
    )
    py.iplot(fig, filename='facet_grid_mpg_two_way_facet')
    ```

    Example 3: Categorical Coloring
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd

    mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

    fig = ff.create_facet_grid(
        mtcars,
        x='mpg',
        y='wt',
        facet_col='cyl',
        color_name='cyl',
        color_is_cat=True,
    )
    py.iplot(fig, filename='facet_grid_mpg_default_colors')
    ```

    Example 4: Sequential Coloring
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd

    tips = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tips.csv')

    fig = ff.create_facet_grid(
        tips,
        x='total_bill',
        y='tip',
        facet_row='sex',
        facet_col='smoker',
        color_name='size',
        colormap='Viridis',
    )
    py.iplot(fig, filename='facet_grid_tips_sequential_colors')
    ```

    Example 5: Custom labels
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd

    mtcars = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv')

    fig = ff.create_facet_grid(
        mtcars,
        x='wt',
        y='mpg',
        facet_col='cyl',
        facet_col_labels={4: "$\\alpha$", 6: '$\\beta$', 8: '$\sqrt[y]{x}$'},
    )

    py.iplot(fig, filename='facet_grid_mtcars_custom_labels')
    ```

    Example 6: Other Trace Type
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd

    mtcars = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv')

    fig = ff.create_facet_grid(
        mtcars,
        x='wt',
        facet_col='cyl',
        trace_type='histogram',
    )

    py.iplot(fig, filename='facet_grid_mtcars_other_trace_type')
    ```
    """
    if not pd:
        raise exceptions.ImportError(
            "'pandas' must be installed for this figure_factory."
        )

    if not isinstance(df, pd.DataFrame):
        raise exceptions.PlotlyError(
            "You must input a pandas DataFrame."
        )

    # make sure all columns are of homogenous datatype
    utils.validate_dataframe(df)

    for key in [x, y, facet_row, facet_col, color_name]:
        if key is not None:
            try:
                df[key]
            except KeyError:
                # TODO: change error message in tests
                raise exceptions.PlotlyError(
                    "x, y, facet_row, facet_col and color_name must be keys "
                    "in your dataframe if they are not set to None."
                )
    # autoscale histogram bars
    if trace_type not in ['scatter', 'scattergl']:
        scales = 'free'

    # validate scales
    if scales not in ['fixed', 'free_x', 'free_y', 'free']:
        raise exceptions.PlotlyError(
            "'scales' must be set to 'fixed', 'free_x', 'free_y' and 'free'."
        )

    if trace_type not in VALID_TRACE_TYPES:
        raise exceptions.PlotlyError(
            "'trace_type' must be in {}".format(VALID_TRACE_TYPES)
        )

    # theme
    if theme not in ['facet', 'sparklines']:
        raise exceptions.PlotlyError(
            "theme must be 'facet' or 'sparklines'"
        )

    if theme == 'sparklines':
        SUBPLOT_SPACING = 0.0
    else:
        if trace_type == 'histogram':
            SUBPLOT_SPACING = 0.06
        else:
            SUBPLOT_SPACING = 0.015

    # seperate kwargs for marker and else
    if 'marker' in kwargs:
        kwargs_marker = kwargs['marker']
    else:
        kwargs_marker = {}
    marker_color = kwargs_marker.pop('color', None)
    kwargs.pop('marker', None)
    kwargs_trace = kwargs

    if 'size' not in kwargs_marker:
        if ggplot2:
            kwargs_marker['size'] = 5
        else:
            kwargs_marker['size'] = 8

    if 'opacity' not in kwargs_marker:
        if not ggplot2:
            kwargs_trace['opacity'] = 0.6

    if 'line' not in kwargs_marker:
        if not ggplot2:
            kwargs_marker['line'] = {'color': 'darkgrey', 'width': 1}
        else:
            kwargs_marker['line'] = {}

    # default marker size
    if not ggplot2:
        if not marker_color:
            marker_color = 'rgb(31, 119, 180)'
    else:
        marker_color = 'rgb(0, 0, 0)'

    # set trace dimension if None
    if trace_dimension is None:
        trace_dimension = 'x'

    # validate trace dimension
    if trace_dimension not in ['x', 'y', 'x+y']:
        raise exceptions.PlotlyError(
            "trace_dimension must be either 'x', 'y' or 'x+y'"
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


    num_of_rows = 1
    num_of_cols = 1
    flipped_rows = False
    flipped_cols = False
    if facet_row:
        num_of_rows = len(df[facet_row].unique())
        flipped_rows = _is_flipped(num_of_rows)
        if isinstance(facet_row_labels, dict):
            for key in df[facet_row].unique():
                if key not in facet_row_labels.keys():
                    unique_keys = df[facet_row].unique().tolist()
                    raise exceptions.PlotlyError(
                        CUSTOM_LABEL_ERROR.format(unique_keys)
                    )
    if facet_col:
        num_of_cols = len(df[facet_col].unique())
        flipped_cols = _is_flipped(num_of_cols)
        if isinstance(facet_col_labels, dict):
            for key in df[facet_col].unique():
                if key not in facet_col_labels.keys():
                    unique_keys = df[facet_col].unique().tolist()
                    raise exceptions.PlotlyError(
                        CUSTOM_LABEL_ERROR.format(unique_keys)
                    )

    if column_width is None:
        column_width = [1 for _ in range(num_of_cols)]

    # validate chart_types
    # TODO: integrate this with trace_type eventually
    # and keep backwards compatibility
    if chart_types is None:
        chart_types = ['scatter' for _ in range(num_of_cols)]
    else:
        # TODO: use sequence checker, not just list
        if not isinstance(chart_types, list):
            raise exceptions.PlotlyError(
                'chart_types must be a list'
            )
        if len(chart_types) != num_of_cols:
            raise exceptions.PlotlyError(
                'number of strings in chart_types must be equal to the '
                'number of columns'
            )
    show_legend = False
    if color_name:
        if isinstance(df[color_name].iloc[0], str) or color_is_cat:
            show_legend = True
            if isinstance(colormap, dict):
                utils.validate_colors_dict(colormap, 'rgb')

                for val in df[color_name].unique():
                    if val not in colormap.keys():
                        raise exceptions.PlotlyError(
                            "If using 'colormap' as a dictionary, make sure "
                            "all the values of the colormap column are in "
                            "the keys of your dictionary."
                        )
            else:
                # use default plotly colors for dictionary
                default_colors = utils.DEFAULT_PLOTLY_COLORS
                colormap = {}
                j = 0
                for val in df[color_name].unique():
                    if j >= len(default_colors):
                        j = 0
                    colormap[val] = default_colors[j]
                    j += 1
            fig = _facet_grid_color_categorical(
                df, x, y, facet_row, facet_col, color_name, colormap,
                num_of_rows, num_of_cols, facet_row_labels, facet_col_labels,
                trace_type, flipped_rows, flipped_cols, show_boxes,
                SUBPLOT_SPACING, marker_color, kwargs_trace, kwargs_marker,
                column_width, trace_dimension
            )

        elif isinstance(df[color_name].iloc[0], Number):
            if isinstance(colormap, dict):
                show_legend = True
                utils.validate_colors_dict(colormap, 'rgb')

                for val in df[color_name].unique():
                    if val not in colormap.keys():
                        raise exceptions.PlotlyError(
                            "If using 'colormap' as a dictionary, make sure "
                            "all the values of the colormap column are in "
                            "the keys of your dictionary."
                        )
                fig = _facet_grid_color_categorical(
                    df, x, y, facet_row, facet_col, color_name, colormap,
                    num_of_rows, num_of_cols, facet_row_labels,
                    facet_col_labels, trace_type, flipped_rows,
                    flipped_cols, show_boxes, SUBPLOT_SPACING, marker_color,
                    kwargs_trace, kwargs_marker, column_width,
                    trace_dimension
                )

            elif isinstance(colormap, list):
                colorscale_list = colormap
                utils.validate_colorscale(colorscale_list)

                fig = _facet_grid_color_numerical(
                    df, x, y, facet_row, facet_col, color_name,
                    colorscale_list, num_of_rows, num_of_cols,
                    facet_row_labels, facet_col_labels, trace_type,
                    flipped_rows, flipped_cols, show_boxes, SUBPLOT_SPACING,
                    marker_color, kwargs_trace, kwargs_marker, column_width,
                    trace_dimension
                )
            elif isinstance(colormap, str):
                if colormap in colors.PLOTLY_SCALES.keys():
                    colorscale_list = colors.PLOTLY_SCALES[colormap]
                else:
                    raise exceptions.PlotlyError(
                        "If 'colormap' is a string, it must be the name "
                        "of a Plotly Colorscale. The available colorscale "
                        "names are {}".format(colors.PLOTLY_SCALES.keys())
                    )
                fig = _facet_grid_color_numerical(
                    df, x, y, facet_row, facet_col, color_name,
                    colorscale_list, num_of_rows, num_of_cols,
                    facet_row_labels, facet_col_labels, trace_type,
                    flipped_rows, flipped_cols, show_boxes, SUBPLOT_SPACING,
                    marker_color, kwargs_trace, kwargs_marker, column_width,
                    trace_dimension
                )
            else:
                colorscale_list = colors.PLOTLY_SCALES['Reds']
                fig = _facet_grid_color_numerical(
                    df, x, y, facet_row, facet_col, color_name,
                    colorscale_list, num_of_rows, num_of_cols,
                    facet_row_labels, facet_col_labels, trace_type,
                    flipped_rows, flipped_cols, show_boxes, SUBPLOT_SPACING,
                    marker_color, kwargs_trace, kwargs_marker, column_width,
                    trace_dimension
                )

    else:
        fig = _facet_grid(
            df, x, y, facet_row, facet_col, num_of_rows, num_of_cols,
            facet_row_labels, facet_col_labels, trace_type, flipped_rows,
            flipped_cols, show_boxes, SUBPLOT_SPACING, marker_color,
            kwargs_trace, kwargs_marker, row_colors, alternate_row_color,
            theme, column_width, trace_dimension, trace_colors_2d
        )

    # style the layout depending on theme
    if not height:
        height = max(600, 100 * num_of_rows)
    if not width:
        width = max(600, 100 * num_of_cols)

    if theme == 'sparklines':
        fig['layout'].update(height=height, width=width, title='')

    else:
        fig['layout'].update(height=height, width=width, title='',
                             paper_bgcolor='rgb(251, 251, 251)')

        if ggplot2:
            fig['layout'].update(plot_bgcolor=PLOT_BGCOLOR,
                                 paper_bgcolor='rgb(255, 255, 255)',
                                 hovermode='closest')

    # axis titles
    x_title_annot = _axis_title_annotation(x, 'x')
    y_title_annot = _axis_title_annotation(y, 'y')
    fig['layout']['annotations'].append(x_title_annot)
    fig['layout']['annotations'].append(y_title_annot)

    # legend
    fig['layout']['showlegend'] = show_legend
    fig['layout']['legend']['bgcolor'] = LEGEND_COLOR
    fig['layout']['legend']['borderwidth'] = LEGEND_BORDER_WIDTH
    fig['layout']['legend']['x'] = 1.05
    fig['layout']['legend']['y'] = 1
    fig['layout']['legend']['yanchor'] = 'top'

    if show_legend:
        fig['layout']['showlegend'] = show_legend
        if ggplot2:
            if color_name:
                legend_annot = _legend_annotation(color_name)
                fig['layout']['annotations'].append(legend_annot)
            fig['layout']['margin']['r'] = 150

    # add shaded boxes behind axis titles
    if show_boxes and ggplot2:
        _add_shapes_to_fig(fig, ANNOT_RECT_COLOR, flipped_rows, flipped_cols)

    # all xaxis and yaxis labels
    axis_labels = {'x': [], 'y': []}
    for key in fig['layout']:
        if 'xaxis' in key:
            axis_labels['x'].append(key)
        elif 'yaxis' in key:
            axis_labels['y'].append(key)

    string_number_in_data = False
    for var in [v for v in [x, y] if v]:
        if isinstance(df[var].tolist()[0], str):
            for item in df[var]:
                try:
                    int(item)
                    string_number_in_data = True
                except ValueError:
                    pass

    if string_number_in_data:
        for x_y in axis_labels.keys():
            for axis_name in axis_labels[x_y]:
                fig['layout'][axis_name]['type'] = 'category'

    if theme == 'facet':
        if scales == 'fixed':
            fixed_axes = ['x', 'y']
        elif scales == 'free_x':
            fixed_axes = ['y']
        elif scales == 'free_y':
            fixed_axes = ['x']
        elif scales == 'free':
            fixed_axes = []
    else:
        fixed_axes = ['x', 'y']

    # fixed ranges
    if theme == 'facet':
        for x_y in fixed_axes:
            min_ranges = []
            max_ranges = []
            for trace in fig['data']:
                if trace[x_y] is not None and len(trace[x_y]) > 0:
                    min_ranges.append(min(trace[x_y]))
                    max_ranges.append(max(trace[x_y]))
            while None in min_ranges:
                min_ranges.remove(None)
            while None in max_ranges:
                max_ranges.remove(None)

            min_range = min(min_ranges)
            max_range = max(max_ranges)

            range_are_numbers = (isinstance(min_range, Number) and
                                 isinstance(max_range, Number))

            if range_are_numbers:
                min_range = math.floor(min_range)
                max_range = math.ceil(max_range)

                # widen frame by 5% on each side
                min_range -= 0.05 * (max_range - min_range)
                max_range += 0.05 * (max_range - min_range)

                if x_y == 'x':
                    if dtick_x:
                        dtick = dtick_x
                    else:
                        dtick = math.floor(
                            (max_range - min_range) / MAX_TICKS_PER_AXIS
                        )
                elif x_y == 'y':
                    if dtick_y:
                        dtick = dtick_y
                    else:
                        dtick = math.floor(
                            (max_range - min_range) / MAX_TICKS_PER_AXIS
                        )
            else:
                dtick = 1

            for axis_title in axis_labels[x_y]:
                fig['layout'][axis_title]['dtick'] = dtick
                fig['layout'][axis_title]['ticklen'] = 0
                fig['layout'][axis_title]['zeroline'] = False
                if ggplot2:
                    fig['layout'][axis_title]['tickwidth'] = 1
                    fig['layout'][axis_title]['ticklen'] = 4
                    fig['layout'][axis_title]['gridwidth'] = GRID_WIDTH

                    fig['layout'][axis_title]['gridcolor'] = GRID_COLOR
                    fig['layout'][axis_title]['gridwidth'] = 2
                    fig['layout'][axis_title]['tickfont'] = {
                        'color': TICK_COLOR, 'size': 10
                    }

            for key in fig['layout']:
                if '{}axis'.format(x_y) in key and range_are_numbers:
                    fig['layout'][key]['range'] = [min_range, max_range]

    # adjust range for individual subplot
    # add bkgd panel colors
    else:
        # layout styling
        for x_y in ['x', 'y']:
            for axis_title in axis_labels[x_y]:
                fig['layout'][axis_title]['showgrid'] = False
                fig['layout'][axis_title]['showticklabels'] = False
                fig['layout'][axis_title]['zeroline'] = False

        # set ranges
        c_idx = 0
        # extract numbers from axis labels (eg. 'xaxis7' -> '7')
        axis_numbers = []
        for xaxis in axis_labels['x']:
            num_from_axis = re.findall('[^xaxis]+', xaxis)[0]
            axis_numbers.append(int(num_from_axis))
        axis_numbers = sorted(axis_numbers)

        for num in axis_numbers:
            # collect all traces with same axes
            traces_with_same_axes = []
            for trace in fig['data']:
                if trace['xaxis'][1:] == str(num):
                    traces_with_same_axes.append(trace)
            if trace['x'] is not None:
                min_x = min(
                    [min(trace['x']) for trace in traces_with_same_axes]
                )
                max_x = max(
                    [max(trace['x']) for trace in traces_with_same_axes]
                )
            else:
                min_x = [None]
                max_x = [None]
            if trace['y'] is not None:
                min_y = min(
                    [min(trace['y']) for trace in traces_with_same_axes]
                )
                max_y = max(
                    [max(trace['y']) for trace in traces_with_same_axes]
                )
            else:
                min_y = [None]
                max_y = [None]

            range_are_numbers = all(
                isinstance(n, Number) for n in [min_x, max_x, min_y, max_y]
            )

            # TODO: set x, y ranges when string data
            if range_are_numbers:
                print('range are numbers')
                min_y = math.floor(min_y)
                max_y = math.ceil(max_y)

                all_x_data = []
                all_y_data = []
                for l in traces_with_same_axes:
                    for x in l['x']:
                        all_x_data.append(x)
                    for y in l['y']:
                        all_y_data.append(y)

                # handle x margin for cells
                if any(item is None or item != item for item in all_x_data):
                    xrange_bottom = -1
                    xrange_top = 1
                elif min_x == max_x:
                    xrange_bottom = min_x - 0.5
                    xrange_top = max_x + 0.5
                else:
                    std_x = np.std(all_x_data)
                    xrange_bottom = min_x - x_margin_factor * std_x
                    xrange_top = max_x + x_margin_factor * std_x

                # handle y margins for cells
                if any(item is None or item != item for item in all_y_data):
                    yrange_bottom = -1
                    yrange_top = 1
                elif min_y == max_y:
                    yrange_bottom = min_y - 0.5
                    yrange_top = max_y + 0.5
                else:
                    std_y = np.std(all_y_data)
                    yrange_bottom = min_y - y_margin_factor * std_y
                    yrange_top = max_y + y_margin_factor * std_y

            else:
                xrange_bottom = -2
                xrange_top = 2
                yrange_bottom = -2
                yrange_top = 2

            some_xaxis = 'xaxis{}'.format(str(num))
            some_yaxis = 'yaxis{}'.format(str(num))
            fig['layout'][some_xaxis]['range'] = [xrange_bottom, xrange_top]
            fig['layout'][some_yaxis]['range'] = [yrange_bottom, yrange_top]

            # add shapes to bkgd
            if alternate_row_color:
                if c_idx >= len(row_colors):
                    c_idx = 0
                r_color = row_colors[c_idx]

                bkg = rect(
                    'x{}'.format(num),
                    'y{}'.format(num),
                    x0=xrange_bottom, x1=xrange_top,
                    y0=yrange_bottom, y1=yrange_top,
                    color=(
                        r_color
                    )
                )
                fig['layout']['shapes'].append(bkg)
                if int(num) % num_of_cols == 0:
                    c_idx += 1

    return fig
