import plotly.graph_objs as go
import plotly.io as pio
from collections import namedtuple, OrderedDict

from _plotly_utils.basevalidators import ColorscaleValidator
from .colors import qualitative, sequential
import math
import pandas

from plotly.subplots import (
    make_subplots,
    _set_trace_grid_reference,
    _subplot_type_for_trace_type,
)


class PxDefaults(object):
    def __init__(self):
        self.template = None
        self.width = None
        self.height = 600
        self.color_discrete_sequence = None
        self.color_continuous_scale = None
        self.symbol_sequence = None
        self.line_dash_sequence = None
        self.size_max = 20


defaults = PxDefaults()
del PxDefaults

MAPBOX_TOKEN = ""


def set_mapbox_access_token(token):
    """
    Arguments:
        token: A Mapbox token to be used in `plotly_express.scatter_mapbox` and \
        `plotly_express.line_mapbox` figures. See \
        https://docs.mapbox.com/help/how-mapbox-works/access-tokens/ for more details
    """
    global MAPBOX_TOKEN
    MAPBOX_TOKEN = token


def get_trendline_results(fig):
    """
    Extracts fit statistics for trendlines (when applied to figures generated with
    the `trendline` argument set to `"ols"`).

    Arguments:
        fig: the output of a `plotly_express` charting call
    Returns:
        A `pandas.DataFrame` with a column "px_fit_results" containing the `statsmodels`
        results objects, along with columns identifying the subset of the data the
        trendline was fit on.
    """
    return fig._px_trendlines


Mapping = namedtuple(
    "Mapping",
    [
        "show_in_trace_name",
        "grouper",
        "val_map",
        "sequence",
        "updater",
        "variable",
        "facet",
    ],
)
TraceSpec = namedtuple("TraceSpec", ["constructor", "attrs", "trace_patch", "marginal"])


def get_label(args, column):
    try:
        return args["labels"][column]
    except Exception:
        return column


def get_decorated_label(args, column, role):
    label = get_label(args, column)
    if "histfunc" in args and (
        (role == "x" and "orientation" in args and args["orientation"] == "h")
        or (role == "y" and "orientation" in args and args["orientation"] == "v")
        or (role == "z")
    ):
        if label:
            return "%s of %s" % (args["histfunc"] or "count", label)
        else:
            return "count"
    else:
        return label


def make_mapping(args, variable):
    if variable == "line_group" or variable == "animation_frame":
        return Mapping(
            show_in_trace_name=False,
            grouper=args[variable],
            val_map={},
            sequence=[""],
            variable=variable,
            updater=(lambda trace, v: v),
            facet=None,
        )
    if variable == "facet_row" or variable == "facet_col":
        letter = "x" if variable == "facet_col" else "y"
        return Mapping(
            show_in_trace_name=False,
            variable=letter,
            grouper=args[variable],
            val_map={},
            sequence=[i for i in range(1, 1000)],
            updater=(lambda trace, v: v),
            facet="row" if variable == "facet_row" else "col",
        )
    (parent, variable) = variable.split(".")
    vprefix = variable
    arg_name = variable
    if variable == "color":
        vprefix = "color_discrete"
    if variable == "dash":
        arg_name = "line_dash"
        vprefix = "line_dash"
    return Mapping(
        show_in_trace_name=True,
        variable=variable,
        grouper=args[arg_name],
        val_map=args[vprefix + "_map"].copy(),
        sequence=args[vprefix + "_sequence"],
        updater=lambda trace, v: trace.update({parent: {variable: v}}),
        facet=None,
    )


