import inspect
from textwrap import TextWrapper


# TODO contents of columns
# TODO explain categorical
# TODO handle color
# TODO handle details of box/violin/histogram
# TODO handle details of column selection with `dimensions`
# TODO document "or `None`, default `None`" in various places
# TODO standardize positioning and casing of 'default'

colref_type = "str or int or Series or array-like"
colref_desc = "Either a name of a column in `data_frame`, or a pandas Series or array_like object."
colref_list_type = "list of str or int, or Series or array-like"
colref_list_desc = (
    "Either names of columns in `data_frame`, or pandas Series, or array_like objects"
)

docs = dict(
    data_frame=[
        "DataFrame or array-like or dict",
        "This argument needs to be passed for column names (and not keyword names) to be used.",
        "Array-like and dict are tranformed internally to a pandas DataFrame.",
        "Optional: if missing, a DataFrame gets constructed under the hood using the other arguments.",
    ],
    x=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks along the x axis in cartesian coordinates.",
        "For horizontal histograms, these values are used as inputs to `histfunc`.",
    ],
    y=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks along the y axis in cartesian coordinates.",
        "For vertical histograms, these values are used as inputs to `histfunc`.",
    ],
    z=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks along the z axis in cartesian coordinates.",
        "For `density_heatmap` and `density_contour` these values are used as the inputs to `histfunc`.",
    ],
    a=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks along the a axis in ternary coordinates.",
    ],
    b=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks along the b axis in ternary coordinates.",
    ],
    c=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks along the c axis in ternary coordinates.",
    ],
    r=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks along the radial axis in polar coordinates.",
    ],
    theta=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks along the angular axis in polar coordinates.",
    ],
    values=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to set values associated to sectors.",
    ],
    parents=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used as parents in sunburst and treemap charts.",
    ],
    ids=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to set ids of sectors",
    ],
    lat=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks according to latitude on a map.",
    ],
    lon=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to position marks according to longitude on a map.",
    ],
    locations=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are to be interpreted according to `locationmode` and mapped to longitude/latitude.",
    ],
    dimensions=[
        colref_list_type,
        colref_list_desc,
        "Values from these columns are used for multidimensional visualization.",
    ],
    error_x=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to size x-axis error bars.",
        "If `error_x_minus` is `None`, error bars will be symmetrical, otherwise `error_x` is used for the positive direction only.",
    ],
    error_x_minus=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to size x-axis error bars in the negative direction.",
        "Ignored if `error_x` is `None`.",
    ],
    error_y=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to size y-axis error bars.",
        "If `error_y_minus` is `None`, error bars will be symmetrical, otherwise `error_y` is used for the positive direction only.",
    ],
    error_y_minus=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to size y-axis error bars in the negative direction.",
        "Ignored if `error_y` is `None`.",
    ],
    error_z=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to size z-axis error bars.",
        "If `error_z_minus` is `None`, error bars will be symmetrical, otherwise `error_z` is used for the positive direction only.",
    ],
    error_z_minus=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to size z-axis error bars in the negative direction.",
        "Ignored if `error_z` is `None`.",
    ],
    color=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to assign color to marks.",
    ],
    opacity=["float", "Value between 0 and 1. Sets the opacity for markers."],
    line_dash=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to assign dash-patterns to lines.",
    ],
    line_group=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to group rows of `data_frame` into lines.",
    ],
    symbol=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to assign symbols to marks.",
    ],
    size=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to assign mark sizes.",
    ],
    radius=["int (default is 30)", "Sets the radius of influence of each point.",],
    hover_name=[
        colref_type,
        colref_desc,
        "Values from this column or array_like appear in bold in the hover tooltip.",
    ],
    hover_data=[
        colref_list_type,
        colref_list_desc,
        "Values from these columns appear as extra data in the hover tooltip.",
    ],
    custom_data=[
        colref_list_type,
        colref_list_desc,
        "Values from these columns are extra data, to be used in widgets or Dash callbacks for example. This data is not user-visible but is included in events emitted by the figure (lasso selection etc.)",
    ],
    text=[
        colref_type,
        colref_desc,
        "Values from this column or array_like appear in the figure as text labels.",
    ],
    names=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used as labels for sectors.",
    ],
    locationmode=[
        "str",
        "One of 'ISO-3', 'USA-states', or 'country names'",
        "Determines the set of locations used to match entries in `locations` to regions on the map.",
    ],
    facet_row=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to assign marks to facetted subplots in the vertical direction.",
    ],
    facet_col=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to assign marks to facetted subplots in the horizontal direction.",
    ],
    facet_col_wrap=[
        "int",
        "Maximum number of facet columns.",
        "Wraps the column variable at this width, so that the column facets span multiple rows.",
        "Ignored if 0, and forced to 0 if `facet_row` or a `marginal` is set.",
    ],
    animation_frame=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to assign marks to animation frames.",
    ],
    animation_group=[
        colref_type,
        colref_desc,
        "Values from this column or array_like are used to provide object-constancy across animation frames: rows with matching `animation_group`s will be treated as if they describe the same object in each frame.",
    ],
    symbol_sequence=[
        "list of str",
        "Strings should define valid plotly.js symbols.",
        "When `symbol` is set, values in that column are assigned symbols by cycling through `symbol_sequence` in the order described in `category_orders`, unless the value of `symbol` is a key in `symbol_map`.",
    ],
    symbol_map=[
        "dict with str keys and str values (default `{}`)",
        "String values should define plotly.js symbols",
        "Used to override `symbol_sequence` to assign a specific symbols to marks corresponding with specific values.",
        "Keys in `symbol_map` should be values in the column denoted by `symbol`.",
    ],
    line_dash_map=[
        "dict with str keys and str values (default `{}`)",
        "Strings values define plotly.js dash-patterns.",
        "Used to override `line_dash_sequences` to assign a specific dash-patterns to lines corresponding with specific values.",
        "Keys in `line_dash_map` should be values in the column denoted by `line_dash`.",
    ],
    line_dash_sequence=[
        "list of str",
        "Strings should define valid plotly.js dash-patterns.",
        "When `line_dash` is set, values in that column are assigned dash-patterns by cycling through `line_dash_sequence` in the order described in `category_orders`, unless the value of `line_dash` is a key in `line_dash_map`.",
    ],
    color_discrete_sequence=[
        "list of str",
        "Strings should define valid CSS-colors.",
        "When `color` is set and the values in the corresponding column are not numeric, values in that column are assigned colors by cycling through `color_discrete_sequence` in the order described in `category_orders`, unless the value of `color` is a key in `color_discrete_map`.",
        "Various useful color sequences are available in the `plotly_express.colors` submodules, specifically `plotly_express.colors.qualitative`.",
    ],
    color_discrete_map=[
        "dict with str keys and str values (default `{}`)",
        "String values should define valid CSS-colors",
        "Used to override `color_discrete_sequence` to assign a specific colors to marks corresponding with specific values.",
        "Keys in `color_discrete_map` should be values in the column denoted by `color`.",
    ],
    color_continuous_scale=[
        "list of str",
        "Strings should define valid CSS-colors",
        "This list is used to build a continuous color scale when the column denoted by `color` contains numeric data.",
        "Various useful color scales are available in the `plotly_express.colors` submodules, specifically `plotly_express.colors.sequential`, `plotly_express.colors.diverging` and `plotly_express.colors.cyclical`.",
    ],
    color_continuous_midpoint=[
        "number (default `None`)",
        "If set, computes the bounds of the continuous color scale to have the desired midpoint.",
        "Setting this value is recommended when using `plotly_express.colors.diverging` color scales as the inputs to `color_continuous_scale`.",
    ],
    size_max=["int (default `20`)", "Set the maximum mark size when using `size`."],
    log_x=[
        "boolean (default `False`)",
        "If `True`, the x-axis is log-scaled in cartesian coordinates.",
    ],
    log_y=[
        "boolean (default `False`)",
        "If `True`, the y-axis is log-scaled in cartesian coordinates.",
    ],
    log_z=[
        "boolean (default `False`)",
        "If `True`, the z-axis is log-scaled in cartesian coordinates.",
    ],
    log_r=[
        "boolean (default `False`)",
        "If `True`, the radial axis is log-scaled in polar coordinates.",
    ],
    range_x=[
        "list of two numbers",
        "If provided, overrides auto-scaling on the x-axis in cartesian coordinates.",
    ],
    range_y=[
        "list of two numbers",
        "If provided, overrides auto-scaling on the y-axis in cartesian coordinates.",
    ],
    range_z=[
        "list of two numbers",
        "If provided, overrides auto-scaling on the z-axis in cartesian coordinates.",
    ],
    range_color=[
        "list of two numbers",
        "If provided, overrides auto-scaling on the continuous color scale.",
    ],
    range_r=[
        "list of two numbers",
        "If provided, overrides auto-scaling on the radial axis in polar coordinates.",
    ],
    range_theta=[
        "list of two numbers",
        "If provided, overrides auto-scaling on the angular axis in polar coordinates.",
    ],
    title=["str", "The figure title."],
    template=[
        "or dict or plotly.graph_objects.layout.Template instance",
        "The figure template name or definition.",
    ],
    width=["int (default `None`)", "The figure width in pixels."],
    height=["int (default `600`)", "The figure height in pixels."],
    labels=[
        "dict with str keys and str values (default `{}`)",
        "By default, column names are used in the figure for axis titles, legend entries and hovers.",
        "This parameter allows this to be overridden.",
        "The keys of this dict should correspond to column names, and the values should correspond to the desired label to be displayed.",
    ],
    category_orders=[
        "dict with str keys and list of str values (default `{}`)",
        "By default, in Python 3.6+, the order of categorical values in axes, legends and facets depends on the order in which these values are first encountered in `data_frame` (and no order is guaranteed by default in Python below 3.6).",
        "This parameter is used to force a specific ordering of values per column.",
        "The keys of this dict should correspond to column names, and the values should be lists of strings corresponding to the specific display order desired.",
    ],
    marginal=[
        "str",
        "One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`.",
        "If set, a subplot is drawn alongside the main plot, visualizing the distribution.",
    ],
    marginal_x=[
        "str",
        "One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`.",
        "If set, a horizontal subplot is drawn above the main plot, visualizing the x-distribution.",
    ],
    marginal_y=[
        "str",
        "One of `'rug'`, `'box'`, `'violin'`, or `'histogram'`.",
        "If set, a vertical subplot is drawn to the right of the main plot, visualizing the y-distribution.",
    ],
    trendline=[
        "str",
        "One of `'ols'` or `'lowess'`.",
        "If `'ols'`, an Ordinary Least Squares regression line will be drawn for each discrete-color/symbol group.",
        "If `'lowess`', a Locally Weighted Scatterplot Smoothing line will be drawn for each discrete-color/symbol group.",
    ],
    trendline_color_override=[
        "str",
        "Valid CSS color.",
        "If provided, and if `trendline` is set, all trendlines will be drawn in this color.",
    ],
    render_mode=[
        "str",
        "One of `'auto'`, `'svg'` or `'webgl'`, default `'auto'`",
        "Controls the browser API used to draw marks.",
        "`'svg`' is appropriate for figures of less than 1000 data points, and will allow for fully-vectorized output.",
        "`'webgl'` is likely necessary for acceptable performance above 1000 points but rasterizes part of the output. ",
        "`'auto'` uses heuristics to choose the mode.",
    ],
    direction=[
        "str",
        "One of '`counterclockwise'` or `'clockwise'`. Default is `'clockwise'`",
        "Sets the direction in which increasing values of the angular axis are drawn.",
    ],
    start_angle=[
        "int (default `90`)",
        "Sets start angle for the angular axis, with 0 being due east and 90 being due north.",
    ],
    histfunc=[
        "str (default `'count'`)",
        "One of `'count'`, `'sum'`, `'avg'`, `'min'`, or `'max'`."
        "Function used to aggregate values for summarization (note: can be normalized with `histnorm`).",
        "The arguments to this function for `histogram` are the values of `y` if `orientation` is `'v'`,",
        "otherwise the arguements are the values of `x`.",
        "The arguments to this function for `density_heatmap` and `density_contour` are the values of `z`.",
    ],
    histnorm=[
        "str (default `None`)",
        "One of `'percent'`, `'probability'`, `'density'`, or `'probability density'`",
        "If `None`, the output of `histfunc` is used as is.",
        "If `'probability'`, the output of `histfunc` for a given bin is divided by the sum of the output of `histfunc` for all bins.",
        "If `'percent'`, the output of `histfunc` for a given bin is divided by the sum of the output of `histfunc` for all bins and multiplied by 100.",
        "If `'density'`, the output of `histfunc` for a given bin is divided by the size of the bin.",
        "If `'probability density'`, the output of `histfunc` for a given bin is normalized such that it corresponds to the probability that a random event whose distribution is described by the output of `histfunc` will fall into that bin.",
    ],
    barnorm=[
        "str (default `None`)",
        "One of `'fraction'` or `'percent'`.",
        "If `'fraction'`, the value of each bar is divided by the sum of all values at that location coordinate.",
        "`'percent'` is the same but multiplied by 100 to show percentages.",
        "`None` will stack up all values at each location coordinate.",
    ],
    groupnorm=[
        "str (default `None`)",
        "One of `'fraction'` or `'percent'`.",
        "If `'fraction'`, the value of each point is divided by the sum of all values at that location coordinate.",
        "`'percent'` is the same but multiplied by 100 to show percentages.",
        "`None` will stack up all values at each location coordinate.",
    ],
    barmode=[
        "str (default `'relative'`)",
        "One of `'group'`, `'overlay'` or `'relative'`",
        "In `'relative'` mode, bars are stacked above zero for positive values and below zero for negative values.",
        "In `'overlay'` mode, bars are drawn on top of one another.",
        "In `'group'` mode, bars are placed beside each other.",
    ],
    boxmode=[
        "str (default `'group'`)",
        "One of `'group'` or `'overlay'`",
        "In `'overlay'` mode, boxes are on drawn top of one another.",
        "In `'group'` mode, baxes are placed beside each other.",
    ],
    violinmode=[
        "str (default `'group'`)",
        "One of `'group'` or `'overlay'`",
        "In `'overlay'` mode, violins are on drawn top of one another.",
        "In `'group'` mode, violins are placed beside each other.",
    ],
    stripmode=[
        "str (default `'group'`)",
        "One of `'group'` or `'overlay'`",
        "In `'overlay'` mode, strips are on drawn top of one another.",
        "In `'group'` mode, strips are placed beside each other.",
    ],
    zoom=["int (default `8`)", "Between 0 and 20.", "Sets map zoom level."],
    orientation=[
        "str (default `'v'`)",
        "One of `'h'` for horizontal or `'v'` for vertical)",
    ],
    line_close=[
        "boolean (default `False`)",
        "If `True`, an extra line segment is drawn between the first and last point.",
    ],
    line_shape=["str (default `'linear'`)", "One of `'linear'` or `'spline'`."],
    scope=[
        "str (default `'world'`).",
        "One of `'world'`, `'usa'`, `'europe'`, `'asia'`, `'africa'`, `'north america'`, or `'south america'`)"
        "Default is `'world'` unless `projection` is set to `'albers usa'`, which forces `'usa'`.",
    ],
    projection=[
        "str ",
        "One of `'equirectangular'`, `'mercator'`, `'orthographic'`, `'natural earth'`, `'kavrayskiy7'`, `'miller'`, `'robinson'`, `'eckert4'`, `'azimuthal equal area'`, `'azimuthal equidistant'`, `'conic equal area'`, `'conic conformal'`, `'conic equidistant'`, `'gnomonic'`, `'stereographic'`, `'mollweide'`, `'hammer'`, `'transverse mercator'`, `'albers usa'`, `'winkel tripel'`, `'aitoff'`, or `'sinusoidal'`"
        "Default depends on `scope`.",
    ],
    center=[
        "dict",
        "Dict keys are `'lat'` and `'lon'`",
        "Sets the center point of the map.",
    ],
    mapbox_style=[
        "str (default `'basic'`, needs Mapbox API token)",
        "Identifier of base map style, some of which require a Mapbox API token to be set using `plotly.express.set_mapbox_access_token()`.",
        "Allowed values which do not require a Mapbox API token are `'open-street-map'`, `'white-bg'`, `'carto-positron'`, `'carto-darkmatter'`, `'stamen-terrain'`, `'stamen-toner'`, `'stamen-watercolor'`.",
        "Allowed values which do require a Mapbox API token are `'basic'`, `'streets'`, `'outdoors'`, `'light'`, `'dark'`, `'satellite'`, `'satellite-streets'`.",
    ],
    points=[
        "str or boolean (default `'outliers'`)",
        "One of `'outliers'`, `'suspectedoutliers'`, `'all'`, or `False`.",
        "If `'outliers'`, only the sample points lying outside the whiskers are shown.",
        "If `'suspectedoutliers'`, all outlier points are shown and those less than 4*Q1-3*Q3 or greater than 4*Q3-3*Q1 are highlighted with the marker's `'outliercolor'`.",
        "If `'outliers'`, only the sample points lying outside the whiskers are shown.",
        "If `'all'`, all sample points are shown.",
        "If `False`, no sample points are shown and the whiskers extend to the full range of the sample.",
    ],
    box=["boolean (default `False`)", "If `True`, boxes are drawn inside the violins."],
    notched=["boolean (default `False`)", "If `True`, boxes are drawn with notches."],
    geojson=[
        "GeoJSON-formatted dict",
        "Must contain a Polygon feature collection, with IDs, which are references from `locations`.",
    ],
    cumulative=[
        "boolean (default `False`)",
        "If `True`, histogram values are cumulative.",
    ],
    nbins=["int", "Positive integer.", "Sets the number of bins."],
    nbinsx=["int", "Positive integer.", "Sets the number of bins along the x axis."],
    nbinsy=["int", "Positive integer.", "Sets the number of bins along the y axis."],
    branchvalues=[
        "str",
        "'total' or 'remainder'",
        "Determines how the items in `values` are summed. When"
        "set to 'total', items in `values` are taken to be value"
        "of all its descendants. When set to 'remainder', items"
        "in `values` corresponding to the root and the branches"
        ":sectors are taken to be the extra part not part of the"
        "sum of the values at their leaves.",
    ],
    maxdepth=[
        "int",
        "Positive integer",
        "Sets the number of rendered sectors from any given `level`. Set `maxdepth` to -1 to render all the"
        "levels in the hierarchy.",
    ],
)


def make_docstring(fn, override_dict={}):
    tw = TextWrapper(width=75, initial_indent="    ", subsequent_indent="    ")
    result = (fn.__doc__ or "") + "\nParameters\n----------\n"
    for param in inspect.getargspec(fn)[0]:
        if override_dict.get(param):
            param_doc = override_dict[param]
        else:
            param_doc = docs[param]
        param_desc_list = param_doc[1:]
        param_desc = (
            tw.fill(" ".join(param_desc_list or ""))
            if param in docs
            else "(documentation missing from map)"
        )

        param_type = param_doc[0]
        result += "%s: %s\n%s\n" % (param, param_type, param_desc)
    result += "\nReturns\n-------\n"
    result += "    A `Figure` object."
    return result
