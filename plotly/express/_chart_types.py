from warnings import warn

from ._core import make_figure
import plotly.graph_objs as go

_wide_mode_xy_append = [
    "Either `x` or `y` can optionally be a list of column references or array_likes, ",
    "in which case the data will be treated as if it were 'wide' rather than 'long'.",
]
_cartesian_append_dict = dict(x=_wide_mode_xy_append, y=_wide_mode_xy_append)


def scatter(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    symbol=None,
    size=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    orientation=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    symbol_sequence=None,
    symbol_map=None,
    opacity=None,
    size_max=None,
    marginal_x=None,
    marginal_y=None,
    trendline=None,
    trendline_options=None,
    trendline_color_override=None,
    trendline_scope="trace",
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    render_mode="auto",
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a scatter plot, each row of `data_frame` is represented by a symbol
    mark in 2D space.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    size : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign mark sizes.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    error_x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars. If `error_x_minus` is `None`, error bars will
        be symmetrical, otherwise `error_x` is used for the positive direction
        only.
    error_x_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars in the negative direction. Ignored if `error_x`
        is `None`.
    error_y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars. If `error_y_minus` is `None`, error bars will
        be symmetrical, otherwise `error_y` is used for the positive direction
        only.
    error_y_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars in the negative direction. Ignored if `error_y`
        is `None`.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    size_max : int (default `20`)
        Set the maximum mark size when using `size`.
    marginal_x : str
        One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`. If set, a
        horizontal subplot is drawn above the main plot, visualizing the
        x-distribution.
    marginal_y : str
        One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`. If set, a
        vertical subplot is drawn to the right of the main plot, visualizing
        the y-distribution.
    trendline : str
        One of `'ols'`, `'lowess'`, `'rolling'`, `'expanding'` or `'ewm'`. If
        `'ols'`, an Ordinary Least Squares regression line will be drawn for
        each discrete-color/symbol group. If `'lowess`', a Locally Weighted
        Scatterplot Smoothing line will be drawn for each discrete-color/symbol
        group. If `'rolling`', a Rolling (e.g. rolling average, rolling median)
        line will be drawn for each discrete-color/symbol group. If
        `'expanding`', an Expanding (e.g. expanding average, expanding sum)
        line will be drawn for each discrete-color/symbol group. If `'ewm`', an
        Exponentially Weighted Moment (e.g. exponentially-weighted moving
        average) line will be drawn for each discrete-color/symbol group. See
        the docstrings for the functions in
        `plotly.express.trendline_functions` for more details on these
        functions and how to configure them with the `trendline_options`
        argument.
    trendline_options : dict
        Options passed as the first argument to the function from
        `plotly.express.trendline_functions`  named in the `trendline`
        argument.
    trendline_color_override : str
        Valid CSS color. If provided, and if `trendline` is set, all trendlines
        will be drawn in this color rather than in the same color as the traces
        from which they draw their inputs.
    trendline_scope : str (one of `'trace'` or `'overall'`, default `'trace'`)
        If `'trace'`, then one trendline is drawn per trace (i.e. per color,
        symbol, facet, animation frame etc) and if `'overall'` then one
        trendline is computed for the entire dataset, and replicated across all
        facets.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    render_mode : str
        One of `'auto'`, `'svg'` or `'webgl'`, default `'auto'` Controls the
        browser API used to draw marks. `'svg'` is appropriate for figures of
        less than 1000 data points, and will allow for fully-vectorized output.
        `'webgl'` is likely necessary for acceptable performance above 1000
        points but rasterizes part of the output.  `'auto'` uses heuristics to
        choose the mode.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatter)


def density_contour(
    data_frame=None,
    x=None,
    y=None,
    z=None,
    color=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    orientation=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    marginal_x=None,
    marginal_y=None,
    trendline=None,
    trendline_options=None,
    trendline_color_override=None,
    trendline_scope="trace",
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    histfunc=None,
    histnorm=None,
    nbinsx=None,
    nbinsy=None,
    text_auto=False,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a density contour plot, rows of `data_frame` are grouped together
    into contour marks to visualize the 2D distribution of an aggregate
    function `histfunc` (e.g. the count or sum) of the value `z`.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    z : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the z axis in cartesian coordinates. For
        `density_heatmap` and `density_contour` these values are used as the
        inputs to `histfunc`.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    marginal_x : str
        One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`. If set, a
        horizontal subplot is drawn above the main plot, visualizing the
        x-distribution.
    marginal_y : str
        One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`. If set, a
        vertical subplot is drawn to the right of the main plot, visualizing
        the y-distribution.
    trendline : str
        One of `'ols'`, `'lowess'`, `'rolling'`, `'expanding'` or `'ewm'`. If
        `'ols'`, an Ordinary Least Squares regression line will be drawn for
        each discrete-color/symbol group. If `'lowess`', a Locally Weighted
        Scatterplot Smoothing line will be drawn for each discrete-color/symbol
        group. If `'rolling`', a Rolling (e.g. rolling average, rolling median)
        line will be drawn for each discrete-color/symbol group. If
        `'expanding`', an Expanding (e.g. expanding average, expanding sum)
        line will be drawn for each discrete-color/symbol group. If `'ewm`', an
        Exponentially Weighted Moment (e.g. exponentially-weighted moving
        average) line will be drawn for each discrete-color/symbol group. See
        the docstrings for the functions in
        `plotly.express.trendline_functions` for more details on these
        functions and how to configure them with the `trendline_options`
        argument.
    trendline_options : dict
        Options passed as the first argument to the function from
        `plotly.express.trendline_functions`  named in the `trendline`
        argument.
    trendline_color_override : str
        Valid CSS color. If provided, and if `trendline` is set, all trendlines
        will be drawn in this color rather than in the same color as the traces
        from which they draw their inputs.
    trendline_scope : str (one of `'trace'` or `'overall'`, default `'trace'`)
        If `'trace'`, then one trendline is drawn per trace (i.e. per color,
        symbol, facet, animation frame etc) and if `'overall'` then one
        trendline is computed for the entire dataset, and replicated across all
        facets.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    histfunc : str (default `'count'` if no arguments are provided, else `'sum'`)
        One of `'count'`, `'sum'`, `'avg'`, `'min'`, or `'max'`. Function used
        to aggregate values for summarization (note: can be normalized with
        `histnorm`). The arguments to this function are the values of `z`.
    histnorm : str (default `None`)
        One of `'percent'`, `'probability'`, `'density'`, or `'probability
        density'` If `None`, the output of `histfunc` is used as is. If
        `'probability'`, the output of `histfunc` for a given bin is divided by
        the sum of the output of `histfunc` for all bins. If `'percent'`, the
        output of `histfunc` for a given bin is divided by the sum of the
        output of `histfunc` for all bins and multiplied by 100. If
        `'density'`, the output of `histfunc` for a given bin is divided by the
        size of the bin. If `'probability density'`, the output of `histfunc`
        for a given bin is normalized such that it corresponds to the
        probability that a random event whose distribution is described by the
        output of `histfunc` will fall into that bin.
    nbinsx : int
        Positive integer. Sets the number of bins along the x axis.
    nbinsy : int
        Positive integer. Sets the number of bins along the y axis.
    text_auto : bool or string (default `False`)
        If `True` or a string, the x or y or z values will be displayed as
        text, depending on the orientation A string like `'.2f'` will be
        interpreted as a `texttemplate` numeric formatting directive.
    title : str
        The figure title.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    --------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Histogram2dContour,
        trace_patch=dict(
            contours=dict(coloring="none"),
            histfunc=histfunc,
            histnorm=histnorm,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            xbingroup="x",
            ybingroup="y",
        ),
    )


def density_heatmap(
    data_frame=None,
    x=None,
    y=None,
    z=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    orientation=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    marginal_x=None,
    marginal_y=None,
    opacity=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    histfunc=None,
    histnorm=None,
    nbinsx=None,
    nbinsy=None,
    text_auto=False,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a density heatmap, rows of `data_frame` are grouped together into
    colored rectangular tiles to visualize the 2D distribution of an
    aggregate function `histfunc` (e.g. the count or sum) of the value `z`.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    z : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the z axis in cartesian coordinates. For
        `density_heatmap` and `density_contour` these values are used as the
        inputs to `histfunc`.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    marginal_x : str
        One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`. If set, a
        horizontal subplot is drawn above the main plot, visualizing the
        x-distribution.
    marginal_y : str
        One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`. If set, a
        vertical subplot is drawn to the right of the main plot, visualizing
        the y-distribution.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    histfunc : str (default `'count'` if no arguments are provided, else `'sum'`)
        One of `'count'`, `'sum'`, `'avg'`, `'min'`, or `'max'`. Function used
        to aggregate values for summarization (note: can be normalized with
        `histnorm`). The arguments to this function are the values of `z`.
    histnorm: str (default `None`)
        One of `'percent'`, `'probability'`, `'density'`, or `'probability
        density'` If `None`, the output of `histfunc` is used as is. If
        `'probability'`, the output of `histfunc` for a given bin is divided by
        the sum of the output of `histfunc` for all bins. If `'percent'`, the
        output of `histfunc` for a given bin is divided by the sum of the
        output of `histfunc` for all bins and multiplied by 100. If
        `'density'`, the output of `histfunc` for a given bin is divided by the
        size of the bin. If `'probability density'`, the output of `histfunc`
        for a given bin is normalized such that it corresponds to the
        probability that a random event whose distribution is described by the
        output of `histfunc` will fall into that bin.
    nbinsx : int
        Positive integer. Sets the number of bins along the x axis.
    nbinsy : int
        Positive integer. Sets the number of bins along the y axis.
    text_auto : bool or string (default `False`)
        If `True` or a string, the x or y or z values will be displayed as
        text, depending on the orientation A string like `'.2f'` will be
        interpreted as a `texttemplate` numeric formatting directive.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Histogram2d,
        trace_patch=dict(
            histfunc=histfunc,
            histnorm=histnorm,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            xbingroup="x",
            ybingroup="y",
        ),
    )


