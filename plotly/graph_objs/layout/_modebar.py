#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Modebar(_BaseLayoutHierarchyType):
    _parent_path_str = "layout"
    _path_str = "layout.modebar"
    _valid_props = {
        "activecolor",
        "add",
        "bgcolor",
        "color",
        "orientation",
        "remove",
        "uirevision",
    }

    @property
    def activecolor(self):
        """
        Sets the color of the active or hovered on icons in the
        modebar.

        The 'activecolor' property is a color and may be specified as a string in the following formats:
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
        return self["activecolor"]

    @activecolor.setter
    def activecolor(self, val):
        self["activecolor"] = val

    @property
    def add(self):
        """
        Determines which predefined modebar buttons to add. Please note
        that these buttons will only be shown if they are compatible
        with all trace types used in a graph. Similar to
        `config.modeBarButtonsToAdd` option. This may include
        "v1hovermode", "hoverclosest", "hovercompare", "togglehover",
        "togglespikelines", "drawline", "drawopenpath",
        "drawclosedpath", "drawcircle", "drawrect", "eraseshape".

        The 'add' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["add"]

    @add.setter
    def add(self, val):
        self["add"] = val

    @property
    def bgcolor(self):
        """
        Sets the background color of the modebar.

        The 'bgcolor' property is a color and may be specified as a string in the following formats:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def color(self):
        """
        Sets the color of the icons in the modebar.

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
    def orientation(self):
        """
        Sets the orientation of the modebar.

        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    @property
    def remove(self):
        """
        Determines which predefined modebar buttons to remove. Similar
        to `config.modeBarButtonsToRemove` option. This may include
        "autoScale2d", "autoscale", "hoverCompareCartesian",
        "hovercompare", "lasso", "lasso2d", "orbitRotation",
        "orbitrotation", "pan", "pan2d", "pan3d", "reset",
        "resetCameraDefault3d", "resetCameraLastSave3d", "resetGeo",
        "resetSankeyGroup", "resetScale2d", "resetViewMap",
        "resetViews", "resetcameradefault", "resetcameralastsave",
        "resetsankeygroup", "resetscale", "resetview", "resetviews",
        "select", "select2d", "sendChartToCloud", "sendcharttocloud",
        "tableRotation", "tablerotation", "toImage", "toggleHover",
        "toggleSpikelines", "togglehover", "togglespikelines",
        "toimage", "zoom", "zoom2d", "zoom3d", "zoomIn2d", "zoomInGeo",
        "zoomInMap", "zoomOut2d", "zoomOutGeo", "zoomOutMap", "zoomin",
        "zoomout".

        The 'remove' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["remove"]

    @remove.setter
    def remove(self, val):
        self["remove"] = val

    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes related to the
        modebar, including `hovermode`, `dragmode`, and `showspikes` at
        both the root level and inside subplots. Defaults to
        `layout.uirevision`.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def _prop_descriptions(self):
        return """\
        activecolor
            Sets the color of the active or hovered on icons in the
            modebar.
        add
            Determines which predefined modebar buttons to add.
            Please note that these buttons will only be shown if
            they are compatible with all trace types used in a
            graph. Similar to `config.modeBarButtonsToAdd` option.
            This may include "v1hovermode", "hoverclosest",
            "hovercompare", "togglehover", "togglespikelines",
            "drawline", "drawopenpath", "drawclosedpath",
            "drawcircle", "drawrect", "eraseshape".
        bgcolor
            Sets the background color of the modebar.
        color
            Sets the color of the icons in the modebar.
        orientation
            Sets the orientation of the modebar.
        remove
            Determines which predefined modebar buttons to remove.
            Similar to `config.modeBarButtonsToRemove` option. This
            may include "autoScale2d", "autoscale",
            "hoverCompareCartesian", "hovercompare", "lasso",
            "lasso2d", "orbitRotation", "orbitrotation", "pan",
            "pan2d", "pan3d", "reset", "resetCameraDefault3d",
            "resetCameraLastSave3d", "resetGeo",
            "resetSankeyGroup", "resetScale2d", "resetViewMap",
            "resetViews", "resetcameradefault",
            "resetcameralastsave", "resetsankeygroup",
            "resetscale", "resetview", "resetviews", "select",
            "select2d", "sendChartToCloud", "sendcharttocloud",
            "tableRotation", "tablerotation", "toImage",
            "toggleHover", "toggleSpikelines", "togglehover",
            "togglespikelines", "toimage", "zoom", "zoom2d",
            "zoom3d", "zoomIn2d", "zoomInGeo", "zoomInMap",
            "zoomOut2d", "zoomOutGeo", "zoomOutMap", "zoomin",
            "zoomout".
        uirevision
            Controls persistence of user-driven changes related to
            the modebar, including `hovermode`, `dragmode`, and
            `showspikes` at both the root level and inside
            subplots. Defaults to `layout.uirevision`.
        """

    def __init__(
        self,
        arg=None,
        activecolor=None,
        add=None,
        bgcolor=None,
        color=None,
        orientation=None,
        remove=None,
        uirevision=None,
        **kwargs,
    ):
        """
        Construct a new Modebar object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.Modebar`
        activecolor
            Sets the color of the active or hovered on icons in the
            modebar.
        add
            Determines which predefined modebar buttons to add.
            Please note that these buttons will only be shown if
            they are compatible with all trace types used in a
            graph. Similar to `config.modeBarButtonsToAdd` option.
            This may include "v1hovermode", "hoverclosest",
            "hovercompare", "togglehover", "togglespikelines",
            "drawline", "drawopenpath", "drawclosedpath",
            "drawcircle", "drawrect", "eraseshape".
        bgcolor
            Sets the background color of the modebar.
        color
            Sets the color of the icons in the modebar.
        orientation
            Sets the orientation of the modebar.
        remove
            Determines which predefined modebar buttons to remove.
            Similar to `config.modeBarButtonsToRemove` option. This
            may include "autoScale2d", "autoscale",
            "hoverCompareCartesian", "hovercompare", "lasso",
            "lasso2d", "orbitRotation", "orbitrotation", "pan",
            "pan2d", "pan3d", "reset", "resetCameraDefault3d",
            "resetCameraLastSave3d", "resetGeo",
            "resetSankeyGroup", "resetScale2d", "resetViewMap",
            "resetViews", "resetcameradefault",
            "resetcameralastsave", "resetsankeygroup",
            "resetscale", "resetview", "resetviews", "select",
            "select2d", "sendChartToCloud", "sendcharttocloud",
            "tableRotation", "tablerotation", "toImage",
            "toggleHover", "toggleSpikelines", "togglehover",
            "togglespikelines", "toimage", "zoom", "zoom2d",
            "zoom3d", "zoomIn2d", "zoomInGeo", "zoomInMap",
            "zoomOut2d", "zoomOutGeo", "zoomOutMap", "zoomin",
            "zoomout".
        uirevision
            Controls persistence of user-driven changes related to
            the modebar, including `hovermode`, `dragmode`, and
            `showspikes` at both the root level and inside
            subplots. Defaults to `layout.uirevision`.

        Returns
        -------
        Modebar
        """
        super().__init__("modebar")
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
The first argument to the plotly.graph_objs.layout.Modebar
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Modebar`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("activecolor", arg, activecolor)
        self._set_property("add", arg, add)
        self._set_property("bgcolor", arg, bgcolor)
        self._set_property("color", arg, color)
        self._set_property("orientation", arg, orientation)
        self._set_property("remove", arg, remove)
        self._set_property("uirevision", arg, uirevision)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
