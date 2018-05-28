from plotly.basedatatypes import BaseLayoutHierarchyType


class Shape(BaseLayoutHierarchyType):

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the color filling the shape's interior.
    
        The 'fillcolor' property is a color and may be specified as:
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
        return self['fillcolor']

    @fillcolor.setter
    def fillcolor(self, val):
        self['fillcolor'] = val

    # layer
    # -----
    @property
    def layer(self):
        """
        Specifies whether shapes are drawn below or above traces.
    
        The 'layer' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['below', 'above']

        Returns
        -------
        Any
        """
        return self['layer']

    @layer.setter
    def layer(self, val):
        self['layer'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.layout.shape.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the line color.
                dash
                    Sets the dash style of lines. Set to a dash
                    type string (*solid*, *dot*, *dash*,
                    *longdash*, *dashdot*, or *longdashdot*) or a
                    dash length list in px (eg *5px,10px,2px,2px*).
                width
                    Sets the line width (in px).

        Returns
        -------
        plotly.graph_objs.layout.shape.Line
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
        Sets the opacity of the shape.
    
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

    # path
    # ----
    @property
    def path(self):
        """
        For `type` *path* - a valid SVG path but with the pixel values
        replaced by data values. There are a few restrictions / quirks
        only absolute instructions, not relative. So the allowed
        segments are: M, L, H, V, Q, C, T, S, and Z arcs (A) are not
        allowed because radius rx and ry are relative. In the future we
        could consider supporting relative commands, but we would have
        to decide on how to handle date and log axes. Note that even as
        is, Q and C Bezier paths that are smooth on linear axes may not
        be smooth on log, and vice versa. no chained "polybezier"
        commands - specify the segment type for each one. On category
        axes, values are numbers scaled to the serial numbers of
        categories because using the categories themselves there would
        be no way to describe fractional positions On data axes:
        because space and T are both normal components of path strings,
        we can't use either to separate date from time parts. Therefore
        we'll use underscore for this purpose: 2015-02-21_13:45:56.789
    
        The 'path' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['path']

    @path.setter
    def path(self, val):
        self['path'] = val

    # type
    # ----
    @property
    def type(self):
        """
        Specifies the shape type to be drawn. If *line*, a line is
        drawn from (`x0`,`y0`) to (`x1`,`y1`) If *circle*, a circle is
        drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
        (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) If *rect*, a
        rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`),
        (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) If *path*, draw a custom
        SVG path using `path`.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['circle', 'rect', 'path', 'line']

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
        Determines whether or not this shape is visible.
    
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

    # x0
    # --
    @property
    def x0(self):
        """
        Sets the shape's starting x position. See `type` for more info.
    
        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['x0']

    @x0.setter
    def x0(self, val):
        self['x0'] = val

    # x1
    # --
    @property
    def x1(self):
        """
        Sets the shape's end x position. See `type` for more info.
    
        The 'x1' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['x1']

    @x1.setter
    def x1(self, val):
        self['x1'] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the shape's x coordinate axis. If set to an x axis id
        (e.g. *x* or *x2*), the `x` position refers to an x coordinate
        If set to *paper*, the `x` position refers to the distance from
        the left side of the plotting area in normalized coordinates
        where *0* (*1*) corresponds to the left (right) side. If the
        axis `type` is *log*, then you must take the log of your
        desired range. If the axis `type` is *date*, then you must
        convert the date to unix time in milliseconds.
    
        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self['xref']

    @xref.setter
    def xref(self, val):
        self['xref'] = val

    # y0
    # --
    @property
    def y0(self):
        """
        Sets the shape's starting y position. See `type` for more info.
    
        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['y0']

    @y0.setter
    def y0(self, val):
        self['y0'] = val

    # y1
    # --
    @property
    def y1(self):
        """
        Sets the shape's end y position. See `type` for more info.
    
        The 'y1' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['y1']

    @y1.setter
    def y1(self, val):
        self['y1'] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the annotation's y coordinate axis. If set to an y axis id
        (e.g. *y* or *y2*), the `y` position refers to an y coordinate
        If set to *paper*, the `y` position refers to the distance from
        the bottom of the plotting area in normalized coordinates where
        *0* (*1*) corresponds to the bottom (top).
    
        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self['yref']

    @yref.setter
    def yref(self, val):
        self['yref'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fillcolor
            Sets the color filling the shape's interior.
        layer
            Specifies whether shapes are drawn below or above
            traces.
        line
            plotly.graph_objs.layout.shape.Line instance or dict
            with compatible properties
        opacity
            Sets the opacity of the shape.
        path
            For `type` *path* - a valid SVG path but with the pixel
            values replaced by data values. There are a few
            restrictions / quirks only absolute instructions, not
            relative. So the allowed segments are: M, L, H, V, Q,
            C, T, S, and Z arcs (A) are not allowed because radius
            rx and ry are relative. In the future we could consider
            supporting relative commands, but we would have to
            decide on how to handle date and log axes. Note that
            even as is, Q and C Bezier paths that are smooth on
            linear axes may not be smooth on log, and vice versa.
            no chained "polybezier" commands - specify the segment
            type for each one. On category axes, values are numbers
            scaled to the serial numbers of categories because
            using the categories themselves there would be no way
            to describe fractional positions On data axes: because
            space and T are both normal components of path strings,
            we can't use either to separate date from time parts.
            Therefore we'll use underscore for this purpose:
            2015-02-21_13:45:56.789
        type
            Specifies the shape type to be drawn. If *line*, a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) If *circle*, a
            circle is drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2))
            with radius (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2
            -`y0`)|) If *rect*, a rectangle is drawn linking
            (`x0`,`y0`), (`x1`,`y0`), (`x1`,`y1`), (`x0`,`y1`),
            (`x0`,`y0`) If *path*, draw a custom SVG path using
            `path`.
        visible
            Determines whether or not this shape is visible.
        x0
            Sets the shape's starting x position. See `type` for
            more info.
        x1
            Sets the shape's end x position. See `type` for more
            info.
        xref
            Sets the shape's x coordinate axis. If set to an x axis
            id (e.g. *x* or *x2*), the `x` position refers to an x
            coordinate If set to *paper*, the `x` position refers
            to the distance from the left side of the plotting area
            in normalized coordinates where *0* (*1*) corresponds
            to the left (right) side. If the axis `type` is *log*,
            then you must take the log of your desired range. If
            the axis `type` is *date*, then you must convert the
            date to unix time in milliseconds.
        y0
            Sets the shape's starting y position. See `type` for
            more info.
        y1
            Sets the shape's end y position. See `type` for more
            info.
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. *y* or *y2*), the `y` position refers to
            an y coordinate If set to *paper*, the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where *0* (*1*)
            corresponds to the bottom (top).
        """

    def __init__(
        self,
        fillcolor=None,
        layer=None,
        line=None,
        opacity=None,
        path=None,
        type=None,
        visible=None,
        x0=None,
        x1=None,
        xref=None,
        y0=None,
        y1=None,
        yref=None,
        **kwargs
    ):
        """
        Construct a new Shape object
        
        Parameters
        ----------
        fillcolor
            Sets the color filling the shape's interior.
        layer
            Specifies whether shapes are drawn below or above
            traces.
        line
            plotly.graph_objs.layout.shape.Line instance or dict
            with compatible properties
        opacity
            Sets the opacity of the shape.
        path
            For `type` *path* - a valid SVG path but with the pixel
            values replaced by data values. There are a few
            restrictions / quirks only absolute instructions, not
            relative. So the allowed segments are: M, L, H, V, Q,
            C, T, S, and Z arcs (A) are not allowed because radius
            rx and ry are relative. In the future we could consider
            supporting relative commands, but we would have to
            decide on how to handle date and log axes. Note that
            even as is, Q and C Bezier paths that are smooth on
            linear axes may not be smooth on log, and vice versa.
            no chained "polybezier" commands - specify the segment
            type for each one. On category axes, values are numbers
            scaled to the serial numbers of categories because
            using the categories themselves there would be no way
            to describe fractional positions On data axes: because
            space and T are both normal components of path strings,
            we can't use either to separate date from time parts.
            Therefore we'll use underscore for this purpose:
            2015-02-21_13:45:56.789
        type
            Specifies the shape type to be drawn. If *line*, a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) If *circle*, a
            circle is drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2))
            with radius (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2
            -`y0`)|) If *rect*, a rectangle is drawn linking
            (`x0`,`y0`), (`x1`,`y0`), (`x1`,`y1`), (`x0`,`y1`),
            (`x0`,`y0`) If *path*, draw a custom SVG path using
            `path`.
        visible
            Determines whether or not this shape is visible.
        x0
            Sets the shape's starting x position. See `type` for
            more info.
        x1
            Sets the shape's end x position. See `type` for more
            info.
        xref
            Sets the shape's x coordinate axis. If set to an x axis
            id (e.g. *x* or *x2*), the `x` position refers to an x
            coordinate If set to *paper*, the `x` position refers
            to the distance from the left side of the plotting area
            in normalized coordinates where *0* (*1*) corresponds
            to the left (right) side. If the axis `type` is *log*,
            then you must take the log of your desired range. If
            the axis `type` is *date*, then you must convert the
            date to unix time in milliseconds.
        y0
            Sets the shape's starting y position. See `type` for
            more info.
        y1
            Sets the shape's end y position. See `type` for more
            info.
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. *y* or *y2*), the `y` position refers to
            an y coordinate If set to *paper*, the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where *0* (*1*)
            corresponds to the bottom (top).

        Returns
        -------
        Shape
        """
        super(Shape, self).__init__('shapes')

        # Import validators
        # -----------------
        from plotly.validators.layout import (shape as v_shape)

        # Initialize validators
        # ---------------------
        self._validators['fillcolor'] = v_shape.FillcolorValidator()
        self._validators['layer'] = v_shape.LayerValidator()
        self._validators['line'] = v_shape.LineValidator()
        self._validators['opacity'] = v_shape.OpacityValidator()
        self._validators['path'] = v_shape.PathValidator()
        self._validators['type'] = v_shape.TypeValidator()
        self._validators['visible'] = v_shape.VisibleValidator()
        self._validators['x0'] = v_shape.X0Validator()
        self._validators['x1'] = v_shape.X1Validator()
        self._validators['xref'] = v_shape.XrefValidator()
        self._validators['y0'] = v_shape.Y0Validator()
        self._validators['y1'] = v_shape.Y1Validator()
        self._validators['yref'] = v_shape.YrefValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.fillcolor = fillcolor
        self.layer = layer
        self.line = line
        self.opacity = opacity
        self.path = path
        self.type = type
        self.visible = visible
        self.x0 = x0
        self.x1 = x1
        self.xref = xref
        self.y0 = y0
        self.y1 = y1
        self.yref = yref

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
