from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Line(_BaseTraceHierarchyType):

    _parent_path_str = "sankey.link"
    _path_str = "sankey.link.line"
    _valid_props = {"color", "colorsrc", "width", "widthsrc"}

    @property
    def color(self):
        """
        Sets the color of the `line` around each `link`.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color
          - A list or array of any of the above

        Returns
        -------
        str|NDArray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def colorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["colorsrc"]

    @colorsrc.setter
    def colorsrc(self, val):
        self["colorsrc"] = val

    @property
    def width(self):
        """
        Sets the width (in px) of the `line` around each `link`.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|NDArray
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    @property
    def widthsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `width`.

        The 'widthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["widthsrc"]

    @widthsrc.setter
    def widthsrc(self, val):
        self["widthsrc"] = val

    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the color of the `line` around each `link`.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        width
            Sets the width (in px) of the `line` around each
            `link`.
        widthsrc
            Sets the source reference on Chart Studio Cloud for
            `width`.
        """

    def __init__(
        self,
        arg=None,
        color: str | None = None,
        colorsrc: str | None = None,
        width: int | float | None = None,
        widthsrc: str | None = None,
        **kwargs,
    ):
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.sankey.link.Line`
        color
            Sets the color of the `line` around each `link`.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        width
            Sets the width (in px) of the `line` around each
            `link`.
        widthsrc
            Sets the source reference on Chart Studio Cloud for
            `width`.

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
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.sankey.link.Line
constructor must be a dict or
an instance of :class:`plotly.graph_objs.sankey.link.Line`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("color", arg, color)
        self._init_provided("colorsrc", arg, colorsrc)
        self._init_provided("width", arg, width)
        self._init_provided("widthsrc", arg, widthsrc)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