def make_trace_kwargs(args, trace_spec, g, mapping_labels, sizeref):

    if "line_close" in args and args["line_close"]:
        g = g.append(g.iloc[0])
    result = trace_spec.trace_patch.copy() or {}
    fit_results = None
    hover_header = ""
    for k in trace_spec.attrs:
        v = args[k]
        v_label = get_decorated_label(args, v, k)
        if k == "dimensions":
            dims = [
                (name, column)
                for (name, column) in g.iteritems()
                if ((not v) or (name in v))
                and (
                    trace_spec.constructor != go.Parcoords
                    or args["data_frame"][name].dtype.kind in "bifc"
                )
                and (
                    trace_spec.constructor != go.Parcats
                    or len(args["data_frame"][name].unique()) <= 20
                )
            ]
            result["dimensions"] = [
                dict(label=get_label(args, name), values=column.values)
                for (name, column) in dims
            ]
            if trace_spec.constructor == go.Splom:
                for d in result["dimensions"]:
                    d["axis"] = dict(matches=True)
                mapping_labels["%{xaxis.title.text}"] = "%{x}"
                mapping_labels["%{yaxis.title.text}"] = "%{y}"

        elif (
            v is not None
            or (trace_spec.constructor == go.Histogram and k in ["x", "y"])
            or (
                trace_spec.constructor in [go.Histogram2d, go.Histogram2dContour]
                and k == "z"
            )
        ):
            if k == "size":
                if "marker" not in result:
                    result["marker"] = dict()
                result["marker"]["size"] = g[v]
                result["marker"]["sizemode"] = "area"
                result["marker"]["sizeref"] = sizeref
                mapping_labels[v_label] = "%{marker.size}"
            elif k == "marginal_x":
                if trace_spec.constructor == go.Histogram:
                    mapping_labels["count"] = "%{y}"
            elif k == "marginal_y":
                if trace_spec.constructor == go.Histogram:
                    mapping_labels["count"] = "%{x}"
            elif k == "trendline":
                if v in ["ols", "lowess"] and args["x"] and args["y"] and len(g) > 1:
                    import statsmodels.api as sm
                    import numpy as np

                    # sorting is bad but trace_specs with "trendline" have no other attrs
                    g2 = g.sort_values(by=args["x"])
                    y = g2[args["y"]]
                    x = g2[args["x"]]
                    result["x"] = x

                    if x.dtype.type == np.datetime64:
                        x = x.astype(int) / 10 ** 9  # convert to unix epoch seconds

                    if v == "lowess":
                        trendline = sm.nonparametric.lowess(y, x)
                        result["y"] = trendline[:, 1]
                        hover_header = "<b>LOWESS trendline</b><br><br>"
                    elif v == "ols":
                        fit_results = sm.OLS(y, sm.add_constant(x)).fit()
                        result["y"] = fit_results.predict()
                        hover_header = "<b>OLS trendline</b><br>"
                        hover_header += "%s = %f * %s + %f<br>" % (
                            args["y"],
                            fit_results.params[1],
                            args["x"],
                            fit_results.params[0],
                        )
                        hover_header += (
                            "R<sup>2</sup>=%f<br><br>" % fit_results.rsquared
                        )
                    mapping_labels[get_label(args, args["x"])] = "%{x}"
                    mapping_labels[get_label(args, args["y"])] = "%{y} <b>(trend)</b>"

            elif k.startswith("error"):
                error_xy = k[:7]
                arr = "arrayminus" if k.endswith("minus") else "array"
                if error_xy not in result:
                    result[error_xy] = {}
                result[error_xy][arr] = g[v]
            elif k == "hover_name":
                if trace_spec.constructor not in [
                    go.Histogram,
                    go.Histogram2d,
                    go.Histogram2dContour,
                ]:
                    result["hovertext"] = g[v]
                    if hover_header == "":
                        hover_header = "<b>%{hovertext}</b><br><br>"
            elif k == "hover_data":
                if trace_spec.constructor not in [
                    go.Histogram,
                    go.Histogram2d,
                    go.Histogram2dContour,
                ]:
                    result["customdata"] = g[v].values
                    for i, col in enumerate(v):
                        v_label_col = get_decorated_label(args, col, None)
                        mapping_labels[v_label_col] = "%%{customdata[%d]}" % i
            elif k == "color":
                if trace_spec.constructor == go.Choropleth:
                    result["z"] = g[v]
                    result["coloraxis"] = "coloraxis1"
                    mapping_labels[v_label] = "%{z}"
                else:
                    colorable = "marker"
                    if trace_spec.constructor in [go.Parcats, go.Parcoords]:
                        colorable = "line"
                    if colorable not in result:
                        result[colorable] = dict()
                    result[colorable]["color"] = g[v]
                    result[colorable]["coloraxis"] = "coloraxis1"
                    mapping_labels[v_label] = "%%{%s.color}" % colorable
            elif k == "animation_group":
                result["ids"] = g[v]
            elif k == "locations":
                result[k] = g[v]
                mapping_labels[v_label] = "%{location}"
            else:
                if v:
                    result[k] = g[v]
                mapping_labels[v_label] = "%%{%s}" % k
    if trace_spec.constructor not in [go.Parcoords, go.Parcats]:
        hover_lines = [k + "=" + v for k, v in mapping_labels.items()]
        result["hovertemplate"] = hover_header + "<br>".join(hover_lines)
    return result, fit_results


