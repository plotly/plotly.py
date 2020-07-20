import plotly.graph_objs as go
import plotly.io as pio
from collections import namedtuple, OrderedDict
from ._special_inputs import IdentityMap, Constant, Range

from _plotly_utils.basevalidators import ColorscaleValidator
from plotly.colors import qualitative, sequential
import math
import pandas as pd
import numpy as np

from plotly.subplots import (
    make_subplots,
    _set_trace_grid_reference,
    _subplot_type_for_trace_type,
)

NO_COLOR = "px_no_color_constant"

# Declare all supported attributes, across all plot types
direct_attrables = (
    ["base", "x", "y", "z", "a", "b", "c", "r", "theta", "size", "x_start", "x_end"]
    + ["hover_name", "text", "names", "values", "parents", "wide_cross"]
    + ["ids", "error_x", "error_x_minus", "error_y", "error_y_minus", "error_z"]
    + ["error_z_minus", "lat", "lon", "locations", "animation_group"]
)
array_attrables = ["dimensions", "custom_data", "hover_data", "path", "wide_variable"]
group_attrables = ["animation_frame", "facet_row", "facet_col", "line_group"]
renameable_group_attrables = [
    "color",  # renamed to marker.color or line.color in infer_config
    "symbol",  # renamed to marker.symbol in infer_config
    "line_dash",  # renamed to line.dash in infer_config
]
all_attrables = (
    direct_attrables + array_attrables + group_attrables + renameable_group_attrables
)

cartesians = [go.Scatter, go.Scattergl, go.Bar, go.Funnel, go.Box, go.Violin]
cartesians += [go.Histogram, go.Histogram2d, go.Histogram2dContour]


class PxDefaults(object):
    __slots__ = [
        "template",
        "width",
        "height",
        "color_discrete_sequence",
        "color_continuous_scale",
        "symbol_sequence",
        "line_dash_sequence",
        "size_max",
    ]

    def __init__(self):
        self.template = None
        self.width = None
        self.height = None
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
        token: A Mapbox token to be used in `plotly.express.scatter_mapbox` and \
        `plotly.express.line_mapbox` figures. See \
        https://docs.mapbox.com/help/how-mapbox-works/access-tokens/ for more details
    """
    global MAPBOX_TOKEN
    MAPBOX_TOKEN = token


def get_trendline_results(fig):
    """
    Extracts fit statistics for trendlines (when applied to figures generated with
    the `trendline` argument set to `"ols"`).

    Arguments:
        fig: the output of a `plotly.express` charting call
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


def invert_label(args, column):
    """Invert mapping.
    Find key corresponding to value column in dict args["labels"].
    Returns `column` if the value does not exist.
    """
    reversed_labels = {value: key for (key, value) in args["labels"].items()}
    try:
        return reversed_labels[column]
    except Exception:
        return column


def _is_continuous(df, col_name):
    return df[col_name].dtype.kind in "ifc"


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
    if args[vprefix + "_map"] == "identity":
        val_map = IdentityMap()
    else:
        val_map = args[vprefix + "_map"].copy()
    return Mapping(
        show_in_trace_name=True,
        variable=variable,
        grouper=args[arg_name],
        val_map=val_map,
        sequence=args[vprefix + "_sequence"],
        updater=lambda trace, v: trace.update({parent: {variable: v}}),
        facet=None,
    )


