from plotly.basedatatypes import BaseTraceHierarchyType


class Meanline(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the mean line color.
    
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

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines if a line corresponding to the sample's mean is
        shown inside the violins. If `box.visible` is turned on, the
        mean line is drawn inside the inner box. Otherwise, the mean
        line is drawn from one side of the violin to other.
    
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
        Sets the mean line width.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

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
        color
            Sets the mean line color.
        visible
            Determines if a line corresponding to the sample's mean
            is shown inside the violins. If `box.visible` is turned
            on, the mean line is drawn inside the inner box.
            Otherwise, the mean line is drawn from one side of the
            violin to other.
        width
            Sets the mean line width.
        """

    def __init__(self, color=None, visible=None, width=None, **kwargs):
        """
        Construct a new Meanline object
        
        Parameters
        ----------
        color
            Sets the mean line color.
        visible
            Determines if a line corresponding to the sample's mean
            is shown inside the violins. If `box.visible` is turned
            on, the mean line is drawn inside the inner box.
            Otherwise, the mean line is drawn from one side of the
            violin to other.
        width
            Sets the mean line width.

        Returns
        -------
        Meanline
        """
        super(Meanline, self).__init__('meanline')

        # Import validators
        # -----------------
        from plotly.validators.violin import (meanline as v_meanline)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_meanline.ColorValidator()
        self._validators['visible'] = v_meanline.VisibleValidator()
        self._validators['width'] = v_meanline.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.color = color
        self.visible = visible
        self.width = width

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
