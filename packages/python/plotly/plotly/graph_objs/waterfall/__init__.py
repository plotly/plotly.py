from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Totals(_BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.waterfall.totals.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of all intermediate sums
                    and total values.
                line
                    :class:`plotly.graph_objects.waterfall.totals.m
                    arker.Line` instance or dict with compatible
                    properties

        Returns
        -------
        plotly.graph_objs.waterfall.totals.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "waterfall"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            :class:`plotly.graph_objects.waterfall.totals.Marker`
            instance or dict with compatible properties
        """

    def __init__(self, arg=None, marker=None, **kwargs):
        """
        Construct a new Totals object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Totals`
        marker
            :class:`plotly.graph_objects.waterfall.totals.Marker`
            instance or dict with compatible properties

        Returns
        -------
        Totals
        """
        super(Totals, self).__init__("totals")

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
The first argument to the plotly.graph_objs.waterfall.Totals 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Totals`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import totals as v_totals

        # Initialize validators
        # ---------------------
        self._validators["marker"] = v_totals.MarkerValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("marker", None)
        self["marker"] = marker if marker is not None else _v

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
        Sets the source reference on Chart Studio Cloud for  color .
    
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
        the system. The Chart Studio Cloud (at https://chart-
        studio.plotly.com or on-premise) generates images on a server,
        where only a select number of fonts are installed and
        supported. These include "Arial", "Balto", "Courier New",
        "Droid Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
        One", "Old Standard TT", "Open Sans", "Overpass", "PT Sans
        Narrow", "Raleway", "Times New Roman".
    
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
        Sets the source reference on Chart Studio Cloud for  family .
    
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
        Sets the source reference on Chart Studio Cloud for  size .
    
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
        return "waterfall"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            color .
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            family .
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            size .
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
        
        Sets the font used for `text`.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Textfont`
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            color .
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            family .
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            size .

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
The first argument to the plotly.graph_objs.waterfall.Textfont 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Textfont`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import textfont as v_textfont

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
        stream. See https://chart-studio.plotly.com/settings for more
        details.
    
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
        return "waterfall"

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
            a stream. See https://chart-studio.plotly.com/settings
            for more details.
        """

    def __init__(self, arg=None, maxpoints=None, token=None, **kwargs):
        """
        Construct a new Stream object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Stream`
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://chart-studio.plotly.com/settings
            for more details.

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
The first argument to the plotly.graph_objs.waterfall.Stream 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Stream`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import stream as v_stream

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
        Sets the source reference on Chart Studio Cloud for  color .
    
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
        the system. The Chart Studio Cloud (at https://chart-
        studio.plotly.com or on-premise) generates images on a server,
        where only a select number of fonts are installed and
        supported. These include "Arial", "Balto", "Courier New",
        "Droid Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
        One", "Old Standard TT", "Open Sans", "Overpass", "PT Sans
        Narrow", "Raleway", "Times New Roman".
    
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
        Sets the source reference on Chart Studio Cloud for  family .
    
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
        Sets the source reference on Chart Studio Cloud for  size .
    
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
        return "waterfall"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            color .
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            family .
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            size .
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
        
        Sets the font used for `text` lying outside the bar.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Outsidetextfont`
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            color .
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            family .
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            size .

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
The first argument to the plotly.graph_objs.waterfall.Outsidetextfont 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Outsidetextfont`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import outsidetextfont as v_outsidetextfont

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
        Sets the source reference on Chart Studio Cloud for  color .
    
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
        the system. The Chart Studio Cloud (at https://chart-
        studio.plotly.com or on-premise) generates images on a server,
        where only a select number of fonts are installed and
        supported. These include "Arial", "Balto", "Courier New",
        "Droid Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
        One", "Old Standard TT", "Open Sans", "Overpass", "PT Sans
        Narrow", "Raleway", "Times New Roman".
    
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
        Sets the source reference on Chart Studio Cloud for  family .
    
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
        Sets the source reference on Chart Studio Cloud for  size .
    
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
        return "waterfall"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            color .
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            family .
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            size .
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
        
        Sets the font used for `text` lying inside the bar.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Insidetextfont`
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            color .
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            family .
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            size .

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
The first argument to the plotly.graph_objs.waterfall.Insidetextfont 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Insidetextfont`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import insidetextfont as v_insidetextfont

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


class Increasing(_BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.waterfall.increasing.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of all increasing values.
                line
                    :class:`plotly.graph_objects.waterfall.increasi
                    ng.marker.Line` instance or dict with
                    compatible properties

        Returns
        -------
        plotly.graph_objs.waterfall.increasing.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "waterfall"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            :class:`plotly.graph_objects.waterfall.increasing.Marke
            r` instance or dict with compatible properties
        """

    def __init__(self, arg=None, marker=None, **kwargs):
        """
        Construct a new Increasing object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Increasing`
        marker
            :class:`plotly.graph_objects.waterfall.increasing.Marke
            r` instance or dict with compatible properties

        Returns
        -------
        Increasing
        """
        super(Increasing, self).__init__("increasing")

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
The first argument to the plotly.graph_objs.waterfall.Increasing 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Increasing`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import increasing as v_increasing

        # Initialize validators
        # ---------------------
        self._validators["marker"] = v_increasing.MarkerValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("marker", None)
        self["marker"] = marker if marker is not None else _v

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
        Sets the source reference on Chart Studio Cloud for  align .
    
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
        Sets the source reference on Chart Studio Cloud for  bgcolor .
    
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
        Sets the source reference on Chart Studio Cloud for
        bordercolor .
    
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
          - An instance of :class:`plotly.graph_objs.waterfall.hoverlabel.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for  color .
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                familysrc
                    Sets the source reference on Chart Studio Cloud
                    for  family .
                size
    
                sizesrc
                    Sets the source reference on Chart Studio Cloud
                    for  size .

        Returns
        -------
        plotly.graph_objs.waterfall.hoverlabel.Font
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
        Sets the source reference on Chart Studio Cloud for  namelength
        .
    
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
        return "waterfall"

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
            Sets the source reference on Chart Studio Cloud for
            align .
        bgcolor
            Sets the background color of the hover labels for this
            trace
        bgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            bgcolor .
        bordercolor
            Sets the border color of the hover labels for this
            trace.
        bordercolorsrc
            Sets the source reference on Chart Studio Cloud for
            bordercolor .
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
            Sets the source reference on Chart Studio Cloud for
            namelength .
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
            an instance of
            :class:`plotly.graph_objs.waterfall.Hoverlabel`
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        alignsrc
            Sets the source reference on Chart Studio Cloud for
            align .
        bgcolor
            Sets the background color of the hover labels for this
            trace
        bgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            bgcolor .
        bordercolor
            Sets the border color of the hover labels for this
            trace.
        bordercolorsrc
            Sets the source reference on Chart Studio Cloud for
            bordercolor .
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
            Sets the source reference on Chart Studio Cloud for
            namelength .

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
The first argument to the plotly.graph_objs.waterfall.Hoverlabel 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Hoverlabel`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import hoverlabel as v_hoverlabel

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


class Decreasing(_BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.waterfall.decreasing.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of all decreasing values.
                line
                    :class:`plotly.graph_objects.waterfall.decreasi
                    ng.marker.Line` instance or dict with
                    compatible properties

        Returns
        -------
        plotly.graph_objs.waterfall.decreasing.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "waterfall"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            :class:`plotly.graph_objects.waterfall.decreasing.Marke
            r` instance or dict with compatible properties
        """

    def __init__(self, arg=None, marker=None, **kwargs):
        """
        Construct a new Decreasing object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Decreasing`
        marker
            :class:`plotly.graph_objects.waterfall.decreasing.Marke
            r` instance or dict with compatible properties

        Returns
        -------
        Decreasing
        """
        super(Decreasing, self).__init__("decreasing")

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
The first argument to the plotly.graph_objs.waterfall.Decreasing 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Decreasing`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import decreasing as v_decreasing

        # Initialize validators
        # ---------------------
        self._validators["marker"] = v_decreasing.MarkerValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("marker", None)
        self["marker"] = marker if marker is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Connector(_BaseTraceHierarchyType):

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.waterfall.connector.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the line color.
                dash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                width
                    Sets the line width (in px).

        Returns
        -------
        plotly.graph_objs.waterfall.connector.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # mode
    # ----
    @property
    def mode(self):
        """
        Sets the shape of connector lines.
    
        The 'mode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['spanning', 'between']

        Returns
        -------
        Any
        """
        return self["mode"]

    @mode.setter
    def mode(self, val):
        self["mode"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines if connector lines are drawn.
    
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

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "waterfall"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        line
            :class:`plotly.graph_objects.waterfall.connector.Line`
            instance or dict with compatible properties
        mode
            Sets the shape of connector lines.
        visible
            Determines if connector lines are drawn.
        """

    def __init__(self, arg=None, line=None, mode=None, visible=None, **kwargs):
        """
        Construct a new Connector object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.waterfall.Connector`
        line
            :class:`plotly.graph_objects.waterfall.connector.Line`
            instance or dict with compatible properties
        mode
            Sets the shape of connector lines.
        visible
            Determines if connector lines are drawn.

        Returns
        -------
        Connector
        """
        super(Connector, self).__init__("connector")

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
The first argument to the plotly.graph_objs.waterfall.Connector 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.waterfall.Connector`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.waterfall import connector as v_connector

        # Initialize validators
        # ---------------------
        self._validators["line"] = v_connector.LineValidator()
        self._validators["mode"] = v_connector.ModeValidator()
        self._validators["visible"] = v_connector.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("line", None)
        self["line"] = line if line is not None else _v
        _v = arg.pop("mode", None)
        self["mode"] = mode if mode is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = [
    "Connector",
    "Decreasing",
    "Hoverlabel",
    "Increasing",
    "Insidetextfont",
    "Outsidetextfont",
    "Stream",
    "Textfont",
    "Totals",
    "connector",
    "decreasing",
    "hoverlabel",
    "increasing",
    "totals",
]

from plotly.graph_objs.waterfall import totals
from plotly.graph_objs.waterfall import increasing
from plotly.graph_objs.waterfall import hoverlabel
from plotly.graph_objs.waterfall import decreasing
from plotly.graph_objs.waterfall import connector
