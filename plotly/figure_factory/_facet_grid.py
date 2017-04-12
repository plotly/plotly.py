from __future__ import absolute_import

from plotly import exceptions, optional_imports
from plotly.figure_factory import utils

from plotly.graph_objs import graph_objs
from plotly.tools import make_subplots

from numbers import Number

pd = optional_imports.get_module('pandas')

TICK_COLOR = '#969696'
AXIS_TITLE_COLOR = '#787878'
GRID_COLOR = '#ffffff'
LEGEND_COLOR = '#efefef'
PLOT_BGCOLOR = '#d7d7d7'
ANNOT_COLOR = '#c7c7c7'


# TODO: change 'num_of_cols' below to 'num_of_slots' or something
def _annotation_dict(text, col, num_of_cols, row_col='col'):
    if row_col == 'col':
        l = 0.05
        w = (1 - (num_of_cols - 1) * l) / num_of_cols
        x = ((2 * col - 1) * w + (2 * col - 2) * l) / 2.
        y = 1.07
        textangle = 0
    elif row_col == 'row':
        l = 0.03
        w = (1 - (num_of_cols - 1) * l) / num_of_cols
        x = 1.07
        y = ((2 * col - 1) * w + (2 * col - 2) * l) / 2.
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
            size=15,
            color=AXIS_TITLE_COLOR
        ),
        bordercolor=ANNOT_COLOR,
        bgcolor=ANNOT_COLOR
    )
    return annotation_dict


def _facet_grid_color_categorical(data, x, y, facet_row=None, facet_col=None,
                color=None, title='facet_grid', height=600, width=600):
    pass


def _facet_grid_color_numerical(data, x, y, facet_row=None, facet_col=None,
                      color=None, title='facet_grid', height=600, width=600):
    pass


