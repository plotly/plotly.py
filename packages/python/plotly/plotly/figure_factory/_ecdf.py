import pandas as pd
import plotly.express as px


def create_ecdf(
    df: pd.DataFrame,
    x: str,
    weight: str = None,
    color: str = None,
    facet_col: str = None,
    facet_row: str = None,
    animation_frame: str = None,
    normalized: bool = True,
    mode: str = "lines+markers",
    line_shape: str = "hv",
    **kwargs,
):
    """
    Returns figure for an ECDF plot.

    :param (pd.DataFrame) df: the input data to plot.
    :param (str) x: the name of the column containing the values whose
        distribution you're trying to plot.
    :param (str, optional) weight: the name of the column with weights to be
        applied to the values
    :param (str, optional) color: the name of the column to be used to split
        values into color groups
    :param (str, optional) facet_col: the name of the column to be used to
        split values into facet column groups
    :param (str, optional) facet_row: the name of the column to be used to
        split values into facet row groups
    :param (str, optional) animation_frame: the name of the column to be used
        to split values into animation frame groups
    :param (bool, optional) normalized: if `True`, ECDF ranges from 0 to 1.
        Otherwise, ECDF ranges from 0 to the number of points in the
        distribution, or the sum of the weight column in the distribution if
        `weight` is defined.
    :param (str, optional) mode: mode option to be used in traces.
        Permitted options are any combination of "lines", "markers", and "text"
        joined with "+" character
    :param (str, optional) line_shape: the shape of the line to be used if
        `mode` contains "lines". Permitted options are "linear", "spline",
        "hv", "vh", "hvh", and "vhv".

    Example 1: Normal distribution ECDFs grouped and colored by category
    '''
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
    '''

    Example 2: Animated, weighted ECDF
    '''
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
    '''
    """
    df = df.sort_values(x, ascending=True).copy()

    if weight is None:
        weight_col = "_weight_"
        df[weight_col] = 1
    else:
        weight_col = weight

    groupby_cols = []
    if color is not None:
        groupby_cols.append(color)
    if facet_col is not None:
        groupby_cols.append(facet_col)
    if facet_row is not None:
        groupby_cols.append(facet_row)
    if animation_frame is not None:
        groupby_cols.append(animation_frame)

    if normalized:
        y = "Normalized "
    else:
        y = "Absolute "

    if weight is None:
        y += "ECDF"
    else:
        y += f"{weight}-Weighted ECDF"

    if len(groupby_cols) == 0:
        groupby_cols = ["_dum_"]
        df["_dum_"] = 1

    df_list = []
    for _, group in df.groupby(groupby_cols):
        group = group.copy()
        group[y] = group[weight_col].cumsum()
        if normalized:
            group[y] /= group[weight_col].sum()
        df_list.append(group)
    df = pd.concat(df_list, ignore_index=True)

    fig = px.line(
        df,
        x=x,
        y=y,
        color=color,
        facet_col=facet_col,
        facet_row=facet_row,
        animation_frame=animation_frame,
        **kwargs,
    )

    if animation_frame is not None:
        for f in fig.frames:
            for d in f.data:
                d.mode = mode
    fig.update_traces(line_shape=line_shape, mode=mode)

    return fig