def make_trace_kwargs(args, trace_spec, trace_data, mapping_labels, sizeref):
    """Populates a dict with arguments to update trace

    Parameters
    ----------
    args : dict
        args to be used for the trace
    trace_spec : NamedTuple
        which kind of trace to be used (has constructor, marginal etc.
        attributes)
    trace_data : pandas DataFrame
        data
    mapping_labels : dict
        to be used for hovertemplate
    sizeref : float
        marker sizeref

    Returns
    -------
    trace_patch : dict
        dict to be used to update trace
    fit_results : dict
        fit information to be used for trendlines
    """
    if "line_close" in args and args["line_close"]:
        trace_data = trace_data.append(trace_data.iloc[0])
    trace_patch = trace_spec.trace_patch.copy() or {}
    fit_results = None
    hover_header = ""
    custom_data_len = 0
    for attr_name in trace_spec.attrs:
        attr_value = args[attr_name]
        attr_label = get_decorated_label(args, attr_value, attr_name)
        if attr_name == "dimensions":
            dims = [
                (name, column)
                for (name, column) in trace_data.iteritems()
                if ((not attr_value) or (name in attr_value))
                and (
                    trace_spec.constructor != go.Parcoords
                    or _is_continuous(args["data_frame"], name)
                )
                and (
                    trace_spec.constructor != go.Parcats
                    or (attr_value is not None and name in attr_value)
                    or len(args["data_frame"][name].unique())
                    <= args["dimensions_max_cardinality"]
                )
            ]
            trace_patch["dimensions"] = [
                dict(label=get_label(args, name), values=column.values)
                for (name, column) in dims
            ]
            if trace_spec.constructor == go.Splom:
                for d in trace_patch["dimensions"]:
                    d["axis"] = dict(matches=True)
                mapping_labels["%{xaxis.title.text}"] = "%{x}"
                mapping_labels["%{yaxis.title.text}"] = "%{y}"

        elif (
            attr_value is not None
            or (trace_spec.constructor == go.Histogram and attr_name in ["x", "y"])
            or (
                trace_spec.constructor in [go.Histogram2d, go.Histogram2dContour]
                and attr_name == "z"
            )
        ):
            if attr_name == "size":
                if "marker" not in trace_patch:
                    trace_patch["marker"] = dict()
                trace_patch["marker"]["size"] = trace_data[attr_value]
                trace_patch["marker"]["sizemode"] = "area"
                trace_patch["marker"]["sizeref"] = sizeref
                mapping_labels[attr_label] = "%{marker.size}"
            elif attr_name == "marginal_x":
                if trace_spec.constructor == go.Histogram:
                    mapping_labels["count"] = "%{y}"
            elif attr_name == "marginal_y":
                if trace_spec.constructor == go.Histogram:
                    mapping_labels["count"] = "%{x}"
            elif attr_name == "trendline":
                if (
                    attr_value in ["ols", "lowess"]
                    and args["x"]
                    and args["y"]
                    and len(trace_data[[args["x"], args["y"]]].dropna()) > 1
                ):
                    import statsmodels.api as sm

                    # sorting is bad but trace_specs with "trendline" have no other attrs
                    sorted_trace_data = trace_data.sort_values(by=args["x"])
                    y = sorted_trace_data[args["y"]].values
                    x = sorted_trace_data[args["x"]].values

                    x_is_date = False
                    if x.dtype.type == np.datetime64:
                        x = x.astype(int) / 10 ** 9  # convert to unix epoch seconds
                        x_is_date = True
                    elif x.dtype.type == np.object_:
                        try:
                            x = x.astype(np.float64)
                        except ValueError:
                            raise ValueError(
                                "Could not convert value of 'x' ('%s') into a numeric type. "
                                "If 'x' contains stringified dates, please convert to a datetime column."
                                % args["x"]
                            )
                    if y.dtype.type == np.object_:
                        try:
                            y = y.astype(np.float64)
                        except ValueError:
                            raise ValueError(
                                "Could not convert value of 'y' into a numeric type."
                            )

                    if attr_value == "lowess":
                        # missing ='drop' is the default value for lowess but not for OLS (None)
                        # we force it here in case statsmodels change their defaults
                        trendline = sm.nonparametric.lowess(y, x, missing="drop")
                        trace_patch["x"] = trendline[:, 0]
                        trace_patch["y"] = trendline[:, 1]
                        hover_header = "<b>LOWESS trendline</b><br><br>"
                    elif attr_value == "ols":
                        fit_results = sm.OLS(
                            y, sm.add_constant(x), missing="drop"
                        ).fit()
                        trace_patch["y"] = fit_results.predict()
                        trace_patch["x"] = x[
                            np.logical_not(np.logical_or(np.isnan(y), np.isnan(x)))
                        ]
                        hover_header = "<b>OLS trendline</b><br>"
                        if len(fit_results.params) == 2:
                            hover_header += "%s = %g * %s + %g<br>" % (
                                args["y"],
                                fit_results.params[1],
                                args["x"],
                                fit_results.params[0],
                            )
                        else:
                            hover_header += "%s = %g<br>" % (
                                args["y"],
                                fit_results.params[0],
                            )
                        hover_header += (
                            "R<sup>2</sup>=%f<br><br>" % fit_results.rsquared
                        )
                    if x_is_date:
                        trace_patch["x"] = pd.to_datetime(trace_patch["x"] * 10 ** 9)
                    mapping_labels[get_label(args, args["x"])] = "%{x}"
                    mapping_labels[get_label(args, args["y"])] = "%{y} <b>(trend)</b>"
            elif attr_name.startswith("error"):
                error_xy = attr_name[:7]
                arr = "arrayminus" if attr_name.endswith("minus") else "array"
                if error_xy not in trace_patch:
                    trace_patch[error_xy] = {}
                trace_patch[error_xy][arr] = trace_data[attr_value]
            elif attr_name == "custom_data":
                trace_patch["customdata"] = trace_data[attr_value].values
                custom_data_len = len(attr_value)  # number of custom data columns
            elif attr_name == "hover_name":
                if trace_spec.constructor not in [
                    go.Histogram,
                    go.Histogram2d,
                    go.Histogram2dContour,
                ]:
                    trace_patch["hovertext"] = trace_data[attr_value]
                    if hover_header == "":
                        hover_header = "<b>%{hovertext}</b><br><br>"
            elif attr_name == "hover_data":
                if trace_spec.constructor not in [
                    go.Histogram,
                    go.Histogram2d,
                    go.Histogram2dContour,
                ]:
                    hover_is_dict = isinstance(attr_value, dict)
                    for col in attr_value:
                        if hover_is_dict and not attr_value[col]:
                            continue
                        try:
                            position = args["custom_data"].index(col)
                        except (ValueError, AttributeError, KeyError):
                            position = custom_data_len
                            custom_data_len += 1
                            if "customdata" in trace_patch:
                                trace_patch["customdata"] = np.hstack(
                                    (
                                        trace_patch["customdata"],
                                        trace_data[col].values[:, None],
                                    )
                                )
                            else:
                                trace_patch["customdata"] = trace_data[col].values[
                                    :, None
                                ]
                        attr_label_col = get_decorated_label(args, col, None)
                        mapping_labels[attr_label_col] = "%%{customdata[%d]}" % (
                            position
                        )
            elif attr_name == "color":
                if trace_spec.constructor in [go.Choropleth, go.Choroplethmapbox]:
                    trace_patch["z"] = trace_data[attr_value]
                    trace_patch["coloraxis"] = "coloraxis1"
                    mapping_labels[attr_label] = "%{z}"
                elif trace_spec.constructor in [
                    go.Sunburst,
                    go.Treemap,
                    go.Pie,
                    go.Funnelarea,
                ]:
                    if "marker" not in trace_patch:
                        trace_patch["marker"] = dict()

                    if args.get("color_is_continuous"):
                        trace_patch["marker"]["colors"] = trace_data[attr_value]
                        trace_patch["marker"]["coloraxis"] = "coloraxis1"
                        mapping_labels[attr_label] = "%{color}"
                    else:
                        trace_patch["marker"]["colors"] = []
                        if args["color_discrete_map"] is not None:
                            mapping = args["color_discrete_map"].copy()
                        else:
                            mapping = {}
                        for cat in trace_data[attr_value]:
                            if mapping.get(cat) is None:
                                mapping[cat] = args["color_discrete_sequence"][
                                    len(mapping) % len(args["color_discrete_sequence"])
                                ]
                            trace_patch["marker"]["colors"].append(mapping[cat])
                else:
                    colorable = "marker"
                    if trace_spec.constructor in [go.Parcats, go.Parcoords]:
                        colorable = "line"
                    if colorable not in trace_patch:
                        trace_patch[colorable] = dict()
                    trace_patch[colorable]["color"] = trace_data[attr_value]
                    trace_patch[colorable]["coloraxis"] = "coloraxis1"
                    mapping_labels[attr_label] = "%%{%s.color}" % colorable
            elif attr_name == "animation_group":
                trace_patch["ids"] = trace_data[attr_value]
            elif attr_name == "locations":
                trace_patch[attr_name] = trace_data[attr_value]
                mapping_labels[attr_label] = "%{location}"
            elif attr_name == "values":
                trace_patch[attr_name] = trace_data[attr_value]
                _label = "value" if attr_label == "values" else attr_label
                mapping_labels[_label] = "%{value}"
            elif attr_name == "parents":
                trace_patch[attr_name] = trace_data[attr_value]
                _label = "parent" if attr_label == "parents" else attr_label
                mapping_labels[_label] = "%{parent}"
            elif attr_name == "ids":
                trace_patch[attr_name] = trace_data[attr_value]
                _label = "id" if attr_label == "ids" else attr_label
                mapping_labels[_label] = "%{id}"
            elif attr_name == "names":
                if trace_spec.constructor in [
                    go.Sunburst,
                    go.Treemap,
                    go.Pie,
                    go.Funnelarea,
                ]:
                    trace_patch["labels"] = trace_data[attr_value]
                    _label = "label" if attr_label == "names" else attr_label
                    mapping_labels[_label] = "%{label}"
                else:
                    trace_patch[attr_name] = trace_data[attr_value]
            else:
                if attr_value:
                    trace_patch[attr_name] = trace_data[attr_value]
                mapping_labels[attr_label] = "%%{%s}" % attr_name
    if trace_spec.constructor not in [
        go.Parcoords,
        go.Parcats,
    ]:
        # Modify mapping_labels according to hover_data keys
        # if hover_data is a dict
        mapping_labels_copy = OrderedDict(mapping_labels)
        if args["hover_data"] and isinstance(args["hover_data"], dict):
            for k, v in mapping_labels.items():
                # We need to invert the mapping here
                k_args = invert_label(args, k)
                if k_args in args["hover_data"]:
                    formatter = args["hover_data"][k_args][0]
                    if formatter:
                        if isinstance(formatter, str):
                            mapping_labels_copy[k] = v.replace("}", "%s}" % formatter)
                    else:
                        _ = mapping_labels_copy.pop(k)
        hover_lines = [k + "=" + v for k, v in mapping_labels_copy.items()]
        trace_patch["hovertemplate"] = hover_header + "<br>".join(hover_lines)
        trace_patch["hovertemplate"] += "<extra></extra>"
    return trace_patch, fit_results