def configure_axes(args, constructor, fig, orders):
    configurators = {
        go.Scatter: configure_cartesian_axes,
        go.Scattergl: configure_cartesian_axes,
        go.Bar: configure_cartesian_axes,
        go.Box: configure_cartesian_axes,
        go.Violin: configure_cartesian_axes,
        go.Histogram: configure_cartesian_axes,
        go.Histogram2dContour: configure_cartesian_axes,
        go.Histogram2d: configure_cartesian_axes,
        go.Scatter3d: configure_3d_axes,
        go.Scatterternary: configure_ternary_axes,
        go.Scatterpolar: configure_polar_axes,
        go.Scatterpolargl: configure_polar_axes,
        go.Barpolar: configure_polar_axes,
        go.Scattermapbox: configure_mapbox,
        go.Scattergeo: configure_geo,
        go.Choropleth: configure_geo,
    }
    if constructor in configurators:
        configurators[constructor](args, fig, orders)


def set_cartesian_axis_opts(args, axis, letter, orders):
    log_key = "log_" + letter
    range_key = "range_" + letter
    if log_key in args and args[log_key]:
        axis["type"] = "log"
        if range_key in args and args[range_key]:
            axis["range"] = [math.log(r, 10) for r in args[range_key]]
    elif range_key in args and args[range_key]:
        axis["range"] = args[range_key]

    if args[letter] in orders:
        axis["categoryorder"] = "array"
        axis["categoryarray"] = (
            orders[args[letter]]
            if isinstance(axis, go.layout.XAxis)
            else list(reversed(orders[args[letter]]))
        )


def configure_cartesian_marginal_axes(args, fig, orders):

    if "histogram" in [args["marginal_x"], args["marginal_y"]]:
        fig.layout["barmode"] = "overlay"

    nrows = len(fig._grid_ref)
    ncols = len(fig._grid_ref[0])

    # Set y-axis titles and axis options in the left-most column
    for yaxis in fig.select_yaxes(col=1):
        set_cartesian_axis_opts(args, yaxis, "y", orders)

    # Set x-axis titles and axis options in the bottom-most row
    for xaxis in fig.select_xaxes(row=1):
        set_cartesian_axis_opts(args, xaxis, "x", orders)

    # Configure axis ticks on marginal subplots
    if args["marginal_x"]:
        fig.update_yaxes(
            showticklabels=False, showgrid=args["marginal_x"] == "histogram", row=nrows
        )
        fig.update_xaxes(showgrid=True, row=nrows)

    if args["marginal_y"]:
        fig.update_xaxes(
            showticklabels=False, showgrid=args["marginal_y"] == "histogram", col=ncols
        )
        fig.update_yaxes(showgrid=True, col=ncols)

    # Add axis titles to non-marginal subplots
    y_title = get_decorated_label(args, args["y"], "y")
    for row in range(1, nrows):
        fig.update_yaxes(title_text=y_title, row=row, col=1)

    x_title = get_decorated_label(args, args["x"], "x")
    for col in range(1, ncols):
        fig.update_xaxes(title_text=x_title, row=1, col=col)

    # Configure axis type across all x-axes
    if "log_x" in args and args["log_x"]:
        fig.update_xaxes(type="log")

    # Configure axis type across all y-axes
    if "log_y" in args and args["log_y"]:
        fig.update_yaxes(type="log")

    # Configure matching and axis type for marginal y-axes
    matches_y = "y" + str(ncols + 1)
    if args["marginal_x"]:
        for row in range(2, nrows + 1, 2):
            fig.update_yaxes(matches=matches_y, type=None, row=row)

    if args["marginal_y"]:
        for col in range(2, ncols + 1, 2):
            fig.update_xaxes(matches="x2", type=None, col=col)


def configure_cartesian_axes(args, fig, orders):
    if ("marginal_x" in args and args["marginal_x"]) or (
        "marginal_y" in args and args["marginal_y"]
    ):
        configure_cartesian_marginal_axes(args, fig, orders)
        return

    # Set y-axis titles and axis options in the left-most column
    y_title = get_decorated_label(args, args["y"], "y")
    for yaxis in fig.select_yaxes(col=1):
        yaxis.update(title_text=y_title)
        set_cartesian_axis_opts(args, yaxis, "y", orders)

    # Set x-axis titles and axis options in the bottom-most row
    x_title = get_decorated_label(args, args["x"], "x")
    for xaxis in fig.select_xaxes(row=1):
        xaxis.update(title_text=x_title)
        set_cartesian_axis_opts(args, xaxis, "x", orders)

    # Configure axis type across all x-axes
    if "log_x" in args and args["log_x"]:
        fig.update_xaxes(type="log")

    # Configure axis type across all y-axes
    if "log_y" in args and args["log_y"]:
        fig.update_yaxes(type="log")

    return fig.layout


def configure_ternary_axes(args, fig, orders):
    fig.update(
        layout=dict(
            ternary=dict(
                aaxis=dict(title=get_label(args, args["a"])),
                baxis=dict(title=get_label(args, args["b"])),
                caxis=dict(title=get_label(args, args["c"])),
            )
        )
    )