def line(
    data_frame=None,
    x=None,
    y=None,
    line_group=None,
    color=None,
    line_dash=None,
    symbol=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    orientation=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    line_dash_sequence=None,
    line_dash_map=None,
    symbol_sequence=None,
    symbol_map=None,
    markers=False,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    line_shape=None,
    render_mode="auto",
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a 2D line plot, each row of `data_frame` is represented as a vertex of
    a polyline mark in 2D space.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    line_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        group rows of `data_frame` into lines.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    line_dash : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign dash-patterns to lines.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    error_x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars. If `error_x_minus` is `None`, error bars will
        be symmetrical, otherwise `error_x` is used for the positive direction
        only.
    error_x_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars in the negative direction. Ignored if `error_x`
        is `None`.
    error_y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars. If `error_y_minus` is `None`, error bars will
        be symmetrical, otherwise `error_y` is used for the positive direction
        only.
    error_y_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars in the negative direction. Ignored if `error_y`
        is `None`.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    line_dash_sequence : list of str
        Strings should define valid plotly.js dash-patterns. When `line_dash`
        is set, values in that column are assigned dash-patterns by cycling
        through `line_dash_sequence` in the order described in
        `category_orders`, unless the value of `line_dash` is a key in
        `line_dash_map`.
    line_dash_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js dash-patterns. Used to override
        `line_dash_sequences` to assign a specific dash-patterns to lines
        corresponding with specific values. Keys in `line_dash_map` should be
        values in the column denoted by `line_dash`. Alternatively, if the
        values of `line_dash` are valid line-dash names, the string
        `'identity'` may be passed to cause them to be used directly.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    markers : boolean (default `False`)
        If `True`, markers are shown on lines.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    line_shape : str (default `'linear'`)
        One of `'linear'`, `'spline'`, `'hv'`, `'vh'`, `'hvh'`, or `'vhv'`
    render_mode : str
        One of `'auto'`, `'svg'` or `'webgl'`, default `'auto'` Controls the
        browser API used to draw marks. `'svg'` is appropriate for figures of
        less than 1000 data points, and will allow for fully-vectorized output.
        `'webgl'` is likely necessary for acceptable performance above 1000
        points but rasterizes part of the output.  `'auto'` uses heuristics to
        choose the mode.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatter)


def area(
    data_frame=None,
    x=None,
    y=None,
    line_group=None,
    color=None,
    pattern_shape=None,
    symbol=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    pattern_shape_sequence=None,
    pattern_shape_map=None,
    symbol_sequence=None,
    symbol_map=None,
    markers=False,
    orientation=None,
    groupnorm=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    line_shape=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a stacked area plot, each row of `data_frame` is represented as
    a vertex of a polyline mark in 2D space. The area between
    successive polylines is filled.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    line_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        group rows of `data_frame` into lines.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    pattern_shape : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign pattern shapes to marks.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    pattern_shape_sequence : list of str
        Strings should define valid plotly.js patterns-shapes. When
        `pattern_shape` is set, values in that column are assigned patterns-
        shapes by cycling through `pattern_shape_sequence` in the order
        described in `category_orders`, unless the value of `pattern_shape` is
        a key in `pattern_shape_map`.
    pattern_shape_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js patterns-shapes. Used to override
        `pattern_shape_sequences` to assign a specific patterns-shapes to lines
        corresponding with specific values. Keys in `pattern_shape_map` should
        be values in the column denoted by `pattern_shape`. Alternatively, if
        the values of `pattern_shape` are valid patterns-shapes names, the
        string `'identity'` may be passed to cause them to be used directly.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    markers : boolean (default `False`)
        If `True`, markers are shown on lines.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    groupnorm : str (default `None`)
        One of `'fraction'` or `'percent'`. If `'fraction'`, the value of each
        point is divided by the sum of all values at that location coordinate.
        `'percent'` is the same but multiplied by 100 to show percentages.
        `None` will stack up all values at each location coordinate.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    line_shape : str (default `'linear'`)
        One of `'linear'`, `'spline'`, `'hv'`, `'vh'`, `'hvh'`, or `'vhv'`
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Scatter,
        trace_patch=dict(stackgroup=1, mode="lines", groupnorm=groupnorm),
    )


def bar(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    pattern_shape=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    base=None,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    pattern_shape_sequence=None,
    pattern_shape_map=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    orientation=None,
    barmode="relative",
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    text_auto=False,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a bar plot, each row of `data_frame` is represented as a rectangular
    mark.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    pattern_shape : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign pattern shapes to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    base : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position the base of the bar.
    error_x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars. If `error_x_minus` is `None`, error bars will
        be symmetrical, otherwise `error_x` is used for the positive direction
        only.
    error_x_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars in the negative direction. Ignored if `error_x`
        is `None`.
    error_y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars. If `error_y_minus` is `None`, error bars will
        be symmetrical, otherwise `error_y` is used for the positive direction
        only.
    error_y_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars in the negative direction. Ignored if `error_y`
        is `None`.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    pattern_shape_sequence : list of str
        Strings should define valid plotly.js patterns-shapes. When
        `pattern_shape` is set, values in that column are assigned patterns-
        shapes by cycling through `pattern_shape_sequence` in the order
        described in `category_orders`, unless the value of `pattern_shape` is
        a key in `pattern_shape_map`.
    pattern_shape_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js patterns-shapes. Used to override
        `pattern_shape_sequences` to assign a specific patterns-shapes to lines
        corresponding with specific values. Keys in `pattern_shape_map` should
        be values in the column denoted by `pattern_shape`. Alternatively, if
        the values of `pattern_shape` are valid patterns-shapes names, the
        string `'identity'` may be passed to cause them to be used directly.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    barmode : str (default `'relative'`)
        One of `'group'`, `'overlay'` or `'relative'` In `'relative'` mode,
        bars are stacked above zero for positive values and below zero for
        negative values. In `'overlay'` mode, bars are drawn on top of one
        another. In `'group'` mode, bars are placed beside each other.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    text_auto : bool or string (default `False`)
        If `True` or a string, the x or y or z values will be displayed as
        text, depending on the orientation A string like `'.2f'` will be
        interpreted as a `texttemplate` numeric formatting directive.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Bar,
        trace_patch=dict(textposition="auto"),
        layout_patch=dict(barmode=barmode),
    )


def timeline(
    data_frame=None,
    x_start=None,
    x_end=None,
    y=None,
    color=None,
    pattern_shape=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    pattern_shape_sequence=None,
    pattern_shape_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    range_x=None,
    range_y=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a timeline plot, each row of `data_frame` is represented as a rectangular
    mark on an x axis of type `date`, spanning from `x_start` to `x_end`.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x_start : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. (required) Values from this column or array_like are
        used to position marks along the x axis in cartesian coordinates.
    x_end : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. (required) Values from this column or array_like are
        used to position marks along the x axis in cartesian coordinates.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    pattern_shape : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign pattern shapes to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    pattern_shape_sequence : list of str
        Strings should define valid plotly.js patterns-shapes. When
        `pattern_shape` is set, values in that column are assigned patterns-
        shapes by cycling through `pattern_shape_sequence` in the order
        described in `category_orders`, unless the value of `pattern_shape` is
        a key in `pattern_shape_map`.
    pattern_shape_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js patterns-shapes. Used to override
        `pattern_shape_sequences` to assign a specific patterns-shapes to lines
        corresponding with specific values. Keys in `pattern_shape_map` should
        be values in the column denoted by `pattern_shape`. Alternatively, if
        the values of `pattern_shape` are valid patterns-shapes names, the
        string `'identity'` may be passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor="timeline",
        trace_patch=dict(textposition="auto", orientation="h"),
        layout_patch=dict(barmode="overlay"),
    )


