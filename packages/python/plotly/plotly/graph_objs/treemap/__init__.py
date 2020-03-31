from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Tiling(_BaseTraceHierarchyType):

    # flip
    # ----
    @property
    def flip(self):
        """
        Determines if the positions obtained from solver are flipped on
        each axis.
    
        The 'flip' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y'] joined with '+' characters
            (e.g. 'x+y')

        Returns
        -------
        Any
        """
        return self["flip"]

    @flip.setter
    def flip(self, val):
        self["flip"] = val

    # packing
    # -------
    @property
    def packing(self):
        """
        Determines d3 treemap solver. For more info please refer to
        https://github.com/d3/d3-hierarchy#treemap-tiling
    
        The 'packing' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['squarify', 'binary', 'dice', 'slice', 'slice-dice',
                'dice-slice']

        Returns
        -------
        Any
        """
        return self["packing"]

    @packing.setter
    def packing(self, val):
        self["packing"] = val

    # pad
    # ---
    @property
    def pad(self):
        """
        Sets the inner padding (in px).
    
        The 'pad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    # squarifyratio
    # -------------
    @property
    def squarifyratio(self):
        """
        When using "squarify" `packing` algorithm, according to https:/
        /github.com/d3/d3-hierarchy/blob/master/README.md#squarify_rati
        o this option specifies the desired aspect ratio of the
        generated rectangles. The ratio must be specified as a number
        greater than or equal to one. Note that the orientation of the
        generated rectangles (tall or wide) is not implied by the
        ratio; for example, a ratio of two will attempt to produce a
        mixture of rectangles whose width:height ratio is either 2:1 or
        1:2. When using "squarify", unlike d3 which uses the Golden
        Ratio i.e. 1.618034, Plotly applies 1 to increase squares in
        treemap layouts.
    
        The 'squarifyratio' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self["squarifyratio"]

    @squarifyratio.setter
    def squarifyratio(self, val):
        self["squarifyratio"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "treemap"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        flip
            Determines if the positions obtained from solver are
            flipped on each axis.
        packing
            Determines d3 treemap solver. For more info please
            refer to https://github.com/d3/d3-hierarchy#treemap-
            tiling
        pad
            Sets the inner padding (in px).
        squarifyratio
            When using "squarify" `packing` algorithm, according to
            https://github.com/d3/d3-hierarchy/blob/master/README.m
            d#squarify_ratio this option specifies the desired
            aspect ratio of the generated rectangles. The ratio
            must be specified as a number greater than or equal to
            one. Note that the orientation of the generated
            rectangles (tall or wide) is not implied by the ratio;
            for example, a ratio of two will attempt to produce a
            mixture of rectangles whose width:height ratio is
            either 2:1 or 1:2. When using "squarify", unlike d3
            which uses the Golden Ratio i.e. 1.618034, Plotly
            applies 1 to increase squares in treemap layouts.
        """

    def __init__(
        self, arg=None, flip=None, packing=None, pad=None, squarifyratio=None, **kwargs
    ):
        """
        Construct a new Tiling object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.Tiling`
        flip
            Determines if the positions obtained from solver are
            flipped on each axis.
        packing
            Determines d3 treemap solver. For more info please
            refer to https://github.com/d3/d3-hierarchy#treemap-
            tiling
        pad
            Sets the inner padding (in px).
        squarifyratio
            When using "squarify" `packing` algorithm, according to
            https://github.com/d3/d3-hierarchy/blob/master/README.m
            d#squarify_ratio this option specifies the desired
            aspect ratio of the generated rectangles. The ratio
            must be specified as a number greater than or equal to
            one. Note that the orientation of the generated
            rectangles (tall or wide) is not implied by the ratio;
            for example, a ratio of two will attempt to produce a
            mixture of rectangles whose width:height ratio is
            either 2:1 or 1:2. When using "squarify", unlike d3
            which uses the Golden Ratio i.e. 1.618034, Plotly
            applies 1 to increase squares in treemap layouts.

        Returns
        -------
        Tiling
        """
        super(Tiling, self).__init__("tiling")

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
The first argument to the plotly.graph_objs.treemap.Tiling 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Tiling`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import tiling as v_tiling

        # Initialize validators
        # ---------------------
        self._validators["flip"] = v_tiling.FlipValidator()
        self._validators["packing"] = v_tiling.PackingValidator()
        self._validators["pad"] = v_tiling.PadValidator()
        self._validators["squarifyratio"] = v_tiling.SquarifyratioValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("flip", None)
        self["flip"] = flip if flip is not None else _v
        _v = arg.pop("packing", None)
        self["packing"] = packing if packing is not None else _v
        _v = arg.pop("pad", None)
        self["pad"] = pad if pad is not None else _v
        _v = arg.pop("squarifyratio", None)
        self["squarifyratio"] = squarifyratio if squarifyratio is not None else _v

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
        return "treemap"

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
        
        Sets the font used for `textinfo`.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.Textfont`
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
The first argument to the plotly.graph_objs.treemap.Textfont 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Textfont`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import textfont as v_textfont

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
        return "treemap"

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
            :class:`plotly.graph_objs.treemap.Stream`
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
The first argument to the plotly.graph_objs.treemap.Stream 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Stream`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import stream as v_stream

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


class Pathbar(_BaseTraceHierarchyType):

    # edgeshape
    # ---------
    @property
    def edgeshape(self):
        """
        Determines which shape is used for edges between `barpath`
        labels.
    
        The 'edgeshape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['>', '<', '|', '\\']
          - A string that matches one of the following regular expressions:
                ['']

        Returns
        -------
        Any
        """
        return self["edgeshape"]

    @edgeshape.setter
    def edgeshape(self, val):
        self["edgeshape"] = val

    # side
    # ----
    @property
    def side(self):
        """
        Determines on which side of the the treemap the `pathbar`
        should be presented.
    
        The 'side' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'bottom']

        Returns
        -------
        Any
        """
        return self["side"]

    @side.setter
    def side(self, val):
        self["side"] = val

    # textfont
    # --------
    @property
    def textfont(self):
        """
        Sets the font used inside `pathbar`.
    
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.pathbar.Textfont`
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
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
        plotly.graph_objs.treemap.pathbar.Textfont
        """
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        Sets the thickness of `pathbar` (in px). If not specified the
        `pathbar.textfont.size` is used with 3 pixles extra padding on
        each side.
    
        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [12, inf]

        Returns
        -------
        int|float
        """
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines if the path bar is drawn i.e. outside the trace
        `domain` and with one pixel gap.
    
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
        return "treemap"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        edgeshape
            Determines which shape is used for edges between
            `barpath` labels.
        side
            Determines on which side of the the treemap the
            `pathbar` should be presented.
        textfont
            Sets the font used inside `pathbar`.
        thickness
            Sets the thickness of `pathbar` (in px). If not
            specified the `pathbar.textfont.size` is used with 3
            pixles extra padding on each side.
        visible
            Determines if the path bar is drawn i.e. outside the
            trace `domain` and with one pixel gap.
        """

    def __init__(
        self,
        arg=None,
        edgeshape=None,
        side=None,
        textfont=None,
        thickness=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Pathbar object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.Pathbar`
        edgeshape
            Determines which shape is used for edges between
            `barpath` labels.
        side
            Determines on which side of the the treemap the
            `pathbar` should be presented.
        textfont
            Sets the font used inside `pathbar`.
        thickness
            Sets the thickness of `pathbar` (in px). If not
            specified the `pathbar.textfont.size` is used with 3
            pixles extra padding on each side.
        visible
            Determines if the path bar is drawn i.e. outside the
            trace `domain` and with one pixel gap.

        Returns
        -------
        Pathbar
        """
        super(Pathbar, self).__init__("pathbar")

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
The first argument to the plotly.graph_objs.treemap.Pathbar 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Pathbar`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import pathbar as v_pathbar

        # Initialize validators
        # ---------------------
        self._validators["edgeshape"] = v_pathbar.EdgeshapeValidator()
        self._validators["side"] = v_pathbar.SideValidator()
        self._validators["textfont"] = v_pathbar.TextfontValidator()
        self._validators["thickness"] = v_pathbar.ThicknessValidator()
        self._validators["visible"] = v_pathbar.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("edgeshape", None)
        self["edgeshape"] = edgeshape if edgeshape is not None else _v
        _v = arg.pop("side", None)
        self["side"] = side if side is not None else _v
        _v = arg.pop("textfont", None)
        self["textfont"] = textfont if textfont is not None else _v
        _v = arg.pop("thickness", None)
        self["thickness"] = thickness if thickness is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v

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
        return "treemap"

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
        
        Sets the font used for `textinfo` lying outside the sector.
        This option refers to the root of the hierarchy presented on
        top left corner of a treemap graph. Please note that if a
        hierarchy has multiple root nodes, this option won't have any
        effect and `insidetextfont` would be used.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.Outsidetextfont`
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
The first argument to the plotly.graph_objs.treemap.Outsidetextfont 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Outsidetextfont`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import outsidetextfont as v_outsidetextfont

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

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `marker.colorscale`. Has an effect only if colorsis set to a
        numerical array. In case `colorscale` is unspecified or
        `autocolorscale` is true, the default  palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.
    
        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autocolorscale"]

    @autocolorscale.setter
    def autocolorscale(self, val):
        self["autocolorscale"] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here colors) or the bounds set in
        `marker.cmin` and `marker.cmax`  Has an effect only if colorsis
        set to a numerical array. Defaults to `false` when
        `marker.cmin` and `marker.cmax` are set by the user.
    
        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["cauto"]

    @cauto.setter
    def cauto(self, val):
        self["cauto"] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Sets the upper bound of the color domain. Has an effect only if
        colorsis set to a numerical array. Value should have the same
        units as colors and if set, `marker.cmin` must be set as well.
    
        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmax"]

    @cmax.setter
    def cmax(self, val):
        self["cmax"] = val

    # cmid
    # ----
    @property
    def cmid(self):
        """
        Sets the mid-point of the color domain by scaling `marker.cmin`
        and/or `marker.cmax` to be equidistant to this point. Has an
        effect only if colorsis set to a numerical array. Value should
        have the same units as colors. Has no effect when
        `marker.cauto` is `false`.
    
        The 'cmid' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmid"]

    @cmid.setter
    def cmid(self, val):
        self["cmid"] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Sets the lower bound of the color domain. Has an effect only if
        colorsis set to a numerical array. Value should have the same
        units as colors and if set, `marker.cmax` must be set as well.
    
        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmin"]

    @cmin.setter
    def cmin(self, val):
        self["cmin"] = val

    # coloraxis
    # ---------
    @property
    def coloraxis(self):
        """
        Sets a reference to a shared color axis. References to these
        shared color axes are "coloraxis", "coloraxis2", "coloraxis3",
        etc. Settings for these shared color axes are set in the
        layout, under `layout.coloraxis`, `layout.coloraxis2`, etc.
        Note that multiple color scales can be linked to the same color
        axis.
    
        The 'coloraxis' property is an identifier of a particular
        subplot, of type 'coloraxis', that may be specified as the string 'coloraxis'
        optionally followed by an integer >= 1
        (e.g. 'coloraxis', 'coloraxis1', 'coloraxis2', 'coloraxis3', etc.)

        Returns
        -------
        str
        """
        return self["coloraxis"]

    @coloraxis.setter
    def coloraxis(self, val):
        self["coloraxis"] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.marker.ColorBar`
          - A dict of string/value properties that will be passed
            to the ColorBar constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the color of padded area.
                bordercolor
                    Sets the axis line color.
                borderwidth
                    Sets the width (in px) or the border enclosing
                    this color bar.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to "log" and "date"
                    axes. If the axis `type` is "log", then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. "log"
                    has several special values; "L<f>", where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use "D1" (all
                    digits) or "D2" (only 2 and 5). `tick0` is
                    ignored for "D1" and "D2". If the axis `type`
                    is "date", then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. "date" also has special values
                    "M<n>" gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to "2000-01-15" and `dtick` to "M3". To
                    set ticks every 4 years, set `dtick` to "M48"
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If "none", it appears as
                    1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                    "power", 1x10^9 (with 9 in a super script). If
                    "SI", 1G. If "B", 1B.
                len
                    Sets the length of the color bar This measure
                    excludes the padding of both ends. That is, the
                    color bar length is this length minus the
                    padding on both ends.
                lenmode
                    Determines whether this color bar's length
                    (i.e. the measure in the color variation
                    direction) is set in units of plot "fraction"
                    or in *pixels. Use `len` to set the value.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                outlinecolor
                    Sets the axis line color.
                outlinewidth
                    Sets the width (in px) of the axis line.
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If "all", all tick labels are displayed with a
                    prefix. If "first", only the first tick is
                    displayed with a prefix. If "last", only the
                    last tick is displayed with a suffix. If
                    "none", tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                thickness
                    Sets the thickness of the color bar This
                    measure excludes the size of the padding, ticks
                    and labels.
                thicknessmode
                    Determines whether this color bar's thickness
                    (i.e. the measure in the constant color
                    direction) is set in units of plot "fraction"
                    or in "pixels". Use `thickness` to set the
                    value.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    "log", then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is "date", it should be a date
                    string, like date data. If the axis `type` is
                    "category", it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the color bar's tick label font
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see:
                    https://github.com/d3/d3-3.x-api-
                    reference/blob/master/Formatting.md#d3_format
                    And for dates see:
                    https://github.com/d3/d3-3.x-api-
                    reference/blob/master/Time-Formatting.md#format
                    We add one item to d3's date formatter: "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                tickformatstops
                    A tuple of :class:`plotly.graph_objects.treemap
                    .marker.colorbar.Tickformatstop` instances or
                    dicts with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.dat
                    a.treemap.marker.colorbar.tickformatstopdefault
                    s), sets the default property values to use for
                    elements of
                    treemap.marker.colorbar.tickformatstops
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If "auto",
                    the number of ticks is set via `nticks`. If
                    "linear", the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` ("linear" is the default
                    value if `tick0` and `dtick` are provided). If
                    "array", the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    ("array" is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    "", this axis' ticks are not drawn. If
                    "outside" ("inside"), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to "array". Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on Chart Studio Cloud
                    for  ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to "array". Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on Chart Studio Cloud
                    for  tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    :class:`plotly.graph_objects.treemap.marker.col
                    orbar.Title` instance or dict with compatible
                    properties
                titlefont
                    Deprecated: Please use
                    treemap.marker.colorbar.title.font instead.
                    Sets this color bar's title font. Note that the
                    title's font used to be set by the now
                    deprecated `titlefont` attribute.
                titleside
                    Deprecated: Please use
                    treemap.marker.colorbar.title.side instead.
                    Determines the location of color bar's title
                    with respect to the color bar. Note that the
                    title's location used to be set by the now
                    deprecated `titleside` attribute.
                x
                    Sets the x position of the color bar (in plot
                    fraction).
                xanchor
                    Sets this color bar's horizontal position
                    anchor. This anchor binds the `x` position to
                    the "left", "center" or "right" of the color
                    bar.
                xpad
                    Sets the amount of padding (in px) along the x
                    direction.
                y
                    Sets the y position of the color bar (in plot
                    fraction).
                yanchor
                    Sets this color bar's vertical position anchor
                    This anchor binds the `y` position to the
                    "top", "middle" or "bottom" of the color bar.
                ypad
                    Sets the amount of padding (in px) along the y
                    direction.

        Returns
        -------
        plotly.graph_objs.treemap.marker.ColorBar
        """
        return self["colorbar"]

    @colorbar.setter
    def colorbar(self, val):
        self["colorbar"] = val

    # colors
    # ------
    @property
    def colors(self):
        """
        Sets the color of each sector of this trace. If not specified,
        the default trace color set is used to pick the sector colors.
    
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

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. Has an effect only if colorsis set to a
        numerical array. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use`marker.cmin` and
        `marker.cmax`. Alternatively, `colorscale` may be a palette
        name string of the following list: Greys,YlGnBu,Greens,YlOrRd,B
        luered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,Hot,Blackbod
        y,Earth,Electric,Viridis,Cividis.
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
                 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
                 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
                 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
                 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
                 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
                 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd'].
            Appending '_r' to a named colorscale reverses it.

        Returns
        -------
        str
        """
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

    # colorssrc
    # ---------
    @property
    def colorssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  colors .
    
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

    # depthfade
    # ---------
    @property
    def depthfade(self):
        """
        Determines if the sector colors are faded towards the
        background from the leaves up to the headers. This option is
        unavailable when a `colorscale` is present, defaults to false
        when `marker.colors` is set, but otherwise defaults to true.
        When set to "reversed", the fading direction is inverted, that
        is the top elements within hierarchy are drawn with fully
        saturated colors while the leaves are faded towards the
        background color.
    
        The 'depthfade' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'reversed']

        Returns
        -------
        Any
        """
        return self["depthfade"]

    @depthfade.setter
    def depthfade(self, val):
        self["depthfade"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.marker.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the line enclosing each
                    sector. Defaults to the `paper_bgcolor` value.
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for  color .
                width
                    Sets the width (in px) of the line enclosing
                    each sector.
                widthsrc
                    Sets the source reference on Chart Studio Cloud
                    for  width .

        Returns
        -------
        plotly.graph_objs.treemap.marker.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # pad
    # ---
    @property
    def pad(self):
        """
        The 'pad' property is an instance of Pad
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.marker.Pad`
          - A dict of string/value properties that will be passed
            to the Pad constructor
    
            Supported dict properties:
                
                b
                    Sets the padding form the bottom (in px).
                l
                    Sets the padding form the left (in px).
                r
                    Sets the padding form the right (in px).
                t
                    Sets the padding form the top (in px).

        Returns
        -------
        plotly.graph_objs.treemap.marker.Pad
        """
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. Has an effect only if
        colorsis set to a numerical array. If true, `marker.cmin` will
        correspond to the last color in the array and `marker.cmax`
        will correspond to the first color.
    
        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["reversescale"]

    @reversescale.setter
    def reversescale(self, val):
        self["reversescale"] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace. Has an effect only if colorsis set to a numerical array.
    
        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showscale"]

    @showscale.setter
    def showscale(self, val):
        self["showscale"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "treemap"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `marker.colorscale`. Has an effect only if colorsis set
            to a numerical array. In case `colorscale` is
            unspecified or `autocolorscale` is true, the default
            palette will be chosen according to whether numbers in
            the `color` array are all positive, all negative or
            mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here colors) or the
            bounds set in `marker.cmin` and `marker.cmax`  Has an
            effect only if colorsis set to a numerical array.
            Defaults to `false` when `marker.cmin` and
            `marker.cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Has an effect
            only if colorsis set to a numerical array. Value should
            have the same units as colors and if set, `marker.cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `marker.cmin` and/or `marker.cmax` to be equidistant to
            this point. Has an effect only if colorsis set to a
            numerical array. Value should have the same units as
            colors. Has no effect when `marker.cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Has an effect
            only if colorsis set to a numerical array. Value should
            have the same units as colors and if set, `marker.cmax`
            must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.treemap.marker.ColorBar`
            instance or dict with compatible properties
        colors
            Sets the color of each sector of this trace. If not
            specified, the default trace color set is used to pick
            the sector colors.
        colorscale
            Sets the colorscale. Has an effect only if colorsis set
            to a numerical array. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`marker.cmin` and
            `marker.cmax`. Alternatively, `colorscale` may be a
            palette name string of the following list: Greys,YlGnBu
            ,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,P
            ortland,Jet,Hot,Blackbody,Earth,Electric,Viridis,Cividi
            s.
        colorssrc
            Sets the source reference on Chart Studio Cloud for
            colors .
        depthfade
            Determines if the sector colors are faded towards the
            background from the leaves up to the headers. This
            option is unavailable when a `colorscale` is present,
            defaults to false when `marker.colors` is set, but
            otherwise defaults to true. When set to "reversed", the
            fading direction is inverted, that is the top elements
            within hierarchy are drawn with fully saturated colors
            while the leaves are faded towards the background
            color.
        line
            :class:`plotly.graph_objects.treemap.marker.Line`
            instance or dict with compatible properties
        pad
            :class:`plotly.graph_objects.treemap.marker.Pad`
            instance or dict with compatible properties
        reversescale
            Reverses the color mapping if true. Has an effect only
            if colorsis set to a numerical array. If true,
            `marker.cmin` will correspond to the last color in the
            array and `marker.cmax` will correspond to the first
            color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace. Has an effect only if colorsis set to a
            numerical array.
        """

    def __init__(
        self,
        arg=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colors=None,
        colorscale=None,
        colorssrc=None,
        depthfade=None,
        line=None,
        pad=None,
        reversescale=None,
        showscale=None,
        **kwargs
    ):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.Marker`
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `marker.colorscale`. Has an effect only if colorsis set
            to a numerical array. In case `colorscale` is
            unspecified or `autocolorscale` is true, the default
            palette will be chosen according to whether numbers in
            the `color` array are all positive, all negative or
            mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here colors) or the
            bounds set in `marker.cmin` and `marker.cmax`  Has an
            effect only if colorsis set to a numerical array.
            Defaults to `false` when `marker.cmin` and
            `marker.cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Has an effect
            only if colorsis set to a numerical array. Value should
            have the same units as colors and if set, `marker.cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `marker.cmin` and/or `marker.cmax` to be equidistant to
            this point. Has an effect only if colorsis set to a
            numerical array. Value should have the same units as
            colors. Has no effect when `marker.cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Has an effect
            only if colorsis set to a numerical array. Value should
            have the same units as colors and if set, `marker.cmax`
            must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.treemap.marker.ColorBar`
            instance or dict with compatible properties
        colors
            Sets the color of each sector of this trace. If not
            specified, the default trace color set is used to pick
            the sector colors.
        colorscale
            Sets the colorscale. Has an effect only if colorsis set
            to a numerical array. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`marker.cmin` and
            `marker.cmax`. Alternatively, `colorscale` may be a
            palette name string of the following list: Greys,YlGnBu
            ,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,P
            ortland,Jet,Hot,Blackbody,Earth,Electric,Viridis,Cividi
            s.
        colorssrc
            Sets the source reference on Chart Studio Cloud for
            colors .
        depthfade
            Determines if the sector colors are faded towards the
            background from the leaves up to the headers. This
            option is unavailable when a `colorscale` is present,
            defaults to false when `marker.colors` is set, but
            otherwise defaults to true. When set to "reversed", the
            fading direction is inverted, that is the top elements
            within hierarchy are drawn with fully saturated colors
            while the leaves are faded towards the background
            color.
        line
            :class:`plotly.graph_objects.treemap.marker.Line`
            instance or dict with compatible properties
        pad
            :class:`plotly.graph_objects.treemap.marker.Pad`
            instance or dict with compatible properties
        reversescale
            Reverses the color mapping if true. Has an effect only
            if colorsis set to a numerical array. If true,
            `marker.cmin` will correspond to the last color in the
            array and `marker.cmax` will correspond to the first
            color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace. Has an effect only if colorsis set to a
            numerical array.

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
The first argument to the plotly.graph_objs.treemap.Marker 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Marker`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import marker as v_marker

        # Initialize validators
        # ---------------------
        self._validators["autocolorscale"] = v_marker.AutocolorscaleValidator()
        self._validators["cauto"] = v_marker.CautoValidator()
        self._validators["cmax"] = v_marker.CmaxValidator()
        self._validators["cmid"] = v_marker.CmidValidator()
        self._validators["cmin"] = v_marker.CminValidator()
        self._validators["coloraxis"] = v_marker.ColoraxisValidator()
        self._validators["colorbar"] = v_marker.ColorBarValidator()
        self._validators["colors"] = v_marker.ColorsValidator()
        self._validators["colorscale"] = v_marker.ColorscaleValidator()
        self._validators["colorssrc"] = v_marker.ColorssrcValidator()
        self._validators["depthfade"] = v_marker.DepthfadeValidator()
        self._validators["line"] = v_marker.LineValidator()
        self._validators["pad"] = v_marker.PadValidator()
        self._validators["reversescale"] = v_marker.ReversescaleValidator()
        self._validators["showscale"] = v_marker.ShowscaleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("autocolorscale", None)
        self["autocolorscale"] = autocolorscale if autocolorscale is not None else _v
        _v = arg.pop("cauto", None)
        self["cauto"] = cauto if cauto is not None else _v
        _v = arg.pop("cmax", None)
        self["cmax"] = cmax if cmax is not None else _v
        _v = arg.pop("cmid", None)
        self["cmid"] = cmid if cmid is not None else _v
        _v = arg.pop("cmin", None)
        self["cmin"] = cmin if cmin is not None else _v
        _v = arg.pop("coloraxis", None)
        self["coloraxis"] = coloraxis if coloraxis is not None else _v
        _v = arg.pop("colorbar", None)
        self["colorbar"] = colorbar if colorbar is not None else _v
        _v = arg.pop("colors", None)
        self["colors"] = colors if colors is not None else _v
        _v = arg.pop("colorscale", None)
        self["colorscale"] = colorscale if colorscale is not None else _v
        _v = arg.pop("colorssrc", None)
        self["colorssrc"] = colorssrc if colorssrc is not None else _v
        _v = arg.pop("depthfade", None)
        self["depthfade"] = depthfade if depthfade is not None else _v
        _v = arg.pop("line", None)
        self["line"] = line if line is not None else _v
        _v = arg.pop("pad", None)
        self["pad"] = pad if pad is not None else _v
        _v = arg.pop("reversescale", None)
        self["reversescale"] = reversescale if reversescale is not None else _v
        _v = arg.pop("showscale", None)
        self["showscale"] = showscale if showscale is not None else _v

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
        return "treemap"

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
        
        Sets the font used for `textinfo` lying inside the sector.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.Insidetextfont`
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
The first argument to the plotly.graph_objs.treemap.Insidetextfont 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Insidetextfont`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import insidetextfont as v_insidetextfont

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
          - An instance of :class:`plotly.graph_objs.treemap.hoverlabel.Font`
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
        plotly.graph_objs.treemap.hoverlabel.Font
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
        return "treemap"

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
            :class:`plotly.graph_objs.treemap.Hoverlabel`
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
The first argument to the plotly.graph_objs.treemap.Hoverlabel 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Hoverlabel`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import hoverlabel as v_hoverlabel

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
        the grid for this treemap trace .
    
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
        grid for this treemap trace .
    
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
        Sets the horizontal domain of this treemap trace (in plot
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
        Sets the vertical domain of this treemap trace (in plot
        fraction).
    
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
        return "treemap"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        column
            If there is a layout grid, use the domain for this
            column in the grid for this treemap trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this treemap trace .
        x
            Sets the horizontal domain of this treemap trace (in
            plot fraction).
        y
            Sets the vertical domain of this treemap trace (in plot
            fraction).
        """

    def __init__(self, arg=None, column=None, row=None, x=None, y=None, **kwargs):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.Domain`
        column
            If there is a layout grid, use the domain for this
            column in the grid for this treemap trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this treemap trace .
        x
            Sets the horizontal domain of this treemap trace (in
            plot fraction).
        y
            Sets the vertical domain of this treemap trace (in plot
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
The first argument to the plotly.graph_objs.treemap.Domain 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.treemap.Domain`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.treemap import domain as v_domain

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
    "Pathbar",
    "Stream",
    "Textfont",
    "Tiling",
    "hoverlabel",
    "marker",
    "pathbar",
]

from plotly.graph_objs.treemap import pathbar
from plotly.graph_objs.treemap import marker
from plotly.graph_objs.treemap import hoverlabel