def configure_polar_axes(args, fig, orders):
    layout = dict(
        polar=dict(
            angularaxis=dict(direction=args["direction"], rotation=args["start_angle"]),
            radialaxis=dict(),
        )
    )

    for var, axis in [("r", "radialaxis"), ("theta", "angularaxis")]:
        if args[var] in orders:
            layout["polar"][axis]["categoryorder"] = "array"
            layout["polar"][axis]["categoryarray"] = orders[args[var]]

    radialaxis = layout["polar"]["radialaxis"]
    if args["log_r"]:
        radialaxis["type"] = "log"
        if args["range_r"]:
            radialaxis["range"] = [math.log(x, 10) for x in args["range_r"]]
    else:
        if args["range_r"]:
            radialaxis["range"] = args["range_r"]
    fig.update(layout=layout)


def configure_3d_axes(args, fig, orders):
    layout = dict(
        scene=dict(
            xaxis=dict(title=get_label(args, args["x"])),
            yaxis=dict(title=get_label(args, args["y"])),
            zaxis=dict(title=get_label(args, args["z"])),
        )
    )

    for letter in ["x", "y", "z"]:
        axis = layout["scene"][letter + "axis"]
        if args["log_" + letter]:
            axis["type"] = "log"
            if args["range_" + letter]:
                axis["range"] = [math.log(x, 10) for x in args["range_" + letter]]
        else:
            if args["range_" + letter]:
                axis["range"] = args["range_" + letter]
        if args[letter] in orders:
            axis["categoryorder"] = "array"
            axis["categoryarray"] = orders[args[letter]]
    fig.update(layout=layout)


def configure_mapbox(args, fig, orders):
    fig.update(
        layout=dict(
            mapbox=dict(
                accesstoken=MAPBOX_TOKEN,
                center=dict(
                    lat=args["data_frame"][args["lat"]].mean(),
                    lon=args["data_frame"][args["lon"]].mean(),
                ),
                zoom=args["zoom"],
            )
        )
    )


def configure_geo(args, fig, orders):
    fig.update(
        layout=dict(
            geo=dict(
                center=args["center"],
                scope=args["scope"],
                projection=dict(type=args["projection"]),
            )
        )
    )


def configure_animation_controls(args, constructor, fig):
    def frame_args(duration):
        return {
            "frame": {"duration": duration, "redraw": constructor != go.Scatter},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": duration, "easing": "linear"},
        }

    if "animation_frame" in args and args["animation_frame"] and len(fig.frames) > 1:
        fig.layout.updatemenus = [
            {
                "buttons": [
                    {
                        "args": [None, frame_args(500)],
                        "label": "&#9654;",
                        "method": "animate",
                    },
                    {
                        "args": [[None], frame_args(0)],
                        "label": "&#9724;",
                        "method": "animate",
                    },
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 70},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top",
            }
        ]
        fig.layout.sliders = [
            {
                "active": 0,
                "yanchor": "top",
                "xanchor": "left",
                "currentvalue": {
                    "prefix": get_label(args, args["animation_frame"]) + "="
                },
                "pad": {"b": 10, "t": 60},
                "len": 0.9,
                "x": 0.1,
                "y": 0,
                "steps": [
                    {
                        "args": [[f.name], frame_args(0)],
                        "label": f.name,
                        "method": "animate",
                    }
                    for f in fig.frames
                ],
            }
        ]