def histogram(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    pattern_shape=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    pattern_shape_sequence=None,
    pattern_shape_map=None,
    marginal=None,
    opacity=None,
    orientation=None,
    barmode="relative",
    barnorm=None,
    histnorm=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    histfunc=None,
    cumulative=None,
    nbins=None,
    text_auto=False,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a histogram, rows of `data_frame` are grouped together into a
    rectangular mark to visualize the 1D distribution of an aggregate
    function `histfunc` (e.g. the count or sum) of the value `y` (or `x` if
    `orientation` is `'h'`).

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. If
        `orientation` is `'h'`, these values are used as inputs to `histfunc`.
        Either `x` or `y` can optionally be a list of column references or
        array_likes,  in which case the data will be treated as if it were
        'wide' rather than 'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. If
        `orientation` is `'v'`, these values are used as inputs to `histfunc`.
        Either `x` or `y` can optionally be a list of column references or
        array_likes,  in which case the data will be treated as if it were
        'wide' rather than 'long'.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    pattern_shape : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign pattern shapes to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    pattern_shape_sequence : list of str
        Strings should define valid plotly.js patterns-shapes. When
        `pattern_shape` is set, values in that column are assigned patterns-
        shapes by cycling through `pattern_shape_sequence` in the order
        described in `category_orders`, unless the value of `pattern_shape` is
        a key in `pattern_shape_map`.
    pattern_shape_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js patterns-shapes. Used to override
        `pattern_shape_sequences` to assign a specific patterns-shapes to lines
        corresponding with specific values. Keys in `pattern_shape_map` should
        be values in the column denoted by `pattern_shape`. Alternatively, if
        the values of `pattern_shape` are valid patterns-shapes names, the
        string `'identity'` may be passed to cause them to be used directly.
    marginal : str
        One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`. If set, a
        subplot is drawn alongside the main plot, visualizing the distribution.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    barmode : str (default `'relative'`)
        One of `'group'`, `'overlay'` or `'relative'` In `'relative'` mode,
        bars are stacked above zero for positive values and below zero for
        negative values. In `'overlay'` mode, bars are drawn on top of one
        another. In `'group'` mode, bars are placed beside each other.
    barnorm : str (default `None`)
        One of `'fraction'` or `'percent'`. If `'fraction'`, the value of each
        bar is divided by the sum of all values at that location coordinate.
        `'percent'` is the same but multiplied by 100 to show percentages.
        `None` will stack up all values at each location coordinate.
    histnorm: str (default `None`)
        One of `'percent'`, `'probability'`, `'density'`, or `'probability
        density'` If `None`, the output of `histfunc` is used as is. If
        `'probability'`, the output of `histfunc` for a given bin is divided by
        the sum of the output of `histfunc` for all bins. If `'percent'`, the
        output of `histfunc` for a given bin is divided by the sum of the
        output of `histfunc` for all bins and multiplied by 100. If
        `'density'`, the output of `histfunc` for a given bin is divided by the
        size of the bin. If `'probability density'`, the output of `histfunc`
        for a given bin is normalized such that it corresponds to the
        probability that a random event whose distribution is described by the
        output of `histfunc` will fall into that bin.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    histfunc : str (default `'count'` if no arguments are provided, else `'sum'`)
        One of `'count'`, `'sum'`, `'avg'`, `'min'`, or `'max'`. Function used
        to aggregate values for summarization (note: can be normalized with
        `histnorm`). The arguments to this function are the values of `y` (`x`)
        if `orientation` is `'v'` (`'h'`).
    cumulative : boolean (default `False`)
        If `True`, histogram values are cumulative.
    nbins : int
        Positive integer. Sets the number of bins.
    text_auto : bool or string (default `False`)
        If `True` or a string, the x or y or z values will be displayed as
        text, depending on the orientation A string like `'.2f'` will be
        interpreted as a `texttemplate` numeric formatting directive.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Histogram,
        trace_patch=dict(
            histnorm=histnorm,
            histfunc=histfunc,
            cumulative=dict(enabled=cumulative),
        ),
        layout_patch=dict(barmode=barmode, barnorm=barnorm),
    )


