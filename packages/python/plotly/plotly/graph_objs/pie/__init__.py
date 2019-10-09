from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Title(_BaseTraceHierarchyType):

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font used for `title`. Note that the title's font used
        to be set by the now deprecated `titlefont` attribute.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.pie.title.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include "Arial",
                    "Balto", "Courier New", "Droid Sans",, "Droid
                    Serif", "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                familysrc
                    Sets the source reference on plot.ly for
                    family .
                size
    
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .

        Returns
        -------
        plotly.graph_objs.pie.title.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # position
    # --------
    @property
    def position(self):
        """
        Specifies the location of the `title`. Note that the title's
        position used to be set by the now deprecated `titleposition`
        attribute.
    
        The 'position' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle center',
                'bottom left', 'bottom center', 'bottom right']

        Returns
        -------
        Any
        """
        return self["position"]

    @position.setter
    def position(self, val):
        self["position"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of the chart. If it is empty, no title is
        displayed. Note that before the existence of `title.text`, the
        title's contents used to be defined as the `title` attribute
        itself. This behavior has been deprecated.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "pie"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets the font used for `title`. Note that the title's
            font used to be set by the now deprecated `titlefont`
            attribute.
        position
            Specifies the location of the `title`. Note that the
            title's position used to be set by the now deprecated
            `titleposition` attribute.
        text
            Sets the title of the chart. If it is empty, no title
            is displayed. Note that before the existence of
            `title.text`, the title's contents used to be defined
            as the `title` attribute itself. This behavior has been
            deprecated.
        """

    def __init__(self, arg=None, font=None, position=None, text=None, **kwargs):
        """
        Construct a new Title object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Title
        font
            Sets the font used for `title`. Note that the title's
            font used to be set by the now deprecated `titlefont`
            attribute.
        position
            Specifies the location of the `title`. Note that the
            title's position used to be set by the now deprecated
            `titleposition` attribute.
        text
            Sets the title of the chart. If it is empty, no title
            is displayed. Note that before the existence of
            `title.text`, the title's contents used to be defined
            as the `title` attribute itself. This behavior has been
            deprecated.

        Returns
        -------
        Title
        """
        super(Title, self).__init__("title")

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
The first argument to the plotly.graph_objs.pie.Title 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Title"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.pie import title as v_title

        # Initialize validators
        # ---------------------
        self._validators["font"] = v_title.FontValidator()
        self._validators["position"] = v_title.PositionValidator()
        self._validators["text"] = v_title.TextValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("position", None)
        self["position"] = position if position is not None else _v
        _v = arg.pop("text", None)
        self["text"] = text if text is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Textfont(_BaseTraceHierarchyType):

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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
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
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

    # familysrc
    # ---------
    @property
    def familysrc(self):
        """
        Sets the source reference on plot.ly for  family .
    
        The 'familysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["familysrc"]

    @familysrc.setter
    def familysrc(self, val):
        self["familysrc"] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # sizesrc
    # -------
    @property
    def sizesrc(self):
        """
        Sets the source reference on plot.ly for  size .
    
        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["sizesrc"]

    @sizesrc.setter
    def sizesrc(self, val):
        self["sizesrc"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "pie"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        colorsrc
            Sets the source reference on plot.ly for  color .
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
        familysrc
            Sets the source reference on plot.ly for  family .
        size

        sizesrc
            Sets the source reference on plot.ly for  size .
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        family=None,
        familysrc=None,
        size=None,
        sizesrc=None,
        **kwargs
    ):
        """
        Construct a new Textfont object
        
        Sets the font used for `textinfo`.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Textfont
        color

        colorsrc
            Sets the source reference on plot.ly for  color .
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
        familysrc
            Sets the source reference on plot.ly for  family .
        size

        sizesrc
            Sets the source reference on plot.ly for  size .

        Returns
        -------
        Textfont
        """
        super(Textfont, self).__init__("textfont")

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
The first argument to the plotly.graph_objs.pie.Textfont 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Textfont"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.pie import textfont as v_textfont

        # Initialize validators
        # ---------------------
        self._validators["color"] = v_textfont.ColorValidator()
        self._validators["colorsrc"] = v_textfont.ColorsrcValidator()
        self._validators["family"] = v_textfont.FamilyValidator()
        self._validators["familysrc"] = v_textfont.FamilysrcValidator()
        self._validators["size"] = v_textfont.SizeValidator()
        self._validators["sizesrc"] = v_textfont.SizesrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("colorsrc", None)
        self["colorsrc"] = colorsrc if colorsrc is not None else _v
        _v = arg.pop("family", None)
        self["family"] = family if family is not None else _v
        _v = arg.pop("familysrc", None)
        self["familysrc"] = familysrc if familysrc is not None else _v
        _v = arg.pop("size", None)
        self["size"] = size if size is not None else _v
        _v = arg.pop("sizesrc", None)
        self["sizesrc"] = sizesrc if sizesrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Stream(_BaseTraceHierarchyType):

    # maxpoints
    # ---------
    @property
    def maxpoints(self):
        """
        Sets the maximum number of points to keep on the plots from an
        incoming stream. If `maxpoints` is set to 50, only the newest
        50 points will be displayed on the plot.
    
        The 'maxpoints' property is a number and may be specified as:
          - An int or float in the interval [0, 10000]

        Returns
        -------
        int|float
        """
        return self["maxpoints"]

    @maxpoints.setter
    def maxpoints(self, val):
        self["maxpoints"] = val

    # token
    # -----
    @property
    def token(self):
        """
        The stream id number links a data trace on a plot with a
        stream. See https://plot.ly/settings for more details.
    
        The 'token' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["token"]

    @token.setter
    def token(self, val):
        self["token"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "pie"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.
        """

    def __init__(self, arg=None, maxpoints=None, token=None, **kwargs):
        """
        Construct a new Stream object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Stream
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.

        Returns
        -------
        Stream
        """
        super(Stream, self).__init__("stream")

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
The first argument to the plotly.graph_objs.pie.Stream 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Stream"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.pie import stream as v_stream

        # Initialize validators
        # ---------------------
        self._validators["maxpoints"] = v_stream.MaxpointsValidator()
        self._validators["token"] = v_stream.TokenValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("maxpoints", None)
        self["maxpoints"] = maxpoints if maxpoints is not None else _v
        _v = arg.pop("token", None)
        self["token"] = token if token is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Outsidetextfont(_BaseTraceHierarchyType):

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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
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
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

    # familysrc
    # ---------
    @property
    def familysrc(self):
        """
        Sets the source reference on plot.ly for  family .
    
        The 'familysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["familysrc"]

    @familysrc.setter
    def familysrc(self, val):
        self["familysrc"] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # sizesrc
    # -------
    @property
    def sizesrc(self):
        """
        Sets the source reference on plot.ly for  size .
    
        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["sizesrc"]

    @sizesrc.setter
    def sizesrc(self, val):
        self["sizesrc"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "pie"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        colorsrc
            Sets the source reference on plot.ly for  color .
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
        familysrc
            Sets the source reference on plot.ly for  family .
        size

        sizesrc
            Sets the source reference on plot.ly for  size .
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        family=None,
        familysrc=None,
        size=None,
        sizesrc=None,
        **kwargs
    ):
        """
        Construct a new Outsidetextfont object
        
        Sets the font used for `textinfo` lying outside the sector.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Outsidetextfont
        color

        colorsrc
            Sets the source reference on plot.ly for  color .
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
        familysrc
            Sets the source reference on plot.ly for  family .
        size

        sizesrc
            Sets the source reference on plot.ly for  size .

        Returns
        -------
        Outsidetextfont
        """
        super(Outsidetextfont, self).__init__("outsidetextfont")

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
The first argument to the plotly.graph_objs.pie.Outsidetextfont 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Outsidetextfont"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.pie import outsidetextfont as v_outsidetextfont

        # Initialize validators
        # ---------------------
        self._validators["color"] = v_outsidetextfont.ColorValidator()
        self._validators["colorsrc"] = v_outsidetextfont.ColorsrcValidator()
        self._validators["family"] = v_outsidetextfont.FamilyValidator()
        self._validators["familysrc"] = v_outsidetextfont.FamilysrcValidator()
        self._validators["size"] = v_outsidetextfont.SizeValidator()
        self._validators["sizesrc"] = v_outsidetextfont.SizesrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("colorsrc", None)
        self["colorsrc"] = colorsrc if colorsrc is not None else _v
        _v = arg.pop("family", None)
        self["family"] = family if family is not None else _v
        _v = arg.pop("familysrc", None)
        self["familysrc"] = familysrc if familysrc is not None else _v
        _v = arg.pop("size", None)
        self["size"] = size if size is not None else _v
        _v = arg.pop("sizesrc", None)
        self["sizesrc"] = sizesrc if sizesrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    # colors
    # ------
    @property
    def colors(self):
        """
        Sets the color of each sector. If not specified, the default
        trace color set is used to pick the sector colors.
    
        The 'colors' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["colors"]

    @colors.setter
    def colors(self, val):
        self["colors"] = val

    # colorssrc
    # ---------
    @property
    def colorssrc(self):
        """
        Sets the source reference on plot.ly for  colors .
    
        The 'colorssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["colorssrc"]

    @colorssrc.setter
    def colorssrc(self, val):
        self["colorssrc"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.pie.marker.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the line enclosing each
                    sector.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                width
                    Sets the width (in px) of the line enclosing
                    each sector.
                widthsrc
                    Sets the source reference on plot.ly for  width
                    .

        Returns
        -------
        plotly.graph_objs.pie.marker.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "pie"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        colors
            Sets the color of each sector. If not specified, the
            default trace color set is used to pick the sector
            colors.
        colorssrc
            Sets the source reference on plot.ly for  colors .
        line
            plotly.graph_objects.pie.marker.Line instance or dict
            with compatible properties
        """

    def __init__(self, arg=None, colors=None, colorssrc=None, line=None, **kwargs):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Marker
        colors
            Sets the color of each sector. If not specified, the
            default trace color set is used to pick the sector
            colors.
        colorssrc
            Sets the source reference on plot.ly for  colors .
        line
            plotly.graph_objects.pie.marker.Line instance or dict
            with compatible properties

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__("marker")

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
The first argument to the plotly.graph_objs.pie.Marker 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Marker"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.pie import marker as v_marker

        # Initialize validators
        # ---------------------
        self._validators["colors"] = v_marker.ColorsValidator()
        self._validators["colorssrc"] = v_marker.ColorssrcValidator()
        self._validators["line"] = v_marker.LineValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("colors", None)
        self["colors"] = colors if colors is not None else _v
        _v = arg.pop("colorssrc", None)
        self["colorssrc"] = colorssrc if colorssrc is not None else _v
        _v = arg.pop("line", None)
        self["line"] = line if line is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Insidetextfont(_BaseTraceHierarchyType):

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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
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
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

    # familysrc
    # ---------
    @property
    def familysrc(self):
        """
        Sets the source reference on plot.ly for  family .
    
        The 'familysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["familysrc"]

    @familysrc.setter
    def familysrc(self, val):
        self["familysrc"] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # sizesrc
    # -------
    @property
    def sizesrc(self):
        """
        Sets the source reference on plot.ly for  size .
    
        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["sizesrc"]

    @sizesrc.setter
    def sizesrc(self, val):
        self["sizesrc"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "pie"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        colorsrc
            Sets the source reference on plot.ly for  color .
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
        familysrc
            Sets the source reference on plot.ly for  family .
        size

        sizesrc
            Sets the source reference on plot.ly for  size .
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        family=None,
        familysrc=None,
        size=None,
        sizesrc=None,
        **kwargs
    ):
        """
        Construct a new Insidetextfont object
        
        Sets the font used for `textinfo` lying inside the sector.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Insidetextfont
        color

        colorsrc
            Sets the source reference on plot.ly for  color .
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
        familysrc
            Sets the source reference on plot.ly for  family .
        size

        sizesrc
            Sets the source reference on plot.ly for  size .

        Returns
        -------
        Insidetextfont
        """
        super(Insidetextfont, self).__init__("insidetextfont")

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
The first argument to the plotly.graph_objs.pie.Insidetextfont 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Insidetextfont"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.pie import insidetextfont as v_insidetextfont

        # Initialize validators
        # ---------------------
        self._validators["color"] = v_insidetextfont.ColorValidator()
        self._validators["colorsrc"] = v_insidetextfont.ColorsrcValidator()
        self._validators["family"] = v_insidetextfont.FamilyValidator()
        self._validators["familysrc"] = v_insidetextfont.FamilysrcValidator()
        self._validators["size"] = v_insidetextfont.SizeValidator()
        self._validators["sizesrc"] = v_insidetextfont.SizesrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("colorsrc", None)
        self["colorsrc"] = colorsrc if colorsrc is not None else _v
        _v = arg.pop("family", None)
        self["family"] = family if family is not None else _v
        _v = arg.pop("familysrc", None)
        self["familysrc"] = familysrc if familysrc is not None else _v
        _v = arg.pop("size", None)
        self["size"] = size if size is not None else _v
        _v = arg.pop("sizesrc", None)
        self["sizesrc"] = sizesrc if sizesrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Hoverlabel(_BaseTraceHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the text content within hover
        label box. Has an effect only if the hover label text spans
        more two or more lines
    
        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'right', 'auto']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    # alignsrc
    # --------
    @property
    def alignsrc(self):
        """
        Sets the source reference on plot.ly for  align .
    
        The 'alignsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["alignsrc"]

    @alignsrc.setter
    def alignsrc(self, val):
        self["alignsrc"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the hover labels for this trace
    
        The 'bgcolor' property is a color and may be specified as:
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bgcolorsrc
    # ----------
    @property
    def bgcolorsrc(self):
        """
        Sets the source reference on plot.ly for  bgcolor .
    
        The 'bgcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["bgcolorsrc"]

    @bgcolorsrc.setter
    def bgcolorsrc(self, val):
        self["bgcolorsrc"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the border color of the hover labels for this trace.
    
        The 'bordercolor' property is a color and may be specified as:
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # bordercolorsrc
    # --------------
    @property
    def bordercolorsrc(self):
        """
        Sets the source reference on plot.ly for  bordercolor .
    
        The 'bordercolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["bordercolorsrc"]

    @bordercolorsrc.setter
    def bordercolorsrc(self, val):
        self["bordercolorsrc"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font used in hover labels.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.pie.hoverlabel.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include "Arial",
                    "Balto", "Courier New", "Droid Sans",, "Droid
                    Serif", "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                familysrc
                    Sets the source reference on plot.ly for
                    family .
                size
    
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .

        Returns
        -------
        plotly.graph_objs.pie.hoverlabel.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # namelength
    # ----------
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
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|numpy.ndarray
        """
        return self["namelength"]

    @namelength.setter
    def namelength(self, val):
        self["namelength"] = val

    # namelengthsrc
    # -------------
    @property
    def namelengthsrc(self):
        """
        Sets the source reference on plot.ly for  namelength .
    
        The 'namelengthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["namelengthsrc"]

    @namelengthsrc.setter
    def namelengthsrc(self, val):
        self["namelengthsrc"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "pie"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        alignsrc
            Sets the source reference on plot.ly for  align .
        bgcolor
            Sets the background color of the hover labels for this
            trace
        bgcolorsrc
            Sets the source reference on plot.ly for  bgcolor .
        bordercolor
            Sets the border color of the hover labels for this
            trace.
        bordercolorsrc
            Sets the source reference on plot.ly for  bordercolor .
        font
            Sets the font used in hover labels.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.
        namelengthsrc
            Sets the source reference on plot.ly for  namelength .
        """

    def __init__(
        self,
        arg=None,
        align=None,
        alignsrc=None,
        bgcolor=None,
        bgcolorsrc=None,
        bordercolor=None,
        bordercolorsrc=None,
        font=None,
        namelength=None,
        namelengthsrc=None,
        **kwargs
    ):
        """
        Construct a new Hoverlabel object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Hoverlabel
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        alignsrc
            Sets the source reference on plot.ly for  align .
        bgcolor
            Sets the background color of the hover labels for this
            trace
        bgcolorsrc
            Sets the source reference on plot.ly for  bgcolor .
        bordercolor
            Sets the border color of the hover labels for this
            trace.
        bordercolorsrc
            Sets the source reference on plot.ly for  bordercolor .
        font
            Sets the font used in hover labels.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.
        namelengthsrc
            Sets the source reference on plot.ly for  namelength .

        Returns
        -------
        Hoverlabel
        """
        super(Hoverlabel, self).__init__("hoverlabel")

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
The first argument to the plotly.graph_objs.pie.Hoverlabel 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Hoverlabel"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.pie import hoverlabel as v_hoverlabel

        # Initialize validators
        # ---------------------
        self._validators["align"] = v_hoverlabel.AlignValidator()
        self._validators["alignsrc"] = v_hoverlabel.AlignsrcValidator()
        self._validators["bgcolor"] = v_hoverlabel.BgcolorValidator()
        self._validators["bgcolorsrc"] = v_hoverlabel.BgcolorsrcValidator()
        self._validators["bordercolor"] = v_hoverlabel.BordercolorValidator()
        self._validators["bordercolorsrc"] = v_hoverlabel.BordercolorsrcValidator()
        self._validators["font"] = v_hoverlabel.FontValidator()
        self._validators["namelength"] = v_hoverlabel.NamelengthValidator()
        self._validators["namelengthsrc"] = v_hoverlabel.NamelengthsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("align", None)
        self["align"] = align if align is not None else _v
        _v = arg.pop("alignsrc", None)
        self["alignsrc"] = alignsrc if alignsrc is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bgcolorsrc", None)
        self["bgcolorsrc"] = bgcolorsrc if bgcolorsrc is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("bordercolorsrc", None)
        self["bordercolorsrc"] = bordercolorsrc if bordercolorsrc is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("namelength", None)
        self["namelength"] = namelength if namelength is not None else _v
        _v = arg.pop("namelengthsrc", None)
        self["namelengthsrc"] = namelengthsrc if namelengthsrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Domain(_BaseTraceHierarchyType):

    # column
    # ------
    @property
    def column(self):
        """
        If there is a layout grid, use the domain for this column in
        the grid for this pie trace .
    
        The 'column' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["column"]

    @column.setter
    def column(self, val):
        self["column"] = val

    # row
    # ---
    @property
    def row(self):
        """
        If there is a layout grid, use the domain for this row in the
        grid for this pie trace .
    
        The 'row' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["row"]

    @row.setter
    def row(self, val):
        self["row"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the horizontal domain of this pie trace (in plot
        fraction).
    
        The 'x' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'x[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'x[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the vertical domain of this pie trace (in plot fraction).
    
        The 'y' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'y[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'y[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "pie"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        column
            If there is a layout grid, use the domain for this
            column in the grid for this pie trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this pie trace .
        x
            Sets the horizontal domain of this pie trace (in plot
            fraction).
        y
            Sets the vertical domain of this pie trace (in plot
            fraction).
        """

    def __init__(self, arg=None, column=None, row=None, x=None, y=None, **kwargs):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Domain
        column
            If there is a layout grid, use the domain for this
            column in the grid for this pie trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this pie trace .
        x
            Sets the horizontal domain of this pie trace (in plot
            fraction).
        y
            Sets the vertical domain of this pie trace (in plot
            fraction).

        Returns
        -------
        Domain
        """
        super(Domain, self).__init__("domain")

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
The first argument to the plotly.graph_objs.pie.Domain 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Domain"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.pie import domain as v_domain

        # Initialize validators
        # ---------------------
        self._validators["column"] = v_domain.ColumnValidator()
        self._validators["row"] = v_domain.RowValidator()
        self._validators["x"] = v_domain.XValidator()
        self._validators["y"] = v_domain.YValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("column", None)
        self["column"] = column if column is not None else _v
        _v = arg.pop("row", None)
        self["row"] = row if row is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = [
    "Domain",
    "Hoverlabel",
    "Insidetextfont",
    "Marker",
    "Outsidetextfont",
    "Stream",
    "Textfont",
    "Title",
    "hoverlabel",
    "marker",
    "title",
]

from plotly.graph_objs.pie import title
from plotly.graph_objs.pie import marker
from plotly.graph_objs.pie import hoverlabel