def make_trace_spec(args, constructor, attrs, trace_patch):
    # Create base trace specification
    result = [TraceSpec(constructor, attrs, trace_patch, None)]

    # Add marginal trace specifications
    for letter in ["x", "y"]:
        if "marginal_" + letter in args and args["marginal_" + letter]:
            trace_spec = None
            axis_map = dict(
                xaxis="x1" if letter == "x" else "x2",
                yaxis="y1" if letter == "y" else "y2",
            )
            if args["marginal_" + letter] == "histogram":
                trace_spec = TraceSpec(
                    constructor=go.Histogram,
                    attrs=[letter, "marginal_" + letter],
                    trace_patch=dict(opacity=0.5, bingroup=letter, **axis_map),
                    marginal=letter,
                )
            elif args["marginal_" + letter] == "violin":
                trace_spec = TraceSpec(
                    constructor=go.Violin,
                    attrs=[letter, "hover_name", "hover_data"],
                    trace_patch=dict(scalegroup=letter),
                    marginal=letter,
                )
            elif args["marginal_" + letter] == "box":
                trace_spec = TraceSpec(
                    constructor=go.Box,
                    attrs=[letter, "hover_name", "hover_data"],
                    trace_patch=dict(notched=True),
                    marginal=letter,
                )
            elif args["marginal_" + letter] == "rug":
                symbols = {"x": "line-ns-open", "y": "line-ew-open"}
                trace_spec = TraceSpec(
                    constructor=go.Box,
                    attrs=[letter, "hover_name", "hover_data"],
                    trace_patch=dict(
                        fillcolor="rgba(255,255,255,0)",
                        line={"color": "rgba(255,255,255,0)"},
                        boxpoints="all",
                        jitter=0,
                        hoveron="points",
                        marker={"symbol": symbols[letter]},
                    ),
                    marginal=letter,
                )
            if "color" in attrs or "color" not in args:
                if "marker" not in trace_spec.trace_patch:
                    trace_spec.trace_patch["marker"] = dict()
                first_default_color = args["color_continuous_scale"][0]
                trace_spec.trace_patch["marker"]["color"] = first_default_color
            result.append(trace_spec)

    # Add trendline trace specifications
    if "trendline" in args and args["trendline"]:
        trace_spec = TraceSpec(
            constructor=go.Scatter,
            attrs=["trendline"],
            trace_patch=dict(mode="lines"),
            marginal=None,
        )
        if args["trendline_color_override"]:
            trace_spec.trace_patch["line"] = dict(
                color=args["trendline_color_override"]
            )
        result.append(trace_spec)
    return result


def one_group(x):
    return ""


def apply_default_cascade(args):
    # first we apply px.defaults to unspecified args
    for param in (
        ["color_discrete_sequence", "color_continuous_scale"]
        + ["symbol_sequence", "line_dash_sequence", "template"]
        + ["width", "height", "size_max"]
    ):
        if param in args and args[param] is None:
            args[param] = getattr(defaults, param)

    # load the default template if set, otherwise "plotly"
    if args["template"] is None:
        if pio.templates.default is not None:
            args["template"] = pio.templates.default
        else:
            args["template"] = "plotly"

    # retrieve the actual template if we were given a name
    try:
        template = pio.templates[args["template"]]
    except Exception:
        template = args["template"]

    # if colors not set explicitly or in px.defaults, defer to a template
    # if the template doesn't have one, we set some final fallback defaults
    if "color_continuous_scale" in args:
        if args["color_continuous_scale"] is None:
            try:
                args["color_continuous_scale"] = [
                    x[1] for x in template.layout.colorscale.sequential
                ]
            except (AttributeError, TypeError):
                pass
        if args["color_continuous_scale"] is None:
            args["color_continuous_scale"] = sequential.Viridis

    if "color_discrete_sequence" in args:
        if args["color_discrete_sequence"] is None:
            try:
                args["color_discrete_sequence"] = template.layout.colorway
            except (AttributeError, TypeError):
                pass
        if args["color_discrete_sequence"] is None:
            args["color_discrete_sequence"] = qualitative.D3

    # if symbol_sequence/line_dash_sequence not set explicitly or in px.defaults,
    # see if we can defer to template. If not, set reasonable defaults
    if "symbol_sequence" in args:
        if args["symbol_sequence"] is None:
            try:
                args["symbol_sequence"] = [
                    scatter.marker.symbol for scatter in template.data.scatter
                ]
            except (AttributeError, TypeError):
                pass
        if not args["symbol_sequence"] or not any(args["symbol_sequence"]):
            args["symbol_sequence"] = ["circle", "diamond", "square", "x", "cross"]

    if "line_dash_sequence" in args:
        if args["line_dash_sequence"] is None:
            try:
                args["line_dash_sequence"] = [
                    scatter.line.dash for scatter in template.data.scatter
                ]
            except (AttributeError, TypeError):
                pass
        if not args["line_dash_sequence"] or not any(args["line_dash_sequence"]):
            args["line_dash_sequence"] = [
                "solid",
                "dot",
                "dash",
                "longdash",
                "dashdot",
                "longdashdot",
            ]

    # If both marginals and faceting are specified, faceting wins
    if args.get("facet_col", None) and args.get("marginal_y", None):
        args["marginal_y"] = None

    if args.get("facet_row", None) and args.get("marginal_x", None):
        args["marginal_x"] = None