def ecdf(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    text=None,
    line_dash=None,
    symbol=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    animation_frame=None,
    animation_group=None,
    markers=False,
    lines=True,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    line_dash_sequence=None,
    line_dash_map=None,
    symbol_sequence=None,
    symbol_map=None,
    marginal=None,
    opacity=None,
    orientation=None,
    ecdfnorm="probability",
    ecdfmode="standard",
    render_mode="auto",
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a Empirical Cumulative Distribution Function (ECDF) plot, rows of `data_frame`
    are sorted by the value `x` (or `y` if `orientation` is `'h'`) and their cumulative
    count (or the cumulative sum of `y` if supplied and `orientation` is `h`) is drawn
    as a line.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. If
        `orientation` is `'h'`, the cumulative sum of this argument is plotted
        rather than the cumulative count. Either `x` or `y` can optionally be a
        list of column references or array_likes,  in which case the data will
        be treated as if it were 'wide' rather than 'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. If
        `orientation` is `'v'`, the cumulative sum of this argument is plotted
        rather than the cumulative count. Either `x` or `y` can optionally be a
        list of column references or array_likes,  in which case the data will
        be treated as if it were 'wide' rather than 'long'.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    line_dash : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign dash-patterns to lines.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    markers : boolean (default `False`)
        If `True`, markers are shown on lines.
    lines : boolean (default `True`)
        If `False`, lines are not drawn (forced to `True` if `markers` is
        `False`).
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    line_dash_sequence : list of str
        Strings should define valid plotly.js dash-patterns. When `line_dash`
        is set, values in that column are assigned dash-patterns by cycling
        through `line_dash_sequence` in the order described in
        `category_orders`, unless the value of `line_dash` is a key in
        `line_dash_map`.
    line_dash_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js dash-patterns. Used to override
        `line_dash_sequences` to assign a specific dash-patterns to lines
        corresponding with specific values. Keys in `line_dash_map` should be
        values in the column denoted by `line_dash`. Alternatively, if the
        values of `line_dash` are valid line-dash names, the string
        `'identity'` may be passed to cause them to be used directly.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    marginal : str
        One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`. If set, a
        subplot is drawn alongside the main plot, visualizing the distribution.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    ecdfnorm : string or `None` (default `'probability'`)
        One of `'probability'` or `'percent'` If `None`, values will be raw
        counts or sums. If `'probability', values will be probabilities
        normalized from 0 to 1. If `'percent', values will be percentages
        normalized from 0 to 100.
    ecdfmode : string (default `'standard'`)
        One of `'standard'`, `'complementary'` or `'reversed'` If `'standard'`,
        the ECDF is plotted such that values represent data at or below the
        point. If `'complementary'`, the CCDF is plotted such that values
        represent data above the point. If `'reversed'`, a variant of the CCDF
        is plotted such that values represent data at or above the point.
    render_mode : str
        One of `'auto'`, `'svg'` or `'webgl'`, default `'auto'` Controls the
        browser API used to draw marks. `'svg'` is appropriate for figures of
        less than 1000 data points, and will allow for fully-vectorized output.
        `'webgl'` is likely necessary for acceptable performance above 1000
        points but rasterizes part of the output.  `'auto'` uses heuristics to
        choose the mode.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatter)


def violin(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    orientation=None,
    violinmode=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    points=None,
    box=False,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a violin plot, rows of `data_frame` are grouped together into a
    curved mark to visualize their distribution.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    violinmode : str (default `'group'`)
        One of `'group'` or `'overlay'` In `'overlay'` mode, violins are on
        drawn top of one another. In `'group'` mode, violins are placed beside
        each other.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    points : str or boolean (default `'outliers'`)
        One of `'outliers'`, `'suspectedoutliers'`, `'all'`, or `False`. If
        `'outliers'`, only the sample points lying outside the whiskers are
        shown. If `'suspectedoutliers'`, all outlier points are shown and those
        less than 4*Q1-3*Q3 or greater than 4*Q3-3*Q1 are highlighted with the
        marker's `'outliercolor'`. If `'outliers'`, only the sample points
        lying outside the whiskers are shown. If `'all'`, all sample points are
        shown. If `False`, no sample points are shown and the whiskers extend
        to the full range of the sample.
    box : boolean (default `False`)
        If `True`, boxes are drawn inside the violins.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Violin,
        trace_patch=dict(
            points=points,
            box=dict(visible=box),
            scalegroup=True,
            x0=" ",
            y0=" ",
        ),
        layout_patch=dict(violinmode=violinmode),
    )


def box(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    orientation=None,
    boxmode=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    points=None,
    notched=False,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a box plot, rows of `data_frame` are grouped together into a
    box-and-whisker mark to visualize their distribution.

    Each box spans from quartile 1 (Q1) to quartile 3 (Q3). The second
    quartile (Q2) is marked by a line inside the box. By default, the
    whiskers correspond to the box' edges +/- 1.5 times the interquartile
    range (IQR: Q3-Q1), see "points" for other options.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    boxmode : str (default `'group'`)
        One of `'group'` or `'overlay'` In `'overlay'` mode, boxes are on drawn
        top of one another. In `'group'` mode, boxes are placed beside each
        other.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    points : str or boolean (default `'outliers'`)
        One of `'outliers'`, `'suspectedoutliers'`, `'all'`, or `False`. If
        `'outliers'`, only the sample points lying outside the whiskers are
        shown. If `'suspectedoutliers'`, all outlier points are shown and those
        less than 4*Q1-3*Q3 or greater than 4*Q3-3*Q1 are highlighted with the
        marker's `'outliercolor'`. If `'outliers'`, only the sample points
        lying outside the whiskers are shown. If `'all'`, all sample points are
        shown. If `False`, no sample points are shown and the whiskers extend
        to the full range of the sample.
    notched : boolean (default `False`)
        If `True`, boxes are drawn with notches.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Box,
        trace_patch=dict(boxpoints=points, notched=notched, x0=" ", y0=" "),
        layout_patch=dict(boxmode=boxmode),
    )


def strip(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    orientation=None,
    stripmode=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a strip plot each row of `data_frame` is represented as a jittered
    mark within categories.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    stripmode: str (default `'group'`)
        One of `'group'` or `'overlay'` In `'overlay'` mode, strips are on
        drawn top of one another. In `'group'` mode, strips are placed beside
        each other.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Box,
        trace_patch=dict(
            boxpoints="all",
            pointpos=0,
            hoveron="points",
            fillcolor="rgba(255,255,255,0)",
            line={"color": "rgba(255,255,255,0)"},
            x0=" ",
            y0=" ",
        ),
        layout_patch=dict(boxmode=stripmode),
    )


def scatter_3d(
    data_frame=None,
    x=None,
    y=None,
    z=None,
    color=None,
    symbol=None,
    size=None,
    text=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    error_z=None,
    error_z_minus=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    size_max=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    symbol_sequence=None,
    symbol_map=None,
    opacity=None,
    log_x=False,
    log_y=False,
    log_z=False,
    range_x=None,
    range_y=None,
    range_z=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a 3D scatter plot, each row of `data_frame` is represented by a
    symbol mark in 3D space.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates.
    z : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the z axis in cartesian coordinates.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    size : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign mark sizes.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    error_x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars. If `error_x_minus` is `None`, error bars will
        be symmetrical, otherwise `error_x` is used for the positive direction
        only.
    error_x_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars in the negative direction. Ignored if `error_x`
        is `None`.
    error_y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars. If `error_y_minus` is `None`, error bars will
        be symmetrical, otherwise `error_y` is used for the positive direction
        only.
    error_y_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars in the negative direction. Ignored if `error_y`
        is `None`.
    error_z : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size z-axis error bars. If `error_z_minus` is `None`, error bars will
        be symmetrical, otherwise `error_z` is used for the positive direction
        only.
    error_z_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size z-axis error bars in the negative direction. Ignored if `error_z`
        is `None`.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    size_max : int (default `20`)
        Set the maximum mark size when using `size`.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    log_z : boolean (default `False`)
        If `True`, the z-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    range_z : list of two numbers
        If provided, overrides auto-scaling on the z-axis in cartesian
        coordinates.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatter3d)


def line_3d(
    data_frame=None,
    x=None,
    y=None,
    z=None,
    color=None,
    line_dash=None,
    text=None,
    line_group=None,
    symbol=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    error_z=None,
    error_z_minus=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    line_dash_sequence=None,
    line_dash_map=None,
    symbol_sequence=None,
    symbol_map=None,
    markers=False,
    log_x=False,
    log_y=False,
    log_z=False,
    range_x=None,
    range_y=None,
    range_z=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a 3D line plot, each row of `data_frame` is represented as a vertex of
    a polyline mark in 3D space.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates.
    z : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the z axis in cartesian coordinates.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    line_dash : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign dash-patterns to lines.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    line_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        group rows of `data_frame` into lines.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    error_x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars. If `error_x_minus` is `None`, error bars will
        be symmetrical, otherwise `error_x` is used for the positive direction
        only.
    error_x_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size x-axis error bars in the negative direction. Ignored if `error_x`
        is `None`.
    error_y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars. If `error_y_minus` is `None`, error bars will
        be symmetrical, otherwise `error_y` is used for the positive direction
        only.
    error_y_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size y-axis error bars in the negative direction. Ignored if `error_y`
        is `None`.
    error_z : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size z-axis error bars. If `error_z_minus` is `None`, error bars will
        be symmetrical, otherwise `error_z` is used for the positive direction
        only.
    error_z_minus : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        size z-axis error bars in the negative direction. Ignored if `error_z`
        is `None`.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    line_dash_sequence : list of str
        Strings should define valid plotly.js dash-patterns. When `line_dash`
        is set, values in that column are assigned dash-patterns by cycling
        through `line_dash_sequence` in the order described in
        `category_orders`, unless the value of `line_dash` is a key in
        `line_dash_map`.
    line_dash_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js dash-patterns. Used to override
        `line_dash_sequences` to assign a specific dash-patterns to lines
        corresponding with specific values. Keys in `line_dash_map` should be
        values in the column denoted by `line_dash`. Alternatively, if the
        values of `line_dash` are valid line-dash names, the string
        `'identity'` may be passed to cause them to be used directly.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    markers : boolean (default `False`)
        If `True`, markers are shown on lines.
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    log_z : boolean (default `False`)
        If `True`, the z-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    range_z : list of two numbers
        If provided, overrides auto-scaling on the z-axis in cartesian
        coordinates.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatter3d)


def scatter_ternary(
    data_frame=None,
    a=None,
    b=None,
    c=None,
    color=None,
    symbol=None,
    size=None,
    text=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    symbol_sequence=None,
    symbol_map=None,
    opacity=None,
    size_max=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a ternary scatter plot, each row of `data_frame` is represented by a
    symbol mark in ternary coordinates.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    a : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the a axis in ternary coordinates.
    b : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the b axis in ternary coordinates.
    c : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the c axis in ternary coordinates.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    size : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign mark sizes.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    size_max : int (default `20`)
        Set the maximum mark size when using `size`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatterternary)


def line_ternary(
    data_frame=None,
    a=None,
    b=None,
    c=None,
    color=None,
    line_dash=None,
    line_group=None,
    symbol=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    line_dash_sequence=None,
    line_dash_map=None,
    symbol_sequence=None,
    symbol_map=None,
    markers=False,
    line_shape=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a ternary line plot, each row of `data_frame` is represented as
    a vertex of a polyline mark in ternary coordinates.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    a : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the a axis in ternary coordinates.
    b : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the b axis in ternary coordinates.
    c : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the c axis in ternary coordinates.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    line_dash : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign dash-patterns to lines.
    line_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        group rows of `data_frame` into lines.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    line_dash_sequence : list of str
        Strings should define valid plotly.js dash-patterns. When `line_dash`
        is set, values in that column are assigned dash-patterns by cycling
        through `line_dash_sequence` in the order described in
        `category_orders`, unless the value of `line_dash` is a key in
        `line_dash_map`.
    line_dash_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js dash-patterns. Used to override
        `line_dash_sequences` to assign a specific dash-patterns to lines
        corresponding with specific values. Keys in `line_dash_map` should be
        values in the column denoted by `line_dash`. Alternatively, if the
        values of `line_dash` are valid line-dash names, the string
        `'identity'` may be passed to cause them to be used directly.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    markers : boolean (default `False`)
        If `True`, markers are shown on lines.
    line_shape : str (default `'linear'`)
        One of `'linear'`, `'spline'`, `'hv'`, `'vh'`, `'hvh'`, or `'vhv'`
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatterternary)


def scatter_polar(
    data_frame=None,
    r=None,
    theta=None,
    color=None,
    symbol=None,
    size=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    symbol_sequence=None,
    symbol_map=None,
    opacity=None,
    direction="clockwise",
    start_angle=90,
    size_max=None,
    range_r=None,
    range_theta=None,
    log_r=False,
    render_mode="auto",
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a polar scatter plot, each row of `data_frame` is represented by a
    symbol mark in polar coordinates.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    r : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the radial axis in polar coordinates.
    theta : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the angular axis in polar coordinates.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    size : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign mark sizes.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    direction : str
        One of '`counterclockwise'` or `'clockwise'`. Default is `'clockwise'`
        Sets the direction in which increasing values of the angular axis are
        drawn.
    start_angle : int (default `90`)
        Sets start angle for the angular axis, with 0 being due east and 90
        being due north.
    size_max : int (default `20`)
        Set the maximum mark size when using `size`.
    range_r : list of two numbers
        If provided, overrides auto-scaling on the radial axis in polar
        coordinates.
    range_theta : list of two numbers
        If provided, overrides auto-scaling on the angular axis in polar
        coordinates.
    log_r : boolean (default `False`)
        If `True`, the radial axis is log-scaled in polar coordinates.
    render_mode : str
        One of `'auto'`, `'svg'` or `'webgl'`, default `'auto'` Controls the
        browser API used to draw marks. `'svg'` is appropriate for figures of
        less than 1000 data points, and will allow for fully-vectorized output.
        `'webgl'` is likely necessary for acceptable performance above 1000
        points but rasterizes part of the output.  `'auto'` uses heuristics to
        choose the mode.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatterpolar)


