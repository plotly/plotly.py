#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Activeshape(_BaseLayoutHierarchyType):
    _parent_path_str = "layout"
    _path_str = "layout.activeshape"
    _valid_props = {"fillcolor", "opacity"}

    @property
    def fillcolor(self):
        """
        Sets the color filling the active shape' interior.

        The 'fillcolor' property is a color and may be specified as a string in the following formats:
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
        return self["fillcolor"]

    @fillcolor.setter
    def fillcolor(self, val):
        self["fillcolor"] = val

    @property
    def opacity(self):
        """
        Sets the opacity of the active shape.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def _prop_descriptions(self):
        return """\
        fillcolor
            Sets the color filling the active shape' interior.
        opacity
            Sets the opacity of the active shape.
        """

    def __init__(self, arg=None, fillcolor=None, opacity=None, **kwargs):
        """
        Construct a new Activeshape object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.Activeshape`
        fillcolor
            Sets the color filling the active shape' interior.
        opacity
            Sets the opacity of the active shape.

        Returns
        -------
        Activeshape
        """
        super().__init__("activeshape")
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
The first argument to the plotly.graph_objs.layout.Activeshape
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Activeshape`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("fillcolor", arg, fillcolor)
        self._set_property("opacity", arg, opacity)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
