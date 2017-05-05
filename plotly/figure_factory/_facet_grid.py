from __future__ import absolute_import

from plotly import colors, exceptions, optional_imports
from plotly.figure_factory import utils
from plotly.graph_objs import graph_objs
from plotly.tools import make_subplots

from numbers import Number

pd = optional_imports.get_module('pandas')

TICK_COLOR = '#969696'
AXIS_TITLE_COLOR = '#0f0f0f'
GRID_COLOR = '#ffffff'
LEGEND_COLOR = '#efefef'
PLOT_BGCOLOR = '#f5f5f5'
ANNOT_RECT_COLOR = '#d0d0d0'
HORIZONTAL_SPACING = 0.015
VERTICAL_SPACING = 0.015
LEGEND_BORDER_WIDTH = 1


def _annotation_dict(text, lane, num_of_lanes, row_col='col'):
    if row_col == 'col':
        l = 0.05
        w = (1 - (num_of_lanes - 1) * l) / num_of_lanes
        x = ((2 * lane - 1) * w + (2 * lane - 2) * l) / 2.
        y = 1.03
        textangle = 0
    elif row_col == 'row':
        l = 0.03
        w = (1 - (num_of_lanes - 1) * l) / num_of_lanes
        x = 1.03
        y = ((2 * lane - 1) * w + (2 * lane - 2) * l) / 2.
        textangle = 90

    annotation_dict = dict(
        textangle=textangle,
        xanchor='center',
        yanchor='middle',
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


def _add_shapes_to_fig(fig):
    fig['layout']['shapes'] = []
    for key in fig['layout'].keys():
        if 'xaxis' in key or 'yaxis' in key:
            if fig['layout'][key]['domain'] != [0.0, 1.0]:
                if 'xaxis' in key:
                    fig['layout']['shapes'].append(
                        {'fillcolor': ANNOT_RECT_COLOR,
                       'layer': 'below',
                       'line': {'color': ANNOT_RECT_COLOR, 'width': 1},
                       'type': 'rect',
                       'x0': fig['layout'][key]['domain'][0],
                       'x1': fig['layout'][key]['domain'][1],
                       'xref': 'paper',
                       'y0': 1.005,
                       'y1': 1.05,
                       'yref': 'paper'}
                    )
                elif 'yaxis' in key:
                    fig['layout']['shapes'].append(
                        {'fillcolor': ANNOT_RECT_COLOR,
                         'layer': 'below',
                         'line': {'color': ANNOT_RECT_COLOR, 'width': 1},
                         'type': 'rect',
                         'x0': 1.005,
                         'x1': 1.05,
                         'xref': 'paper',
                         'y0': fig['layout'][key]['domain'][0],
                         'y1': fig['layout'][key]['domain'][1],
                         'yref': 'paper'}
                    )


def _facet_grid_color_categorical(df, x, y, facet_row, facet_col, color_name,
                                  color, title, height, width, num_of_rows,
                                  num_of_cols, **kwargs):
    fig = make_subplots(rows=num_of_rows, cols=num_of_cols,
                        shared_xaxes=True, shared_yaxes=True,
                        horizontal_spacing=HORIZONTAL_SPACING,
                        vertical_spacing=VERTICAL_SPACING, print_grid=False)

    annotations = []
    if not facet_row and not facet_col:
        color_groups = list(df.groupby(color))
        for group in color_groups:
            trace = graph_objs.Scatter(
                x=group[1][x].tolist(),
                y=group[1][y].tolist(),
                mode='markers',
                name=group[0],
                marker=dict(
                    color=color_dict[group[0]]
                ),
                **kwargs
            )
            fig.append_trace(trace, 1, 1)

    elif facet_row and not facet_col:
        groups_by_facet_row = list(df.groupby(facet_row))
        for j, group in enumerate(groups_by_facet_row):
            for color_val in df[color].unique():
                data_by_color = group[1][group[1][color] == color_val]
                trace = graph_objs.Scatter(
                    x=data_by_color[x].tolist(),
                    y=data_by_color[y].tolist(),
                    mode='markers',
                    name=color_val,
                    marker=dict(
                        color=color_dict[color_val]
                    ),
                    **kwargs
                )
                fig.append_trace(trace, j + 1, 1)

            annotations.append(
                _annotation_dict(group[0], num_of_rows - j, num_of_rows,
                                 row_col='row')
            )

    elif not facet_row and facet_col:
        groups_by_facet_col = list(df.groupby(facet_col))
        for j, group in enumerate(groups_by_facet_col):
            for color_val in df[color].unique():
                data_by_color = group[1][group[1][color] == color_val]
                trace = graph_objs.Scatter(
                    x=data_by_color[x].tolist(),
                    y=data_by_color[y].tolist(),
                    mode='markers',
                    name=color_val,
                    marker=dict(
                        color=color_dict[color_val]
                    ),
                    **kwargs
                )
                fig.append_trace(trace, 1, j + 1)

            annotations.append(
                _annotation_dict(group[0], j + 1, num_of_cols, row_col='col')
            )

    elif facet_row and facet_col:
        groups_by_facets = list(df.groupby([facet_row, facet_col]))
        tuple_to_facet_group = {item[0]: item[1] for
                                item in groups_by_facets}

        row_values = df[facet_row].unique()
        col_values = df[facet_col].unique()
        color_vals = df[color].unique()
        for row_count, x_val in enumerate(row_values):
            for col_count, y_val in enumerate(col_values):
                try:
                    group = tuple_to_facet_group[(x_val, y_val)]
                except KeyError:
                    group = pd.DataFrame([[None, None, None]],
                                         columns=[x, y, color])

                for color_val in color_vals:
                    if group.values.tolist() != [[None, None, None]]:
                        group_filtered = group[group[color] == color_val]

                        trace = graph_objs.Scatter(
                            x=group_filtered[x].tolist(),
                            y=group_filtered[y].tolist(),
                            mode='markers',
                            name=color_val,
                            marker=dict(
                                color=color_dict[color_val]
                            ),
                            **kwargs
                        )
                    else:
                        trace = graph_objs.Scatter(
                            x=group[x].tolist(),
                            y=group[y].tolist(),
                            mode='markers',
                            name=color_val,
                            marker=dict(
                                color=color_dict[color_val]
                            ),
                            showlegend=False,
                            **kwargs
                        )
                    fig.append_trace(trace, row_count + 1, col_count + 1)
                    if row_count == 0:
                        annotations.append(
                            _annotation_dict(col_values[col_count],
                                             col_count + 1,
                                             num_of_cols,
                                             row_col='col')
                            )
                annotations.append(
                    _annotation_dict(row_values[row_count],
                                     num_of_rows - row_count,
                                     num_of_rows,
                                     row_col='row')
                    )

    # add annotations
    fig['layout']['annotations'] = annotations

    return fig


def _facet_grid_color_numerical(df, x, y, facet_row, facet_col, color,
                                colorscale, color_dict, title, height, width,
                                num_of_rows, num_of_cols, **kwargs):
    fig = make_subplots(rows=num_of_rows, cols=num_of_cols,
                        shared_xaxes=True, shared_yaxes=True,
                        horizontal_spacing=HORIZONTAL_SPACING,
                        vertical_spacing=VERTICAL_SPACING, print_grid=False)

    annotations = []
    if not facet_row and not facet_col:
        trace = graph_objs.Scatter(
            x=df[x].tolist(),
            y=df[y].tolist(),
            mode='markers',
            marker=dict(
                color=df[color],
                colorscale=colorscale,
                showscale=True
            ),
            **kwargs
        )
        fig.append_trace(trace, 1, 1)

    elif facet_row and not facet_col:
        groups_by_facet_row = list(df.groupby(facet_row))
        for j, group in enumerate(groups_by_facet_row):
            trace = graph_objs.Scatter(
                x=group[1][x].tolist(),
                y=group[1][y].tolist(),
                mode='markers',
                marker=dict(
                    color=df[color].tolist(),
                    colorscale=colorscale,
                    showscale=True,
                    colorbar=dict(x=1.15)
                ),
                **kwargs
            )
            fig.append_trace(trace, j + 1, 1)

            annotations.append(
                _annotation_dict(group[0], num_of_rows - j,
                                 num_of_rows, row_col='row')
            )

    elif not facet_row and facet_col:
        groups_by_facet_col = list(df.groupby(facet_col))
        for j, group in enumerate(groups_by_facet_col):
            trace = graph_objs.Scatter(
                x=group[1][x].tolist(),
                y=group[1][y].tolist(),
                mode='markers',
                marker=dict(
                    color=df[color].tolist(),
                    colorscale=colorscale,
                    showscale=True,
                    colorbar=dict(x=1.15)
                ),
                **kwargs
            )
            fig.append_trace(trace, 1, j + 1)

            annotations.append(
                _annotation_dict(group[0], j + 1, num_of_cols, row_col='col')
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
                                         columns=[x, y, color])

                if group.values.tolist() != [[None, None, None]]:
                    trace = graph_objs.Scatter(
                        x=group[x].tolist(),
                        y=group[y].tolist(),
                        mode='markers',
                        marker=dict(
                            color=df[color].tolist(),
                            colorscale=colorscale,
                            showscale=(row_count == 0),
                            colorbar=dict(x=1.15)
                        ),
                        **kwargs
                    )
                else:
                    trace = graph_objs.Scatter(
                        x=group[x].tolist(),
                        y=group[y].tolist(),
                        mode='markers',
                        showlegend=False,
                        **kwargs
                    )
                fig.append_trace(trace, row_count + 1, col_count + 1)
                if row_count == 0:
                    annotations.append(
                        _annotation_dict(col_values[col_count],
                                         col_count + 1,
                                         num_of_cols,
                                         row_col='col')
                        )
            annotations.append(
                _annotation_dict(row_values[row_count],
                                 num_of_rows - row_count,
                                 num_of_rows,
                                 row_col='row')
                )

    # add annotations
    fig['layout']['annotations'] = annotations

    return fig


def _facet_grid(df, x, y, facet_row, facet_col, title, height, width,
                num_of_rows, num_of_cols, **kwargs):
    fig = make_subplots(rows=num_of_rows, cols=num_of_cols,
                        shared_xaxes=True, shared_yaxes=True,
                        horizontal_spacing=HORIZONTAL_SPACING,
                        vertical_spacing=VERTICAL_SPACING, print_grid=False)
    annotations = []
    if not facet_row and not facet_col:
        trace = graph_objs.Scatter(
            x=df[x].tolist(),
            y=df[y].tolist(),
            mode='markers',
            marker=dict(
                color='#000000'
            ),
            **kwargs
        )
        fig.append_trace(trace, 1, 1)

    elif facet_row and not facet_col:
        groups_by_facet_row = list(df.groupby(facet_row))
        for j, group in enumerate(groups_by_facet_row):
            trace = graph_objs.Scatter(
                x=group[1][x].tolist(),
                y=group[1][y].tolist(),
                mode='markers',
                marker=dict(
                    color='#000000'
                ),
                **kwargs
            )
            fig.append_trace(trace, j + 1, 1)

            annotations.append(
                _annotation_dict(group[0], num_of_rows - j,
                                 num_of_rows, row_col='row')
            )

    elif not facet_row and facet_col:
        groups_by_facet_col = list(df.groupby(facet_col))
        for j, group in enumerate(groups_by_facet_col):
            trace = graph_objs.Scatter(
                x=group[1][x].tolist(),
                y=group[1][y].tolist(),
                mode='markers',
                marker=dict(
                    color='#000000'
                ),
                **kwargs
            )
            fig.append_trace(trace, 1, j + 1)

            annotations.append(
                _annotation_dict(group[0], j + 1, num_of_cols, row_col='col')
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
                    group = pd.DataFrame([[None, None]], columns=[x, y])
                trace = graph_objs.Scatter(
                    x=group[x].tolist(),
                    y=group[y].tolist(),
                    mode='markers',
                    marker=dict(
                        color='#000000'
                    ),
                    **kwargs
                )
                fig.append_trace(trace, row_count + 1, col_count + 1)
                if row_count == 0:
                    annotations.append(
                        _annotation_dict(col_values[col_count],
                                         col_count + 1,
                                         num_of_cols,
                                         row_col='col')
                        )
            annotations.append(
                _annotation_dict(row_values[row_count],
                                 num_of_rows - row_count,
                                 num_of_rows,
                                 row_col='row')
                )

    # add annotations
    fig['layout']['annotations'] = annotations

    return fig


def create_facet_grid(df, x, y, facet_row=None, facet_col=None,
                      color_name=None, color=None, title='facet grid',
                      height=800, width=800, **kwargs):
    """
    Returns figure for facet grid.

    :param (pd.DataFrame) df: the dataFrame of columns for the facet grid.
    :param (str) x: the key of the dataFrame to be used as the x axis df.
    :param (str) y: the key of the dataFrame to be used as the y axis df.
    :param (str) facet_row: the key of the row filter column for the facet
        grid. The column must be categorical.
    :param (str) facet_col: the key of the column filter column for the facet
        grid. The column must be categorical.
    :param (str) color_name: the name of your dataframe column that will
        function as the heatmap variable.
    :param (str|list|dict) color: the param that determines how the color_name
        column (the heatmap variable) colors the data. If the dataframe
        contains numeric data, then a dictionary of colors will group the data
        categorically while a Plotly Colorscale name or a custom colorscale
        will treat it numerically. To learn more about colors and types of
        heatmaps, run `help(plotly.colors)`
    :param (str) title: the title of the facet grid figure.
    :param (int) height: the height of the facet grid figure.
    :param (int) width: the width of the facet grid figure.

    Example 1: Facet Grid with no filtering
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd
    import random

    tot_length = 40
    data_list = []
    for _ in range(tot_length):
        data_list.append([10*random.random() for _ in range(2)])
    df = pd.DataFrame(data_list, columns=['column a', 'column b'])

    my_grid = ff.create_facet_grid(
        df,
        x='column a',
        y='column b',
    )

    py.iplot(my_grid, filename='facet_grid_no_filtering')
    ```

    Example 2: Facet Grid with row filtering
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd
    import random

    tot_length = 40
    data_list = []
    for _ in range(tot_length):
        data_list.append([10*random.random() for _ in range(2)])
    df = pd.DataFrame(data_list, columns=['column a', 'column b'])

    row_list = []
    for _ in range(tot_length):
        row_list.append(random.choice(['apple', 'orange']))
    df['fruit'] = row_list

    my_grid = ff.create_facet_grid(
        df,
        x='column a',
        y='column b',
        facet_row='fruit'
    )

    py.iplot(my_grid, filename='facet_grid_row_facet')
    ```

    Example 3: Facet Grid with column filtering
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd
    import random

    tot_length = 40
    data_list = []
    for _ in range(tot_length):
        data_list.append([10*random.random() for _ in range(2)])
    df = pd.DataFrame(data_list, columns=['column a', 'column b'])

    row_list = []
    for _ in range(tot_length):
        row_list.append(random.choice(['apple', 'orange']))
    df['fruit'] = row_list

    my_grid = ff.create_facet_grid(
        df,
        x='column a',
        y='column b',
        facet_col='fruit'
    )

    py.iplot(my_grid, filename='facet_grid_col_facet')
    ```

    Example 4: Facet Grid with row and column filtering
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd
    import random

    tot_length = 40
    data_list = []
    for _ in range(tot_length):
        data_list.append([10*random.random() for _ in range(2)])
    df = pd.DataFrame(data_list, columns=['column a', 'column b'])

    row_list = []
    col_list = []
    for _ in range(tot_length):
        row_list.append(random.choice(['apple', 'orange']))
        col_list.append(random.choice(['dog', 'cat', 'bunny']))
    df['fruit'] = row_list
    df['animal'] = col_list

    my_grid = ff.create_facet_grid(
        df,
        x='column a',
        y='column b',
        facet_row='fruit',
        facet_col='animal'
    )

    py.iplot(my_grid, filename='facet_grid_row_and_col_facet')
    ```

    Example 5: Facet Grid with categorical color variable
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd
    import random

    tot_length = 40
    data_list = []
    for _ in range(tot_length):
        data_list.append([10*random.random() for _ in range(2)])
    df = pd.DataFrame(data_list, columns=['column a', 'column b'])

    row_list = []
    col_list = []
    for _ in range(tot_length):
        row_list.append(random.choice(['apple', 'orange']))
        col_list.append(random.choice(['dog', 'cat', 'bunny']))
    df['fruit'] = row_list
    df['animal'] = col_list

    color_dict = {'dog': 'rgb(255,0,0)',
                  'cat':'rgb(44,210,40)',
                  'bunny':'rgb(0,0,255)'}
    my_grid = ff.create_facet_grid(
        df,
        x='column a',
        y='column b',
        facet_row='fruit',
        facet_col='animal',
        color='animal',
        color_dict=color_dict
    )

    py.iplot(my_grid, filename='facet_grid_cat_color')
    ```

    Example 6: Facet Grid with numerical color variable
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import pandas as pd
    import random

    tot_length = 40
    data_list = []
    for _ in range(tot_length):
        data_list.append([10*random.random() for _ in range(3)])
    df = pd.DataFrame(data_list, columns=['column a',
                                            'column b',
                                            'column c'])

    row_list = []
    col_list = []
    for _ in range(tot_length):
        row_list.append(random.choice(['apple', 'orange']))
        col_list.append(random.choice(['dog', 'cat', 'bunny']))
    df['fruit'] = row_list
    df['animal'] = col_list

    color_dict = {'dog': 'rgb(255,0,0)',
                  'cat':'rgb(44,210,40)',
                  'bunny':'rgb(0,0,255)'}
    my_grid = ff.create_facet_grid(
        df,
        x='column a',
        y='column b',
        facet_row='fruit',
        facet_col='animal',
        color='column c',
        colorscale='Viridis'
    )

    py.iplot(my_grid, filename='facet_grid_numerical_color')
    ```
    """
    if not pd:
        raise exceptions.ImportError(
            "'pandas' must be imported for this figure_factory."
        )

    if not isinstance(df, pd.DataFrame):
        raise exceptions.PlotlyError(
            "df must be a dataframe."
        )

    # make sure all columns are of homogenous datatype
    utils.validate_dataframe(df)

    for key in [x, y, facet_row, facet_col, color]:
        if key is not None:
            try:
                df[key]
            except KeyError:
                raise exceptions.PlotlyError(
                    "x, y, facet_row, facet_col and color must be keys in "
                    "your pandas DataFrame, where facet_row, facet_col and "
                    "color should be categorical variables."
                )

    # make sure dataframe index starts at 0
    df.index = range(len(df))

    num_of_rows = 1
    num_of_cols = 1

    if facet_row:
        num_of_rows = len(df[facet_row].unique())
    if facet_col:
        num_of_cols = len(df[facet_col].unique())

    if color_name:
        if isinstance(df[color_name][0], str):
            show_legend = False
            if isinstance(color, dict):
                utils.validate_colors_dict(color, 'rgb')

                for val in df[color_name].unique():
                    if val not in color_dict.keys():
                        raise exceptions.PlotlyError(
                            "If using 'color' as a dictionary, make sure all "
                            "the values of the color column are in the keys "
                            "of your dictionary."
                        )
            else:
                # use default plotly colors for dictionary
                default_colors = utils.DEFAULT_PLOTLY_COLORS
                color = {}
                j = 0
                for val in df[color_name].unique():
                    if j >= len(default_colors):
                        j = 0
                    color[val] = default_colors[j]
                    j += 1

            fig = _facet_grid_color_categorical(df, x, y, facet_row,
                                                facet_col, color_name, color,
                                                title, height, width,
                                                num_of_rows, num_of_cols,
                                                **kwargs)


        elif isinstance(df[color_name][0], Number):
            if isinstance(color, dict):
                show_legend = False
                utils.validate_colors_dict(color, 'rgb')

                for val in df[color_name].unique():
                    if val not in color_dict.keys():
                        raise exceptions.PlotlyError(
                            "If using 'color' as a dictionary, make sure all "
                            "the values of the color column are in the keys "
                            "of your dictionary."
                        )

            elif isinstance(color, list):
                colorscale_list = color
                utils.validate_colorscale(colorscale_list)

            elif isinstance(color, str):
                if color in colors.PLOTLY_SCALES.keys():
                    colorscale_list = colors.PLOTLY_SCALES[color]
                else:
                    raise exceptions.PlotlyError(
                        "If 'color' is a string, it must be the name "
                        "of a Plotly Colorscale. The available colorscale "
                        "names are {}".format(colors.PLOTLY_SCALES.keys())
                    )
            else:
                colorscale_list = colors.PLOTLY_SCALES['Reds']












    if color:
        if isinstance(df[color][0], Number):
            show_legend = False
            # numerical color variable
            if isinstance(colorscale, str):
                if colorscale in colors.PLOTLY_SCALES.keys():
                    colorscale_list = colors.PLOTLY_SCALES[colorscale]
                else:
                    raise exceptions.PlotlyError(
                        "If 'colorscale' is a string, it must be the name "
                        "of a Plotly Colorscale. The available colorscale "
                        "names are {}".format(colors.PLOTLY_SCALES.keys())
                    )
            elif isinstance(colorscale, list):
                colorscale_list = colorscale
                utils.validate_colorscale(colorscale_list)

            else:
                # select default colorscale if not picked
                colorscale_list = colors.PLOTLY_SCALES['Reds']

            fig = _facet_grid_color_numerical(df, x, y, facet_row,
                                              facet_col, color,
                                              colorscale_list,
                                              color_dict, title,
                                              height, width, num_of_rows,
                                              num_of_cols, **kwargs)

        elif isinstance(df[color][0], str):
            show_legend = True
            # categorical color variable
            if isinstance(color_dict, dict):
                utils.validate_colors_dict(color_dict, 'rgb')

                for val in df[color].unique():
                    if val not in color_dict.keys():
                        raise exceptions.PlotlyError(
                            "If using a color_dict, make sure all the values "
                            "of the color column are in the keys of your "
                            "color_dict."
                        )
            else:
                # didn't specify a color dictionary
                default_colors = utils.DEFAULT_PLOTLY_COLORS
                color_dict = {}
                j = 0
                for val in df[color].unique():
                    if j >= len(default_colors):
                        j = 0
                    color_dict[val] = default_colors[j]
                    j += 1

            fig = _facet_grid_color_categorical(df, x, y, facet_row,
                                                facet_col, color, [],
                                                color_dict, title,
                                                height, width, num_of_rows,
                                                num_of_cols, **kwargs)

    else:
        show_legend = False
        fig = _facet_grid(df, x, y, facet_row, facet_col, title, height,
                          width, num_of_rows, num_of_cols, **kwargs)

    fig['layout'].update(height=height, width=width, title=title)
    fig['layout'].update(plot_bgcolor=PLOT_BGCOLOR)

    # color the axes
    all_axis_keys = []
    for key in fig['layout']:
        if 'xaxis' in key or 'yaxis' in key:
            all_axis_keys.append(key)
            fig['layout'][key]['titlefont']['color'] = AXIS_TITLE_COLOR
            fig['layout'][key]['tickfont']['color'] = TICK_COLOR
            fig['layout'][key]['gridcolor'] = GRID_COLOR
            fig['layout'][key]['gridwidth'] = 2
            fig['layout'][key]['zeroline'] = False

    # axis titles
    axis_titles = {'xaxis': x, 'yaxis': y}
    for axis in axis_titles.keys():
        xkeys = [key for key in all_axis_keys if axis in key]
        max_index = max(int(xkey[-1]) for xkey in xkeys)
        index_for_title = max_index // 2 + 1
        axis_key = '{}{}'.format(axis, index_for_title)
        fig['layout'][axis_key]['title'] = axis_titles[axis]


    # legend
    fig['layout']['showlegend'] = show_legend
    fig['layout']['legend']['bgcolor'] = LEGEND_COLOR
    fig['layout']['legend']['borderwidth'] = LEGEND_BORDER_WIDTH
    fig['layout']['legend']['y'] = 0.5
    fig['layout']['legend']['x'] = 1.15

    # add shaded regions behind axis titles
    _add_shapes_to_fig(fig)

    return fig
