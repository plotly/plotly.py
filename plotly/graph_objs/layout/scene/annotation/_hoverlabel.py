#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Hoverlabel(_BaseLayoutHierarchyType):
    _parent_path_str = "layout.scene.annotation"
    _path_str = "layout.scene.annotation.hoverlabel"
    _valid_props = {"bgcolor", "bordercolor", "font"}

    @property
    def bgcolor(self):
        """
        Sets the background color of the hover label. By default uses
        the annotation's `bgcolor` made opaque, or white if it was
        transparent.

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
    def bordercolor(self):
        """
        Sets the border color of the hover label. By default uses
        either dark grey or white, for maximum contrast with
        `hoverlabel.bgcolor`.

        The 'bordercolor' property is a color and may be specified as a string in the following formats:
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
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    @property
    def font(self):
        """
        Sets the hover label text font. By default uses the global
        hover font and size, with color from `hoverlabel.bordercolor`.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.annotation.hoverlabel.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.annotation.hoverlabel.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Sets the background color of the hover label. By
            default uses the annotation's `bgcolor` made opaque, or
            white if it was transparent.
        bordercolor
            Sets the border color of the hover label. By default
            uses either dark grey or white, for maximum contrast
            with `hoverlabel.bgcolor`.
        font
            Sets the hover label text font. By default uses the
            global hover font and size, with color from
            `hoverlabel.bordercolor`.
        """

    def __init__(self, arg=None, bgcolor=None, bordercolor=None, font=None, **kwargs):
        """
        Construct a new Hoverlabel object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.scene.a
            nnotation.Hoverlabel`
        bgcolor
            Sets the background color of the hover label. By
            default uses the annotation's `bgcolor` made opaque, or
            white if it was transparent.
        bordercolor
            Sets the border color of the hover label. By default
            uses either dark grey or white, for maximum contrast
            with `hoverlabel.bgcolor`.
        font
            Sets the hover label text font. By default uses the
            global hover font and size, with color from
            `hoverlabel.bordercolor`.

        Returns
        -------
        Hoverlabel
        """
        super().__init__("hoverlabel")
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
The first argument to the plotly.graph_objs.layout.scene.annotation.Hoverlabel
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.scene.annotation.Hoverlabel`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("bgcolor", arg, bgcolor)
        self._set_property("bordercolor", arg, bordercolor)
        self._set_property("font", arg, font)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