def configure_axes(args, constructor, fig, orders):
    configurators = {
        go.Scatter3d: configure_3d_axes,
        go.Scatterternary: configure_ternary_axes,
        go.Scatterpolar: configure_polar_axes,
        go.Scatterpolargl: configure_polar_axes,
        go.Barpolar: configure_polar_axes,
        go.Scattermapbox: configure_mapbox,
        go.Choroplethmapbox: configure_mapbox,
        go.Densitymapbox: configure_mapbox,
        go.Scattergeo: configure_geo,
        go.Choropleth: configure_geo,
    }
    for c in cartesians:
        configurators[c] = configure_cartesian_axes
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
            showticklabels=False, showline=False, ticks="", range=None, row=nrows
        )
        if args["template"].layout.yaxis.showgrid is None:
            fig.update_yaxes(showgrid=args["marginal_x"] == "histogram", row=nrows)
        if args["template"].layout.xaxis.showgrid is None:
            fig.update_xaxes(showgrid=True, row=nrows)

    if args["marginal_y"]:
        fig.update_xaxes(
            showticklabels=False, showline=False, ticks="", range=None, col=ncols
        )
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
        if "is_timeline" not in args:
            xaxis.update(title_text=x_title)
        set_cartesian_axis_opts(args, xaxis, "x", orders)

    # Configure axis type across all x-axes
    if "log_x" in args and args["log_x"]:
        fig.update_xaxes(type="log")

    # Configure axis type across all y-axes
    if "log_y" in args and args["log_y"]:
        fig.update_yaxes(type="log")

    if "is_timeline" in args:
        fig.update_xaxes(type="date")

    return fig.layout


