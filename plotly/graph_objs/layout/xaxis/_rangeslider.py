from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Rangeslider(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.xaxis"
    _path_str = "layout.xaxis.rangeslider"
    _valid_props = {
        "autorange",
        "bgcolor",
        "bordercolor",
        "borderwidth",
        "range",
        "thickness",
        "visible",
        "yaxis",
    }

    @property
    def autorange(self):
        """
        Determines whether or not the range slider range is computed in
        relation to the input data. If `range` is provided, then
        `autorange` is set to False.

        The 'autorange' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autorange"]

    @autorange.setter
    def autorange(self, val):
        self["autorange"] = val

    @property
    def bgcolor(self):
        """
        Sets the background color of the range slider.

        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def bordercolor(self):
        """
        Sets the border color of the range slider.

        The 'bordercolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    @property
    def borderwidth(self):
        """
        Sets the border width of the range slider.

        The 'borderwidth' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    @property
    def range(self):
        """
            Sets the range of the range slider. If not set, defaults to the
            full xaxis range. If the axis `type` is "log", then you must
            take the log of your desired range. If the axis `type` is
            "date", it should be date strings, like date data, though Date
            objects and unix milliseconds will be accepted and converted to
            strings. If the axis `type` is "category", it should be
            numbers, using the scale where each category is assigned a
            serial number from zero in the order it appears.

            The 'range' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'range[0]' property accepts values of any type
        (1) The 'range[1]' property accepts values of any type

            Returns
            -------
            list
        """
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    @property
    def thickness(self):
        """
        The height of the range slider as a fraction of the total plot
        area height.

        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    @property
    def visible(self):
        """
        Determines whether or not the range slider will be visible. If
        visible, perpendicular axes will be set to `fixedrange`

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def yaxis(self):
        """
        The 'yaxis' property is an instance of YAxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.xaxis.rangeslider.YAxis`
          - A dict of string/value properties that will be passed
            to the YAxis constructor

        Returns
        -------
        plotly.graph_objs.layout.xaxis.rangeslider.YAxis
        """
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    @property
    def _prop_descriptions(self):
        return """\
        autorange
            Determines whether or not the range slider range is
            computed in relation to the input data. If `range` is
            provided, then `autorange` is set to False.
        bgcolor
            Sets the background color of the range slider.
        bordercolor
            Sets the border color of the range slider.
        borderwidth
            Sets the border width of the range slider.
        range
            Sets the range of the range slider. If not set,
            defaults to the full xaxis range. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        thickness
            The height of the range slider as a fraction of the
            total plot area height.
        visible
            Determines whether or not the range slider will be
            visible. If visible, perpendicular axes will be set to
            `fixedrange`
        yaxis
            :class:`plotly.graph_objects.layout.xaxis.rangeslider.Y
            Axis` instance or dict with compatible properties
        """

    def __init__(
        self,
        arg=None,
        autorange: bool | None = None,
        bgcolor: str | None = None,
        bordercolor: str | None = None,
        borderwidth: int | None = None,
        range: list | None = None,
        thickness: int | float | None = None,
        visible: bool | None = None,
        yaxis: None | None = None,
        **kwargs,
    ):
        """
        Construct a new Rangeslider object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.xaxis.Rangeslider`
        autorange
            Determines whether or not the range slider range is
            computed in relation to the input data. If `range` is
            provided, then `autorange` is set to False.
        bgcolor
            Sets the background color of the range slider.
        bordercolor
            Sets the border color of the range slider.
        borderwidth
            Sets the border width of the range slider.
        range
            Sets the range of the range slider. If not set,
            defaults to the full xaxis range. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        thickness
            The height of the range slider as a fraction of the
            total plot area height.
        visible
            Determines whether or not the range slider will be
            visible. If visible, perpendicular axes will be set to
            `fixedrange`
        yaxis
            :class:`plotly.graph_objects.layout.xaxis.rangeslider.Y
            Axis` instance or dict with compatible properties

        Returns
        -------
        Rangeslider
        """
        super().__init__("rangeslider")
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
The first argument to the plotly.graph_objs.layout.xaxis.Rangeslider
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.xaxis.Rangeslider`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("autorange", arg, autorange)
        self._init_provided("bgcolor", arg, bgcolor)
        self._init_provided("bordercolor", arg, bordercolor)
        self._init_provided("borderwidth", arg, borderwidth)
        self._init_provided("range", arg, range)
        self._init_provided("thickness", arg, thickness)
        self._init_provided("visible", arg, visible)
        self._init_provided("yaxis", arg, yaxis)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
