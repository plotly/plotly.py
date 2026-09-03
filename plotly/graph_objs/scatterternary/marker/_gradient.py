#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Gradient(_BaseTraceHierarchyType):
    _parent_path_str = "scatterternary.marker"
    _path_str = "scatterternary.marker.gradient"
    _valid_props = {"color", "type"}

    @property
    def color(self):
        """
        Sets the final color of the gradient fill: the center color for
        radial, the right for horizontal, or the bottom for vertical.

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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def type(self):
        """
        Sets the type of gradient used to fill the markers

        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['radial', 'horizontal', 'vertical', 'none']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the final color of the gradient fill: the center
            color for radial, the right for horizontal, or the
            bottom for vertical.
        type
            Sets the type of gradient used to fill the markers
        """

    def __init__(self, arg=None, color=None, type=None, **kwargs):
        """
        Construct a new Gradient object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.scatterternary
            .marker.Gradient`
        color
            Sets the final color of the gradient fill: the center
            color for radial, the right for horizontal, or the
            bottom for vertical.
        type
            Sets the type of gradient used to fill the markers

        Returns
        -------
        Gradient
        """
        super().__init__("gradient")
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
The first argument to the plotly.graph_objs.scatterternary.marker.Gradient
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatterternary.marker.Gradient`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("color", arg, color)
        self._set_property("type", arg, type)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