def configure_ternary_axes(args, fig, orders):
    fig.update_layout(
        ternary=dict(
            aaxis=dict(title_text=get_label(args, args["a"])),
            baxis=dict(title_text=get_label(args, args["b"])),
            caxis=dict(title_text=get_label(args, args["c"])),
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

    if args["range_theta"]:
        layout["polar"]["sector"] = args["range_theta"]
    fig.update(layout=layout)


def configure_3d_axes(args, fig, orders):
    layout = dict(
        scene=dict(
            xaxis=dict(title_text=get_label(args, args["x"])),
            yaxis=dict(title_text=get_label(args, args["y"])),
            zaxis=dict(title_text=get_label(args, args["z"])),
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
    center = args["center"]
    if not center and "lat" in args and "lon" in args:
        center = dict(
            lat=args["data_frame"][args["lat"]].mean(),
            lon=args["data_frame"][args["lon"]].mean(),
        )
    fig.update_layout(
        mapbox=dict(
            accesstoken=MAPBOX_TOKEN,
            center=center,
            zoom=args["zoom"],
            style=args["mapbox_style"],
        )
    )


def configure_geo(args, fig, orders):
    fig.update_layout(
        geo=dict(
            center=args["center"],
            scope=args["scope"],
            projection=dict(type=args["projection"]),
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
    if constructor in [go.Scatter, go.Scatterpolar]:
        if "render_mode" in args and (
            args["render_mode"] == "webgl"
            or (
                args["render_mode"] == "auto"
                and len(args["data_frame"]) > 1000
                and args["animation_frame"] is None
            )
        ):
            if constructor == go.Scatter:
                constructor = go.Scattergl
                if "orientation" in trace_patch:
                    del trace_patch["orientation"]
            else:
                constructor = go.Scatterpolargl
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
            constructor=go.Scattergl if constructor == go.Scattergl else go.Scatter,
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
            "A name conflict was encountered for argument '%s'. "
            "A column or index with name '%s' is ambiguous." % (field_name, field_name)
        )


def _get_reserved_col_names(args):
    """
    This function builds a list of columns of the data_frame argument used
    as arguments, either as str/int arguments or given as columns
    (pandas series type).
    """
    df = args["data_frame"]
    reserved_names = set()
    for field in args:
        if field not in all_attrables:
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
            elif arg is df.index and arg.name is not None:
                reserved_names.add(arg.name)

    return reserved_names


def _is_col_list(df_input, arg):
    """Returns True if arg looks like it's a list of columns or references to columns
    in df_input, and False otherwise (in which case it's assumed to be a single column
    or reference to a column).
    """
    if arg is None or isinstance(arg, str) or isinstance(arg, int):
        return False
    if isinstance(arg, pd.MultiIndex):
        return False  # just to keep existing behaviour for now
    try:
        iter(arg)
    except TypeError:
        return False  # not iterable
    for c in arg:
        if isinstance(c, str) or isinstance(c, int):
            if df_input is None or c not in df_input.columns:
                return False
        else:
            try:
                iter(c)
            except TypeError:
                return False  # not iterable
    return True


def _isinstance_listlike(x):
    """Returns True if x is an iterable which can be transformed into a pandas Series,
    False for the other types of possible values of a `hover_data` dict.
    A tuple of length 2 is a special case corresponding to a (format, data) tuple.
    """
    if (
        isinstance(x, str)
        or (isinstance(x, tuple) and len(x) == 2)
        or isinstance(x, bool)
        or x is None
    ):
        return False
    else:
        return True


def _escape_col_name(df_input, col_name, extra):
    while df_input is not None and (col_name in df_input.columns or col_name in extra):
        col_name = "_" + col_name
    return col_name


def process_args_into_dataframe(args, wide_mode, var_name, value_name):
    """
    After this function runs, the `all_attrables` keys of `args` all contain only
    references to columns of `df_output`. This function handles the extraction of data
    from `args["attrable"]` and column-name-generation as appropriate, and adds the
    data to `df_output` and then replaces `args["attrable"]` with the appropriate
    reference.
    """

    df_input = args["data_frame"]
    df_provided = df_input is not None

    df_output = pd.DataFrame()
    constants = dict()
    ranges = list()
    wide_id_vars = set()
    reserved_names = _get_reserved_col_names(args) if df_provided else set()

    # Case of functions with a "dimensions" kw: scatter_matrix, parcats, parcoords
    if "dimensions" in args and args["dimensions"] is None:
        if not df_provided:
            raise ValueError(
                "No data were provided. Please provide data either with the `data_frame` or with the `dimensions` argument."
            )
        else:
            df_output[df_input.columns] = df_input[df_input.columns]

    # hover_data is a dict
    hover_data_is_dict = (
        "hover_data" in args
        and args["hover_data"]
        and isinstance(args["hover_data"], dict)
    )
    # If dict, convert all values of hover_data to tuples to simplify processing
    if hover_data_is_dict:
        for k in args["hover_data"]:
            if _isinstance_listlike(args["hover_data"][k]):
                args["hover_data"][k] = (True, args["hover_data"][k])
            if not isinstance(args["hover_data"][k], tuple):
                args["hover_data"][k] = (args["hover_data"][k], None)
            if df_provided and args["hover_data"][k][1] is not None and k in df_input:
                raise ValueError(
                    "Ambiguous input: values for '%s' appear both in hover_data and data_frame"
                    % k
                )
    # Loop over possible arguments
    for field_name in all_attrables:
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
            col_name = None
            # Case of multiindex
            if isinstance(argument, pd.MultiIndex):
                raise TypeError(
                    "Argument '%s' is a pandas MultiIndex. "
                    "pandas MultiIndex is not supported by plotly express "
                    "at the moment." % field
                )
            # ----------------- argument is a special value ----------------------
            if isinstance(argument, Constant) or isinstance(argument, Range):
                col_name = _check_name_not_reserved(
                    str(argument.label) if argument.label is not None else field,
                    reserved_names,
                )
                if isinstance(argument, Constant):
                    constants[col_name] = argument.value
                else:
                    ranges.append(col_name)
            # ----------------- argument is likely a col name ----------------------
            elif isinstance(argument, str) or not hasattr(argument, "__len__"):
                if (
                    field_name == "hover_data"
                    and hover_data_is_dict
                    and args["hover_data"][str(argument)][1] is not None
                ):
                    # hover_data has onboard data
                    # previously-checked to have no name-conflict with data_frame
                    col_name = str(argument)
                    real_argument = args["hover_data"][col_name][1]

                    if length and len(real_argument) != length:
                        raise ValueError(
                            "All arguments should have the same length. "
                            "The length of hover_data key `%s` is %d, whereas the "
                            "length of previously-processed arguments %s is %d"
                            % (
                                argument,
                                len(real_argument),
                                str(list(df_output.columns)),
                                length,
                            )
                        )
                    if hasattr(real_argument, "values"):
                        df_output[col_name] = real_argument.values
                    else:
                        df_output[col_name] = np.array(real_argument)
                elif not df_provided:
                    raise ValueError(
                        "String or int arguments are only possible when a "
                        "DataFrame or an array is provided in the `data_frame` "
                        "argument. No DataFrame was provided, but argument "
                        "'%s' is of type str or int." % field
                    )
                # Check validity of column name
                elif argument not in df_input.columns:
                    if wide_mode and argument in (value_name, var_name):
                        continue
                    else:
                        err_msg = (
                            "Value of '%s' is not the name of a column in 'data_frame'. "
                            "Expected one of %s but received: %s"
                            % (field, str(list(df_input.columns)), argument)
                        )
                        if argument == "index":
                            err_msg += "\n To use the index, pass it in directly as `df.index`."
                        raise ValueError(err_msg)
                elif length and len(df_input[argument]) != length:
                    raise ValueError(
                        "All arguments should have the same length. "
                        "The length of column argument `df[%s]` is %d, whereas the "
                        "length of  previously-processed arguments %s is %d"
                        % (
                            field,
                            len(df_input[argument]),
                            str(list(df_output.columns)),
                            length,
                        )
                    )
                else:
                    col_name = str(argument)
                    df_output[col_name] = df_input[argument].values
            # ----------------- argument is likely a column / array / list.... -------
            else:
                if df_provided and hasattr(argument, "name"):
                    if argument is df_input.index:
                        if argument.name is None or argument.name in df_input:
                            col_name = "index"
                        else:
                            col_name = argument.name
                        col_name = _escape_col_name(
                            df_input, col_name, [var_name, value_name]
                        )
                    else:
                        if (
                            argument.name is not None
                            and argument.name in df_input
                            and argument is df_input[argument.name]
                        ):
                            col_name = argument.name
                if col_name is None:  # numpy array, list...
                    col_name = _check_name_not_reserved(field, reserved_names)

                if length and len(argument) != length:
                    raise ValueError(
                        "All arguments should have the same length. "
                        "The length of argument `%s` is %d, whereas the "
                        "length of  previously-processed arguments %s is %d"
                        % (field, len(argument), str(list(df_output.columns)), length)
                    )
                if hasattr(argument, "values"):
                    df_output[str(col_name)] = argument.values
                else:
                    df_output[str(col_name)] = np.array(argument)

            # Finally, update argument with column name now that column exists
            assert col_name is not None, (
                "Data-frame processing failure, likely due to a internal bug. "
                "Please report this to "
                "https://github.com/plotly/plotly.py/issues/new and we will try to "
                "replicate and fix it."
            )
            if field_name not in array_attrables:
                args[field_name] = str(col_name)
            elif isinstance(args[field_name], dict):
                pass
            else:
                args[field_name][i] = str(col_name)
            if field_name != "wide_variable":
                wide_id_vars.add(str(col_name))

    for col_name in ranges:
        df_output[col_name] = range(len(df_output))

    for col_name in constants:
        df_output[col_name] = constants[col_name]

    return df_output, wide_id_vars


def build_dataframe(args, constructor):
    """
    Constructs a dataframe and modifies `args` in-place.

    The argument values in `args` can be either strings corresponding to
    existing columns of a dataframe, or data arrays (lists, numpy arrays,
    pandas columns, series).

    Parameters
    ----------
    args : OrderedDict
        arguments passed to the px function and subsequently modified
    constructor : graph_object trace class
        the trace type selected for this figure
    """

    # make copies of all the fields via dict() and list()
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

    # now we handle special cases like wide-mode or x-xor-y specification
    # by rearranging args to tee things up for process_args_into_dataframe to work
    no_x = args.get("x", None) is None
    no_y = args.get("y", None) is None
    wide_x = False if no_x else _is_col_list(df_input, args["x"])
    wide_y = False if no_y else _is_col_list(df_input, args["y"])

    wide_mode = False
    var_name = None  # will likely be "variable" in wide_mode
    wide_cross_name = None  # will likely be "index" in wide_mode
    value_name = None  # will likely be "value" in wide_mode
    hist2d_types = [go.Histogram2d, go.Histogram2dContour]
    if constructor in cartesians:
        if wide_x and wide_y:
            raise ValueError(
                "Cannot accept list of column references or list of columns for both `x` and `y`."
            )
        if df_provided and no_x and no_y:
            wide_mode = True
            if isinstance(df_input.columns, pd.MultiIndex):
                raise TypeError(
                    "Data frame columns is a pandas MultiIndex. "
                    "pandas MultiIndex is not supported by plotly express "
                    "at the moment."
                )
            args["wide_variable"] = list(df_input.columns)
            var_name = df_input.columns.name
            if var_name in [None, "value", "index"] or var_name in df_input:
                var_name = "variable"
            if constructor == go.Funnel:
                wide_orientation = args.get("orientation", None) or "h"
            else:
                wide_orientation = args.get("orientation", None) or "v"
            args["orientation"] = wide_orientation
            args["wide_cross"] = None
        elif wide_x != wide_y:
            wide_mode = True
            args["wide_variable"] = args["y"] if wide_y else args["x"]
            if df_provided and args["wide_variable"] is df_input.columns:
                var_name = df_input.columns.name
            if isinstance(args["wide_variable"], pd.Index):
                args["wide_variable"] = list(args["wide_variable"])
            if var_name in [None, "value", "index"] or (
                df_provided and var_name in df_input
            ):
                var_name = "variable"
            if constructor == go.Histogram:
                wide_orientation = "v" if wide_x else "h"
            else:
                wide_orientation = "v" if wide_y else "h"
            args["y" if wide_y else "x"] = None
            args["wide_cross"] = None
            if not no_x and not no_y:
                wide_cross_name = "__x__" if wide_y else "__y__"

    if wide_mode:
        value_name = _escape_col_name(df_input, "value", [])
        var_name = _escape_col_name(df_input, var_name, [])

    missing_bar_dim = None
    if constructor in [go.Scatter, go.Bar, go.Funnel] + hist2d_types:
        if not wide_mode and (no_x != no_y):
            for ax in ["x", "y"]:
                if args.get(ax, None) is None:
                    args[ax] = df_input.index if df_provided else Range()
                    if constructor == go.Bar:
                        missing_bar_dim = ax
                    else:
                        if args["orientation"] is None:
                            args["orientation"] = "v" if ax == "x" else "h"
        if wide_mode and wide_cross_name is None:
            if no_x != no_y and args["orientation"] is None:
                args["orientation"] = "v" if no_x else "h"
            if df_provided:
                if isinstance(df_input.index, pd.MultiIndex):
                    raise TypeError(
                        "Data frame index is a pandas MultiIndex. "
                        "pandas MultiIndex is not supported by plotly express "
                        "at the moment."
                    )
                args["wide_cross"] = df_input.index
            else:
                args["wide_cross"] = Range(
                    label=_escape_col_name(df_input, "index", [var_name, value_name])
                )

    no_color = False
    if type(args.get("color", None)) == str and args["color"] == NO_COLOR:
        no_color = True
        args["color"] = None
    # now that things have been prepped, we do the systematic rewriting of `args`

    df_output, wide_id_vars = process_args_into_dataframe(
        args, wide_mode, var_name, value_name
    )

    # now that `df_output` exists and `args` contains only references, we complete
    # the special-case and wide-mode handling by further rewriting args and/or mutating
    # df_output

    count_name = _escape_col_name(df_output, "count", [var_name, value_name])
    if not wide_mode and missing_bar_dim and constructor == go.Bar:
        # now that we've populated df_output, we check to see if the non-missing
        # dimension is categorical: if so, then setting the missing dimension to a
        # constant 1 is a less-insane thing to do than setting it to the index by
        # default and we let the normal auto-orientation-code do its thing later
        other_dim = "x" if missing_bar_dim == "y" else "y"
        if not _is_continuous(df_output, args[other_dim]):
            args[missing_bar_dim] = count_name
            df_output[count_name] = 1
        else:
            # on the other hand, if the non-missing dimension is continuous, then we
            # can use this information to override the normal auto-orientation code
            if args["orientation"] is None:
                args["orientation"] = "v" if missing_bar_dim == "x" else "h"

    if constructor in hist2d_types:
        del args["orientation"]

    if wide_mode:
        # at this point, `df_output` is semi-long/semi-wide, but we know which columns
        # are which, so we melt it and reassign `args` to refer to the newly-tidy
        # columns, keeping track of various names and manglings set up above
        wide_value_vars = [c for c in args["wide_variable"] if c not in wide_id_vars]
        del args["wide_variable"]
        if wide_cross_name == "__x__":
            wide_cross_name = args["x"]
        elif wide_cross_name == "__y__":
            wide_cross_name = args["y"]
        else:
            wide_cross_name = args["wide_cross"]
        del args["wide_cross"]
        dtype = None
        for v in wide_value_vars:
            v_dtype = df_output[v].dtype.kind
            v_dtype = "number" if v_dtype in ["i", "f", "u"] else v_dtype
            if dtype is None:
                dtype = v_dtype
            elif dtype != v_dtype:
                raise ValueError(
                    "Plotly Express cannot process wide-form data with columns of different type."
                )
        df_output = df_output.melt(
            id_vars=wide_id_vars,
            value_vars=wide_value_vars,
            var_name=var_name,
            value_name=value_name,
        )
        assert len(df_output.columns) == len(set(df_output.columns)), (
            "Wide-mode name-inference failure, likely due to a internal bug. "
            "Please report this to "
            "https://github.com/plotly/plotly.py/issues/new and we will try to "
            "replicate and fix it."
        )
        df_output[var_name] = df_output[var_name].astype(str)
        orient_v = wide_orientation == "v"

        if constructor in [go.Scatter, go.Funnel] + hist2d_types:
            args["x" if orient_v else "y"] = wide_cross_name
            args["y" if orient_v else "x"] = value_name
            if constructor != go.Histogram2d:
                args["color"] = args["color"] or var_name
            if "line_group" in args:
                args["line_group"] = args["line_group"] or var_name
        if constructor == go.Bar:
            if _is_continuous(df_output, value_name):
                args["x" if orient_v else "y"] = wide_cross_name
                args["y" if orient_v else "x"] = value_name
                args["color"] = args["color"] or var_name
            else:
                args["x" if orient_v else "y"] = value_name
                args["y" if orient_v else "x"] = count_name
                df_output[count_name] = 1
                args["color"] = args["color"] or var_name
        if constructor in [go.Violin, go.Box]:
            args["x" if orient_v else "y"] = wide_cross_name or var_name
            args["y" if orient_v else "x"] = value_name
        if constructor == go.Histogram:
            args["x" if orient_v else "y"] = value_name
            args["y" if orient_v else "x"] = wide_cross_name
            args["color"] = args["color"] or var_name
    if no_color:
        args["color"] = None
    args["data_frame"] = df_output
    return args


def _check_dataframe_all_leaves(df):
    df_sorted = df.sort_values(by=list(df.columns))
    null_mask = df_sorted.isnull()
    df_sorted = df_sorted.astype(str)
    null_indices = np.nonzero(null_mask.any(axis=1).values)[0]
    for null_row_index in null_indices:
        row = null_mask.iloc[null_row_index]
        i = np.nonzero(row.values)[0][0]
        if not row[i:].all():
            raise ValueError(
                "None entries cannot have not-None children",
                df_sorted.iloc[null_row_index],
            )
    df_sorted[null_mask] = ""
    row_strings = list(df_sorted.apply(lambda x: "".join(x), axis=1))
    for i, row in enumerate(row_strings[:-1]):
        if row_strings[i + 1] in row and (i + 1) in null_indices:
            raise ValueError(
                "Non-leaves rows are not permitted in the dataframe \n",
                df_sorted.iloc[i + 1],
                "is not a leaf.",
            )


def process_dataframe_hierarchy(args):
    """
    Build dataframe for sunburst or treemap when the path argument is provided.
    """
    df = args["data_frame"]
    path = args["path"][::-1]
    _check_dataframe_all_leaves(df[path[::-1]])
    discrete_color = False

    new_path = []
    for col_name in path:
        new_col_name = col_name + "_path_copy"
        new_path.append(new_col_name)
        df[new_col_name] = df[col_name]
    path = new_path
    # ------------ Define aggregation functions --------------------------------

    def aggfunc_discrete(x):
        uniques = x.unique()
        if len(uniques) == 1:
            return uniques[0]
        else:
            return "(?)"

    agg_f = {}
    aggfunc_color = None
    if args["values"]:
        try:
            df[args["values"]] = pd.to_numeric(df[args["values"]])
        except ValueError:
            raise ValueError(
                "Column `%s` of `df` could not be converted to a numerical data type."
                % args["values"]
            )

        if args["color"]:
            if args["color"] == args["values"]:
                new_value_col_name = args["values"] + "_sum"
                df[new_value_col_name] = df[args["values"]]
                args["values"] = new_value_col_name
        count_colname = args["values"]
    else:
        # we need a count column for the first groupby and the weighted mean of color
        # trick to be sure the col name is unused: take the sum of existing names
        count_colname = (
            "count"
            if "count" not in df.columns
            else "".join([str(el) for el in list(df.columns)])
        )
        # we can modify df because it's a copy of the px argument
        df[count_colname] = 1
        args["values"] = count_colname
    agg_f[count_colname] = "sum"

    if args["color"]:
        if not _is_continuous(df, args["color"]):
            aggfunc_color = aggfunc_discrete
            discrete_color = True
        else:

            def aggfunc_continuous(x):
                return np.average(x, weights=df.loc[x.index, count_colname])

            aggfunc_color = aggfunc_continuous
        agg_f[args["color"]] = aggfunc_color

    #  Other columns (for color, hover_data, custom_data etc.)
    cols = list(set(df.columns).difference(path))
    for col in cols:  # for hover_data, custom_data etc.
        if col not in agg_f:
            agg_f[col] = aggfunc_discrete
    # Avoid collisions with reserved names - columns in the path have been copied already
    cols = list(set(cols) - set(["labels", "parent", "id"]))
    # ----------------------------------------------------------------------------
    df_all_trees = pd.DataFrame(columns=["labels", "parent", "id"] + cols)
    #  Set column type here (useful for continuous vs discrete colorscale)
    for col in cols:
        df_all_trees[col] = df_all_trees[col].astype(df[col].dtype)
    for i, level in enumerate(path):
        df_tree = pd.DataFrame(columns=df_all_trees.columns)
        dfg = df.groupby(path[i:]).agg(agg_f)
        dfg = dfg.reset_index()
        # Path label massaging
        df_tree["labels"] = dfg[level].copy().astype(str)
        df_tree["parent"] = ""
        df_tree["id"] = dfg[level].copy().astype(str)
        if i < len(path) - 1:
            j = i + 1
            while j < len(path):
                df_tree["parent"] = (
                    dfg[path[j]].copy().astype(str) + "/" + df_tree["parent"]
                )
                df_tree["id"] = dfg[path[j]].copy().astype(str) + "/" + df_tree["id"]
                j += 1

        df_tree["parent"] = df_tree["parent"].str.rstrip("/")
        if cols:
            df_tree[cols] = dfg[cols]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)

    # we want to make sure than (?) is the first color of the sequence
    if args["color"] and discrete_color:
        sort_col_name = "sort_color_if_discrete_color"
        while sort_col_name in df_all_trees.columns:
            sort_col_name += "0"
        df_all_trees[sort_col_name] = df[args["color"]].astype(str)
        df_all_trees = df_all_trees.sort_values(by=sort_col_name)

    # Now modify arguments
    args["data_frame"] = df_all_trees
    args["path"] = None
    args["ids"] = "id"
    args["names"] = "labels"
    args["parents"] = "parent"
    if args["color"]:
        if not args["hover_data"]:
            args["hover_data"] = [args["color"]]
        elif isinstance(args["hover_data"], dict):
            if not args["hover_data"].get(args["color"]):
                args["hover_data"][args["color"]] = (True, None)
        else:
            args["hover_data"].append(args["color"])
    return args


def process_dataframe_timeline(args):
    """
    Massage input for bar traces for px.timeline()
    """
    args["is_timeline"] = True
    if args["x_start"] is None or args["x_end"] is None:
        raise ValueError("Both x_start and x_end are required")

    try:
        x_start = pd.to_datetime(args["data_frame"][args["x_start"]])
        x_end = pd.to_datetime(args["data_frame"][args["x_end"]])
    except (ValueError, TypeError):
        raise TypeError(
            "Both x_start and x_end must refer to data convertible to datetimes."
        )

    # note that we are not adding any columns to the data frame here, so no risk of overwrite
    args["data_frame"][args["x_end"]] = (x_end - x_start).astype("timedelta64[ms]")
    args["x"] = args["x_end"]
    del args["x_end"]
    args["base"] = args["x_start"]
    del args["x_start"]
    return args


def infer_config(args, constructor, trace_patch, layout_patch):
    attrs = [k for k in direct_attrables + array_attrables if k in args]
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
                if args["color"] and _is_continuous(args["data_frame"], args["color"]):
                    attrs.append("color")
                    args["color_is_continuous"] = True
                elif constructor in [go.Sunburst, go.Treemap]:
                    attrs.append("color")
                    args["color_is_continuous"] = False
                else:
                    grouped_attrs.append("marker.color")
        elif "line_group" in args or constructor == go.Histogram2dContour:
            grouped_attrs.append("line.color")
        elif constructor in [go.Pie, go.Funnelarea]:
            attrs.append("color")
            if args["color"]:
                if args["hover_data"] is None:
                    args["hover_data"] = []
                args["hover_data"].append(args["color"])
        else:
            grouped_attrs.append("marker.color")

        show_colorbar = bool(
            "color" in attrs
            and args["color"]
            and constructor not in [go.Pie, go.Funnelarea]
            and (
                constructor not in [go.Treemap, go.Sunburst]
                or args.get("color_is_continuous")
            )
        )
    else:
        show_colorbar = False

    # Compute line_dash grouping attribute
    if "line_dash" in args:
        grouped_attrs.append("line.dash")

    # Compute symbol grouping attribute
    if "symbol" in args:
        grouped_attrs.append("marker.symbol")

    if "orientation" in args:
        has_x = args["x"] is not None
        has_y = args["y"] is not None
        if args["orientation"] is None:
            if constructor in [go.Histogram, go.Scatter]:
                if has_y and not has_x:
                    args["orientation"] = "h"
            elif constructor in [go.Violin, go.Box, go.Bar, go.Funnel]:
                if has_x and not has_y:
                    args["orientation"] = "h"

        if args["orientation"] is None and has_x and has_y:
            x_is_continuous = _is_continuous(args["data_frame"], args["x"])
            y_is_continuous = _is_continuous(args["data_frame"], args["y"])
            if x_is_continuous and not y_is_continuous:
                args["orientation"] = "h"
            if y_is_continuous and not x_is_continuous:
                args["orientation"] = "v"

        if args["orientation"] is None:
            args["orientation"] = "v"

        if constructor == go.Histogram:
            if has_x and has_y and args["histfunc"] is None:
                args["histfunc"] = trace_patch["histfunc"] = "sum"

            orientation = args["orientation"]
            nbins = args["nbins"]
            trace_patch["nbinsx"] = nbins if orientation == "v" else None
            trace_patch["nbinsy"] = None if orientation == "v" else nbins
            trace_patch["bingroup"] = "x" if orientation == "v" else "y"
        trace_patch["orientation"] = args["orientation"]

        if constructor in [go.Violin, go.Box]:
            mode = "boxmode" if constructor == go.Box else "violinmode"
            if layout_patch[mode] is None and args["color"] is not None:
                if args["y"] == args["color"] and args["orientation"] == "h":
                    layout_patch[mode] = "overlay"
                elif args["x"] == args["color"] and args["orientation"] == "v":
                    layout_patch[mode] = "overlay"
            if layout_patch[mode] is None:
                layout_patch[mode] = "group"

    if (
        constructor == go.Histogram2d
        and args["z"] is not None
        and args["histfunc"] is None
    ):
        args["histfunc"] = trace_patch["histfunc"] = "sum"

    if constructor in [go.Histogram2d, go.Densitymapbox]:
        show_colorbar = True
        trace_patch["coloraxis"] = "coloraxis1"

    if "opacity" in args:
        if args["opacity"] is None:
            if "barmode" in args and args["barmode"] == "overlay":
                trace_patch["marker"] = dict(opacity=0.5)
        elif constructor in [go.Densitymapbox, go.Pie, go.Funnel, go.Funnelarea]:
            trace_patch["opacity"] = args["opacity"]
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
    return trace_specs, grouped_mappings, sizeref, show_colorbar


def get_orderings(args, grouper, grouped):
    """
    `orders` is the user-supplied ordering (with the remaining data-frame-supplied
    ordering appended if the column is used for grouping). It includes anything the user
    gave, for any variable, including values not present in the dataset. It is used
    downstream to set e.g. `categoryarray` for cartesian axes

    `group_names` is the set of groups, ordered by the order above

    `group_values` is a subset of `orders` in both keys and values. It contains a key
     for every grouped mapping and its values are the sorted *data* values for these
     mappings.
    """
    orders = {} if "category_orders" not in args else args["category_orders"].copy()
    group_names = []
    group_values = {}
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
                group_values[col] = sorted(uniques, key=orders[col].index)

    for i, col in reversed(list(enumerate(grouper))):
        if col != one_group:
            group_names = sorted(
                group_names,
                key=lambda g: orders[col].index(g[i]) if g[i] in orders[col] else -1,
            )

    return orders, group_names, group_values


def make_figure(args, constructor, trace_patch=None, layout_patch=None):
    trace_patch = trace_patch or {}
    layout_patch = layout_patch or {}
    apply_default_cascade(args)

    args = build_dataframe(args, constructor)
    if constructor in [go.Treemap, go.Sunburst] and args["path"] is not None:
        args = process_dataframe_hierarchy(args)
    if constructor == "timeline":
        constructor = go.Bar
        args = process_dataframe_timeline(args)

    trace_specs, grouped_mappings, sizeref, show_colorbar = infer_config(
        args, constructor, trace_patch, layout_patch
    )
    grouper = [x.grouper or one_group for x in grouped_mappings] or [one_group]
    grouped = args["data_frame"].groupby(grouper, sort=False)

    orders, sorted_group_names, sorted_group_values = get_orderings(
        args, grouper, grouped
    )

    col_labels = []
    row_labels = []

    for m in grouped_mappings:
        if m.grouper:
            if m.facet == "col":
                prefix = get_label(args, args["facet_col"]) + "="
                col_labels = [prefix + str(s) for s in sorted_group_values[m.grouper]]
            if m.facet == "row":
                prefix = get_label(args, args["facet_row"]) + "="
                row_labels = [prefix + str(s) for s in sorted_group_values[m.grouper]]
            for val in sorted_group_values[m.grouper]:
                if val not in m.val_map:
                    m.val_map[val] = m.sequence[len(m.val_map) % len(m.sequence)]

    subplot_type = _subplot_type_for_trace_type(constructor().type)

    trace_names_by_frame = {}
    frames = OrderedDict()
    trendline_rows = []
    nrows = ncols = 1
    trace_name_labels = None
    for group_name in sorted_group_names:
        group = grouped.get_group(group_name if len(group_name) > 1 else group_name[0])
        mapping_labels = OrderedDict()
        trace_name_labels = OrderedDict()
        frame_name = ""
        for col, val, m in zip(grouper, group_name, grouped_mappings):
            if col != one_group:
                key = get_label(args, col)
                if not isinstance(m.val_map, IdentityMap):
                    mapping_labels[key] = str(val)
                    if m.show_in_trace_name:
                        trace_name_labels[key] = str(val)
                if m.variable == "animation_frame":
                    frame_name = val
        trace_name = ", ".join(trace_name_labels.values())
        if frame_name not in trace_names_by_frame:
            trace_names_by_frame[frame_name] = set()
        trace_names = trace_names_by_frame[frame_name]

        for trace_spec in trace_specs:
            # Create the trace
            trace = trace_spec.constructor(name=trace_name)
            if trace_spec.constructor not in [
                go.Parcats,
                go.Parcoords,
                go.Choropleth,
                go.Choroplethmapbox,
                go.Densitymapbox,
                go.Histogram2d,
                go.Sunburst,
                go.Treemap,
            ]:
                trace.update(
                    legendgroup=trace_name,
                    showlegend=(trace_name != "" and trace_name not in trace_names),
                )
            if trace_spec.constructor in [go.Bar, go.Violin, go.Box, go.Histogram]:
                trace.update(alignmentgroup=True, offsetgroup=trace_name)
            trace_names.add(trace_name)

            # Init subplot row/col
            trace._subplot_row = 1
            trace._subplot_col = 1

            for i, m in enumerate(grouped_mappings):
                val = group_name[i]
                if val not in m.val_map:
                    m.val_map[val] = m.sequence[len(m.val_map) % len(m.sequence)]
                try:
                    m.updater(trace, m.val_map[val])  # covers most cases
                except ValueError:
                    # this catches some odd cases like marginals
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
                    elif (
                        trace_spec.constructor in [go.Choropleth, go.Choroplethmapbox]
                        and m.variable == "color"
                    ):
                        trace.update(
                            z=[1] * len(group),
                            colorscale=[m.val_map[val]] * 2,
                            showscale=False,
                            showlegend=True,
                        )
                    else:
                        raise

                # Find row for trace, handling facet_row and marginal_x
                if m.facet == "row":
                    row = m.val_map[val]
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

    if show_colorbar:
        colorvar = "z" if constructor in [go.Histogram2d, go.Densitymapbox] else "color"
        range_color = args["range_color"] or [None, None]

        colorscale_validator = ColorscaleValidator("colorscale", "make_figure")
        layout_patch["coloraxis1"] = dict(
            colorscale=colorscale_validator.validate_coerce(
                args["color_continuous_scale"]
            ),
            cmid=args["color_continuous_midpoint"],
            cmin=range_color[0],
            cmax=range_color[1],
            colorbar=dict(
                title_text=get_decorated_label(args, args[colorvar], colorvar)
            ),
        )
    for v in ["height", "width"]:
        if args[v]:
            layout_patch[v] = args[v]
    layout_patch["legend"] = dict(tracegroupgap=0)
    if trace_name_labels:
        layout_patch["legend"]["title_text"] = ", ".join(trace_name_labels)
    if args["title"]:
        layout_patch["title_text"] = args["title"]
    elif args["template"].layout.margin.t is None:
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
    fig.update_layout(layout_patch)
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
            vertical_spacing = args.get("facet_row_spacing", None) or 0.07
        else:
            vertical_spacing = args.get("facet_row_spacing", None) or 0.03

        if bool(args.get("marginal_y", False)):
            if args["marginal_y"] == "histogram" or ("color" in args and args["color"]):
                main_size = 0.74
            else:
                main_size = 0.84

            column_widths = [main_size] * (ncols - 1) + [1 - main_size]
            horizontal_spacing = 0.005
        else:
            horizontal_spacing = args.get("facet_col_spacing", None) or 0.02
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
