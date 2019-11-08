import plotly.graph_objs as go
import plotly.io as pio
from collections import namedtuple, OrderedDict

from _plotly_utils.basevalidators import ColorscaleValidator
from .colors import qualitative, sequential
import math
import pandas as pd
import numpy as np

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

MAPBOX_TOKEN = None


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
    """Populates a dict with arguments to update trace

    Parameters
    ----------
    args : dict
        args to be used for the trace
    trace_spec : NamedTuple
        which kind of trace to be used (has constructor, marginal etc.
        attributes)
    g : pandas DataFrame
        data
    mapping_labels : dict
        to be used for hovertemplate
    sizeref : float
        marker sizeref

    Returns
    -------
    result : dict
        dict to be used to update trace
    fit_results : dict
        fit information to be used for trendlines
    """
    if "line_close" in args and args["line_close"]:
        g = g.append(g.iloc[0])
    result = trace_spec.trace_patch.copy() or {}
    fit_results = None
    hover_header = ""
    custom_data_len = 0
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
                        fit_results = sm.OLS(y.values, sm.add_constant(x.values)).fit()
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
            elif k == "custom_data":
                result["customdata"] = g[v].values
                custom_data_len = len(v)  # number of custom data columns
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
                    for col in v:
                        try:
                            position = args["custom_data"].index(col)
                        except (ValueError, AttributeError, KeyError):
                            position = custom_data_len
                            custom_data_len += 1
                            if "customdata" in result:
                                result["customdata"] = np.hstack(
                                    (result["customdata"], g[col].values[:, None])
                                )
                            else:
                                result["customdata"] = g[col].values[:, None]
                        v_label_col = get_decorated_label(args, col, None)
                        mapping_labels[v_label_col] = "%%{customdata[%d]}" % (position)
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
        fig.update_yaxes(showticklabels=False, showline=False, ticks="", row=nrows)
        if args["template"].layout.yaxis.showgrid is None:
            fig.update_yaxes(showgrid=args["marginal_x"] == "histogram", row=nrows)
        if args["template"].layout.xaxis.showgrid is None:
            fig.update_xaxes(showgrid=True, row=nrows)

    if args["marginal_y"]:
        fig.update_xaxes(showticklabels=False, showline=False, ticks="", col=ncols)
        if args["template"].layout.xaxis.showgrid is None:
            fig.update_xaxes(showgrid=args["marginal_y"] == "histogram", col=ncols)
        if args["template"].layout.yaxis.showgrid is None:
            fig.update_yaxes(showgrid=True, col=ncols)

    # Add axis titles to non-marginal subplots
    y_title = get_decorated_label(args, args["y"], "y")
    if args["marginal_x"]:
        fig.update_yaxes(title_text=y_title, row=1, col=1)
    else:
        for row in range(1, nrows + 1):
            fig.update_yaxes(title_text=y_title, row=row, col=1)

    x_title = get_decorated_label(args, args["x"], "x")
    if args["marginal_y"]:
        fig.update_xaxes(title_text=x_title, row=1, col=1)
    else:
        for col in range(1, ncols + 1):
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

    try:
        # retrieve the actual template if we were given a name
        args["template"] = pio.templates[args["template"]]
    except Exception:
        # otherwise try to build a real template
        args["template"] = go.layout.Template(args["template"])

    # if colors not set explicitly or in px.defaults, defer to a template
    # if the template doesn't have one, we set some final fallback defaults
    if "color_continuous_scale" in args:
        if (
            args["color_continuous_scale"] is None
            and args["template"].layout.colorscale.sequential
        ):
            args["color_continuous_scale"] = [
                x[1] for x in args["template"].layout.colorscale.sequential
            ]
        if args["color_continuous_scale"] is None:
            args["color_continuous_scale"] = sequential.Viridis

    if "color_discrete_sequence" in args:
        if args["color_discrete_sequence"] is None and args["template"].layout.colorway:
            args["color_discrete_sequence"] = args["template"].layout.colorway
        if args["color_discrete_sequence"] is None:
            args["color_discrete_sequence"] = qualitative.D3

    # if symbol_sequence/line_dash_sequence not set explicitly or in px.defaults,
    # see if we can defer to template. If not, set reasonable defaults
    if "symbol_sequence" in args:
        if args["symbol_sequence"] is None and args["template"].data.scatter:
            args["symbol_sequence"] = [
                scatter.marker.symbol for scatter in args["template"].data.scatter
            ]
        if not args["symbol_sequence"] or not any(args["symbol_sequence"]):
            args["symbol_sequence"] = ["circle", "diamond", "square", "x", "cross"]

    if "line_dash_sequence" in args:
        if args["line_dash_sequence"] is None and args["template"].data.scatter:
            args["line_dash_sequence"] = [
                scatter.line.dash for scatter in args["template"].data.scatter
            ]
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
    if args.get("facet_col", None) is not None and args.get("marginal_y", None):
        args["marginal_y"] = None

    if args.get("facet_row", None) is not None and args.get("marginal_x", None):
        args["marginal_x"] = None


