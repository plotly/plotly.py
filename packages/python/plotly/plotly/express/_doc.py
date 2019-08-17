import inspect

colref = "(string: name of column in `data_frame`)"
colref_list = "(list of string: names of columns in `data_frame`)"

# TODO contents of columns
# TODO explain categorical
# TODO handle color
# TODO handle details of box/violin/histogram
# TODO handle details of column selection with `dimensions`
# TODO document "or `None`, default `None`" in various places
# TODO standardize positioning and casing of 'default'

docs = dict(
    data_frame=["A 'tidy' `pandas.DataFrame`"],
    x=[
        colref,
        "Values from this column are used to position marks along the x axis in cartesian coordinates.",
        "For horizontal `histogram`s, these values are used as inputs to `histfunc`.",
    ],
    y=[
        colref,
        "Values from this column are used to position marks along the y axis in cartesian coordinates.",
        "For vertical `histogram`s, these values are used as inputs to `histfunc`.",
    ],
    z=[
        colref,
        "Values from this column are used to position marks along the z axis in cartesian coordinates.",
        "For `density_heatmap` and `density_contour` these values are used as the inputs to `histfunc`.",
    ],
    a=[
        colref,
        "Values from this column are used to position marks along the a axis in ternary coordinates.",
    ],
    b=[
        colref,
        "Values from this column are used to position marks along the b axis in ternary coordinates.",
    ],
    c=[
        colref,
        "Values from this column are used to position marks along the c axis in ternary coordinates.",
    ],
    r=[
        colref,
        "Values from this column are used to position marks along the radial axis in polar coordinates.",
    ],
    theta=[
        colref,
        "Values from this column are used to position marks along the angular axis in polar coordinates.",
    ],
    lat=[
        colref,
        "Values from this column are used to position marks according to latitude on a map.",
    ],
    lon=[
        colref,
        "Values from this column are used to position marks according to longitude on a map.",
    ],
    locations=[
        colref,
        "Values from this column are be interpreted according to `locationmode` and mapped to longitude/latitude.",
    ],
    dimensions=[
        "(list of strings, names of columns in `data_frame`)",
        "Columns to be used in multidimensional visualization.",
    ],
    error_x=[
        colref,
        "Values from this column are used to size x-axis error bars.",
        "If `error_x_minus` is `None`, error bars will be symmetrical, otherwise `error_x` is used for the positive direction only.",
    ],
    error_x_minus=[
        colref,
        "Values from this column are used to size x-axis error bars in the negative direction.",
        "Ignored if `error_x` is `None`.",
    ],
    error_y=[
        colref,
        "Values from this column are used to size y-axis error bars.",
        "If `error_y_minus` is `None`, error bars will be symmetrical, otherwise `error_y` is used for the positive direction only.",
    ],
    error_y_minus=[
        colref,
        "Values from this column are used to size y-axis error bars in the negative direction.",
        "Ignored if `error_y` is `None`.",
    ],
    error_z=[
        colref,
        "Values from this column are used to size z-axis error bars.",
        "If `error_z_minus` is `None`, error bars will be symmetrical, otherwise `error_z` is used for the positive direction only.",
    ],
    error_z_minus=[
        colref,
        "Values from this column are used to size z-axis error bars in the negative direction.",
        "Ignored if `error_z` is `None`.",
    ],
    color=[colref, "Values from this column are used to assign color to marks."],
    opacity=["(number, between 0 and 1) Sets the opacity for markers."],
    line_dash=[
        colref,
        "Values from this column are used to assign dash-patterns to lines.",
    ],
    line_group=[
        colref,
        "Values from this column are used to group rows of `data_frame` into lines.",
    ],
    symbol=[colref, "Values from this column are used to assign symbols to marks."],
    size=[colref, "Values from this column are used to assign mark sizes."],
    hover_name=[colref, "Values from this column appear in bold in the hover tooltip."],
    hover_data=[
        colref_list,
        "Values from these columns appear as extra data in the hover tooltip.",
    ],
    text=[colref, "Values from this column appear in the figure as text labels."],
    locationmode=[
        "(string, one of 'ISO-3', 'USA-states', 'country names')",
        "Determines the set of locations used to match entries in `locations` to regions on the map.",
    ],
    facet_row=[
        colref,
        "Values from this column are used to assign marks to facetted subplots in the vertical direction.",
    ],
    facet_col=[
        colref,
        "Values from this column are used to assign marks to facetted subplots in the horizontal direction.",
    ],
    animation_frame=[
        colref,
        "Values from this column are used to assign marks to animation frames.",
    ],
    animation_group=[
        colref,
        "Values from this column are used to provide object-constancy across animation frames: rows with matching `animation_group`s will be treated as if they describe the same object in each frame.",
    ],
    symbol_sequence=[
        "(list of strings defining plotly.js symbols)",
        "When `symbol` is set, values in that column are assigned symbols by cycling through `symbol_sequence` in the order described in `category_orders`, unless the value of `symbol` is a key in `symbol_map`.",
    ],
    symbol_map=[
        "(dict with string keys and values that are strings defining plotly.js symbols, default `{}`)",
        "Used to override `symbol_sequence` to assign a specific symbols to marks corresponding with specific values.",
        "Keys in `symbol_map` should be values in the column denoted by `symbol`.",
    ],
    line_dash_map=[
        "(dict with string keys and values that are strings defining plotly.js dash-patterns, default `{}`)"
        "Used to override `line_dash_sequences` to assign a specific dash-patterns to lines corresponding with specific values.",
        "Keys in `line_dash_map` should be values in the column denoted by `line_dash`.",
    ],
    line_dash_sequence=[
        "(list of strings defining plotly.js dash-patterns)",
        "When `line_dash` is set, values in that column are assigned dash-patterns by cycling through `line_dash_sequence` in the order described in `category_orders`, unless the value of `line_dash` is a key in `line_dash_map`.",
    ],
    color_discrete_sequence=[
        "(list of valid CSS-color strings)",
        "When `color` is set and the values in the corresponding column are not numeric, values in that column are assigned colors by cycling through `color_discrete_sequence` in the order described in `category_orders`, unless the value of `color` is a key in `color_discrete_map`.",
        "Various useful color sequences are available in the `plotly_express.colors` submodules, specifically `plotly_express.colors.qualitative`.",
    ],
    color_discrete_map=[
        "(dict with string keys and values that are valid CSS-color strings, default `{}`)",
        "Used to override `color_discrete_sequence` to assign a specific colors to marks corresponding with specific values.",
        "Keys in `color_discrete_map` should be values in the column denoted by `color`.",
    ],
    color_continuous_scale=[
        "(list of valid CSS-color strings)",
        "This list is used to build a continuous color scale when the column denoted by `color` contains numeric data.",
        "Various useful color scales are available in the `plotly_express.colors` submodules, specifically `plotly_express.colors.sequential`, `plotly_express.colors.diverging` and `plotly_express.colors.cyclical`.",
    ],
    color_continuous_midpoint=[
        "(number, defaults to `None`)",
        "If set, computes the bounds of the continuous color scale to have the desired midpoint.",
        "Setting this value is recommended when using `plotly_express.colors.diverging` color scales as the inputs to `color_continuous_scale`.",
    ],
    size_max=["(integer, default 20)", "Set the maximum mark size when using `size`."],
    log_x=[
        "(boolean, default `False`)",
        "If `True`, the x-axis is log-scaled in cartesian coordinates.",
    ],
    log_y=[
        "(boolean, default `False`)",
        "If `True`, the y-axis is log-scaled in cartesian coordinates.",
    ],
    log_z=[
        "(boolean, default `False`)",
        "If `True`, the z-axis is log-scaled in cartesian coordinates.",
    ],
    log_r=[
        "(boolean, default `False`)",
        "If `True`, the radial axis is log-scaled in polar coordinates.",
    ],
    range_x=[
        "(2-element list of numbers)",
        "If provided, overrides auto-scaling on the x-axis in cartesian coordinates.",
    ],
    range_y=[
        "(2-element list of numbers)",
        "If provided, overrides auto-scaling on the y-axis in cartesian coordinates.",
    ],
    range_z=[
        "(2-element list of numbers)",
        "If provided, overrides auto-scaling on the z-axis in cartesian coordinates.",
    ],
    range_color=[
        "(2-element list of numbers)",
        "If provided, overrides auto-scaling on the continuous color scale.",
    ],
    range_r=[
        "(2-element list of numbers)",
        "If provided, overrides auto-scaling on the radial axis in polar coordinates.",
    ],
    title=["(string)", "The figure title."],
    template=[
        "(string or Plotly.py template object)",
        "The figure template name or definition.",
    ],
    width=["(integer, default `None`)", "The figure width in pixels."],
    height=["(integer, default `600`)", "The figure height in pixels."],
    labels=[
        "(dict with string keys and string values, default `{}`)",
        "By default, column names are used in the figure for axis titles, legend entries and hovers.",
        "This parameter allows this to be overridden.",
        "The keys of this dict should correspond to column names, and the values should correspond to the desired label to be displayed.",
    ],
    category_orders=[
        "(dict with string keys and list-of-string values, default `{}`)",
        "By default, in Python 3.6+, the order of categorical values in axes, legends and facets depends on the order in which these values are first encountered in `data_frame` (and no order is guaranteed by default in Python below 3.6).",
        "This parameter is used to force a specific ordering of values per column.",
        "The keys of this dict should correspond to column names, and the values should be lists of strings corresponding to the specific display order desired.",
    ],
    marginal=[
        "(string, one of `'rug'`, `'box'`, `'violin'`, `'histogram'`)",
        "If set, a subplot is drawn alongside the main plot, visualizing the distribution.",
    ],
    marginal_x=[
        "(string, one of `'rug'`, `'box'`, `'violin'`, `'histogram'`)",
        "If set, a horizontal subplot is drawn above the main plot, visualizing the x-distribution.",
    ],
    marginal_y=[
        "(string, one of `'rug'`, `'box'`, `'violin'`, `'histogram'`)",
        "If set, a vertical subplot is drawn to the right of the main plot, visualizing the y-distribution.",
    ],
    trendline=[
        "(string, one of `'ols'` or `'lowess'`, default `None`)",
        "If `'ols'`, an Ordinary Least Squares regression line will be drawn for each discrete-color/symbol group.",
        "If `'lowess`', a Locally Weighted Scatterplot Smoothing line will be drawn for each discrete-color/symbol group.",
    ],
    trendline_color_override=[
        "(string, valid CSS color)",
        "If provided, and if `trendline` is set, all trendlines will be drawn in this color.",
    ],
    render_mode=[
        "(string, one of `'auto'`, `'svg'` or `'webgl'`, default `'auto'`)",
        "Controls the browser API used to draw marks.",
        "`'svg`' is appropriate for figures of less than 1000 data points, and will allow for fully-vectorized output.",
        "`'webgl'` is likely necessary for acceptable performance above 1000 points but rasterizes part of the output. ",
        "`'auto'` uses heuristics to choose the mode.",
    ],
    direction=[
        "(string, one of '`counterclockwise'`, `'clockwise'`. Default is `'clockwise'`)",
        "Sets the direction in which increasing values of the angular axis are drawn.",
    ],
    start_angle=[
        "(integer, default is 90)",
        "Sets start angle for the angular axis, with 0 being due east and 90 being due north.",
    ],
    histfunc=[
        "(string, one of `'count'`, `'sum'`, `'avg'`, `'min'`, `'max'`. Default is `'count'`)"
        "Function used to aggregate values for summarization (note: can be normalized with `histnorm`).",
        "The arguments to this function for `histogram` are the values of `y` if `orientation` is `'v'`,",
        "otherwise the arguements are the values of `x`.",
        "The arguments to this function for `density_heatmap` and `density_contour` are the values of `z`.",
    ],
    histnorm=[
        "(string, one of `'percent'`, `'probability'`, `'density'`, `'probability density'`, default `None`)",
        "If `None`, the output of `histfunc` is used as is.",
        "If `'probability'`, the output of `histfunc` for a given bin is divided by the sum of the output of `histfunc` for all bins.",
        "If `'percent'`, the output of `histfunc` for a given bin is divided by the sum of the output of `histfunc` for all bins and multiplied by 100.",
        "If `'density'`, the output of `histfunc` for a given bin is divided by the size of the bin.",
        "If `'probability density'`, the output of `histfunc` for a given bin is normalized such that it corresponds to the probability that a random event whose distribution is described by the output of `histfunc` will fall into that bin.",
    ],
    barnorm=[
        "(string, one of `'fraction'` or `'percent'`, default is `None`)",
        "If set to `'fraction'`, the value of each bar is divided by the sum of all values at that location coordinate.",
        "`'percent'` is the same but multiplied by 100 to show percentages.",
    ],
    groupnorm=[
        "(string, one of `'fraction'` or `'percent'`, default is `None`)",
        "If set to `'fraction'`, the value of each point is divided by the sum of all values at that location coordinate.",
        "`'percent'` is the same but multiplied by 100 to show percentages.",
    ],
    barmode=[
        "(string, one of `'group'`, `'overlay'` or `'relative'`. Default is `'relative'`)",
        "In `'relative'` mode, bars are stacked above zero for positive values and below zero for negative values.",
        "In `'overlay'` mode, bars are on drawn top of one another.",
        "In `'group'` mode, bars are placed beside each other.",
    ],
    boxmode=[
        "(string, one of `'group'` or `'overlay'`. Default is `'group'`)",
        "In `'overlay'` mode, boxes are on drawn top of one another.",
        "In `'group'` mode, baxes are placed beside each other.",
    ],
    violinmode=[
        "(string, one of `'group'` or `'overlay'`. Default is `'group'`)",
        "In `'overlay'` mode, violins are on drawn top of one another.",
        "In `'group'` mode, violins are placed beside each other.",
    ],
    stripmode=[
        "(string, one of `'group'` or `'overlay'`. Default is `'group'`)",
        "In `'overlay'` mode, strips are on drawn top of one another.",
        "In `'group'` mode, strips are placed beside each other.",
    ],
    zoom=["(integer between 0 and 20, default is 8)", "Sets map zoom level."],
    orientation=[
        "(string, one of `'h'` for horizontal or `'v'` for vertical)",
        "Default is `'v'`.",
    ],
    line_close=[
        "(boolean, default `False`)",
        "If `True`, an extra line segment is drawn between the first and last point.",
    ],
    line_shape=["(string, one of `'linear'` or `'spline'`)", "Default is `'linear'`."],
    scope=[
        "(string, one of `'world'`, `'usa'`, `'europe'`, `'asia'`, `'africa'`, `'north america'`, `'south america'`)"
        "Default is `'world'` unless `projection` is set to `'albers usa'`, which forces `'usa'`."
    ],
    projection=[
        "(string, one of `'equirectangular'`, `'mercator'`, `'orthographic'`, `'natural earth'`, `'kavrayskiy7'`, `'miller'`, `'robinson'`, `'eckert4'`, `'azimuthal equal area'`, `'azimuthal equidistant'`, `'conic equal area'`, `'conic conformal'`, `'conic equidistant'`, `'gnomonic'`, `'stereographic'`, `'mollweide'`, `'hammer'`, `'transverse mercator'`, `'albers usa'`, `'winkel tripel'`, `'aitoff'`, `'sinusoidal'`)"
        "Default depends on `scope`."
    ],
    center=["(dict with `lat` and `lon` keys)", "Sets the center point of the map."],
    points=[
        "(string or boolean, one of `'all'`, `'outliers'`, or `False`. Default is `'outliers'`)",
        "If `'outliers'`, only the sample points lying outside the whiskers are shown.",
        "If `'all'`, all sample points are shown.",
        "If `False`, no sample points are shown",
    ],
    box=[
        "(boolean, default `False`)",
        "If `True`, boxes are drawn inside the violins.",
    ],
    notched=["(boolean, default `False`)", "If `True`, boxes are drawn with notches."],
    cumulative=[
        "(boolean, default `False`)",
        "If `True`, histogram values are cumulative.",
    ],
    nbins=["(positive integer)", "Sets the number of bins."],
    nbinsx=["(positive integer)", "Sets the number of bins along the x axis."],
    nbinsy=["(positive integer)", "Sets the number of bins along the y axis."],
)


def make_docstring(fn):
    result = (fn.__doc__ or "") + "\nArguments:\n"
    for arg in inspect.getargspec(fn)[0]:
        d = (
            " ".join(docs[arg] or "")
            if arg in docs
            else "(documentation missing from map)"
        )
        result += "    %s: %s\n" % (arg, d)
    result += "Returns:\n"
    result += "    A `Figure` object."
    return result
