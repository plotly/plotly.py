from plotly.basedatatypes import BaseTraceHierarchyType


class Fill(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the cell fill color. It accepts either a specific color or
        an array of colors.
    
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
    
        The 'colorsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'table.cells'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the cell fill color. It accepts either a specific
            color or an array of colors.
        colorsrc
            Sets the source reference on plot.ly for  color .
        """

    def __init__(self, color=None, colorsrc=None, **kwargs):
        """
        Construct a new Fill object
        
        Parameters
        ----------
        color
            Sets the cell fill color. It accepts either a specific
            color or an array of colors.
        colorsrc
            Sets the source reference on plot.ly for  color .

        Returns
        -------
        Fill
        """
        super(Fill, self).__init__('fill')

        # Import validators
        # -----------------
        from plotly.validators.table.cells import (fill as v_fill)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_fill.ColorValidator()
        self._validators['colorsrc'] = v_fill.ColorsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.color = color
        self.colorsrc = colorsrc

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