def _check_name_not_reserved(field_name, reserved_names):
    if field_name not in reserved_names:
        return field_name
    else:
        raise NameError(
            "A name conflict was encountered for argument %s. "
            "A column with name %s is already used." % (field_name, field_name)
        )


def _get_reserved_col_names(args, attrables, array_attrables):
    """
    This function builds a list of columns of the data_frame argument used
    as arguments, either as str/int arguments or given as columns
    (pandas series type).
    """
    df = args["data_frame"]
    reserved_names = set()
    for field in args:
        if field not in attrables:
            continue
        names = args[field] if field in array_attrables else [args[field]]
        if names is None:
            continue
        for arg in names:
            if arg is None:
                continue
            elif isinstance(arg, str):  # no need to add ints since kw arg are not ints
                reserved_names.add(arg)
            elif isinstance(arg, pd.Series):
                arg_name = arg.name
                if arg_name and hasattr(df, arg_name):
                    in_df = arg is df[arg_name]
                    if in_df:
                        reserved_names.add(arg_name)

    return reserved_names


def build_dataframe(args, attrables, array_attrables):
    """
    Constructs a dataframe and modifies `args` in-place.

    The argument values in `args` can be either strings corresponding to
    existing columns of a dataframe, or data arrays (lists, numpy arrays,
    pandas columns, series).

    Parameters
    ----------
    args : OrderedDict
        arguments passed to the px function and subsequently modified
    attrables : list
        list of keys into `args`, all of whose corresponding values are
        converted into columns of a dataframe.
    array_attrables : list
        argument names corresponding to iterables, such as `hover_data`, ...
    """
    for field in args:
        if field in array_attrables and args[field] is not None:
            args[field] = (
                dict(args[field])
                if isinstance(args[field], dict)
                else list(args[field])
            )
    # Cast data_frame argument to DataFrame (it could be a numpy array, dict etc.)
    df_provided = args["data_frame"] is not None
    if df_provided and not isinstance(args["data_frame"], pd.DataFrame):
        args["data_frame"] = pd.DataFrame(args["data_frame"])
    df_input = args["data_frame"]

    # We start from an empty DataFrame
    df_output = pd.DataFrame()

    # Initialize set of column names
    # These are reserved names
    if df_provided:
        reserved_names = _get_reserved_col_names(args, attrables, array_attrables)
    else:
        reserved_names = set()

    # Case of functions with a "dimensions" kw: scatter_matrix, parcats, parcoords
    if "dimensions" in args and args["dimensions"] is None:
        if not df_provided:
            raise ValueError(
                "No data were provided. Please provide data either with the `data_frame` or with the `dimensions` argument."
            )
        else:
            df_output[df_input.columns] = df_input[df_input.columns]

    # Loop over possible arguments
    for field_name in attrables:
        # Massaging variables
        argument_list = (
            [args.get(field_name)]
            if field_name not in array_attrables
            else args.get(field_name)
        )
        # argument not specified, continue
        if argument_list is None or argument_list is [None]:
            continue
        # Argument name: field_name if the argument is not a list
        # Else we give names like ["hover_data_0, hover_data_1"] etc.
        field_list = (
            [field_name]
            if field_name not in array_attrables
            else [field_name + "_" + str(i) for i in range(len(argument_list))]
        )
        # argument_list and field_list ready, iterate over them
        # Core of the loop starts here
        for i, (argument, field) in enumerate(zip(argument_list, field_list)):
            length = len(df_output)
            if argument is None:
                continue
            # Case of multiindex
            if isinstance(argument, pd.MultiIndex):
                raise TypeError(
                    "Argument '%s' is a pandas MultiIndex. "
                    "pandas MultiIndex is not supported by plotly express "
                    "at the moment." % field
                )
            # ----------------- argument is a col name ----------------------
            if isinstance(argument, str) or isinstance(
                argument, int
            ):  # just a column name given as str or int
                if not df_provided:
                    raise ValueError(
                        "String or int arguments are only possible when a "
                        "DataFrame or an array is provided in the `data_frame` "
                        "argument. No DataFrame was provided, but argument "
                        "'%s' is of type str or int." % field
                    )
                # Check validity of column name
                if argument not in df_input.columns:
                    err_msg = (
                        "Value of '%s' is not the name of a column in 'data_frame'. "
                        "Expected one of %s but received: %s"
                        % (field, str(list(df_input.columns)), argument)
                    )
                    if argument == "index":
                        err_msg += (
                            "\n To use the index, pass it in directly as `df.index`."
                        )
                    raise ValueError(err_msg)
                if length and len(df_input[argument]) != length:
                    raise ValueError(
                        "All arguments should have the same length. "
                        "The length of column argument `df[%s]` is %d, whereas the "
                        "length of previous arguments %s is %d"
                        % (
                            field,
                            len(df_input[argument]),
                            str(list(df_output.columns)),
                            length,
                        )
                    )
                col_name = str(argument)
                df_output[col_name] = df_input[argument]
            # ----------------- argument is a column / array / list.... -------
            else:
                is_index = isinstance(argument, pd.RangeIndex)
                # First pandas
                # pandas series have a name but it's None
                if (
                    hasattr(argument, "name") and argument.name is not None
                ) or is_index:
                    col_name = argument.name  # pandas df
                    if col_name is None and is_index:
                        col_name = "index"
                    if not df_provided:
                        col_name = field
                    else:
                        if is_index:
                            keep_name = df_provided and argument is df_input.index
                        else:
                            keep_name = (
                                col_name in df_input and argument is df_input[col_name]
                            )
                        col_name = (
                            col_name
                            if keep_name
                            else _check_name_not_reserved(field, reserved_names)
                        )
                else:  # numpy array, list...
                    col_name = _check_name_not_reserved(field, reserved_names)
                if length and len(argument) != length:
                    raise ValueError(
                        "All arguments should have the same length. "
                        "The length of argument `%s` is %d, whereas the "
                        "length of previous arguments %s is %d"
                        % (field, len(argument), str(list(df_output.columns)), length)
                    )
                df_output[str(col_name)] = argument

            # Finally, update argument with column name now that column exists
            if field_name not in array_attrables:
                args[field_name] = str(col_name)
            else:
                args[field_name][i] = str(col_name)

    args["data_frame"] = df_output
    return args


