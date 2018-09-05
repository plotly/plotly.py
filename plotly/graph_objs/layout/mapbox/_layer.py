from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


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
                    `type` is set to "circle".

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
        Sets the primary layer color. If `type` is "circle", color
        corresponds to the circle color If `type` is "line", color
        corresponds to the line color If `type` is "fill", color
        corresponds to the fill color If `type` is "symbol", color
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
                    when `type` is set to "fill".

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
                    `type` is set to "line".

        Returns
        -------
        plotly.graph_objs.layout.mapbox.layer.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

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
        URL, a geojson object (with `sourcetype` set to "geojson") or
        an array of tile URLS (with `sourcetype` set to "vector").
    
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
        for "vector" source type that supports multiple layers.
    
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
        Sets the source type for this layer. Support for "raster",
        "image" and "video" source types is coming soon.
    
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
                    when `type` is set to "symbol".
                text
                    Sets the symbol text.
                textfont
                    Sets the icon text font. Has an effect only
                    when `type` is set to "symbol".
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

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['templateitemname']

    @templateitemname.setter
    def templateitemname(self, val):
        self['templateitemname'] = val

    # type
    # ----
    @property
    def type(self):
        """
        Sets the layer type. Support for "raster", "background" types
        is coming soon. Note that "line" and "fill" are not compatible
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

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether this layer is displayed
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

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
            Sets the primary layer color. If `type` is "circle",
            color corresponds to the circle color If `type` is
            "line", color corresponds to the line color If `type`
            is "fill", color corresponds to the fill color If
            `type` is "symbol", color corresponds to the icon color
        fill
            plotly.graph_objs.layout.mapbox.layer.Fill instance or
            dict with compatible properties
        line
            plotly.graph_objs.layout.mapbox.layer.Line instance or
            dict with compatible properties
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the layer.
        source
            Sets the source data for this layer. Source can be
            either a URL, a geojson object (with `sourcetype` set
            to "geojson") or an array of tile URLS (with
            `sourcetype` set to "vector").
        sourcelayer
            Specifies the layer to use from a vector tile source.
            Required for "vector" source type that supports
            multiple layers.
        sourcetype
            Sets the source type for this layer. Support for
            "raster", "image" and "video" source types is coming
            soon.
        symbol
            plotly.graph_objs.layout.mapbox.layer.Symbol instance
            or dict with compatible properties
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Sets the layer type. Support for "raster", "background"
            types is coming soon. Note that "line" and "fill" are
            not compatible with Point GeoJSON geometries.
        visible
            Determines whether this layer is displayed
        """

    def __init__(
        self,
        arg=None,
        below=None,
        circle=None,
        color=None,
        fill=None,
        line=None,
        name=None,
        opacity=None,
        source=None,
        sourcelayer=None,
        sourcetype=None,
        symbol=None,
        templateitemname=None,
        type=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Layer object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.mapbox.Layer
        below
            Determines if the layer will be inserted before the
            layer with the specified ID. If omitted or set to '',
            the layer will be inserted above every existing layer.
        circle
            plotly.graph_objs.layout.mapbox.layer.Circle instance
            or dict with compatible properties
        color
            Sets the primary layer color. If `type` is "circle",
            color corresponds to the circle color If `type` is
            "line", color corresponds to the line color If `type`
            is "fill", color corresponds to the fill color If
            `type` is "symbol", color corresponds to the icon color
        fill
            plotly.graph_objs.layout.mapbox.layer.Fill instance or
            dict with compatible properties
        line
            plotly.graph_objs.layout.mapbox.layer.Line instance or
            dict with compatible properties
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the layer.
        source
            Sets the source data for this layer. Source can be
            either a URL, a geojson object (with `sourcetype` set
            to "geojson") or an array of tile URLS (with
            `sourcetype` set to "vector").
        sourcelayer
            Specifies the layer to use from a vector tile source.
            Required for "vector" source type that supports
            multiple layers.
        sourcetype
            Sets the source type for this layer. Support for
            "raster", "image" and "video" source types is coming
            soon.
        symbol
            plotly.graph_objs.layout.mapbox.layer.Symbol instance
            or dict with compatible properties
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Sets the layer type. Support for "raster", "background"
            types is coming soon. Note that "line" and "fill" are
            not compatible with Point GeoJSON geometries.
        visible
            Determines whether this layer is displayed

        Returns
        -------
        Layer
        """
        super(Layer, self).__init__('layers')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.mapbox.Layer 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.Layer"""
            )

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
        self._validators['name'] = v_layer.NameValidator()
        self._validators['opacity'] = v_layer.OpacityValidator()
        self._validators['source'] = v_layer.SourceValidator()
        self._validators['sourcelayer'] = v_layer.SourcelayerValidator()
        self._validators['sourcetype'] = v_layer.SourcetypeValidator()
        self._validators['symbol'] = v_layer.SymbolValidator()
        self._validators['templateitemname'
                        ] = v_layer.TemplateitemnameValidator()
        self._validators['type'] = v_layer.TypeValidator()
        self._validators['visible'] = v_layer.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('below', None)
        self.below = below if below is not None else _v
        _v = arg.pop('circle', None)
        self.circle = circle if circle is not None else _v
        _v = arg.pop('color', None)
        self.color = color if color is not None else _v
        _v = arg.pop('fill', None)
        self.fill = fill if fill is not None else _v
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('source', None)
        self.source = source if source is not None else _v
        _v = arg.pop('sourcelayer', None)
        self.sourcelayer = sourcelayer if sourcelayer is not None else _v
        _v = arg.pop('sourcetype', None)
        self.sourcetype = sourcetype if sourcetype is not None else _v
        _v = arg.pop('symbol', None)
        self.symbol = symbol if symbol is not None else _v
        _v = arg.pop('templateitemname', None)
        self.templateitemname = templateitemname if templateitemname is not None else _v
        _v = arg.pop('type', None)
        self.type = type if type is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