def line_polar(
    data_frame=None,
    r=None,
    theta=None,
    color=None,
    line_dash=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    line_group=None,
    text=None,
    symbol=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    line_dash_sequence=None,
    line_dash_map=None,
    symbol_sequence=None,
    symbol_map=None,
    markers=False,
    direction="clockwise",
    start_angle=90,
    line_close=False,
    line_shape=None,
    render_mode="auto",
    range_r=None,
    range_theta=None,
    log_r=False,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a polar line plot, each row of `data_frame` is represented as a
    vertex of a polyline mark in polar coordinates.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    r : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the radial axis in polar coordinates.
    theta : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the angular axis in polar coordinates.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    line_dash : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign dash-patterns to lines.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    line_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        group rows of `data_frame` into lines.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    line_dash_sequence : list of str
        Strings should define valid plotly.js dash-patterns. When `line_dash`
        is set, values in that column are assigned dash-patterns by cycling
        through `line_dash_sequence` in the order described in
        `category_orders`, unless the value of `line_dash` is a key in
        `line_dash_map`.
    line_dash_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js dash-patterns. Used to override
        `line_dash_sequences` to assign a specific dash-patterns to lines
        corresponding with specific values. Keys in `line_dash_map` should be
        values in the column denoted by `line_dash`. Alternatively, if the
        values of `line_dash` are valid line-dash names, the string
        `'identity'` may be passed to cause them to be used directly.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    markers : boolean (default `False`)
        If `True`, markers are shown on lines.
    direction : str
        One of '`counterclockwise'` or `'clockwise'`. Default is `'clockwise'`
        Sets the direction in which increasing values of the angular axis are
        drawn.
    start_angle : int (default `90`)
        Sets start angle for the angular axis, with 0 being due east and 90
        being due north.
    line_close: boolean (default `False`)
        If `True`, an extra line segment is drawn between the first and last
        point.
    line_shape : str (default `'linear'`)
        One of `'linear'`, `'spline'`, `'hv'`, `'vh'`, `'hvh'`, or `'vhv'`
    render_mode : str
        One of `'auto'`, `'svg'` or `'webgl'`, default `'auto'` Controls the
        browser API used to draw marks. `'svg'` is appropriate for figures of
        less than 1000 data points, and will allow for fully-vectorized output.
        `'webgl'` is likely necessary for acceptable performance above 1000
        points but rasterizes part of the output.  `'auto'` uses heuristics to
        choose the mode.
    range_r : list of two numbers
        If provided, overrides auto-scaling on the radial axis in polar
        coordinates.
    range_theta : list of two numbers
        If provided, overrides auto-scaling on the angular axis in polar
        coordinates.
    log_r : boolean (default `False`)
        If `True`, the radial axis is log-scaled in polar coordinates.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scatterpolar)


def bar_polar(
    data_frame=None,
    r=None,
    theta=None,
    color=None,
    pattern_shape=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    base=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    pattern_shape_sequence=None,
    pattern_shape_map=None,
    range_color=None,
    color_continuous_midpoint=None,
    barnorm=None,
    barmode="relative",
    direction="clockwise",
    start_angle=90,
    range_r=None,
    range_theta=None,
    log_r=False,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a polar bar plot, each row of `data_frame` is represented as a wedge
    mark in polar coordinates.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    r : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the radial axis in polar coordinates.
    theta : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the angular axis in polar coordinates.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    pattern_shape : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign pattern shapes to marks.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    base : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position the base of the bar.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    pattern_shape_sequence : list of str
        Strings should define valid plotly.js patterns-shapes. When
        `pattern_shape` is set, values in that column are assigned patterns-
        shapes by cycling through `pattern_shape_sequence` in the order
        described in `category_orders`, unless the value of `pattern_shape` is
        a key in `pattern_shape_map`.
    pattern_shape_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js patterns-shapes. Used to override
        `pattern_shape_sequences` to assign a specific patterns-shapes to lines
        corresponding with specific values. Keys in `pattern_shape_map` should
        be values in the column denoted by `pattern_shape`. Alternatively, if
        the values of `pattern_shape` are valid patterns-shapes names, the
        string `'identity'` may be passed to cause them to be used directly.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    barnorm : str (default `None`)
        One of `'fraction'` or `'percent'`. If `'fraction'`, the value of each
        bar is divided by the sum of all values at that location coordinate.
        `'percent'` is the same but multiplied by 100 to show percentages.
        `None` will stack up all values at each location coordinate.
    barmode : str (default `'relative'`)
        One of `'group'`, `'overlay'` or `'relative'` In `'relative'` mode,
        bars are stacked above zero for positive values and below zero for
        negative values. In `'overlay'` mode, bars are drawn on top of one
        another. In `'group'` mode, bars are placed beside each other.
    direction : str
        One of '`counterclockwise'` or `'clockwise'`. Default is `'clockwise'`
        Sets the direction in which increasing values of the angular axis are
        drawn.
    start_angle : int (default `90`)
        Sets start angle for the angular axis, with 0 being due east and 90
        being due north.
    range_r : list of two numbers
        If provided, overrides auto-scaling on the radial axis in polar
        coordinates.
    range_theta : list of two numbers
        If provided, overrides auto-scaling on the angular axis in polar
        coordinates.
    log_r : boolean (default `False`)
        If `True`, the radial axis is log-scaled in polar coordinates.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Barpolar,
        layout_patch=dict(barnorm=barnorm, barmode=barmode),
    )


def choropleth(
    data_frame=None,
    lat=None,
    lon=None,
    locations=None,
    locationmode=None,
    geojson=None,
    featureidkey=None,
    color=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    projection=None,
    scope=None,
    center=None,
    fitbounds=None,
    basemap_visible=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a choropleth map, each row of `data_frame` is represented by a
    colored region mark on a map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    locations : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are to be
        interpreted according to `locationmode` and mapped to
        longitude/latitude.
    locationmode : str
        One of 'ISO-3', 'USA-states', or 'country names' Determines the set of
        locations used to match entries in `locations` to regions on the map.
    geojson : GeoJSON-formatted dict
        Must contain a Polygon feature collection, with IDs, which are
        references from `locations`.
    featureidkey : str (default: `'id'`)
        Path to field in GeoJSON feature object with which to match the values
        passed in to `locations`.The most common alternative to the default is
        of the form `'properties.<key>`.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    projection : str
        One of `'equirectangular'`, `'mercator'`, `'orthographic'`, `'natural
        earth'`, `'kavrayskiy7'`, `'miller'`, `'robinson'`, `'eckert4'`,
        `'azimuthal equal area'`, `'azimuthal equidistant'`, `'conic equal
        area'`, `'conic conformal'`, `'conic equidistant'`, `'gnomonic'`,
        `'stereographic'`, `'mollweide'`, `'hammer'`, `'transverse mercator'`,
        `'albers usa'`, `'winkel tripel'`, `'aitoff'`, or `'sinusoidal'`Default
        depends on `scope`.
    scope : str (default `'world'`).
        One of `'world'`, `'usa'`, `'europe'`, `'asia'`, `'africa'`, `'north
        america'`, or `'south america'`Default is `'world'` unless `projection`
        is set to `'albers usa'`, which forces `'usa'`.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    fitbounds : str (default `False`).
        One of `False`, `locations` or `geojson`.
    basemap_visible : bool
        Force the basemap visibility.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Choropleth,
        trace_patch=dict(locationmode=locationmode),
    )


def scatter_geo(
    data_frame=None,
    lat=None,
    lon=None,
    locations=None,
    locationmode=None,
    geojson=None,
    featureidkey=None,
    color=None,
    text=None,
    symbol=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    size=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    symbol_sequence=None,
    symbol_map=None,
    opacity=None,
    size_max=None,
    projection=None,
    scope=None,
    center=None,
    fitbounds=None,
    basemap_visible=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a geographic scatter plot, each row of `data_frame` is represented
    by a symbol mark on a map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    locations : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are to be
        interpreted according to `locationmode` and mapped to
        longitude/latitude.
    locationmode : str
        One of 'ISO-3', 'USA-states', or 'country names' Determines the set of
        locations used to match entries in `locations` to regions on the map.
    geojson : GeoJSON-formatted dict
        Must contain a Polygon feature collection, with IDs, which are
        references from `locations`.
    featureidkey : str (default: `'id'`)
        Path to field in GeoJSON feature object with which to match the values
        passed in to `locations`.The most common alternative to the default is
        of the form `'properties.<key>`.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    size : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign mark sizes.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    size_max : int (default `20`)
        Set the maximum mark size when using `size`.
    projection : str
        One of `'equirectangular'`, `'mercator'`, `'orthographic'`, `'natural
        earth'`, `'kavrayskiy7'`, `'miller'`, `'robinson'`, `'eckert4'`,
        `'azimuthal equal area'`, `'azimuthal equidistant'`, `'conic equal
        area'`, `'conic conformal'`, `'conic equidistant'`, `'gnomonic'`,
        `'stereographic'`, `'mollweide'`, `'hammer'`, `'transverse mercator'`,
        `'albers usa'`, `'winkel tripel'`, `'aitoff'`, or `'sinusoidal'`Default
        depends on `scope`.
    scope : str (default `'world'`).
        One of `'world'`, `'usa'`, `'europe'`, `'asia'`, `'africa'`, `'north
        america'`, or `'south america'`Default is `'world'` unless `projection`
        is set to `'albers usa'`, which forces `'usa'`.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    fitbounds : str (default `False`).
        One of `False`, `locations` or `geojson`.
    basemap_visible : bool
        Force the basemap visibility.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Scattergeo,
        trace_patch=dict(locationmode=locationmode),
    )