def infer_config(args, constructor, trace_patch):
    # Declare all supported attributes, across all plot types
    attrables = (
        ["x", "y", "z", "a", "b", "c", "r", "theta", "size"]
        + ["dimensions", "hover_name", "hover_data", "text", "error_x", "error_x_minus"]
        + ["error_y", "error_y_minus", "error_z", "error_z_minus"]
        + ["lat", "lon", "locations", "animation_group"]
    )
    array_attrables = ["dimensions", "hover_data"]
    group_attrables = ["animation_frame", "facet_row", "facet_col", "line_group"]

    # Validate that the strings provided as attribute values reference columns
    # in the provided data_frame
    df_columns = args["data_frame"].columns

    for attr in attrables + group_attrables + ["color"]:
        if attr in args and args[attr] is not None:
            maybe_col_list = [args[attr]] if attr not in array_attrables else args[attr]
            for maybe_col in maybe_col_list:
                try:
                    in_cols = maybe_col in df_columns
                except TypeError:
                    in_cols = False
                if not in_cols:
                    value_str = (
                        "Element of value" if attr in array_attrables else "Value"
                    )
                    raise ValueError(
                        "%s of '%s' is not the name of a column in 'data_frame'. "
                        "Expected one of %s but received: %s"
                        % (value_str, attr, str(list(df_columns)), str(maybe_col))
                    )

    attrs = [k for k in attrables if k in args]
    grouped_attrs = []

    # Compute sizeref
    sizeref = 0
    if "size" in args and args["size"]:
        sizeref = args["data_frame"][args["size"]].max() / args["size_max"] ** 2

    # Compute color attributes and grouping attributes
    if "color" in args:
        if "color_continuous_scale" in args:
            if "color_discrete_sequence" not in args:
                attrs.append("color")
            else:
                if (
                    args["color"]
                    and args["data_frame"][args["color"]].dtype.kind in "bifc"
                ):
                    attrs.append("color")
                else:
                    grouped_attrs.append("marker.color")
        elif "line_group" in args or constructor == go.Histogram2dContour:
            grouped_attrs.append("line.color")
        else:
            grouped_attrs.append("marker.color")

        show_colorbar = bool("color" in attrs and args["color"])

    # Compute line_dash grouping attribute
    if "line_dash" in args:
        grouped_attrs.append("line.dash")

    # Compute symbol grouping attribute
    if "symbol" in args:
        grouped_attrs.append("marker.symbol")

    # Compute final trace patch
    trace_patch = trace_patch.copy()

    if constructor == go.Histogram2d:
        show_colorbar = True
        trace_patch["coloraxis"] = "coloraxis1"

    if "opacity" in args:
        if args["opacity"] is None:
            if "barmode" in args and args["barmode"] == "overlay":
                trace_patch["marker"] = dict(opacity=0.5)
        else:
            trace_patch["marker"] = dict(opacity=args["opacity"])
    if "line_group" in args:
        trace_patch["mode"] = "lines" + ("+markers+text" if args["text"] else "")
    elif constructor != go.Splom and (
        "symbol" in args or constructor == go.Scattermapbox
    ):
        trace_patch["mode"] = "markers" + ("+text" if args["text"] else "")

    if "line_shape" in args:
        trace_patch["line"] = dict(shape=args["line_shape"])

    # Compute marginal attribute
    if "marginal" in args:
        position = "marginal_x" if args["orientation"] == "v" else "marginal_y"
        other_position = "marginal_x" if args["orientation"] == "h" else "marginal_y"
        args[position] = args["marginal"]
        args[other_position] = None

    # Compute applicable grouping attributes
    for k in group_attrables:
        if k in args:
            grouped_attrs.append(k)

    # Create grouped mappings
    grouped_mappings = [make_mapping(args, a) for a in grouped_attrs]

    # Create trace specs
    trace_specs = make_trace_spec(args, constructor, attrs, trace_patch)
    return trace_specs, grouped_mappings, sizeref, show_colorbar


def get_orderings(args, grouper, grouped):
    """
    `orders` is the user-supplied ordering (with the remaining data-frame-supplied
    ordering appended if the column is used for grouping)
    `group_names` is the set of groups, ordered by the order above
    """
    orders = {} if "category_orders" not in args else args["category_orders"].copy()
    group_names = []
    for group_name in grouped.groups:
        if len(grouper) == 1:
            group_name = (group_name,)
        group_names.append(group_name)
        for col in grouper:
            if col != one_group:
                uniques = args["data_frame"][col].unique()
                if col not in orders:
                    orders[col] = list(uniques)
                else:
                    for val in uniques:
                        if val not in orders[col]:
                            orders[col].append(val)

    for i, col in reversed(list(enumerate(grouper))):
        if col != one_group:
            group_names = sorted(
                group_names,
                key=lambda g: orders[col].index(g[i]) if g[i] in orders[col] else -1,
            )

    return orders, group_names