def create_facet_grid(data, x, y, facet_row=None, facet_col=None, color=None,
                      colorscale='Reds', color_dict=None, title='facet_grid',
                      height=600, width=600):
    """
    Returns data for a facet grid.

    :param (pd.DataFrame) data: the DataFrame of columns for the facet grid.
    :param (str) x: the key of the DataFrame to be used as the x axis data.
    :param (str) y: the key of the DataFrame to be used as the y axis data.
    :param (str) facet_row: the key of the row filter column for the facet
        grid. The column must be categorical.
    :param (str) facet_col: the key of the column filter column for the facet
        grid. The column must be categorical.
    :param (str) color: the key that will function as the heatmap variable.
    :param (str|list) colorscale: either the name of a plotly colorscale
        name or a custom colorscale list.
    :param (dict) color_dict: a dictionary that maps the values of the color
        variable column values to color values. Colors can be tuples, rgb
        tuples or hex strings. Run 'help(plotly.colors)' for information.
    :param (str) title: the title of the facet grid figure.
    :param (int) height: the height of the facet grid figure.
    :param (int) width: the width of the facet grid figure.

    Example 1: Facet Grid with no filtering
    ```

    ```

    Example 2: Facet Grid with row filtering
    ```

    ```

    Example 3: Facet Grid with no column filtering
    ```

    ```

    Example 4: Facet Grid with row and column filtering
    ```

    ```

    Example 5: Facet Grid with heatmap variable
    ```

    ```
    """
    # variables
    num_of_rows = 1
    num_of_cols = 1
    annotations = []

    # make sure all columns are of homogenous datatype
    utils.validate_dataframe(data)

    for key in [x, y, facet_row, facet_col, color]:
        if key is not None:
            try:
                data[key]
            except ValueError:
                raise exceptions.PlotlyError(
                    "x, y, facet_row, facet_col and color must be keys in "
                    "your pandas DataFrame, where facet_row, facet_col and "
                    "color should be categorical variables."
                )

    if color:
        show_legend = True

        if isinstance(data[color][0], Number):
            # numerical color variable
            if isinstance(colorscale, str):
                if colorscale in utils.PLOTLY_SCALES.keys():
                    colorscale_dict = utils.PLOTLY_SCALES[colorscale]
                else:
                    raise exceptions.PlotlyError(
                        "If 'colorscale' is a string, it must be the name "
                        "of a Plotly Colorscale. The available colorscale "
                        "names are {}".format(utils.PLOTLY_SCALES.keys())
                    )
            elif isinstance(colorscale, list):
                utils.va


            else:
                raise exceptions.PlotlyError(
                    "Your 'colorscale' variable must be either a string "
                    "or a list of lists. For more information on what a "
                    "colorscale is, run "
                    "'help(plotly.colors.validate_scale_values)'."
                )


        elif isinstance(data[color][0], str):
            # categorical color variable
            if isinstance(color_dict, dict):
                utils.validate_colors_dict(color_dict)

                for val in data[color].unique():
                    if val not in color_dict.keys():
                        raise exceptions.PlotlyError(
                            "If using a color_dict, make sure all the values of "
                            "the color column are in the keys of your color_dict."
                        )
            else:
                # you didn't specify a color dictionary
                default_colors = utils.DEFAULT_PLOTLY_COLORS
                color_dict = {}
                j = 0
                for val in data[color].unique():
                    if j >= len(default_colors):
                        j = 0
                    color_dict[val] = default_colors[j]
                    j += 1



    show_legend = False

    if facet_row:
        num_of_rows = len(data[facet_row].unique())

    if facet_col:
        num_of_cols = len(data[facet_col].unique())

    fig = make_subplots(rows=num_of_rows, cols=num_of_cols,
                        shared_xaxes=True, shared_yaxes=True,
                        vertical_spacing=0.03, print_grid=False)

    fig['layout'].update(height=height, width=width, title=title)
    fig['layout'].update(plot_bgcolor=PLOT_BGCOLOR)

    if not facet_row and not facet_col:
        trace = graph_objs.Scatter(
            x=data[x].tolist(),
            y=data[y].tolist(),
            mode='markers',
            marker=dict(
                color='#000000'
            )
        )
        fig.append_trace(trace, 1, 1)

    elif facet_row and not facet_col:
        groups_by_facet_row = list(data.groupby(facet_row))
        for j, group in enumerate(groups_by_facet_row):
            trace = graph_objs.Scatter(
                x=group[1][x].tolist(),
                y=group[1][y].tolist(),
                mode='markers',
                marker=dict(
                    color='#000000'
                )
            )
            fig.append_trace(trace, j + 1, 1)

            annotations.append(
                _annotation_dict(group[0], num_of_rows - j,
                                 num_of_rows, row_col='row')
            )

    elif not facet_row and facet_col:
        groups_by_facet_col = list(data.groupby(facet_col))
        for j, group in enumerate(groups_by_facet_col):
            trace = graph_objs.Scatter(
                x=groups_by_facet_col[j][1][x].tolist(),
                y=groups_by_facet_col[j][1][y].tolist(),
                mode='markers',
                marker=dict(
                    color='#000000'
                )
            )
            fig.append_trace(trace, 1, j + 1)

            annotations.append(
                _annotation_dict(group[0], j + 1, num_of_cols, row_col='col')
            )

    elif facet_row and facet_col:
        groups_by_facets = list(data.groupby([facet_row, facet_col]))
        tuple_to_facet_group = {item[0]: item[1] for
                                item in groups_by_facets}

        row_values = data[facet_row].unique()
        col_values = data[facet_col].unique()
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
                    )
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
        fig['layout']['{}{}'.format(
            axis, index_for_title
        )]['title'] = axis_titles[axis]

    # legend
    fig['layout']['showlegend'] = show_legend
    fig['layout']['legend']['bgcolor'] = LEGEND_COLOR
    fig['layout']['legend']['y'] = 0.5
    fig['layout']['legend']['x'] = 1.15

    # annotations
    fig['layout']['annotations'] = annotations

    return fig
