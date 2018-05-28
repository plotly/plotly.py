from plotly.basedatatypes import BaseLayoutHierarchyType


class Layer(BaseLayoutHierarchyType):

    # below
    # -----
    @property
    def below(self):
        """
        Determines if the layer will be inserted before the layer with
        the specified ID. If omitted or set to '', the layer will be
        inserted above every existing layer.
    
        The 'below' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['below']

    @below.setter
    def below(self, val):
        self['below'] = val

    # circle
    # ------
    @property
    def circle(self):
        """
        The 'circle' property is an instance of Circle
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.layer.Circle
          - A dict of string/value properties that will be passed
            to the Circle constructor
    
            Supported dict properties:
                
                radius
                    Sets the circle radius. Has an effect only when
                    `type` is set to *circle*.

        Returns
        -------
        plotly.graph_objs.layout.mapbox.layer.Circle
        """
        return self['circle']

    @circle.setter
    def circle(self, val):
        self['circle'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the primary layer color. If `type` is *circle*, color
        corresponds to the circle color If `type` is *line*, color
        corresponds to the line color If `type` is *fill*, color
        corresponds to the fill color If `type` is *symbol*, color
        corresponds to the icon color
    
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
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # fill
    # ----
    @property
    def fill(self):
        """
        The 'fill' property is an instance of Fill
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.layer.Fill
          - A dict of string/value properties that will be passed
            to the Fill constructor
    
            Supported dict properties:
                
                outlinecolor
                    Sets the fill outline color. Has an effect only
                    when `type` is set to *fill*.

        Returns
        -------
        plotly.graph_objs.layout.mapbox.layer.Fill
        """
        return self['fill']

    @fill.setter
    def fill(self, val):
        self['fill'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.layer.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                width
                    Sets the line width. Has an effect only when
                    `type` is set to *line*.

        Returns
        -------
        plotly.graph_objs.layout.mapbox.layer.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the layer.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # source
    # ------
    @property
    def source(self):
        """
        Sets the source data for this layer. Source can be either a
        URL, a geojson object (with `sourcetype` set to *geojson*) or
        an array of tile URLS (with `sourcetype` set to *vector*).
    
        The 'source' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['source']

    @source.setter
    def source(self, val):
        self['source'] = val

    # sourcelayer
    # -----------
    @property
    def sourcelayer(self):
        """
        Specifies the layer to use from a vector tile source. Required
        for *vector* source type that supports multiple layers.
    
        The 'sourcelayer' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['sourcelayer']

    @sourcelayer.setter
    def sourcelayer(self, val):
        self['sourcelayer'] = val

    # sourcetype
    # ----------
    @property
    def sourcetype(self):
        """
        Sets the source type for this layer. Support for *raster*,
        *image* and *video* source types is coming soon.
    
        The 'sourcetype' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['geojson', 'vector']

        Returns
        -------
        Any
        """
        return self['sourcetype']

    @sourcetype.setter
    def sourcetype(self, val):
        self['sourcetype'] = val

    # symbol
    # ------
    @property
    def symbol(self):
        """
        The 'symbol' property is an instance of Symbol
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.layer.Symbol
          - A dict of string/value properties that will be passed
            to the Symbol constructor
    
            Supported dict properties:
                
                icon
                    Sets the symbol icon image. Full list:
                    https://www.mapbox.com/maki-icons/
                iconsize
                    Sets the symbol icon size. Has an effect only
                    when `type` is set to *symbol*.
                text
                    Sets the symbol text.
                textfont
                    Sets the icon text font. Has an effect only
                    when `type` is set to *symbol*.
                textposition
                    Sets the positions of the `text` elements with
                    respects to the (x,y) coordinates.

        Returns
        -------
        plotly.graph_objs.layout.mapbox.layer.Symbol
        """
        return self['symbol']

    @symbol.setter
    def symbol(self, val):
        self['symbol'] = val

    # type
    # ----
    @property
    def type(self):
        """
        Sets the layer type. Support for *raster*, *background* types
        is coming soon. Note that *line* and *fill* are not compatible
        with Point GeoJSON geometries.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['circle', 'line', 'fill', 'symbol']

        Returns
        -------
        Any
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.mapbox'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        below
            Determines if the layer will be inserted before the
            layer with the specified ID. If omitted or set to '',
            the layer will be inserted above every existing layer.
        circle
            plotly.graph_objs.layout.mapbox.layer.Circle instance
            or dict with compatible properties
        color
            Sets the primary layer color. If `type` is *circle*,
            color corresponds to the circle color If `type` is
            *line*, color corresponds to the line color If `type`
            is *fill*, color corresponds to the fill color If
            `type` is *symbol*, color corresponds to the icon color
        fill
            plotly.graph_objs.layout.mapbox.layer.Fill instance or
            dict with compatible properties
        line
            plotly.graph_objs.layout.mapbox.layer.Line instance or
            dict with compatible properties
        opacity
            Sets the opacity of the layer.
        source
            Sets the source data for this layer. Source can be
            either a URL, a geojson object (with `sourcetype` set
            to *geojson*) or an array of tile URLS (with
            `sourcetype` set to *vector*).
        sourcelayer
            Specifies the layer to use from a vector tile source.
            Required for *vector* source type that supports
            multiple layers.
        sourcetype
            Sets the source type for this layer. Support for
            *raster*, *image* and *video* source types is coming
            soon.
        symbol
            plotly.graph_objs.layout.mapbox.layer.Symbol instance
            or dict with compatible properties
        type
            Sets the layer type. Support for *raster*, *background*
            types is coming soon. Note that *line* and *fill* are
            not compatible with Point GeoJSON geometries.
        """

    def __init__(
        self,
        below=None,
        circle=None,
        color=None,
        fill=None,
        line=None,
        opacity=None,
        source=None,
        sourcelayer=None,
        sourcetype=None,
        symbol=None,
        type=None,
        **kwargs
    ):
        """
        Construct a new Layer object
        
        Parameters
        ----------
        below
            Determines if the layer will be inserted before the
            layer with the specified ID. If omitted or set to '',
            the layer will be inserted above every existing layer.
        circle
            plotly.graph_objs.layout.mapbox.layer.Circle instance
            or dict with compatible properties
        color
            Sets the primary layer color. If `type` is *circle*,
            color corresponds to the circle color If `type` is
            *line*, color corresponds to the line color If `type`
            is *fill*, color corresponds to the fill color If
            `type` is *symbol*, color corresponds to the icon color
        fill
            plotly.graph_objs.layout.mapbox.layer.Fill instance or
            dict with compatible properties
        line
            plotly.graph_objs.layout.mapbox.layer.Line instance or
            dict with compatible properties
        opacity
            Sets the opacity of the layer.
        source
            Sets the source data for this layer. Source can be
            either a URL, a geojson object (with `sourcetype` set
            to *geojson*) or an array of tile URLS (with
            `sourcetype` set to *vector*).
        sourcelayer
            Specifies the layer to use from a vector tile source.
            Required for *vector* source type that supports
            multiple layers.
        sourcetype
            Sets the source type for this layer. Support for
            *raster*, *image* and *video* source types is coming
            soon.
        symbol
            plotly.graph_objs.layout.mapbox.layer.Symbol instance
            or dict with compatible properties
        type
            Sets the layer type. Support for *raster*, *background*
            types is coming soon. Note that *line* and *fill* are
            not compatible with Point GeoJSON geometries.

        Returns
        -------
        Layer
        """
        super(Layer, self).__init__('layers')

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox import (layer as v_layer)

        # Initialize validators
        # ---------------------
        self._validators['below'] = v_layer.BelowValidator()
        self._validators['circle'] = v_layer.CircleValidator()
        self._validators['color'] = v_layer.ColorValidator()
        self._validators['fill'] = v_layer.FillValidator()
        self._validators['line'] = v_layer.LineValidator()
        self._validators['opacity'] = v_layer.OpacityValidator()
        self._validators['source'] = v_layer.SourceValidator()
        self._validators['sourcelayer'] = v_layer.SourcelayerValidator()
        self._validators['sourcetype'] = v_layer.SourcetypeValidator()
        self._validators['symbol'] = v_layer.SymbolValidator()
        self._validators['type'] = v_layer.TypeValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.below = below
        self.circle = circle
        self.color = color
        self.fill = fill
        self.line = line
        self.opacity = opacity
        self.source = source
        self.sourcelayer = sourcelayer
        self.sourcetype = sourcetype
        self.symbol = symbol
        self.type = type

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