def make_figure(args, constructor, trace_patch={}, layout_patch={}):
    apply_default_cascade(args)

    trace_specs, grouped_mappings, sizeref, show_colorbar = infer_config(
        args, constructor, trace_patch
    )
    grouper = [x.grouper or one_group for x in grouped_mappings] or [one_group]
    grouped = args["data_frame"].groupby(grouper, sort=False)

    orders, sorted_group_names = get_orderings(args, grouper, grouped)

    has_marginal_x = bool(args.get("marginal_x", False))
    has_marginal_y = bool(args.get("marginal_y", False))

    subplot_type = _subplot_type_for_trace_type(constructor().type)

    trace_names_by_frame = {}
    frames = OrderedDict()
    trendline_rows = []
    nrows = ncols = 1
    for group_name in sorted_group_names:
        group = grouped.get_group(group_name if len(group_name) > 1 else group_name[0])
        mapping_labels = OrderedDict()
        trace_name_labels = OrderedDict()
        frame_name = ""
        for col, val, m in zip(grouper, group_name, grouped_mappings):
            if col != one_group:
                key = get_label(args, col)
                mapping_labels[key] = str(val)
                if m.show_in_trace_name:
                    trace_name_labels[key] = str(val)
                if m.variable == "animation_frame":
                    frame_name = val
        trace_name = ", ".join(k + "=" + v for k, v in trace_name_labels.items())
        if frame_name not in trace_names_by_frame:
            trace_names_by_frame[frame_name] = set()
        trace_names = trace_names_by_frame[frame_name]

        for trace_spec in trace_specs:
            constructor_to_use = trace_spec.constructor
            if constructor_to_use in [go.Scatter, go.Scatterpolar]:
                if "render_mode" in args and (
                    args["render_mode"] == "webgl"
                    or (
                        args["render_mode"] == "auto"
                        and len(args["data_frame"]) > 1000
                        and args["animation_frame"] is None
                    )
                ):
                    constructor_to_use = (
                        go.Scattergl
                        if constructor_to_use == go.Scatter
                        else go.Scatterpolargl
                    )
            trace = constructor_to_use(name=trace_name)
            if trace_spec.constructor not in [
                go.Parcats,
                go.Parcoords,
                go.Choropleth,
                go.Histogram2d,
            ]:
                trace.update(
                    legendgroup=trace_name,
                    showlegend=(trace_name != "" and trace_name not in trace_names),
                )
            if trace_spec.constructor in [go.Bar, go.Violin, go.Box, go.Histogram]:
                trace.update(alignmentgroup=True, offsetgroup=trace_name)
            if trace_spec.constructor not in [go.Parcats, go.Parcoords]:
                trace.update(hoverlabel=dict(namelength=0))
            trace_names.add(trace_name)

            # Init subplot row/col
            trace._subplot_row = 1
            trace._subplot_col = 1

            for i, m in enumerate(grouped_mappings):
                val = group_name[i]
                if val not in m.val_map:
                    m.val_map[val] = m.sequence[len(m.val_map) % len(m.sequence)]
                try:
                    m.updater(trace, m.val_map[val])
                except ValueError:
                    if (
                        trace_spec != trace_specs[0]
                        and trace_spec.constructor in [go.Violin, go.Box, go.Histogram]
                        and m.variable == "symbol"
                    ):
                        pass
                    elif (
                        trace_spec != trace_specs[0]
                        and trace_spec.constructor in [go.Histogram]
                        and m.variable == "color"
                    ):
                        trace.update(marker=dict(color=m.val_map[val]))
                    else:
                        raise

                # Find row for trace, handling facet_row and marginal_x
                if m.facet == "row":
                    row = m.val_map[val]
                    trace._subplot_row_val = val
                else:
                    if trace_spec.marginal == "x":
                        row = 2
                    else:
                        row = 1

                nrows = max(nrows, row)
                if row > 1:
                    trace._subplot_row = row

                # Find col for trace, handling facet_col and marginal_y
                if m.facet == "col":
                    col = m.val_map[val]
                    trace._subplot_col_val = val
                else:
                    if trace_spec.marginal == "y":
                        col = 2
                    else:
                        col = 1

                ncols = max(ncols, col)
                if col > 1:
                    trace._subplot_col = col
            if (
                trace_specs[0].constructor == go.Histogram2dContour
                and trace_spec.constructor == go.Box
                and trace.line.color
            ):
                trace.update(marker=dict(color=trace.line.color))

            patch, fit_results = make_trace_kwargs(
                args, trace_spec, group, mapping_labels.copy(), sizeref
            )
            trace.update(patch)
            if fit_results is not None:
                trendline_rows.append(mapping_labels.copy())
                trendline_rows[-1]["px_fit_results"] = fit_results
            if frame_name not in frames:
                frames[frame_name] = dict(data=[], name=frame_name)
            frames[frame_name]["data"].append(trace)
    frame_list = [f for f in frames.values()]
    if len(frame_list) > 1:
        frame_list = sorted(
            frame_list, key=lambda f: orders[args["animation_frame"]].index(f["name"])
        )
    layout_patch = layout_patch.copy()
    if show_colorbar:
        colorvar = "z" if constructor == go.Histogram2d else "color"
        range_color = args["range_color"] or [None, None]
        d = len(args["color_continuous_scale"]) - 1

        colorscale_validator = ColorscaleValidator("colorscale", "make_figure")
        layout_patch["coloraxis1"] = dict(
            colorscale=colorscale_validator.validate_coerce(
                args["color_continuous_scale"]
            ),
            cmid=args["color_continuous_midpoint"],
            cmin=range_color[0],
            cmax=range_color[1],
            colorbar=dict(title=get_decorated_label(args, args[colorvar], colorvar)),
        )
    for v in ["title", "height", "width", "template"]:
        if args[v]:
            layout_patch[v] = args[v]
    layout_patch["legend"] = {"tracegroupgap": 0}
    if "title" not in layout_patch:
        layout_patch["margin"] = {"t": 60}
    if "size" in args and args["size"]:
        layout_patch["legend"]["itemsizing"] = "constant"

    fig = init_figure(
        args, subplot_type, frame_list, ncols, nrows, has_marginal_x, has_marginal_y
    )

    # Position traces in subplots
    for frame in frame_list:
        for trace in frame["data"]:
            if isinstance(trace, go.Splom):
                # Special case that is not compatible with make_subplots
                continue

            _set_trace_grid_reference(
                trace, fig.layout, fig._grid_ref, trace._subplot_row, trace._subplot_col
            )

    # Add traces, layout and frames to figure
    fig.add_traces(frame_list[0]["data"] if len(frame_list) > 0 else [])
    fig.layout.update(layout_patch)
    fig.frames = frame_list if len(frames) > 1 else []

    fig._px_trendlines = pandas.DataFrame(trendline_rows)

    configure_axes(args, constructor, fig, orders)
    configure_animation_controls(args, constructor, fig)
    return fig


