#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):
    _parent_path_str = "scatterternary"
    _path_str = "scatterternary.line"
    _valid_props = {"backoff", "color", "dash", "shape", "smoothing", "width"}

    @property
    def backoff(self):
        """
        Sets the line back off from the end point of the nth line
        segment (in px). This option is useful e.g. to avoid overlap
        with arrowhead markers. With "auto" the lines would trim before
        markers if `marker.angleref` is set to "previous".

        The 'backoff' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["backoff"]

    @backoff.setter
    def backoff(self, val):
        self["backoff"] = val

    @property
    def color(self):
        """
        Sets the line color.

        The 'color' property is a color and may be specified as a string in the following formats:
          - hex or short hex (e.g. '#d3d3d3', '#d3d')
          - hex or short hex with alpha (e.g. '#d3d3d380', '#d3d8')
          - rgb (e.g. 'rgb(255, 0, 0)', 'rgb(255 0 0)')
          - rgba (e.g. 'rgba(255, 0, 0, 0.5)', 'rgba(255 0 0 / 0.5)')
          - hsl (e.g. 'hsl(0, 100%, 50%)', 'hsl(0deg 100% 50%)')
          - hsla (e.g. 'hsla(0, 100%, 50%, 0.5)', 'hsla(0deg 100% 50% / 0.5)')
          - hwb (e.g. 'hwb(0 0% 100%)')
          - lab/lch/oklab/oklch (e.g. 'oklch(0.7 0.15 180)')
          - color (e.g. 'color(display-p3 1 0 0)')
          - named colors (full list: https://www.w3.org/TR/css-color-4/#named-color)
          - Any other supported CSS 4 color format: https://www.w3.org/TR/css-color-4/

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def dash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").

        The 'dash' property is an enumeration that may be specified as:
          - One of the following dash styles:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
          - A string containing a dash length list in pixels or percentages
                (e.g. '5px 10px 2px 2px', '5, 10, 2, 2', '10% 20% 40%', etc.)

        Returns
        -------
        str
        """
        return self["dash"]

    @dash.setter
    def dash(self, val):
        self["dash"] = val

    @property
    def shape(self):
        """
        Determines the line shape. With "spline" the lines are drawn
        using spline interpolation. The other available values
        correspond to step-wise line shapes.

        The 'shape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'spline']

        Returns
        -------
        Any
        """
        return self["shape"]

    @shape.setter
    def shape(self, val):
        self["shape"] = val

    @property
    def smoothing(self):
        """
        Has an effect only if `shape` is set to "spline" Sets the
        amount of smoothing. 0 corresponds to no smoothing (equivalent
        to a "linear" shape).

        The 'smoothing' property is a number and may be specified as:
          - An int or float in the interval [0, 1.3]

        Returns
        -------
        int|float
        """
        return self["smoothing"]

    @smoothing.setter
    def smoothing(self, val):
        self["smoothing"] = val

    @property
    def width(self):
        """
        Sets the line width (in px).

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    @property
    def _prop_descriptions(self):
        return """\
        backoff
            Sets the line back off from the end point of the nth
            line segment (in px). This option is useful e.g. to
            avoid overlap with arrowhead markers. With "auto" the
            lines would trim before markers if `marker.angleref` is
            set to "previous".
        color
            Sets the line color.
        dash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        shape
            Determines the line shape. With "spline" the lines are
            drawn using spline interpolation. The other available
            values correspond to step-wise line shapes.
        smoothing
            Has an effect only if `shape` is set to "spline" Sets
            the amount of smoothing. 0 corresponds to no smoothing
            (equivalent to a "linear" shape).
        width
            Sets the line width (in px).
        """

    def __init__(
        self,
        arg=None,
        backoff=None,
        color=None,
        dash=None,
        shape=None,
        smoothing=None,
        width=None,
        **kwargs,
    ):
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scatterternary.Line`
        backoff
            Sets the line back off from the end point of the nth
            line segment (in px). This option is useful e.g. to
            avoid overlap with arrowhead markers. With "auto" the
            lines would trim before markers if `marker.angleref` is
            set to "previous".
        color
            Sets the line color.
        dash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        shape
            Determines the line shape. With "spline" the lines are
            drawn using spline interpolation. The other available
            values correspond to step-wise line shapes.
        smoothing
            Has an effect only if `shape` is set to "spline" Sets
            the amount of smoothing. 0 corresponds to no smoothing
            (equivalent to a "linear" shape).
        width
            Sets the line width (in px).

        Returns
        -------
        Line
        """
        super().__init__("line")
        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.scatterternary.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatterternary.Line`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("backoff", arg, backoff)
        self._set_property("color", arg, color)
        self._set_property("dash", arg, dash)
        self._set_property("shape", arg, shape)
        self._set_property("smoothing", arg, smoothing)
        self._set_property("width", arg, width)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
