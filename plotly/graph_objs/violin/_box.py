from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Box(BaseTraceHierarchyType):

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the inner box plot fill color.
    
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

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.violin.box.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the inner box plot bounding line color.
                width
                    Sets the inner box plot bounding line width.

        Returns
        -------
        plotly.graph_objs.violin.box.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines if an miniature box plot is drawn inside the
        violins.
    
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

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width of the inner box plots relative to the violins'
        width. For example, with 1, the inner box plots are as wide as
        the violins.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'violin'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fillcolor
            Sets the inner box plot fill color.
        line
            plotly.graph_objs.violin.box.Line instance or dict with
            compatible properties
        visible
            Determines if an miniature box plot is drawn inside the
            violins.
        width
            Sets the width of the inner box plots relative to the
            violins' width. For example, with 1, the inner box
            plots are as wide as the violins.
        """

    def __init__(
        self,
        arg=None,
        fillcolor=None,
        line=None,
        visible=None,
        width=None,
        **kwargs
    ):
        """
        Construct a new Box object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.violin.Box
        fillcolor
            Sets the inner box plot fill color.
        line
            plotly.graph_objs.violin.box.Line instance or dict with
            compatible properties
        visible
            Determines if an miniature box plot is drawn inside the
            violins.
        width
            Sets the width of the inner box plots relative to the
            violins' width. For example, with 1, the inner box
            plots are as wide as the violins.

        Returns
        -------
        Box
        """
        super(Box, self).__init__('box')

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
The first argument to the plotly.graph_objs.violin.Box 
constructor must be a dict or 
an instance of plotly.graph_objs.violin.Box"""
            )

        # Import validators
        # -----------------
        from plotly.validators.violin import (box as v_box)

        # Initialize validators
        # ---------------------
        self._validators['fillcolor'] = v_box.FillcolorValidator()
        self._validators['line'] = v_box.LineValidator()
        self._validators['visible'] = v_box.VisibleValidator()
        self._validators['width'] = v_box.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('fillcolor', None)
        self.fillcolor = fillcolor if fillcolor is not None else _v
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v
        _v = arg.pop('width', None)
        self.width = width if width is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
