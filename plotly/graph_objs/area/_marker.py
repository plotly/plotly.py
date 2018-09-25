from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Marker(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Area traces are deprecated! Please switch to the "barpolar"
        trace type. Sets themarkercolor. It accepts either a specific
        color or an array of numbers that are mapped to the colorscale
        relative to the max and min values of the array or relative to
        `marker.cmin` and `marker.cmax` if set.
    
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

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
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Area traces are deprecated! Please switch to the "barpolar"
        trace type. Sets the marker opacity.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # opacitysrc
    # ----------
    @property
    def opacitysrc(self):
        """
        Sets the source reference on plot.ly for  opacity .
    
        The 'opacitysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['opacitysrc']

    @opacitysrc.setter
    def opacitysrc(self, val):
        self['opacitysrc'] = val

    # size
    # ----
    @property
    def size(self):
        """
        Area traces are deprecated! Please switch to the "barpolar"
        trace type. Sets the marker size (in px).
    
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

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
        return self['sizesrc']

    @sizesrc.setter
    def sizesrc(self, val):
        self['sizesrc'] = val

    # symbol
    # ------
    @property
    def symbol(self):
        """
        Area traces are deprecated! Please switch to the "barpolar"
        trace type. Sets the marker symbol type. Adding 100 is
        equivalent to appending "-open" to a symbol name. Adding 200 is
        equivalent to appending "-dot" to a symbol name. Adding 300 is
        equivalent to appending "-open-dot" or "dot-open" to a symbol
        name.
    
        The 'symbol' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [0, 'circle', 100, 'circle-open', 200, 'circle-dot', 300,
                'circle-open-dot', 1, 'square', 101, 'square-open', 201,
                'square-dot', 301, 'square-open-dot', 2, 'diamond', 102,
                'diamond-open', 202, 'diamond-dot', 302,
                'diamond-open-dot', 3, 'cross', 103, 'cross-open', 203,
                'cross-dot', 303, 'cross-open-dot', 4, 'x', 104, 'x-open',
                204, 'x-dot', 304, 'x-open-dot', 5, 'triangle-up', 105,
                'triangle-up-open', 205, 'triangle-up-dot', 305,
                'triangle-up-open-dot', 6, 'triangle-down', 106,
                'triangle-down-open', 206, 'triangle-down-dot', 306,
                'triangle-down-open-dot', 7, 'triangle-left', 107,
                'triangle-left-open', 207, 'triangle-left-dot', 307,
                'triangle-left-open-dot', 8, 'triangle-right', 108,
                'triangle-right-open', 208, 'triangle-right-dot', 308,
                'triangle-right-open-dot', 9, 'triangle-ne', 109,
                'triangle-ne-open', 209, 'triangle-ne-dot', 309,
                'triangle-ne-open-dot', 10, 'triangle-se', 110,
                'triangle-se-open', 210, 'triangle-se-dot', 310,
                'triangle-se-open-dot', 11, 'triangle-sw', 111,
                'triangle-sw-open', 211, 'triangle-sw-dot', 311,
                'triangle-sw-open-dot', 12, 'triangle-nw', 112,
                'triangle-nw-open', 212, 'triangle-nw-dot', 312,
                'triangle-nw-open-dot', 13, 'pentagon', 113,
                'pentagon-open', 213, 'pentagon-dot', 313,
                'pentagon-open-dot', 14, 'hexagon', 114, 'hexagon-open',
                214, 'hexagon-dot', 314, 'hexagon-open-dot', 15,
                'hexagon2', 115, 'hexagon2-open', 215, 'hexagon2-dot',
                315, 'hexagon2-open-dot', 16, 'octagon', 116,
                'octagon-open', 216, 'octagon-dot', 316,
                'octagon-open-dot', 17, 'star', 117, 'star-open', 217,
                'star-dot', 317, 'star-open-dot', 18, 'hexagram', 118,
                'hexagram-open', 218, 'hexagram-dot', 318,
                'hexagram-open-dot', 19, 'star-triangle-up', 119,
                'star-triangle-up-open', 219, 'star-triangle-up-dot', 319,
                'star-triangle-up-open-dot', 20, 'star-triangle-down',
                120, 'star-triangle-down-open', 220,
                'star-triangle-down-dot', 320,
                'star-triangle-down-open-dot', 21, 'star-square', 121,
                'star-square-open', 221, 'star-square-dot', 321,
                'star-square-open-dot', 22, 'star-diamond', 122,
                'star-diamond-open', 222, 'star-diamond-dot', 322,
                'star-diamond-open-dot', 23, 'diamond-tall', 123,
                'diamond-tall-open', 223, 'diamond-tall-dot', 323,
                'diamond-tall-open-dot', 24, 'diamond-wide', 124,
                'diamond-wide-open', 224, 'diamond-wide-dot', 324,
                'diamond-wide-open-dot', 25, 'hourglass', 125,
                'hourglass-open', 26, 'bowtie', 126, 'bowtie-open', 27,
                'circle-cross', 127, 'circle-cross-open', 28, 'circle-x',
                128, 'circle-x-open', 29, 'square-cross', 129,
                'square-cross-open', 30, 'square-x', 130, 'square-x-open',
                31, 'diamond-cross', 131, 'diamond-cross-open', 32,
                'diamond-x', 132, 'diamond-x-open', 33, 'cross-thin', 133,
                'cross-thin-open', 34, 'x-thin', 134, 'x-thin-open', 35,
                'asterisk', 135, 'asterisk-open', 36, 'hash', 136,
                'hash-open', 236, 'hash-dot', 336, 'hash-open-dot', 37,
                'y-up', 137, 'y-up-open', 38, 'y-down', 138,
                'y-down-open', 39, 'y-left', 139, 'y-left-open', 40,
                'y-right', 140, 'y-right-open', 41, 'line-ew', 141,
                'line-ew-open', 42, 'line-ns', 142, 'line-ns-open', 43,
                'line-ne', 143, 'line-ne-open', 44, 'line-nw', 144,
                'line-nw-open']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['symbol']

    @symbol.setter
    def symbol(self, val):
        self['symbol'] = val

    # symbolsrc
    # ---------
    @property
    def symbolsrc(self):
        """
        Sets the source reference on plot.ly for  symbol .
    
        The 'symbolsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['symbolsrc']

    @symbolsrc.setter
    def symbolsrc(self, val):
        self['symbolsrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'area'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets themarkercolor. It accepts
            either a specific color or an array of numbers that are
            mapped to the colorscale relative to the max and min
            values of the array or relative to `marker.cmin` and
            `marker.cmax` if set.
        colorsrc
            Sets the source reference on plot.ly for  color .
        opacity
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the marker opacity.
        opacitysrc
            Sets the source reference on plot.ly for  opacity .
        size
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the marker size (in px).
        sizesrc
            Sets the source reference on plot.ly for  size .
        symbol
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the marker symbol type.
            Adding 100 is equivalent to appending "-open" to a
            symbol name. Adding 200 is equivalent to appending
            "-dot" to a symbol name. Adding 300 is equivalent to
            appending "-open-dot" or "dot-open" to a symbol name.
        symbolsrc
            Sets the source reference on plot.ly for  symbol .
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        opacity=None,
        opacitysrc=None,
        size=None,
        sizesrc=None,
        symbol=None,
        symbolsrc=None,
        **kwargs
    ):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.area.Marker
        color
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets themarkercolor. It accepts
            either a specific color or an array of numbers that are
            mapped to the colorscale relative to the max and min
            values of the array or relative to `marker.cmin` and
            `marker.cmax` if set.
        colorsrc
            Sets the source reference on plot.ly for  color .
        opacity
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the marker opacity.
        opacitysrc
            Sets the source reference on plot.ly for  opacity .
        size
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the marker size (in px).
        sizesrc
            Sets the source reference on plot.ly for  size .
        symbol
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the marker symbol type.
            Adding 100 is equivalent to appending "-open" to a
            symbol name. Adding 200 is equivalent to appending
            "-dot" to a symbol name. Adding 300 is equivalent to
            appending "-open-dot" or "dot-open" to a symbol name.
        symbolsrc
            Sets the source reference on plot.ly for  symbol .

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__('marker')

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
The first argument to the plotly.graph_objs.area.Marker 
constructor must be a dict or 
an instance of plotly.graph_objs.area.Marker"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.area import (marker as v_marker)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_marker.ColorValidator()
        self._validators['colorsrc'] = v_marker.ColorsrcValidator()
        self._validators['opacity'] = v_marker.OpacityValidator()
        self._validators['opacitysrc'] = v_marker.OpacitysrcValidator()
        self._validators['size'] = v_marker.SizeValidator()
        self._validators['sizesrc'] = v_marker.SizesrcValidator()
        self._validators['symbol'] = v_marker.SymbolValidator()
        self._validators['symbolsrc'] = v_marker.SymbolsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('color', None)
        self['color'] = color if color is not None else _v
        _v = arg.pop('colorsrc', None)
        self['colorsrc'] = colorsrc if colorsrc is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('opacitysrc', None)
        self['opacitysrc'] = opacitysrc if opacitysrc is not None else _v
        _v = arg.pop('size', None)
        self['size'] = size if size is not None else _v
        _v = arg.pop('sizesrc', None)
        self['sizesrc'] = sizesrc if sizesrc is not None else _v
        _v = arg.pop('symbol', None)
        self['symbol'] = symbol if symbol is not None else _v
        _v = arg.pop('symbolsrc', None)
        self['symbolsrc'] = symbolsrc if symbolsrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
