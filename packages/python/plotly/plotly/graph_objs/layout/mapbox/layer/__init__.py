from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Symbol(_BaseLayoutHierarchyType):

    # icon
    # ----
    @property
    def icon(self):
        """
        Sets the symbol icon image (mapbox.layer.layout.icon-image).
        Full list: https://www.mapbox.com/maki-icons/
    
        The 'icon' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["icon"]

    @icon.setter
    def icon(self, val):
        self["icon"] = val

    # iconsize
    # --------
    @property
    def iconsize(self):
        """
        Sets the symbol icon size (mapbox.layer.layout.icon-size). Has
        an effect only when `type` is set to "symbol".
    
        The 'iconsize' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["iconsize"]

    @iconsize.setter
    def iconsize(self, val):
        self["iconsize"] = val

    # placement
    # ---------
    @property
    def placement(self):
        """
        Sets the symbol and/or text placement
        (mapbox.layer.layout.symbol-placement). If `placement` is
        "point", the label is placed where the geometry is located If
        `placement` is "line", the label is placed along the line of
        the geometry If `placement` is "line-center", the label is
        placed on the center of the geometry
    
        The 'placement' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['point', 'line', 'line-center']

        Returns
        -------
        Any
        """
        return self["placement"]

    @placement.setter
    def placement(self, val):
        self["placement"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the symbol text (mapbox.layer.layout.text-field).
    
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

    # textfont
    # --------
    @property
    def textfont(self):
        """
        Sets the icon text font (color=mapbox.layer.paint.text-color,
        size=mapbox.layer.layout.text-size). Has an effect only when
        `type` is set to "symbol".
    
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.layer.symbol.Textfont
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
            Supported dict properties:
                
                color
    
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
                size

        Returns
        -------
        plotly.graph_objs.layout.mapbox.layer.symbol.Textfont
        """
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    # textposition
    # ------------
    @property
    def textposition(self):
        """
        Sets the positions of the `text` elements with respects to the
        (x,y) coordinates.
    
        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle left',
                'middle center', 'middle right', 'bottom left', 'bottom
                center', 'bottom right']

        Returns
        -------
        Any
        """
        return self["textposition"]

    @textposition.setter
    def textposition(self, val):
        self["textposition"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.mapbox.layer"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        icon
            Sets the symbol icon image (mapbox.layer.layout.icon-
            image). Full list: https://www.mapbox.com/maki-icons/
        iconsize
            Sets the symbol icon size (mapbox.layer.layout.icon-
            size). Has an effect only when `type` is set to
            "symbol".
        placement
            Sets the symbol and/or text placement
            (mapbox.layer.layout.symbol-placement). If `placement`
            is "point", the label is placed where the geometry is
            located If `placement` is "line", the label is placed
            along the line of the geometry If `placement` is "line-
            center", the label is placed on the center of the
            geometry
        text
            Sets the symbol text (mapbox.layer.layout.text-field).
        textfont
            Sets the icon text font (color=mapbox.layer.paint.text-
            color, size=mapbox.layer.layout.text-size). Has an
            effect only when `type` is set to "symbol".
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        """

    def __init__(
        self,
        arg=None,
        icon=None,
        iconsize=None,
        placement=None,
        text=None,
        textfont=None,
        textposition=None,
        **kwargs
    ):
        """
        Construct a new Symbol object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.mapbox.layer.Symbol
        icon
            Sets the symbol icon image (mapbox.layer.layout.icon-
            image). Full list: https://www.mapbox.com/maki-icons/
        iconsize
            Sets the symbol icon size (mapbox.layer.layout.icon-
            size). Has an effect only when `type` is set to
            "symbol".
        placement
            Sets the symbol and/or text placement
            (mapbox.layer.layout.symbol-placement). If `placement`
            is "point", the label is placed where the geometry is
            located If `placement` is "line", the label is placed
            along the line of the geometry If `placement` is "line-
            center", the label is placed on the center of the
            geometry
        text
            Sets the symbol text (mapbox.layer.layout.text-field).
        textfont
            Sets the icon text font (color=mapbox.layer.paint.text-
            color, size=mapbox.layer.layout.text-size). Has an
            effect only when `type` is set to "symbol".
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.

        Returns
        -------
        Symbol
        """
        super(Symbol, self).__init__("symbol")

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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Symbol 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.layer.Symbol"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import symbol as v_symbol

        # Initialize validators
        # ---------------------
        self._validators["icon"] = v_symbol.IconValidator()
        self._validators["iconsize"] = v_symbol.IconsizeValidator()
        self._validators["placement"] = v_symbol.PlacementValidator()
        self._validators["text"] = v_symbol.TextValidator()
        self._validators["textfont"] = v_symbol.TextfontValidator()
        self._validators["textposition"] = v_symbol.TextpositionValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("icon", None)
        self["icon"] = icon if icon is not None else _v
        _v = arg.pop("iconsize", None)
        self["iconsize"] = iconsize if iconsize is not None else _v
        _v = arg.pop("placement", None)
        self["placement"] = placement if placement is not None else _v
        _v = arg.pop("text", None)
        self["text"] = text if text is not None else _v
        _v = arg.pop("textfont", None)
        self["textfont"] = textfont if textfont is not None else _v
        _v = arg.pop("textposition", None)
        self["textposition"] = textposition if textposition is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Line(_BaseLayoutHierarchyType):

    # dash
    # ----
    @property
    def dash(self):
        """
        Sets the length of dashes and gaps (mapbox.layer.paint.line-
        dasharray). Has an effect only when `type` is set to "line".
    
        The 'dash' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["dash"]

    @dash.setter
    def dash(self, val):
        self["dash"] = val

    # dashsrc
    # -------
    @property
    def dashsrc(self):
        """
        Sets the source reference on plot.ly for  dash .
    
        The 'dashsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["dashsrc"]

    @dashsrc.setter
    def dashsrc(self, val):
        self["dashsrc"] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the line width (mapbox.layer.paint.line-width). Has an
        effect only when `type` is set to "line".
    
        The 'width' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.mapbox.layer"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        dash
            Sets the length of dashes and gaps
            (mapbox.layer.paint.line-dasharray). Has an effect only
            when `type` is set to "line".
        dashsrc
            Sets the source reference on plot.ly for  dash .
        width
            Sets the line width (mapbox.layer.paint.line-width).
            Has an effect only when `type` is set to "line".
        """

    def __init__(self, arg=None, dash=None, dashsrc=None, width=None, **kwargs):
        """
        Construct a new Line object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.mapbox.layer.Line
        dash
            Sets the length of dashes and gaps
            (mapbox.layer.paint.line-dasharray). Has an effect only
            when `type` is set to "line".
        dashsrc
            Sets the source reference on plot.ly for  dash .
        width
            Sets the line width (mapbox.layer.paint.line-width).
            Has an effect only when `type` is set to "line".

        Returns
        -------
        Line
        """
        super(Line, self).__init__("line")

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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Line 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.layer.Line"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import line as v_line

        # Initialize validators
        # ---------------------
        self._validators["dash"] = v_line.DashValidator()
        self._validators["dashsrc"] = v_line.DashsrcValidator()
        self._validators["width"] = v_line.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("dash", None)
        self["dash"] = dash if dash is not None else _v
        _v = arg.pop("dashsrc", None)
        self["dashsrc"] = dashsrc if dashsrc is not None else _v
        _v = arg.pop("width", None)
        self["width"] = width if width is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Fill(_BaseLayoutHierarchyType):

    # outlinecolor
    # ------------
    @property
    def outlinecolor(self):
        """
        Sets the fill outline color (mapbox.layer.paint.fill-outline-
        color). Has an effect only when `type` is set to "fill".
    
        The 'outlinecolor' property is a color and may be specified as:
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
        return self["outlinecolor"]

    @outlinecolor.setter
    def outlinecolor(self, val):
        self["outlinecolor"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.mapbox.layer"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        outlinecolor
            Sets the fill outline color (mapbox.layer.paint.fill-
            outline-color). Has an effect only when `type` is set
            to "fill".
        """

    def __init__(self, arg=None, outlinecolor=None, **kwargs):
        """
        Construct a new Fill object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.mapbox.layer.Fill
        outlinecolor
            Sets the fill outline color (mapbox.layer.paint.fill-
            outline-color). Has an effect only when `type` is set
            to "fill".

        Returns
        -------
        Fill
        """
        super(Fill, self).__init__("fill")

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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Fill 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.layer.Fill"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import fill as v_fill

        # Initialize validators
        # ---------------------
        self._validators["outlinecolor"] = v_fill.OutlinecolorValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("outlinecolor", None)
        self["outlinecolor"] = outlinecolor if outlinecolor is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Circle(_BaseLayoutHierarchyType):

    # radius
    # ------
    @property
    def radius(self):
        """
        Sets the circle radius (mapbox.layer.paint.circle-radius). Has
        an effect only when `type` is set to "circle".
    
        The 'radius' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["radius"]

    @radius.setter
    def radius(self, val):
        self["radius"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.mapbox.layer"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        radius
            Sets the circle radius (mapbox.layer.paint.circle-
            radius). Has an effect only when `type` is set to
            "circle".
        """

    def __init__(self, arg=None, radius=None, **kwargs):
        """
        Construct a new Circle object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.mapbox.layer.Circle
        radius
            Sets the circle radius (mapbox.layer.paint.circle-
            radius). Has an effect only when `type` is set to
            "circle".

        Returns
        -------
        Circle
        """
        super(Circle, self).__init__("circle")

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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Circle 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.layer.Circle"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import circle as v_circle

        # Initialize validators
        # ---------------------
        self._validators["radius"] = v_circle.RadiusValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("radius", None)
        self["radius"] = radius if radius is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = ["Circle", "Fill", "Line", "Symbol", "symbol"]

from plotly.graph_objs.layout.mapbox.layer import symbol
