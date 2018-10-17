from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


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
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
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
        For `type` "path" - a valid SVG path with the pixel values
        replaced by data values in `xsizemode`/`ysizemode` being
        "scaled" and taken unmodified as pixels relative to `xanchor`
        and `yanchor` in case of "pixel" size mode. There are a few
        restrictions / quirks only absolute instructions, not relative.
        So the allowed segments are: M, L, H, V, Q, C, T, S, and Z arcs
        (A) are not allowed because radius rx and ry are relative. In
        the future we could consider supporting relative commands, but
        we would have to decide on how to handle date and log axes.
        Note that even as is, Q and C Bezier paths that are smooth on
        linear axes may not be smooth on log, and vice versa. no
        chained "polybezier" commands - specify the segment type for
        each one. On category axes, values are numbers scaled to the
        serial numbers of categories because using the categories
        themselves there would be no way to describe fractional
        positions On data axes: because space and T are both normal
        components of path strings, we can't use either to separate
        date from time parts. Therefore we'll use underscore for this
        purpose: 2015-02-21_13:45:56.789
    
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
        Specifies the shape type to be drawn. If "line", a line is
        drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect to the axes'
        sizing mode. If "circle", a circle is drawn from
        ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius (|(`x0`+`x1`)/2 -
        `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with respect to the axes' sizing
        mode. If "rect", a rectangle is drawn linking (`x0`,`y0`),
        (`x1`,`y0`), (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect
        to the axes' sizing mode. If "path", draw a custom SVG path
        using `path`. with respect to the axes' sizing mode.
    
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
        Sets the shape's starting x position. See `type` and
        `xsizemode` for more info.
    
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
        Sets the shape's end x position. See `type` and `xsizemode` for
        more info.
    
        The 'x1' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['x1']

    @x1.setter
    def x1(self, val):
        self['x1'] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Only relevant in conjunction with `xsizemode` set to "pixel".
        Specifies the anchor point on the x axis to which `x0`, `x1`
        and x coordinates within `path` are relative to. E.g. useful to
        attach a pixel sized shape to a certain data value. No effect
        when `xsizemode` not set to "pixel".
    
        The 'xanchor' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['xanchor']

    @xanchor.setter
    def xanchor(self, val):
        self['xanchor'] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the shape's x coordinate axis. If set to an x axis id
        (e.g. "x" or "x2"), the `x` position refers to an x coordinate.
        If set to "paper", the `x` position refers to the distance from
        the left side of the plotting area in normalized coordinates
        where 0 (1) corresponds to the left (right) side. If the axis
        `type` is "log", then you must take the log of your desired
        range. If the axis `type` is "date", then you must convert the
        date to unix time in milliseconds.
    
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

    # xsizemode
    # ---------
    @property
    def xsizemode(self):
        """
        Sets the shapes's sizing mode along the x axis. If set to
        "scaled", `x0`, `x1` and x coordinates within `path` refer to
        data values on the x axis or a fraction of the plot area's
        width (`xref` set to "paper"). If set to "pixel", `xanchor`
        specifies the x position in terms of data or plot fraction but
        `x0`, `x1` and x coordinates within `path` are pixels relative
        to `xanchor`. This way, the shape can have a fixed width while
        maintaining a position relative to data or plot fraction.
    
        The 'xsizemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['scaled', 'pixel']

        Returns
        -------
        Any
        """
        return self['xsizemode']

    @xsizemode.setter
    def xsizemode(self, val):
        self['xsizemode'] = val

    # y0
    # --
    @property
    def y0(self):
        """
        Sets the shape's starting y position. See `type` and
        `ysizemode` for more info.
    
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
        Sets the shape's end y position. See `type` and `ysizemode` for
        more info.
    
        The 'y1' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['y1']

    @y1.setter
    def y1(self, val):
        self['y1'] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Only relevant in conjunction with `ysizemode` set to "pixel".
        Specifies the anchor point on the y axis to which `y0`, `y1`
        and y coordinates within `path` are relative to. E.g. useful to
        attach a pixel sized shape to a certain data value. No effect
        when `ysizemode` not set to "pixel".
    
        The 'yanchor' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['yanchor']

    @yanchor.setter
    def yanchor(self, val):
        self['yanchor'] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the annotation's y coordinate axis. If set to an y axis id
        (e.g. "y" or "y2"), the `y` position refers to an y coordinate
        If set to "paper", the `y` position refers to the distance from
        the bottom of the plotting area in normalized coordinates where
        0 (1) corresponds to the bottom (top).
    
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

    # ysizemode
    # ---------
    @property
    def ysizemode(self):
        """
        Sets the shapes's sizing mode along the y axis. If set to
        "scaled", `y0`, `y1` and y coordinates within `path` refer to
        data values on the y axis or a fraction of the plot area's
        height (`yref` set to "paper"). If set to "pixel", `yanchor`
        specifies the y position in terms of data or plot fraction but
        `y0`, `y1` and y coordinates within `path` are pixels relative
        to `yanchor`. This way, the shape can have a fixed height while
        maintaining a position relative to data or plot fraction.
    
        The 'ysizemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['scaled', 'pixel']

        Returns
        -------
        Any
        """
        return self['ysizemode']

    @ysizemode.setter
    def ysizemode(self, val):
        self['ysizemode'] = val

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
            Sets the opacity of the shape.
        path
            For `type` "path" - a valid SVG path with the pixel
            values replaced by data values in
            `xsizemode`/`ysizemode` being "scaled" and taken
            unmodified as pixels relative to `xanchor` and
            `yanchor` in case of "pixel" size mode. There are a few
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
            Specifies the shape type to be drawn. If "line", a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect
            to the axes' sizing mode. If "circle", a circle is
            drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
            (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with
            respect to the axes' sizing mode. If "rect", a
            rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`),
            (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect to
            the axes' sizing mode. If "path", draw a custom SVG
            path using `path`. with respect to the axes' sizing
            mode.
        visible
            Determines whether or not this shape is visible.
        x0
            Sets the shape's starting x position. See `type` and
            `xsizemode` for more info.
        x1
            Sets the shape's end x position. See `type` and
            `xsizemode` for more info.
        xanchor
            Only relevant in conjunction with `xsizemode` set to
            "pixel". Specifies the anchor point on the x axis to
            which `x0`, `x1` and x coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `xsizemode` not
            set to "pixel".
        xref
            Sets the shape's x coordinate axis. If set to an x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            coordinate. If set to "paper", the `x` position refers
            to the distance from the left side of the plotting area
            in normalized coordinates where 0 (1) corresponds to
            the left (right) side. If the axis `type` is "log",
            then you must take the log of your desired range. If
            the axis `type` is "date", then you must convert the
            date to unix time in milliseconds.
        xsizemode
            Sets the shapes's sizing mode along the x axis. If set
            to "scaled", `x0`, `x1` and x coordinates within `path`
            refer to data values on the x axis or a fraction of the
            plot area's width (`xref` set to "paper"). If set to
            "pixel", `xanchor` specifies the x position in terms of
            data or plot fraction but `x0`, `x1` and x coordinates
            within `path` are pixels relative to `xanchor`. This
            way, the shape can have a fixed width while maintaining
            a position relative to data or plot fraction.
        y0
            Sets the shape's starting y position. See `type` and
            `ysizemode` for more info.
        y1
            Sets the shape's end y position. See `type` and
            `ysizemode` for more info.
        yanchor
            Only relevant in conjunction with `ysizemode` set to
            "pixel". Specifies the anchor point on the y axis to
            which `y0`, `y1` and y coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `ysizemode` not
            set to "pixel".
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. "y" or "y2"), the `y` position refers to
            an y coordinate If set to "paper", the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        ysizemode
            Sets the shapes's sizing mode along the y axis. If set
            to "scaled", `y0`, `y1` and y coordinates within `path`
            refer to data values on the y axis or a fraction of the
            plot area's height (`yref` set to "paper"). If set to
            "pixel", `yanchor` specifies the y position in terms of
            data or plot fraction but `y0`, `y1` and y coordinates
            within `path` are pixels relative to `yanchor`. This
            way, the shape can have a fixed height while
            maintaining a position relative to data or plot
            fraction.
        """

    def __init__(
        self,
        arg=None,
        fillcolor=None,
        layer=None,
        line=None,
        name=None,
        opacity=None,
        path=None,
        templateitemname=None,
        type=None,
        visible=None,
        x0=None,
        x1=None,
        xanchor=None,
        xref=None,
        xsizemode=None,
        y0=None,
        y1=None,
        yanchor=None,
        yref=None,
        ysizemode=None,
        **kwargs
    ):
        """
        Construct a new Shape object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Shape
        fillcolor
            Sets the color filling the shape's interior.
        layer
            Specifies whether shapes are drawn below or above
            traces.
        line
            plotly.graph_objs.layout.shape.Line instance or dict
            with compatible properties
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
            Sets the opacity of the shape.
        path
            For `type` "path" - a valid SVG path with the pixel
            values replaced by data values in
            `xsizemode`/`ysizemode` being "scaled" and taken
            unmodified as pixels relative to `xanchor` and
            `yanchor` in case of "pixel" size mode. There are a few
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
            Specifies the shape type to be drawn. If "line", a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect
            to the axes' sizing mode. If "circle", a circle is
            drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
            (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with
            respect to the axes' sizing mode. If "rect", a
            rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`),
            (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect to
            the axes' sizing mode. If "path", draw a custom SVG
            path using `path`. with respect to the axes' sizing
            mode.
        visible
            Determines whether or not this shape is visible.
        x0
            Sets the shape's starting x position. See `type` and
            `xsizemode` for more info.
        x1
            Sets the shape's end x position. See `type` and
            `xsizemode` for more info.
        xanchor
            Only relevant in conjunction with `xsizemode` set to
            "pixel". Specifies the anchor point on the x axis to
            which `x0`, `x1` and x coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `xsizemode` not
            set to "pixel".
        xref
            Sets the shape's x coordinate axis. If set to an x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            coordinate. If set to "paper", the `x` position refers
            to the distance from the left side of the plotting area
            in normalized coordinates where 0 (1) corresponds to
            the left (right) side. If the axis `type` is "log",
            then you must take the log of your desired range. If
            the axis `type` is "date", then you must convert the
            date to unix time in milliseconds.
        xsizemode
            Sets the shapes's sizing mode along the x axis. If set
            to "scaled", `x0`, `x1` and x coordinates within `path`
            refer to data values on the x axis or a fraction of the
            plot area's width (`xref` set to "paper"). If set to
            "pixel", `xanchor` specifies the x position in terms of
            data or plot fraction but `x0`, `x1` and x coordinates
            within `path` are pixels relative to `xanchor`. This
            way, the shape can have a fixed width while maintaining
            a position relative to data or plot fraction.
        y0
            Sets the shape's starting y position. See `type` and
            `ysizemode` for more info.
        y1
            Sets the shape's end y position. See `type` and
            `ysizemode` for more info.
        yanchor
            Only relevant in conjunction with `ysizemode` set to
            "pixel". Specifies the anchor point on the y axis to
            which `y0`, `y1` and y coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `ysizemode` not
            set to "pixel".
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. "y" or "y2"), the `y` position refers to
            an y coordinate If set to "paper", the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        ysizemode
            Sets the shapes's sizing mode along the y axis. If set
            to "scaled", `y0`, `y1` and y coordinates within `path`
            refer to data values on the y axis or a fraction of the
            plot area's height (`yref` set to "paper"). If set to
            "pixel", `yanchor` specifies the y position in terms of
            data or plot fraction but `y0`, `y1` and y coordinates
            within `path` are pixels relative to `yanchor`. This
            way, the shape can have a fixed height while
            maintaining a position relative to data or plot
            fraction.

        Returns
        -------
        Shape
        """
        super(Shape, self).__init__('shapes')

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
The first argument to the plotly.graph_objs.layout.Shape 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Shape"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout import (shape as v_shape)

        # Initialize validators
        # ---------------------
        self._validators['fillcolor'] = v_shape.FillcolorValidator()
        self._validators['layer'] = v_shape.LayerValidator()
        self._validators['line'] = v_shape.LineValidator()
        self._validators['name'] = v_shape.NameValidator()
        self._validators['opacity'] = v_shape.OpacityValidator()
        self._validators['path'] = v_shape.PathValidator()
        self._validators['templateitemname'
                        ] = v_shape.TemplateitemnameValidator()
        self._validators['type'] = v_shape.TypeValidator()
        self._validators['visible'] = v_shape.VisibleValidator()
        self._validators['x0'] = v_shape.X0Validator()
        self._validators['x1'] = v_shape.X1Validator()
        self._validators['xanchor'] = v_shape.XanchorValidator()
        self._validators['xref'] = v_shape.XrefValidator()
        self._validators['xsizemode'] = v_shape.XsizemodeValidator()
        self._validators['y0'] = v_shape.Y0Validator()
        self._validators['y1'] = v_shape.Y1Validator()
        self._validators['yanchor'] = v_shape.YanchorValidator()
        self._validators['yref'] = v_shape.YrefValidator()
        self._validators['ysizemode'] = v_shape.YsizemodeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('fillcolor', None)
        self['fillcolor'] = fillcolor if fillcolor is not None else _v
        _v = arg.pop('layer', None)
        self['layer'] = layer if layer is not None else _v
        _v = arg.pop('line', None)
        self['line'] = line if line is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('path', None)
        self['path'] = path if path is not None else _v
        _v = arg.pop('templateitemname', None)
        self['templateitemname'
            ] = templateitemname if templateitemname is not None else _v
        _v = arg.pop('type', None)
        self['type'] = type if type is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v
        _v = arg.pop('x0', None)
        self['x0'] = x0 if x0 is not None else _v
        _v = arg.pop('x1', None)
        self['x1'] = x1 if x1 is not None else _v
        _v = arg.pop('xanchor', None)
        self['xanchor'] = xanchor if xanchor is not None else _v
        _v = arg.pop('xref', None)
        self['xref'] = xref if xref is not None else _v
        _v = arg.pop('xsizemode', None)
        self['xsizemode'] = xsizemode if xsizemode is not None else _v
        _v = arg.pop('y0', None)
        self['y0'] = y0 if y0 is not None else _v
        _v = arg.pop('y1', None)
        self['y1'] = y1 if y1 is not None else _v
        _v = arg.pop('yanchor', None)
        self['yanchor'] = yanchor if yanchor is not None else _v
        _v = arg.pop('yref', None)
        self['yref'] = yref if yref is not None else _v
        _v = arg.pop('ysizemode', None)
        self['ysizemode'] = ysizemode if ysizemode is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