def init_figure(
    args, subplot_type, frame_list, ncols, nrows, has_marginal_x, has_marginal_y
):
    # Build subplot specs
    specs = [[{}] * ncols for _ in range(nrows)]
    column_titles = [None] * ncols
    row_titles = [None] * nrows
    for frame in frame_list:
        for trace in frame["data"]:
            row0 = nrows - trace._subplot_row
            col0 = trace._subplot_col - 1

            if isinstance(trace, go.Splom):
                # Splom not compatible with make_subplots, treat as domain
                specs[row0][col0] = {"type": "domain"}
            else:
                specs[row0][col0] = {"type": trace.type}
            if args.get("facet_row", None) and hasattr(trace, "_subplot_row_val"):
                row_titles[row0] = args["facet_row"] + "=" + str(trace._subplot_row_val)

            if args.get("facet_col", None) and hasattr(trace, "_subplot_col_val"):
                column_titles[col0] = (
                    args["facet_col"] + "=" + str(trace._subplot_col_val)
                )

    # Default row/column widths uniform
    column_widths = [1.0] * ncols
    row_heights = [1.0] * nrows

    # Build column_widths/row_heights
    if subplot_type == "xy":
        if has_marginal_x:
            if args["marginal_x"] == "histogram" or ("color" in args and args["color"]):
                main_size = 0.74
            else:
                main_size = 0.84

            row_heights = [main_size] * (nrows - 1) + [1 - main_size]
            vertical_spacing = 0.01
        else:
            vertical_spacing = 0.03

        if has_marginal_y:
            if args["marginal_y"] == "histogram" or ("color" in args and args["color"]):
                main_size = 0.74
            else:
                main_size = 0.84

            column_widths = [main_size] * (ncols - 1) + [1 - main_size]
            horizontal_spacing = 0.005
        else:
            horizontal_spacing = 0.02
    else:
        # Other subplot types:
        #   'scene', 'geo', 'polar', 'ternary', 'mapbox', 'domain', None
        #
        # We can customize subplot spacing per type once we enable faceting
        # for all plot types
        vertical_spacing = 0.1
        horizontal_spacing = 0.1

    # Create figure with subplots
    fig = make_subplots(
        rows=nrows,
        cols=ncols,
        specs=specs,
        shared_xaxes="all",
        shared_yaxes="all",
        row_titles=row_titles,
        column_titles=column_titles,
        horizontal_spacing=horizontal_spacing,
        vertical_spacing=vertical_spacing,
        row_heights=row_heights,
        column_widths=column_widths,
        start_cell="bottom-left",
    )

    # Remove explicit font size of row/col titles so template can take over
    for annot in fig.layout.annotations:
        annot.update(font=None)

    return fig
