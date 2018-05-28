from plotly.basedatatypes import BaseTraceHierarchyType


class Increasing(BaseTraceHierarchyType):

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the fill color. Defaults to a half-transparent variant of
        the line color, marker color, or marker line color, whichever
        is available.
    
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
          - An instance of plotly.graph_objs.candlestick.increasing.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of line bounding the box(es).
                width
                    Sets the width (in px) of line bounding the
                    box(es).

        Returns
        -------
        plotly.graph_objs.candlestick.increasing.Line
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
        Sets the segment name. The segment name appear as the legend
        item and on hover.
    
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

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this segment
        is shown in the legend.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlegend']

    @showlegend.setter
    def showlegend(self, val):
        self['showlegend'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'candlestick'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        line
            plotly.graph_objs.candlestick.increasing.Line instance
            or dict with compatible properties
        name
            Sets the segment name. The segment name appear as the
            legend item and on hover.
        showlegend
            Determines whether or not an item corresponding to this
            segment is shown in the legend.
        """

    def __init__(
        self, fillcolor=None, line=None, name=None, showlegend=None, **kwargs
    ):
        """
        Construct a new Increasing object
        
        Parameters
        ----------
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        line
            plotly.graph_objs.candlestick.increasing.Line instance
            or dict with compatible properties
        name
            Sets the segment name. The segment name appear as the
            legend item and on hover.
        showlegend
            Determines whether or not an item corresponding to this
            segment is shown in the legend.

        Returns
        -------
        Increasing
        """
        super(Increasing, self).__init__('increasing')

        # Import validators
        # -----------------
        from plotly.validators.candlestick import (increasing as v_increasing)

        # Initialize validators
        # ---------------------
        self._validators['fillcolor'] = v_increasing.FillcolorValidator()
        self._validators['line'] = v_increasing.LineValidator()
        self._validators['name'] = v_increasing.NameValidator()
        self._validators['showlegend'] = v_increasing.ShowlegendValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.fillcolor = fillcolor
        self.line = line
        self.name = name
        self.showlegend = showlegend

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
