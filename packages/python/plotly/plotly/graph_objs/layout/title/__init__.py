from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Pad(_BaseLayoutHierarchyType):

    # b
    # -
    @property
    def b(self):
        """
        The amount of padding (in px) along the bottom of the
        component.
    
        The 'b' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["b"]

    @b.setter
    def b(self, val):
        self["b"] = val

    # l
    # -
    @property
    def l(self):
        """
        The amount of padding (in px) on the left side of the
        component.
    
        The 'l' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["l"]

    @l.setter
    def l(self, val):
        self["l"] = val

    # r
    # -
    @property
    def r(self):
        """
        The amount of padding (in px) on the right side of the
        component.
    
        The 'r' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["r"]

    @r.setter
    def r(self, val):
        self["r"] = val

    # t
    # -
    @property
    def t(self):
        """
        The amount of padding (in px) along the top of the component.
    
        The 't' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["t"]

    @t.setter
    def t(self, val):
        self["t"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.title"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        b
            The amount of padding (in px) along the bottom of the
            component.
        l
            The amount of padding (in px) on the left side of the
            component.
        r
            The amount of padding (in px) on the right side of the
            component.
        t
            The amount of padding (in px) along the top of the
            component.
        """

    def __init__(self, arg=None, b=None, l=None, r=None, t=None, **kwargs):
        """
        Construct a new Pad object
        
        Sets the padding of the title. Each padding value only applies
        when the corresponding `xanchor`/`yanchor` value is set
        accordingly. E.g. for left padding to take effect, `xanchor`
        must be set to "left". The same rule applies if
        `xanchor`/`yanchor` is determined automatically. Padding is
        muted if the respective anchor value is "middle*/*center".

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.title.Pad`
        b
            The amount of padding (in px) along the bottom of the
            component.
        l
            The amount of padding (in px) on the left side of the
            component.
        r
            The amount of padding (in px) on the right side of the
            component.
        t
            The amount of padding (in px) along the top of the
            component.

        Returns
        -------
        Pad
        """
        super(Pad, self).__init__("pad")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.title.Pad 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.title.Pad`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.title import pad as v_pad

        # Initialize validators
        # ---------------------
        self._validators["b"] = v_pad.BValidator()
        self._validators["l"] = v_pad.LValidator()
        self._validators["r"] = v_pad.RValidator()
        self._validators["t"] = v_pad.TValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("b", None)
        self["b"] = b if b is not None else _v
        _v = arg.pop("l", None)
        self["l"] = l if l is not None else _v
        _v = arg.pop("r", None)
        self["r"] = r if r is not None else _v
        _v = arg.pop("t", None)
        self["t"] = t if t is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Font(_BaseLayoutHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # family
    # ------
    @property
    def family(self):
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser will only be able to apply a font if
        it is available on the system which it operates. Provide
        multiple font families, separated by commas, to indicate the
        preference in which to apply fonts if they aren't available on
        the system. The plotly service (at https://plot.ly or on-
        premise) generates images on a server, where only a select
        number of fonts are installed and supported. These include
        "Arial", "Balto", "Courier New", "Droid Sans",, "Droid Serif",
        "Droid Sans Mono", "Gravitas One", "Old Standard TT", "Open
        Sans", "Overpass", "PT Sans Narrow", "Raleway", "Times New
        Roman".
    
        The 'family' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.title"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include "Arial", "Balto", "Courier New", "Droid Sans",,
            "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old
            Standard TT", "Open Sans", "Overpass", "PT Sans
            Narrow", "Raleway", "Times New Roman".
        size

        """

    def __init__(self, arg=None, color=None, family=None, size=None, **kwargs):
        """
        Construct a new Font object
        
        Sets the title font. Note that the title's font used to be
        customized by the now deprecated `titlefont` attribute.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.title.Font`
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include "Arial", "Balto", "Courier New", "Droid Sans",,
            "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old
            Standard TT", "Open Sans", "Overpass", "PT Sans
            Narrow", "Raleway", "Times New Roman".
        size


        Returns
        -------
        Font
        """
        super(Font, self).__init__("font")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.title.Font 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.title.Font`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.title import font as v_font

        # Initialize validators
        # ---------------------
        self._validators["color"] = v_font.ColorValidator()
        self._validators["family"] = v_font.FamilyValidator()
        self._validators["size"] = v_font.SizeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("family", None)
        self["family"] = family if family is not None else _v
        _v = arg.pop("size", None)
        self["size"] = size if size is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = ["Font", "Pad"]
