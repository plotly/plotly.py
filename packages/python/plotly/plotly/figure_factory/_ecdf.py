import pandas as pd
import plotly.express as px


def create_ecdf(
    data_frame=None,
    x=None,
    weight=None,
    color=None,
    line_dash=None,
    line_group=None,
    facet_row=None,
    facet_col=None,
    animation_frame=None,
    animation_group=None,
    hover_name=None,
    hover_data=None,
    normalized=True,
    reverse_ecdf=False,
    mode="lines+markers",
    line_shape="hv",
    **kwargs,
):
    """
    Returns figure for an ECDF plot.

    :param (DataFrame or dict) data_frame: This argument needs to be passed
        for column names (and not keyword names) to be used. Array-like and
        dict are tranformed internally to a pandas DataFrame. Optional: if
        missing, a DataFrame gets constructed under the hood using the other
        arguments.
    :param (str or int or array-like) x: Either a name of a column in
        `data_frame`, or a pandas Series or array_like object. Values from this
        column or array_like are used to position marks along the x axis in
        cartesian coordinates and correspond to the distribution that will be
        plotted.
    :param (str or int or array-like, optional) weight: Either a name of a
        column in `data_frame`, or a pandas Series or array_like object. Values
        from this column or array_like are used to weight `x` values. If
        `normalized` is `False`, the resulting `y` values correspond to the
        cumulative sum of the `weight` values in each group. If `normalized` is
        `True`, the `y` values are scaled to be in range (0, 1]. Optional: if
        missing, all `x` values are given a weight of 1.
    :param (str or int or array-like, optional) color: Either a name of a
        column in data_frame, or a pandas Series or array_like object. Values
        from this column or array_like are used to assign color to marks.
    :param (str or int or array-like, optional) line_dash: Either a name of a
        column in `data_frame`, or a pandas Series or array-like object. Values
        from this column or array-like are used to assign dash-patterns to
        lines.
    :param (str or int or array-like, optional) line_group: Either a name of a
        column in `data_frame`, or a pandas Series or array_like object. Values
        from this column or array-like are used to group rows of data_frame
        into lines.
    :param (str or int or array-like, optional) facet_row: Either a name of a
        column in data_frame, or a pandas Series or array_like object. Values
        from this column or array-like are used to assign marks to facetted
        subplots in the vertical direction.
    :param (str or int or array-like, optional) facet_col: Either a name of a
        column in data_frame, or a pandas Series or array_like object. Values
        from this column or array_like are used to assign marks to facetted
        subplots in the horizontal direction.
    :param (str or int or array-like, optional) animation_frame: Either a name
        of a column in `data_frame`, or a pandas Series or array-like object.
        Values from this column or array-like are used to assign marks to
        animation frames.
    :param (str or int or array-like, optional) animation_group: Either a name
        of a column in `data_frame`, or a pandas Series or array-like object.
        Values from this column or array-like are used to provide
        object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    :param (str or int or array-like, optional) hover_name: Either a name of a
        column in `data_frame`, or a pandas Series or array-like object. Values
        from this column or array-like appear in bold in the hover tooltip.
    :param (list of str or int, or array-like, optional) hover_data: Either a
        from this column or array-like appear in bold in the hover tooltip.
    :param (bool) normalized: If `True`, ECDF ranges from 0 to 1.
        Otherwise, ECDF ranges from 0 to the number of points in the
        distribution, or the sum of the weight column in the distribution if
        `weight` is defined. Defaults to `True`.
    :param (bool) reverse_ecdf: If `True`, ECDF values increase with decreasing
        `x` values rather than the default of increasing with increasing `x`
        values.
    :param (str) mode: Mode option to be used in traces.
        Permitted options are any combination of "lines", "markers", and "text"
        joined with "+" character.
    :param (str) line_shape: the shape of the line to be used if
        `mode` contains "lines". Permitted options are "linear", "spline",
        "hv", "vh", "hvh", and "vhv".

    Example 1: Normal distribution ECDFs grouped and colored by category

    >>> import pandas as pd
    >>> import plotly.figure_factory as ff
    >>> import numpy as np

    >>> df = pd.DataFrame(
    ...     {
    ...         "category": ["a"] * 100 + ["b"] * 30,
    ...         "value": np.concatenate(
    ...             [
    ...                 np.random.normal(0, size=100),
    ...                 np.random.normal(5, size=30),
    ...             ],
    ...         ),
    ...     }
    ... )
    >>> fig = ff.create_ecdf(df, x="value", color="category")
    >>> fig.show()


    Example 2: Animated, weighted ECDF
    
    >>> import plotly.express as px
    >>> import plotly.figure_factory as ff

    >>> df = px.data.gapminder()
    >>> fig = ff.create_ecdf(
    ...     df,
    ...     x="pop",
    ...     color="continent",
    ...     hover_data=["continent", "country"],
    ...     animation_frame="year",
    ...     normalized=False,
    ...     range_x=[-50_000_000, 1_400_000_000],
    ...     range_y=[-100_000_000, 5_000_000_000],
    ...     weight="pop",
    ... )
    >>> fig.show()
    """
    col_dict = dict(
        x=x,
        weight=weight,
        color=color,
        line_group=line_group,
        line_dash=line_dash,
        facet_row=facet_row,
        facet_col=facet_col,
        animation_frame=animation_frame,
        animation_group=animation_group,
        hover_name=hover_name,
        hover_data=hover_data,
    )
    col_dict, data_frame = _prep_col_dict_and_data_frame(
        col_dict, data_frame, normalized
    )

    groupby_col_types = [
        "color",
        "line_group",
        "line_dash",
        "facet_row",
        "facet_col",
        "animation_frame",
        "animation_group",
    ]
    groupby_cols = [
        col_name
        for col_type, col_name in col_dict.items()
        if col_type in groupby_col_types
    ]

    if len(groupby_cols) == 0:
        groupby_cols = ["_dum_"]
        data_frame["_dum_"] = 1

    ascending = not reverse_ecdf
    data_frame = data_frame.sort_values(col_dict["x"], ascending=ascending).copy()

    df_list = []
    for _, group in data_frame.groupby(groupby_cols):
        group = group.copy()
        group[col_dict["y"]] = group[col_dict["weight"]].cumsum()
        if normalized:
            group[col_dict["y"]] /= group[col_dict["weight"]].sum()
        df_list.append(group)
    data_frame = pd.concat(df_list, ignore_index=True)

    fig = px.line(
        data_frame,
        x=col_dict.get("x"),
        y=col_dict.get("y"),
        color=col_dict.get("color"),
        line_group=col_dict.get("line_group"),
        line_dash=col_dict.get("line_dash"),
        facet_row=col_dict.get("facet_row"),
        facet_col=col_dict.get("facet_col"),
        animation_frame=col_dict.get("animation_frame"),
        animation_group=col_dict.get("animation_group"),
        hover_name=col_dict.get("hover_name"),
        hover_data=col_dict.get("hover_data"),
        **kwargs,
    )

    if "animation_frame" in col_dict:
        for frame in fig.frames:
            for trace in frame.data:
                trace.mode = mode
    fig.update_traces(line_shape=line_shape, mode=mode)

    return fig


