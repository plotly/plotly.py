#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Cluster(_BaseTraceHierarchyType):
    _parent_path_str = "scattermap"
    _path_str = "scattermap.cluster"
    _valid_props = {"color", "enabled", "maxzoom", "opacity", "size", "step"}

    @property
    def color(self):
        """
        Sets the color for each cluster step.

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
    def enabled(self):
        """
        Determines whether clustering is enabled or disabled.

        The 'enabled' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        return self["enabled"]

    @enabled.setter
    def enabled(self, val):
        self["enabled"] = val

    @property
    def maxzoom(self):
        """
        Sets the maximum zoom level. At zoom levels equal to or greater
        than this, points will never be clustered.

        The 'maxzoom' property is a number and may be specified as:
          - An int or float in the interval [0, 24]

        Returns
        -------
        int|float
        """
        return self["maxzoom"]

    @maxzoom.setter
    def maxzoom(self, val):
        self["maxzoom"] = val

    @property
    def opacity(self):
        """
        Sets the marker opacity.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def size(self):
        """
        Sets the size for each cluster step.

        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    @property
    def step(self):
        """
        Sets how many points it takes to create a cluster or advance to
        the next cluster step. Use this in conjunction with arrays for
        `size` and / or `color`. If an integer, steps start at
        multiples of this number. If an array, each step extends from
        the given value until one less than the next value.

        The 'step' property is a number and may be specified as:
          - An int or float in the interval [-1, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["step"]

    @step.setter
    def step(self, val):
        self["step"] = val

    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the color for each cluster step.
        enabled
            Determines whether clustering is enabled or disabled.
        maxzoom
            Sets the maximum zoom level. At zoom levels equal to or
            greater than this, points will never be clustered.
        opacity
            Sets the marker opacity.
        size
            Sets the size for each cluster step.
        step
            Sets how many points it takes to create a cluster or
            advance to the next cluster step. Use this in
            conjunction with arrays for `size` and / or `color`. If
            an integer, steps start at multiples of this number. If
            an array, each step extends from the given value until
            one less than the next value.
        """

    def __init__(
        self,
        arg=None,
        color=None,
        enabled=None,
        maxzoom=None,
        opacity=None,
        size=None,
        step=None,
        **kwargs,
    ):
        """
        Construct a new Cluster object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scattermap.Cluster`
        color
            Sets the color for each cluster step.
        enabled
            Determines whether clustering is enabled or disabled.
        maxzoom
            Sets the maximum zoom level. At zoom levels equal to or
            greater than this, points will never be clustered.
        opacity
            Sets the marker opacity.
        size
            Sets the size for each cluster step.
        step
            Sets how many points it takes to create a cluster or
            advance to the next cluster step. Use this in
            conjunction with arrays for `size` and / or `color`. If
            an integer, steps start at multiples of this number. If
            an array, each step extends from the given value until
            one less than the next value.

        Returns
        -------
        Cluster
        """
        super().__init__("cluster")
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
The first argument to the plotly.graph_objs.scattermap.Cluster
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattermap.Cluster`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("color", arg, color)
        self._set_property("enabled", arg, enabled)
        self._set_property("maxzoom", arg, maxzoom)
        self._set_property("opacity", arg, opacity)
        self._set_property("size", arg, size)
        self._set_property("step", arg, step)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