def line_geo(
    data_frame=None,
    lat=None,
    lon=None,
    locations=None,
    locationmode=None,
    geojson=None,
    featureidkey=None,
    color=None,
    line_dash=None,
    text=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    line_group=None,
    symbol=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    line_dash_sequence=None,
    line_dash_map=None,
    symbol_sequence=None,
    symbol_map=None,
    markers=False,
    projection=None,
    scope=None,
    center=None,
    fitbounds=None,
    basemap_visible=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a geographic line plot, each row of `data_frame` is represented as
    a vertex of a polyline mark on a map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    locations : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are to be
        interpreted according to `locationmode` and mapped to
        longitude/latitude.
    locationmode : str
        One of 'ISO-3', 'USA-states', or 'country names' Determines the set of
        locations used to match entries in `locations` to regions on the map.
    geojson : GeoJSON-formatted dict
        Must contain a Polygon feature collection, with IDs, which are
        references from `locations`.
    featureidkey : str (default: `'id'`)
        Path to field in GeoJSON feature object with which to match the values
        passed in to `locations`.The most common alternative to the default is
        of the form `'properties.<key>`.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    line_dash : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign dash-patterns to lines.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    line_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        group rows of `data_frame` into lines.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    line_dash_sequence : list of str
        Strings should define valid plotly.js dash-patterns. When `line_dash`
        is set, values in that column are assigned dash-patterns by cycling
        through `line_dash_sequence` in the order described in
        `category_orders`, unless the value of `line_dash` is a key in
        `line_dash_map`.
    line_dash_map : dict with str keys and str values (default `{}`)
        Strings values define plotly.js dash-patterns. Used to override
        `line_dash_sequences` to assign a specific dash-patterns to lines
        corresponding with specific values. Keys in `line_dash_map` should be
        values in the column denoted by `line_dash`. Alternatively, if the
        values of `line_dash` are valid line-dash names, the string
        `'identity'` may be passed to cause them to be used directly.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    markers : boolean (default `False`)
        If `True`, markers are shown on lines.
    projection : str
        One of `'equirectangular'`, `'mercator'`, `'orthographic'`, `'natural
        earth'`, `'kavrayskiy7'`, `'miller'`, `'robinson'`, `'eckert4'`,
        `'azimuthal equal area'`, `'azimuthal equidistant'`, `'conic equal
        area'`, `'conic conformal'`, `'conic equidistant'`, `'gnomonic'`,
        `'stereographic'`, `'mollweide'`, `'hammer'`, `'transverse mercator'`,
        `'albers usa'`, `'winkel tripel'`, `'aitoff'`, or `'sinusoidal'`Default
        depends on `scope`.
    scope : str (default `'world'`).
        One of `'world'`, `'usa'`, `'europe'`, `'asia'`, `'africa'`, `'north
        america'`, or `'south america'`Default is `'world'` unless `projection`
        is set to `'albers usa'`, which forces `'usa'`.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    fitbounds : str (default `False`).
        One of `False`, `locations` or `geojson`.
    basemap_visible : bool
        Force the basemap visibility.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(),
        constructor=go.Scattergeo,
        trace_patch=dict(locationmode=locationmode),
    )


def scatter_map(
    data_frame=None,
    lat=None,
    lon=None,
    color=None,
    text=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    size=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    size_max=None,
    zoom=8,
    center=None,
    map_style=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a scatter map, each row of `data_frame` is represented by a
    symbol mark on the map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    size : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign mark sizes.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    size_max : int (default `20`)
        Set the maximum mark size when using `size`.
    zoom : int (default `8`)
        Between 0 and 20. Sets map zoom level.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    map_style : str (default `'basic'`)
        Identifier of base map style. Allowed values are `'basic'`, `'carto-
        darkmatter'`, `'carto-darkmatter-nolabels'`, `'carto-positron'`,
        `'carto-positron-nolabels'`, `'carto-voyager'`, `'carto-voyager-
        nolabels'`, `'dark'`, `'light'`, `'open-street-map'`, `'outdoors'`,
        `'satellite'`, `'satellite-streets'`, `'streets'`, `'white-bg'`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure

    """
    return make_figure(args=locals(), constructor=go.Scattermap)


def choropleth_map(
    data_frame=None,
    geojson=None,
    featureidkey=None,
    locations=None,
    color=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    zoom=8,
    center=None,
    map_style=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a choropleth map, each row of `data_frame` is represented by a
    colored region on the map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    geojson : GeoJSON-formatted dict
        Must contain a Polygon feature collection, with IDs, which are
        references from `locations`.
    featureidkey : str (default: `'id'`)
        Path to field in GeoJSON feature object with which to match the values
        passed in to `locations`.The most common alternative to the default is
        of the form `'properties.<key>`.
    locations : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are to be
        interpreted according to `locationmode` and mapped to
        longitude/latitude.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    zoom : int (default `8`)
        Between 0 and 20. Sets map zoom level.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    map_style : str (default `'basic'`)
        Identifier of base map style. Allowed values are `'basic'`, `'carto-
        darkmatter'`, `'carto-darkmatter-nolabels'`, `'carto-positron'`,
        `'carto-positron-nolabels'`, `'carto-voyager'`, `'carto-voyager-
        nolabels'`, `'dark'`, `'light'`, `'open-street-map'`, `'outdoors'`,
        `'satellite'`, `'satellite-streets'`, `'streets'`, `'white-bg'`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Choroplethmap)


def density_map(
    data_frame=None,
    lat=None,
    lon=None,
    z=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    zoom=8,
    center=None,
    map_style=None,
    radius=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a density map, each row of `data_frame` contributes to the intensity of
    the color of the region around the corresponding point on the map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    z : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the z axis in cartesian coordinates.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    zoom : int (default `8`)
        Between 0 and 20. Sets map zoom level.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    map_style : str (default `'basic'`)
        Identifier of base map style. Allowed values are `'basic'`, `'carto-
        darkmatter'`, `'carto-darkmatter-nolabels'`, `'carto-positron'`,
        `'carto-positron-nolabels'`, `'carto-voyager'`, `'carto-voyager-
        nolabels'`, `'dark'`, `'light'`, `'open-street-map'`, `'outdoors'`,
        `'satellite'`, `'satellite-streets'`, `'streets'`, `'white-bg'`.
    radius : int (default is 30)
        Sets the radius of influence of each point.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(), constructor=go.Densitymap, trace_patch=dict(radius=radius)
    )


def line_map(
    data_frame=None,
    lat=None,
    lon=None,
    color=None,
    text=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    line_group=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    zoom=8,
    center=None,
    map_style=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a line map, each row of `data_frame` is represented as
    a vertex of a polyline mark on the map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    line_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        group rows of `data_frame` into lines.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    zoom : int (default `8`)
        Between 0 and 20. Sets map zoom level.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    map_style : str (default `'basic'`)
        Identifier of base map style. Allowed values are `'basic'`, `'carto-
        darkmatter'`, `'carto-darkmatter-nolabels'`, `'carto-positron'`,
        `'carto-positron-nolabels'`, `'carto-voyager'`, `'carto-voyager-
        nolabels'`, `'dark'`, `'light'`, `'open-street-map'`, `'outdoors'`,
        `'satellite'`, `'satellite-streets'`, `'streets'`, `'white-bg'`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Scattermap)


def scatter_mapbox(
    data_frame=None,
    lat=None,
    lon=None,
    color=None,
    text=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    size=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    size_max=None,
    zoom=8,
    center=None,
    mapbox_style=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    *scatter_mapbox* is deprecated! Use *scatter_map* instead.
    Learn more at: https://plotly.com/python/mapbox-to-maplibre/
    In a Mapbox scatter plot, each row of `data_frame` is represented by a
    symbol mark on a Mapbox map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    size : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign mark sizes.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    size_max : int (default `20`)
        Set the maximum mark size when using `size`.
    zoom : int (default `8`)
        Between 0 and 20. Sets map zoom level.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    mapbox_style : str (default `'basic'`, needs Mapbox API token)
        Identifier of base map style, some of which require a Mapbox or Stadia
        Maps API token to be set using
        `plotly.express.set_mapbox_access_token()`. Allowed values which do not
        require a token are `'open-street-map'`, `'white-bg'`, `'carto-
        positron'`, `'carto-darkmatter'`. Allowed values which require a Mapbox
        API token are `'basic'`, `'streets'`, `'outdoors'`, `'light'`,
        `'dark'`, `'satellite'`, `'satellite-streets'`. Allowed values which
        require a Stadia Maps API token are `'stamen-terrain'`, `'stamen-
        toner'`, `'stamen-watercolor'`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    warn(
        "*scatter_mapbox* is deprecated!"
        + " Use *scatter_map* instead."
        + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
        stacklevel=2,
        category=DeprecationWarning,
    )
    return make_figure(args=locals(), constructor=go.Scattermapbox)


def choropleth_mapbox(
    data_frame=None,
    geojson=None,
    featureidkey=None,
    locations=None,
    color=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    zoom=8,
    center=None,
    mapbox_style=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    *choropleth_mapbox* is deprecated! Use *choropleth_map* instead.
    Learn more at: https://plotly.com/python/mapbox-to-maplibre/
    In a Mapbox choropleth map, each row of `data_frame` is represented by a
    colored region on a Mapbox map.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    geojson : GeoJSON-formatted dict
        Must contain a Polygon feature collection, with IDs, which are
        references from `locations`.
    featureidkey : str (default: `'id'`)
        Path to field in GeoJSON feature object with which to match the values
        passed in to `locations`.The most common alternative to the default is
        of the form `'properties.<key>`.
    locations : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are to be
        interpreted according to `locationmode` and mapped to
        longitude/latitude.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    zoom : int (default `8`)
        Between 0 and 20. Sets map zoom level.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    mapbox_style : str (default `'basic'`, needs Mapbox API token)
        Identifier of base map style, some of which require a Mapbox or Stadia
        Maps API token to be set using
        `plotly.express.set_mapbox_access_token()`. Allowed values which do not
        require a token are `'open-street-map'`, `'white-bg'`, `'carto-
        positron'`, `'carto-darkmatter'`. Allowed values which require a Mapbox
        API token are `'basic'`, `'streets'`, `'outdoors'`, `'light'`,
        `'dark'`, `'satellite'`, `'satellite-streets'`. Allowed values which
        require a Stadia Maps API token are `'stamen-terrain'`, `'stamen-
        toner'`, `'stamen-watercolor'`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    warn(
        "*choropleth_mapbox* is deprecated!"
        + " Use *choropleth_map* instead."
        + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
        stacklevel=2,
        category=DeprecationWarning,
    )
    return make_figure(args=locals(), constructor=go.Choroplethmapbox)


def density_mapbox(
    data_frame=None,
    lat=None,
    lon=None,
    z=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    zoom=8,
    center=None,
    mapbox_style=None,
    radius=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    *density_mapbox* is deprecated! Use *density_map* instead.
    Learn more at: https://plotly.com/python/mapbox-to-maplibre/
    In a Mapbox density map, each row of `data_frame` contributes to the intensity of
    the color of the region around the corresponding point on the map

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    z : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the z axis in cartesian coordinates.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    zoom : int (default `8`)
        Between 0 and 20. Sets map zoom level.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    mapbox_style : str (default `'basic'`, needs Mapbox API token)
        Identifier of base map style, some of which require a Mapbox or Stadia
        Maps API token to be set using
        `plotly.express.set_mapbox_access_token()`. Allowed values which do not
        require a token are `'open-street-map'`, `'white-bg'`, `'carto-
        positron'`, `'carto-darkmatter'`. Allowed values which require a Mapbox
        API token are `'basic'`, `'streets'`, `'outdoors'`, `'light'`,
        `'dark'`, `'satellite'`, `'satellite-streets'`. Allowed values which
        require a Stadia Maps API token are `'stamen-terrain'`, `'stamen-
        toner'`, `'stamen-watercolor'`.
    radius : int (default is 30)
        Sets the radius of influence of each point.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    warn(
        "*density_mapbox* is deprecated!"
        + " Use *density_map* instead."
        + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
        stacklevel=2,
        category=DeprecationWarning,
    )
    return make_figure(
        args=locals(), constructor=go.Densitymapbox, trace_patch=dict(radius=radius)
    )


def line_mapbox(
    data_frame=None,
    lat=None,
    lon=None,
    color=None,
    text=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    line_group=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    zoom=8,
    center=None,
    mapbox_style=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    *line_mapbox* is deprecated! Use *line_map* instead.
    Learn more at: https://plotly.com/python/mapbox-to-maplibre/
    In a Mapbox line plot, each row of `data_frame` is represented as
    a vertex of a polyline mark on a Mapbox map.


    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    lat : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to latitude on a map.
    lon : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks according to longitude on a map.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    line_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        group rows of `data_frame` into lines.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    zoom : int (default `8`)
        Between 0 and 20. Sets map zoom level.
    center : dict
        Dict keys are `'lat'` and `'lon'` Sets the center point of the map.
    mapbox_style : str (default `'basic'`, needs Mapbox API token)
        Identifier of base map style, some of which require a Mapbox or Stadia
        Maps API token to be set using
        `plotly.express.set_mapbox_access_token()`. Allowed values which do not
        require a token are `'open-street-map'`, `'white-bg'`, `'carto-
        positron'`, `'carto-darkmatter'`. Allowed values which require a Mapbox
        API token are `'basic'`, `'streets'`, `'outdoors'`, `'light'`,
        `'dark'`, `'satellite'`, `'satellite-streets'`. Allowed values which
        require a Stadia Maps API token are `'stamen-terrain'`, `'stamen-
        toner'`, `'stamen-watercolor'`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    warn(
        "*line_mapbox* is deprecated!"
        + " Use *line_map* instead."
        + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
        stacklevel=2,
        category=DeprecationWarning,
    )
    return make_figure(args=locals(), constructor=go.Scattermapbox)


def scatter_matrix(
    data_frame=None,
    dimensions=None,
    color=None,
    symbol=None,
    size=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    symbol_sequence=None,
    symbol_map=None,
    opacity=None,
    size_max=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a scatter plot matrix (or SPLOM), each row of `data_frame` is
    represented by a multiple symbol marks, one in each cell of a grid of
    2D scatter plots, which plot each pair of `dimensions` against each
    other.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    dimensions : list of str or int, or Series or array-like
        Either names of columns in `data_frame`, or pandas Series, or
        array_like objects Values from these columns are used for
        multidimensional visualization.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    symbol : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign symbols to marks.
    size : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign mark sizes.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    symbol_sequence : list of str
        Strings should define valid plotly.js symbols. When `symbol` is set,
        values in that column are assigned symbols by cycling through
        `symbol_sequence` in the order described in `category_orders`, unless
        the value of `symbol` is a key in `symbol_map`.
    symbol_map : dict with str keys and str values (default `{}`)
        String values should define plotly.js symbols Used to override
        `symbol_sequence` to assign a specific symbols to marks corresponding
        with specific values. Keys in `symbol_map` should be values in the
        column denoted by `symbol`. Alternatively, if the values of `symbol`
        are valid symbol names, the string `'identity'` may be passed to cause
        them to be used directly.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    size_max : int (default `20`)
        Set the maximum mark size when using `size`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(
        args=locals(), constructor=go.Splom, layout_patch=dict(dragmode="select")
    )


def parallel_coordinates(
    data_frame=None,
    dimensions=None,
    color=None,
    labels=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a parallel coordinates plot, each row of `data_frame` is represented
    by a polyline mark which traverses a set of parallel axes, one for each
    of the `dimensions`.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    dimensions : list of str or int, or Series or array-like
        Either names of columns in `data_frame`, or pandas Series, or
        array_like objects Values from these columns are used for
        multidimensional visualization.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Parcoords)


def parallel_categories(
    data_frame=None,
    dimensions=None,
    color=None,
    labels=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
    dimensions_max_cardinality=50,
) -> go.Figure:
    """
    In a parallel categories (or parallel sets) plot, each row of
    `data_frame` is grouped with other rows that share the same values of
    `dimensions` and then plotted as a polyline mark through a set of
    parallel axes, one for each of the `dimensions`.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    dimensions : list of str or int, or Series or array-like
        Either names of columns in `data_frame`, or pandas Series, or
        array_like objects Values from these columns are used for
        multidimensional visualization.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.
    dimensions_max_cardinality : int (default 50)
        When `dimensions` is `None` and `data_frame` is provided, columns with
        more than this number of unique values are excluded from the output.
        Not used when `dimensions` is passed.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Parcats)