def _prep_col_dict_and_data_frame(col_dict, data_frame, normalized):
    """Prepare col_dict and data_frame prior to computing ECDF"""
    col_dict = {
        col_type: col_value
        for col_type, col_value in col_dict.items()
        if col_value is not None
    }
    if data_frame is None:
        col_dict, data_frame = _handle_hover_data(col_dict)

    elif isinstance(data_frame, dict):
        data_frame = pd.DataFrame(data_frame)

    if not isinstance(data_frame, pd.DataFrame):
        raise TypeError("data_frame must be of type pd.DataFrame or dict")
    for col_type, col_name in col_dict.items():
        if col_type == "hover_data":
            for name in col_name:
                _error_if_column_not_found(data_frame, col_type, name)
        else:
            _error_if_column_not_found(data_frame, col_type, col_name)

    col_dict["y"] = ""
    if not normalized:
        col_dict["y"] += "Unnormalized "

    if "weight" in col_dict:
        col_dict["y"] += "{}-Weighted ".format(col_dict["weight"])
    else:
        col_dict["weight"] = "_weight_"
        data_frame[col_dict["weight"]] = 1

    col_dict["y"] += "ECDF"

    return col_dict, data_frame


def _error_if_column_not_found(data_frame, col_type, col_name):
    if col_name not in data_frame.columns:
        raise ValueError(
            "{} column '{}' not found in data_frame".format(col_type, col_name)
        )


def _handle_hover_data(col_dict):
    """Convert col_dict with data into a data_frame, handling the complexities
    of hover_data. If `"hover_data"` is part of `col_dict`, add the data as
    new columns in `data_frame`. Return a new `col_dict` that maps column types
    to column names, with `col_dict["hover_data"]` containing a list of
    `hover_data` column names, as well as the `data_frame`"""

    if "hover_data" in col_dict:
        hover_data = col_dict.pop("hover_data")
        new_hover_data = []
        if isinstance(hover_data, dict):
            for col_name, col_data in hover_data.items():
                if col_name in col_dict:
                    raise ValueError(
                        str(col_name)
                        + " from hover_data is already represented."
                        + " Choose a different column name."
                    )
                col_dict[col_name] = col_data
                new_hover_data.append(col_name)
        else:
            for i, d in enumerate(hover_data):
                col_name = "hover_data_" + str(i)
                col_dict[col_name] = d
                new_hover_data.append(col_name)
    else:
        hover_data = None

    data_frame = pd.DataFrame(col_dict)
    col_dict = {col_type: col_type for col_type in col_dict.keys()}

    if hover_data is not None:
        col_dict["hover_data"] = new_hover_data
    return col_dict, data_frame