def infer_config(args, constructor, trace_patch):
    # Declare all supported attributes, across all plot types
    attrables = (
        ["x", "y", "z", "a", "b", "c", "r", "theta", "size", "dimensions"]
        + ["custom_data", "hover_name", "hover_data", "text"]
        + ["error_x", "error_x_minus"]
        + ["error_y", "error_y_minus", "error_z", "error_z_minus"]
        + ["lat", "lon", "locations", "animation_group"]
    )
    array_attrables = ["dimensions", "custom_data", "hover_data"]
    group_attrables = ["animation_frame", "facet_row", "facet_col", "line_group"]
    all_attrables = attrables + group_attrables + ["color"]
    group_attrs = ["symbol", "line_dash"]
    for group_attr in group_attrs:
        if group_attr in args:
            all_attrables += [group_attr]

    args = build_dataframe(args, all_attrables, array_attrables)

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

    if (
        args.get("marginal_x", None) is not None
        or args.get("marginal_y", None) is not None
        or args.get("facet_row", None) is not None
    ):
        args["facet_col_wrap"] = 0

    # Compute applicable grouping attributes
    for k in group_attrables:
        if k in args:
            grouped_attrs.append(k)

    # Create grouped mappings
    grouped_mappings = [make_mapping(args, a) for a in grouped_attrs]

    # Create trace specs
    trace_specs = make_trace_spec(args, constructor, attrs, trace_patch)
    return args, trace_specs, grouped_mappings, sizeref, show_colorbar


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

    args, trace_specs, grouped_mappings, sizeref, show_colorbar = infer_config(
        args, constructor, trace_patch
    )
    grouper = [x.grouper or one_group for x in grouped_mappings] or [one_group]
    grouped = args["data_frame"].groupby(grouper, sort=False)

    orders, sorted_group_names = get_orderings(args, grouper, grouped)

    subplot_type = _subplot_type_for_trace_type(constructor().type)

    trace_names_by_frame = {}
    frames = OrderedDict()
    trendline_rows = []
    nrows = ncols = 1
    col_labels = []
    row_labels = []
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
            # Create the trace
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
                    if args["facet_row"] and len(row_labels) < row:
                        row_labels.append(args["facet_row"] + "=" + str(val))
                else:
                    if (
                        bool(args.get("marginal_x", False))
                        and trace_spec.marginal != "x"
                    ):
                        row = 2
                    else:
                        row = 1

                facet_col_wrap = args.get("facet_col_wrap", 0)
                # Find col for trace, handling facet_col and marginal_y
                if m.facet == "col":
                    col = m.val_map[val]
                    if args["facet_col"] and len(col_labels) < col:
                        col_labels.append(args["facet_col"] + "=" + str(val))
                    if facet_col_wrap:  # assumes no facet_row, no marginals
                        row = 1 + ((col - 1) // facet_col_wrap)
                        col = 1 + ((col - 1) % facet_col_wrap)
                else:
                    if trace_spec.marginal == "y":
                        col = 2
                    else:
                        col = 1

                nrows = max(nrows, row)
                if row > 1:
                    trace._subplot_row = row

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
    for v in ["title", "height", "width"]:
        if args[v]:
            layout_patch[v] = args[v]
    layout_patch["legend"] = {"tracegroupgap": 0}
    if "title" not in layout_patch and args["template"].layout.margin.t is None:
        layout_patch["margin"] = {"t": 60}
    if (
        "size" in args
        and args["size"]
        and args["template"].layout.legend.itemsizing is None
    ):
        layout_patch["legend"]["itemsizing"] = "constant"

    fig = init_figure(
        args, subplot_type, frame_list, nrows, ncols, col_labels, row_labels
    )

    # Position traces in subplots
    for frame in frame_list:
        for trace in frame["data"]:
            if isinstance(trace, go.Splom):
                # Special case that is not compatible with make_subplots
                continue

            _set_trace_grid_reference(
                trace,
                fig.layout,
                fig._grid_ref,
                nrows - trace._subplot_row + 1,
                trace._subplot_col,
            )

    # Add traces, layout and frames to figure
    fig.add_traces(frame_list[0]["data"] if len(frame_list) > 0 else [])
    fig.layout.update(layout_patch)
    if "template" in args and args["template"] is not None:
        fig.update_layout(template=args["template"], overwrite=True)
    fig.frames = frame_list if len(frames) > 1 else []

    fig._px_trendlines = pd.DataFrame(trendline_rows)

    configure_axes(args, constructor, fig, orders)
    configure_animation_controls(args, constructor, fig)
    return fig


def init_figure(args, subplot_type, frame_list, nrows, ncols, col_labels, row_labels):
    # Build subplot specs
    specs = [[{}] * ncols for _ in range(nrows)]
    for frame in frame_list:
        for trace in frame["data"]:
            row0 = trace._subplot_row - 1
            col0 = trace._subplot_col - 1
            if isinstance(trace, go.Splom):
                # Splom not compatible with make_subplots, treat as domain
                specs[row0][col0] = {"type": "domain"}
            else:
                specs[row0][col0] = {"type": trace.type}

    # Default row/column widths uniform
    column_widths = [1.0] * ncols
    row_heights = [1.0] * nrows

    # Build column_widths/row_heights
    if subplot_type == "xy":
        if bool(args.get("marginal_x", False)):
            if args["marginal_x"] == "histogram" or ("color" in args and args["color"]):
                main_size = 0.74
            else:
                main_size = 0.84

            row_heights = [main_size] * (nrows - 1) + [1 - main_size]
            vertical_spacing = 0.01
        elif args.get("facet_col_wrap", 0):
            vertical_spacing = 0.07
        else:
            vertical_spacing = 0.03

        if bool(args.get("marginal_y", False)):
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

    facet_col_wrap = args.get("facet_col_wrap", 0)
    if facet_col_wrap:
        subplot_labels = [None] * nrows * ncols
        while len(col_labels) < nrows * ncols:
            col_labels.append(None)
        for i in range(nrows):
            for j in range(ncols):
                subplot_labels[i * ncols + j] = col_labels[(nrows - 1 - i) * ncols + j]

    # Create figure with subplots
    fig = make_subplots(
        rows=nrows,
        cols=ncols,
        specs=specs,
        shared_xaxes="all",
        shared_yaxes="all",
        row_titles=[] if facet_col_wrap else list(reversed(row_labels)),
        column_titles=[] if facet_col_wrap else col_labels,
        subplot_titles=subplot_labels if facet_col_wrap else [],
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