def pie(
    data_frame=None,
    names=None,
    values=None,
    color=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    category_orders=None,
    labels=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
    opacity=None,
    hole=None,
) -> go.Figure:
    """
    In a pie plot, each row of `data_frame` is represented as a sector of a
    pie.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    names : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used as
        labels for sectors.
    values : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        set values associated to sectors.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    hole : float
        Sets the fraction of the radius to cut out of the pie.Use this to make
        a donut chart.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    if color_discrete_sequence is not None:
        layout_patch = {"piecolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    return make_figure(
        args=locals(),
        constructor=go.Pie,
        trace_patch=dict(showlegend=(names is not None), hole=hole),
        layout_patch=layout_patch,
    )


def sunburst(
    data_frame=None,
    names=None,
    values=None,
    parents=None,
    path=None,
    ids=None,
    color=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    labels=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
    branchvalues=None,
    maxdepth=None,
) -> go.Figure:
    """
    A sunburst plot represents hierarchial data as sectors laid out over
    several levels of concentric rings.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    names : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used as
        labels for sectors.
    values : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        set values associated to sectors.
    parents : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used as
        parents in sunburst and treemap charts.
    path : list of str or int, or Series or array-like
        Either names of columns in `data_frame`, or pandas Series, or
        array_like objects List of columns names or columns of a rectangular
        dataframe defining the hierarchy of sectors, from root to leaves. An
        error is raised if path AND ids or parents is passed
    ids : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        set ids of sectors
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.
    branchvalues : str
        'total' or 'remainder' Determines how the items in `values` are summed.
        Whenset to 'total', items in `values` are taken to be valueof all its
        descendants. When set to 'remainder', itemsin `values` corresponding to
        the root and the branches:sectors are taken to be the extra part not
        part of thesum of the values at their leaves.
    maxdepth : int
        Positive integer Sets the number of rendered sectors from any given
        `level`. Set `maxdepth` to -1 to render all thelevels in the hierarchy.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    if color_discrete_sequence is not None:
        layout_patch = {"sunburstcolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    if path is not None and (ids is not None or parents is not None):
        raise ValueError(
            "Either `path` should be provided, or `ids` and `parents`."
            "These parameters are mutually exclusive and cannot be passed together."
        )
    if path is not None and branchvalues is None:
        branchvalues = "total"
    return make_figure(
        args=locals(),
        constructor=go.Sunburst,
        trace_patch=dict(branchvalues=branchvalues, maxdepth=maxdepth),
        layout_patch=layout_patch,
    )


def treemap(
    data_frame=None,
    names=None,
    values=None,
    parents=None,
    ids=None,
    path=None,
    color=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    labels=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
    branchvalues=None,
    maxdepth=None,
) -> go.Figure:
    """
    A treemap plot represents hierarchial data as nested rectangular
    sectors.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    names : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used as
        labels for sectors.
    values : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        set values associated to sectors.
    parents : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used as
        parents in sunburst and treemap charts.
    ids : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        set ids of sectors
    path : list of str or int, or Series or array-like
        Either names of columns in `data_frame`, or pandas Series, or
        array_like objects List of columns names or columns of a rectangular
        dataframe defining the hierarchy of sectors, from root to leaves. An
        error is raised if path AND ids or parents is passed
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.
    branchvalues : str
        'total' or 'remainder' Determines how the items in `values` are summed.
        Whenset to 'total', items in `values` are taken to be valueof all its
        descendants. When set to 'remainder', itemsin `values` corresponding to
        the root and the branches:sectors are taken to be the extra part not
        part of thesum of the values at their leaves.
    maxdepth : int
        Positive integer Sets the number of rendered sectors from any given
        `level`. Set `maxdepth` to -1 to render all thelevels in the hierarchy.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    if color_discrete_sequence is not None:
        layout_patch = {"treemapcolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    if path is not None and (ids is not None or parents is not None):
        raise ValueError(
            "Either `path` should be provided, or `ids` and `parents`."
            "These parameters are mutually exclusive and cannot be passed together."
        )
    if path is not None and branchvalues is None:
        branchvalues = "total"
    return make_figure(
        args=locals(),
        constructor=go.Treemap,
        trace_patch=dict(branchvalues=branchvalues, maxdepth=maxdepth),
        layout_patch=layout_patch,
    )


def icicle(
    data_frame=None,
    names=None,
    values=None,
    parents=None,
    path=None,
    ids=None,
    color=None,
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    labels=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
    branchvalues=None,
    maxdepth=None,
) -> go.Figure:
    """
    An icicle plot represents hierarchial data with adjoined rectangular
    sectors that all cascade from root down to leaf in one direction.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    names : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used as
        labels for sectors.
    values : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        set values associated to sectors.
    parents : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used as
        parents in sunburst and treemap charts.
    path : list of str or int, or Series or array-like
        Either names of columns in `data_frame`, or pandas Series, or
        array_like objects List of columns names or columns of a rectangular
        dataframe defining the hierarchy of sectors, from root to leaves. An
        error is raised if path AND ids or parents is passed
    ids : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        set ids of sectors
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    color_continuous_scale : list of str
        Strings should define valid CSS-colors This list is used to build a
        continuous color scale when the column denoted by `color` contains
        numeric data. Various useful color scales are available in the
        `plotly.express.colors` submodules, specifically
        `plotly.express.colors.sequential`, `plotly.express.colors.diverging`
        and `plotly.express.colors.cyclical`.
    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale.
    color_continuous_midpoint : number (default `None`)
        If set, computes the bounds of the continuous color scale to have the
        desired midpoint. Setting this value is recommended when using
        `plotly.express.colors.diverging` color scales as the inputs to
        `color_continuous_scale`.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.
    branchvalues : str
        'total' or 'remainder' Determines how the items in `values` are summed.
        Whenset to 'total', items in `values` are taken to be valueof all its
        descendants. When set to 'remainder', itemsin `values` corresponding to
        the root and the branches:sectors are taken to be the extra part not
        part of thesum of the values at their leaves.
    maxdepth : int
        Positive integer Sets the number of rendered sectors from any given
        `level`. Set `maxdepth` to -1 to render all thelevels in the hierarchy.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    if color_discrete_sequence is not None:
        layout_patch = {"iciclecolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    if path is not None and (ids is not None or parents is not None):
        raise ValueError(
            "Either `path` should be provided, or `ids` and `parents`."
            "These parameters are mutually exclusive and cannot be passed together."
        )
    if path is not None and branchvalues is None:
        branchvalues = "total"
    return make_figure(
        args=locals(),
        constructor=go.Icicle,
        trace_patch=dict(branchvalues=branchvalues, maxdepth=maxdepth),
        layout_patch=layout_patch,
    )


def funnel(
    data_frame=None,
    x=None,
    y=None,
    color=None,
    facet_row=None,
    facet_col=None,
    facet_col_wrap=0,
    facet_row_spacing=None,
    facet_col_spacing=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    text=None,
    animation_frame=None,
    animation_group=None,
    category_orders=None,
    labels=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    opacity=None,
    orientation=None,
    log_x=False,
    log_y=False,
    range_x=None,
    range_y=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
) -> go.Figure:
    """
    In a funnel plot, each row of `data_frame` is represented as a
    rectangular sector of a funnel.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    x : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the x axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    y : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        position marks along the y axis in cartesian coordinates. Either `x` or
        `y` can optionally be a list of column references or array_likes,  in
        which case the data will be treated as if it were 'wide' rather than
        'long'.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    facet_row : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the vertical direction.
    facet_col : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to facetted subplots in the horizontal direction.
    facet_col_wrap : int
        Maximum number of facet columns. Wraps the column variable at this
        width, so that the column facets span multiple rows. Ignored if 0, and
        forced to 0 if `facet_row` or a `marginal` is set.
    facet_row_spacing : float between 0 and 1
        Spacing between facet rows, in paper units. Default is 0.03 or 0.07
        when facet_col_wrap is used.
    facet_col_spacing : float between 0 and 1
        Spacing between facet columns, in paper units Default is 0.02.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    text : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in the
        figure as text labels.
    animation_frame : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign marks to animation frames.
    animation_group : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        provide object-constancy across animation frames: rows with matching
        `animation_group`s will be treated as if they describe the same object
        in each frame.
    category_orders : dict with str keys and list of str values (default `{}`)
        By default, in Python 3.6+, the order of categorical values in axes,
        legends and facets depends on the order in which these values are first
        encountered in `data_frame` (and no order is guaranteed by default in
        Python below 3.6). This parameter is used to force a specific ordering
        of values per column. The keys of this dict should correspond to column
        names, and the values should be lists of strings corresponding to the
        specific display order desired.
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.
    orientation : str, one of `'h'` for horizontal or `'v'` for vertical.
        (default `'v'` if `x` and `y` are provided and both continuous or both
        categorical,  otherwise `'v'`(`'h'`) if `x`(`y`) is categorical and
        `y`(`x`) is continuous,  otherwise `'v'`(`'h'`) if only `x`(`y`) is
        provided)
    log_x : boolean (default `False`)
        If `True`, the x-axis is log-scaled in cartesian coordinates.
    log_y : boolean (default `False`)
        If `True`, the y-axis is log-scaled in cartesian coordinates.
    range_x : list of two numbers
        If provided, overrides auto-scaling on the x-axis in cartesian
        coordinates.
    range_y : list of two numbers
        If provided, overrides auto-scaling on the y-axis in cartesian
        coordinates.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    return make_figure(args=locals(), constructor=go.Funnel)


def funnel_area(
    data_frame=None,
    names=None,
    values=None,
    color=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    hover_name=None,
    hover_data=None,
    custom_data=None,
    labels=None,
    title=None,
    subtitle=None,
    template=None,
    width=None,
    height=None,
    opacity=None,
) -> go.Figure:
    """
    In a funnel area plot, each row of `data_frame` is represented as a
    trapezoidal sector of a funnel.

    Parameters
    ----------
    data_frame : DataFrame or array-like or dict
        This argument needs to be passed for column names (and not keyword
        names) to be used. Array-like and dict are transformed internally to a
        pandas DataFrame. Optional: if missing, a DataFrame gets constructed
        under the hood using the other arguments.
    names : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used as
        labels for sectors.
    values : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        set values associated to sectors.
    color : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like are used to
        assign color to marks.
    color_discrete_sequence : list of str
        Strings should define valid CSS-colors. When `color` is set and the
        values in the corresponding column are not numeric, values in that
        column are assigned colors by cycling through `color_discrete_sequence`
        in the order described in `category_orders`, unless the value of
        `color` is a key in `color_discrete_map`. Various useful color
        sequences are available in the `plotly.express.colors` submodules,
        specifically `plotly.express.colors.qualitative`.
    color_discrete_map : dict with str keys and str values (default `{}`)
        String values should define valid CSS-colors Used to override
        `color_discrete_sequence` to assign a specific colors to marks
        corresponding with specific values. Keys in `color_discrete_map` should
        be values in the column denoted by `color`. Alternatively, if the
        values of `color` are valid colors, the string `'identity'` may be
        passed to cause them to be used directly.
    hover_name : str or int or Series or array-like
        Either a name of a column in `data_frame`, or a pandas Series or
        array_like object. Values from this column or array_like appear in bold
        in the hover tooltip.
    hover_data : str, or list of str or int, or Series or array-like, or dict
        Either a name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects or a dict with column names as keys, with
        values True (for default formatting) False (in order to remove this
        column from hover information), or a formatting string, for example
        ':.3f' or '|%a' or list-like data to appear in the hover tooltip or
        tuples with a bool or formatting string as first element, and list-like
        data to appear in hover as second element Values from these columns
        appear as extra data in the hover tooltip.
    custom_data : str, or list of str or int, or Series or array-like
        Either name or list of names of columns in `data_frame`, or pandas
        Series, or array_like objects Values from these columns are extra data,
        to be used in widgets or Dash callbacks for example. This data is not
        user-visible but is included in events emitted by the figure (lasso
        selection etc.)
    labels : dict with str keys and str values (default `{}`)
        By default, column names are used in the figure for axis titles, legend
        entries and hovers. This parameter allows this to be overridden. The
        keys of this dict should correspond to column names, and the values
        should correspond to the desired label to be displayed.
    title : str
        The figure title.
    subtitle : str
        The figure subtitle.
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name (must be a key in plotly.io.templates) or
        definition.
    width : int (default `None`)
        The figure width in pixels.
    height : int (default `None`)
        The figure height in pixels.
    opacity : float
        Value between 0 and 1. Sets the opacity for markers.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    if color_discrete_sequence is not None:
        layout_patch = {"funnelareacolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    return make_figure(
        args=locals(),
        constructor=go.Funnelarea,
        trace_patch=dict(showlegend=(names is not None)),
        layout_patch=layout_patch,
    )
