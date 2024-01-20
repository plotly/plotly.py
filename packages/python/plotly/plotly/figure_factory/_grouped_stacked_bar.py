import colorsys
from copy import deepcopy
from typing import Union

import plotly.colors as pyc
import plotly.io as pio
import plotly.graph_objects as go
from plotly.express._core import build_dataframe
from plotly.express._doc import make_docstring
from plotly.express._chart_types import bar


def get_colors(base_color: Union[str, tuple], n_colors: int):
    """Get a palette of colors derived from base color.

    This function leverages the HLS color space.
    """
    hls_tuple = colorsys.rgb_to_hls(
        *pyc.convert_colors_to_same_type(base_color, "tuple")[0][0]
    )
    if n_colors == 1:
        return [base_color]

    if n_colors == 2:
        light = colorsys.hls_to_rgb(
            hls_tuple[0], min(1, max(0.75, hls_tuple[1] + 0.2)), hls_tuple[2]
        )
        return pyc.sample_colorscale([light, base_color], n_colors)

    light = colorsys.hls_to_rgb(
        hls_tuple[0], min(1, max(0.8, hls_tuple[1] + 0.2)), hls_tuple[2]
    )
    dark = colorsys.hls_to_rgb(
        hls_tuple[0], max(0, min(0.3, hls_tuple[1] - 0.2)), hls_tuple[2]
    )
    return pyc.sample_colorscale([light, base_color, dark], n_colors)


def create_grouped_stacked_bar(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    stack_group=None,
    stack_group_gap=None,
    bar_gap=None,
    color_discrete_sequence=None,
    labels=None,
    category_orders=None,
    hover_name=None,
    hover_data=None,
    hover_unified=False,
    custom_data=None,
    text=None,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    orientation=None,
    opacity=None,
    range_x=None,
    range_y=None,
    title=None,
    template=None,
    width=None,
    height=None,
):
    """
    Returns a bar chart with grouped and stacked bars.
    """

    # Leverage the `build_dataframe` function twice to create the dataframe
    # with color and stack_group columns
    args = deepcopy(locals())
    if data_frame is not None:
        df_copy = deepcopy(data_frame)
    if color is not None:
        color_copy = deepcopy(color)
    args = build_dataframe(args=args, constructor=go.Bar)
    df_color = args["data_frame"].copy()
    args["color"] = stack_group
    args["data_frame"] = df_copy
    args = build_dataframe(args=args, constructor=go.Bar)
    color_col = color if isinstance(color, str) else "color"
    group_col = stack_group if isinstance(stack_group, str) else "stack_group"
    x_col = x if isinstance(x, str) else "x"
    if not isinstance(stack_group, str):
        args["data_frame"] = args["data_frame"].rename(columns={"color": "stack_group"})
    args["data_frame"] = args["data_frame"].join(df_color[[color_col]])
    args["color"] = color_copy

    data_frame = args.pop("data_frame").sort_values([color_col, group_col, x_col])
    hover_data = args.pop("hover_data") or [group_col]

    # Remove arguments that can't be passed to px.bar, they are used separately
    args.pop("stack_group")
    args.pop("hover_unified")

    # Create the groups metadata, including their order and bar width
    groups = list(data_frame[group_col].unique())
    if category_orders is not None and group_col in category_orders:
        groups = [g for g in category_orders[group_col] if g in groups] + [
            g for g in groups if g not in category_orders[group_col]
        ]
    n_groups = len(groups)
    stack_group_gap = args.pop("stack_group_gap") or 1 / n_groups
    bar_gap = args.pop("bar_gap") or 0
    group_width = (1 - stack_group_gap - (n_groups - 1) * bar_gap) / n_groups
    n_colors = data_frame[color_col].nunique()

    # Retrieve the template information to create groups with the right colors
    if template is None:
        if pio.templates.default is not None:
            template = pio.templates.default
        else:
            template = "plotly"
    try:
        # retrieve the actual template if we were given a name
        template = pio.templates[template]
    except Exception:
        # otherwise try to build a real template
        template = go.layout.Template(template)

    # `color_discrete_sequence` can be used to override the template colors
    color_discrete_sequence = args.pop("color_discrete_sequence")
    if color_discrete_sequence is None:
        color_discrete_sequence = template.layout.colorway
    elif isinstance(color_discrete_sequence, str):
        color_discrete_sequence = pyc.colorscale_to_colors(
            pyc.get_colorscale(color_discrete_sequence)
        )

    # Manage the orientation
    value_axis = "y"
    base_axis = "x"
    if orientation == "h":
        value_axis = "x"
        base_axis = "y"

    fig = None
    # Create the figures for each group then combine into one,
    # with overlapping y-axis (or x-axis if horizontal)
    for i, group in enumerate(groups):
        group_df = data_frame.query(f"{group_col} == @group")
        n_colors = group_df[color_col].nunique()
        colors = get_colors(
            color_discrete_sequence[i % len(color_discrete_sequence)],
            n_colors,
        )
        group_fig = bar(
            group_df,
            color_discrete_sequence=colors,
            hover_data=hover_data,
            **args,
        ).update_traces(
            offsetgroup=str(i),
            offset=(i - n_groups / 2) * (group_width + bar_gap) + 1 / 2 * bar_gap,
            width=group_width,
            legendgroup=group,
            legendgrouptitle_text=group,
            **{f"{value_axis}axis": f"{value_axis}{i + 1}"},
        )
        if fig is None:
            fig = group_fig
        else:
            fig.add_traces(group_fig.data)
            # Ensure the y-axes (or x-axes) overlap and match
            fig.update_layout(
                **{
                    f"{value_axis}axis{i + 1}": {
                        "visible": False,
                        "matches": value_axis,
                        "overlaying": value_axis,
                        "anchor": base_axis,
                    }
                }
            )

    # Set the base axis type to category to work well with groups
    fig.update_layout(**{f"{base_axis}axis_type": "category"})

    # Optionally unify the hover, with a modification of the hovertemplate
    # to have a nice display
    if hover_unified:
        fig.update_layout(hovermode="x unified").update_traces(hovertemplate="%{y}")

    return fig


create_grouped_stacked_bar.__doc__ = make_docstring(
    create_grouped_stacked_bar,
    override_dict={
        "stack_group": "Values from this column or array_like are used to group the bar stacks.",
        "stack_group_gap": "Value between 0 and 1. Sets the gap between the stack groups.",
        "bar_gap": "Value between 0 and 1. Sets the gap between the bars within each group.",
        "hover_unified": "Whether to show the hover in a unified format.",
    },
)
