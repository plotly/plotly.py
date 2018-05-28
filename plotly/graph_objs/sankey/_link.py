from plotly.basedatatypes import BaseTraceHierarchyType


class Link(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the `link` color. It can be a single value, or an array
        for specifying color for each `link`. If `link.color` is
        omitted, then by default, a translucent grey link will be used.
    
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

    # label
    # -----
    @property
    def label(self):
        """
        The shown name of the link.
    
        The 'label' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['label']

    @label.setter
    def label(self, val):
        self['label'] = val

    # labelsrc
    # --------
    @property
    def labelsrc(self):
        """
        Sets the source reference on plot.ly for  label .
    
        The 'labelsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['labelsrc']

    @labelsrc.setter
    def labelsrc(self, val):
        self['labelsrc'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.sankey.link.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the `line` around each
                    `link`.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                width
                    Sets the width (in px) of the `line` around
                    each `link`.
                widthsrc
                    Sets the source reference on plot.ly for  width
                    .

        Returns
        -------
        plotly.graph_objs.sankey.link.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # source
    # ------
    @property
    def source(self):
        """
        An integer number `[0..nodes.length - 1]` that represents the
        source node.
    
        The 'source' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['source']

    @source.setter
    def source(self, val):
        self['source'] = val

    # sourcesrc
    # ---------
    @property
    def sourcesrc(self):
        """
        Sets the source reference on plot.ly for  source .
    
        The 'sourcesrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['sourcesrc']

    @sourcesrc.setter
    def sourcesrc(self, val):
        self['sourcesrc'] = val

    # target
    # ------
    @property
    def target(self):
        """
        An integer number `[0..nodes.length - 1]` that represents the
        target node.
    
        The 'target' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['target']

    @target.setter
    def target(self, val):
        self['target'] = val

    # targetsrc
    # ---------
    @property
    def targetsrc(self):
        """
        Sets the source reference on plot.ly for  target .
    
        The 'targetsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['targetsrc']

    @targetsrc.setter
    def targetsrc(self, val):
        self['targetsrc'] = val

    # value
    # -----
    @property
    def value(self):
        """
        A numeric value representing the flow volume value.
    
        The 'value' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

    # valuesrc
    # --------
    @property
    def valuesrc(self):
        """
        Sets the source reference on plot.ly for  value .
    
        The 'valuesrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['valuesrc']

    @valuesrc.setter
    def valuesrc(self, val):
        self['valuesrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'sankey'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the `link` color. It can be a single value, or an
            array for specifying color for each `link`. If
            `link.color` is omitted, then by default, a translucent
            grey link will be used.
        colorsrc
            Sets the source reference on plot.ly for  color .
        label
            The shown name of the link.
        labelsrc
            Sets the source reference on plot.ly for  label .
        line
            plotly.graph_objs.sankey.link.Line instance or dict
            with compatible properties
        source
            An integer number `[0..nodes.length - 1]` that
            represents the source node.
        sourcesrc
            Sets the source reference on plot.ly for  source .
        target
            An integer number `[0..nodes.length - 1]` that
            represents the target node.
        targetsrc
            Sets the source reference on plot.ly for  target .
        value
            A numeric value representing the flow volume value.
        valuesrc
            Sets the source reference on plot.ly for  value .
        """

    def __init__(
        self,
        color=None,
        colorsrc=None,
        label=None,
        labelsrc=None,
        line=None,
        source=None,
        sourcesrc=None,
        target=None,
        targetsrc=None,
        value=None,
        valuesrc=None,
        **kwargs
    ):
        """
        Construct a new Link object
        
        The links of the Sankey plot.

        Parameters
        ----------
        color
            Sets the `link` color. It can be a single value, or an
            array for specifying color for each `link`. If
            `link.color` is omitted, then by default, a translucent
            grey link will be used.
        colorsrc
            Sets the source reference on plot.ly for  color .
        label
            The shown name of the link.
        labelsrc
            Sets the source reference on plot.ly for  label .
        line
            plotly.graph_objs.sankey.link.Line instance or dict
            with compatible properties
        source
            An integer number `[0..nodes.length - 1]` that
            represents the source node.
        sourcesrc
            Sets the source reference on plot.ly for  source .
        target
            An integer number `[0..nodes.length - 1]` that
            represents the target node.
        targetsrc
            Sets the source reference on plot.ly for  target .
        value
            A numeric value representing the flow volume value.
        valuesrc
            Sets the source reference on plot.ly for  value .

        Returns
        -------
        Link
        """
        super(Link, self).__init__('link')

        # Import validators
        # -----------------
        from plotly.validators.sankey import (link as v_link)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_link.ColorValidator()
        self._validators['colorsrc'] = v_link.ColorsrcValidator()
        self._validators['label'] = v_link.LabelValidator()
        self._validators['labelsrc'] = v_link.LabelsrcValidator()
        self._validators['line'] = v_link.LineValidator()
        self._validators['source'] = v_link.SourceValidator()
        self._validators['sourcesrc'] = v_link.SourcesrcValidator()
        self._validators['target'] = v_link.TargetValidator()
        self._validators['targetsrc'] = v_link.TargetsrcValidator()
        self._validators['value'] = v_link.ValueValidator()
        self._validators['valuesrc'] = v_link.ValuesrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.color = color
        self.colorsrc = colorsrc
        self.label = label
        self.labelsrc = labelsrc
        self.line = line
        self.source = source
        self.sourcesrc = sourcesrc
        self.target = target
        self.targetsrc = targetsrc
        self.value = value
        self.valuesrc = valuesrc

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
