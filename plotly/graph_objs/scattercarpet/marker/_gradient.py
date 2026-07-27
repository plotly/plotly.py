#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Gradient(_BaseTraceHierarchyType):
    _parent_path_str = "scattercarpet.marker"
    _path_str = "scattercarpet.marker.gradient"
    _valid_props = {"color", "type"}

    @property
    def color(self):
        """
        Sets the final color of the gradient fill: the center color for
        radial, the right for horizontal, or the bottom for vertical.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color: see https://plotly.com/python/css-colors/ for a list
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
            an instance of :class:`plotly.graph_objs.scattercarpet.
            marker.Gradient`
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
The first argument to the plotly.graph_objs.scattercarpet.marker.Gradient
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattercarpet.marker.Gradient`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("color", arg, color)
        self._set_property("type", arg, type)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
