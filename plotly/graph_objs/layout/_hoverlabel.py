from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Hoverlabel(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.hoverlabel"
    _valid_props = {
        "align",
        "bgcolor",
        "bordercolor",
        "font",
        "grouptitlefont",
        "namelength",
    }

    @property
    def align(self):
        """
        Sets the horizontal alignment of the text content within hover
        label box. Has an effect only if the hover label text spans
        more two or more lines

        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'right', 'auto']

        Returns
        -------
        Any
        """
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    @property
    def bgcolor(self):
        """
        Sets the background color of all hover labels on graph

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
        Sets the border color of all hover labels on graph.

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
    def font(self):
        """
        Sets the default hover label font used by all traces on the
        graph.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.hoverlabel.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.layout.hoverlabel.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def grouptitlefont(self):
        """
        Sets the font for group titles in hover (unified modes).
        Defaults to `hoverlabel.font`.

        The 'grouptitlefont' property is an instance of Grouptitlefont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.hoverlabel.Grouptitlefont`
          - A dict of string/value properties that will be passed
            to the Grouptitlefont constructor

        Returns
        -------
        plotly.graph_objs.layout.hoverlabel.Grouptitlefont
        """
        return self["grouptitlefont"]

    @grouptitlefont.setter
    def grouptitlefont(self, val):
        self["grouptitlefont"] = val

    @property
    def namelength(self):
        """
        Sets the default length (in number of characters) of the trace
        name in the hover labels for all traces. -1 shows the whole
        name regardless of length. 0-3 shows the first 0-3 characters,
        and an integer >3 will show the whole name if it is less than
        that many characters, but if it is longer, will truncate to
        `namelength - 3` characters and add an ellipsis.

        The 'namelength' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [-1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["namelength"]

    @namelength.setter
    def namelength(self, val):
        self["namelength"] = val

    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        bgcolor
            Sets the background color of all hover labels on graph
        bordercolor
            Sets the border color of all hover labels on graph.
        font
            Sets the default hover label font used by all traces on
            the graph.
        grouptitlefont
            Sets the font for group titles in hover (unified
            modes). Defaults to `hoverlabel.font`.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.
        """

    def __init__(
        self,
        arg=None,
        align: Any | None = None,
        bgcolor: str | None = None,
        bordercolor: str | None = None,
        font: None | None = None,
        grouptitlefont: None | None = None,
        namelength: int | None = None,
        **kwargs,
    ):
        """
        Construct a new Hoverlabel object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.Hoverlabel`
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        bgcolor
            Sets the background color of all hover labels on graph
        bordercolor
            Sets the border color of all hover labels on graph.
        font
            Sets the default hover label font used by all traces on
            the graph.
        grouptitlefont
            Sets the font for group titles in hover (unified
            modes). Defaults to `hoverlabel.font`.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.

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
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.Hoverlabel
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Hoverlabel`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("align", arg, align)
        self._init_provided("bgcolor", arg, bgcolor)
        self._init_provided("bordercolor", arg, bordercolor)
        self._init_provided("font", arg, font)
        self._init_provided("grouptitlefont", arg, grouptitlefont)
        self._init_provided("namelength", arg, namelength)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
