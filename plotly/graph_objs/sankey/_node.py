from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Node(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the `node` color. It can be a single value, or an array
        for specifying color for each `node`. If `node.color` is
        omitted, then the default `Plotly` color palette will be cycled
        through to have a variety of colors. These defaults are not
        fully opaque, to allow some visibility of what is beneath the
        node.
    
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

    # label
    # -----
    @property
    def label(self):
        """
        The shown name of the node.
    
        The 'label' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

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
    
        The 'labelsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

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
          - An instance of plotly.graph_objs.sankey.node.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the `line` around each
                    `node`.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                width
                    Sets the width (in px) of the `line` around
                    each `node`.
                widthsrc
                    Sets the source reference on plot.ly for  width
                    .

        Returns
        -------
        plotly.graph_objs.sankey.node.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # pad
    # ---
    @property
    def pad(self):
        """
        Sets the padding (in px) between the `nodes`.
    
        The 'pad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['pad']

    @pad.setter
    def pad(self, val):
        self['pad'] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        Sets the thickness (in px) of the `nodes`.
    
        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self['thickness']

    @thickness.setter
    def thickness(self, val):
        self['thickness'] = val

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
            Sets the `node` color. It can be a single value, or an
            array for specifying color for each `node`. If
            `node.color` is omitted, then the default `Plotly`
            color palette will be cycled through to have a variety
            of colors. These defaults are not fully opaque, to
            allow some visibility of what is beneath the node.
        colorsrc
            Sets the source reference on plot.ly for  color .
        label
            The shown name of the node.
        labelsrc
            Sets the source reference on plot.ly for  label .
        line
            plotly.graph_objs.sankey.node.Line instance or dict
            with compatible properties
        pad
            Sets the padding (in px) between the `nodes`.
        thickness
            Sets the thickness (in px) of the `nodes`.
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        label=None,
        labelsrc=None,
        line=None,
        pad=None,
        thickness=None,
        **kwargs
    ):
        """
        Construct a new Node object
        
        The nodes of the Sankey plot.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.sankey.Node
        color
            Sets the `node` color. It can be a single value, or an
            array for specifying color for each `node`. If
            `node.color` is omitted, then the default `Plotly`
            color palette will be cycled through to have a variety
            of colors. These defaults are not fully opaque, to
            allow some visibility of what is beneath the node.
        colorsrc
            Sets the source reference on plot.ly for  color .
        label
            The shown name of the node.
        labelsrc
            Sets the source reference on plot.ly for  label .
        line
            plotly.graph_objs.sankey.node.Line instance or dict
            with compatible properties
        pad
            Sets the padding (in px) between the `nodes`.
        thickness
            Sets the thickness (in px) of the `nodes`.

        Returns
        -------
        Node
        """
        super(Node, self).__init__('node')

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
The first argument to the plotly.graph_objs.sankey.Node 
constructor must be a dict or 
an instance of plotly.graph_objs.sankey.Node"""
            )

        # Import validators
        # -----------------
        from plotly.validators.sankey import (node as v_node)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_node.ColorValidator()
        self._validators['colorsrc'] = v_node.ColorsrcValidator()
        self._validators['label'] = v_node.LabelValidator()
        self._validators['labelsrc'] = v_node.LabelsrcValidator()
        self._validators['line'] = v_node.LineValidator()
        self._validators['pad'] = v_node.PadValidator()
        self._validators['thickness'] = v_node.ThicknessValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('color', None)
        self.color = color if color is not None else _v
        _v = arg.pop('colorsrc', None)
        self.colorsrc = colorsrc if colorsrc is not None else _v
        _v = arg.pop('label', None)
        self.label = label if label is not None else _v
        _v = arg.pop('labelsrc', None)
        self.labelsrc = labelsrc if labelsrc is not None else _v
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v
        _v = arg.pop('pad', None)
        self.pad = pad if pad is not None else _v
        _v = arg.pop('thickness', None)
        self.thickness = thickness if thickness is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
