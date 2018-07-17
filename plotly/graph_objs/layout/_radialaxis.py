from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class RadialAxis(BaseLayoutHierarchyType):

    # domain
    # ------
    @property
    def domain(self):
        """
        Polar chart subplots are not supported yet. This key has
        currently no effect.
    
        The 'domain' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'domain[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'domain[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # endpadding
    # ----------
    @property
    def endpadding(self):
        """
        The 'endpadding' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['endpadding']

    @endpadding.setter
    def endpadding(self, val):
        self['endpadding'] = val

    # orientation
    # -----------
    @property
    def orientation(self):
        """
        Sets the orientation (an angle with respect to the origin) of
        the radial axis.
    
        The 'orientation' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['orientation']

    @orientation.setter
    def orientation(self, val):
        self['orientation'] = val

    # range
    # -----
    @property
    def range(self):
        """
        Defines the start and end point of this radial axis.
    
        The 'range' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'range[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'range[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self['range']

    @range.setter
    def range(self, val):
        self['range'] = val

    # showline
    # --------
    @property
    def showline(self):
        """
        Determines whether or not the line bounding this radial axis
        will be shown on the figure.
    
        The 'showline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showline']

    @showline.setter
    def showline(self, val):
        self['showline'] = val

    # showticklabels
    # --------------
    @property
    def showticklabels(self):
        """
        Determines whether or not the radial axis ticks will feature
        tick labels.
    
        The 'showticklabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showticklabels']

    @showticklabels.setter
    def showticklabels(self, val):
        self['showticklabels'] = val

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Sets the color of the tick lines on this radial axis.
    
        The 'tickcolor' property is a color and may be specified as:
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
        return self['tickcolor']

    @tickcolor.setter
    def tickcolor(self, val):
        self['tickcolor'] = val

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Sets the length of the tick lines on this radial axis.
    
        The 'ticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['ticklen']

    @ticklen.setter
    def ticklen(self, val):
        self['ticklen'] = val

    # tickorientation
    # ---------------
    @property
    def tickorientation(self):
        """
        Sets the orientation (from the paper perspective) of the radial
        axis tick labels.
    
        The 'tickorientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['horizontal', 'vertical']

        Returns
        -------
        Any
        """
        return self['tickorientation']

    @tickorientation.setter
    def tickorientation(self, val):
        self['tickorientation'] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Sets the length of the tick lines on this radial axis.
    
        The 'ticksuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['ticksuffix']

    @ticksuffix.setter
    def ticksuffix(self, val):
        self['ticksuffix'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this axis will be visible.
    
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
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        domain
            Polar chart subplots are not supported yet. This key
            has currently no effect.
        endpadding

        orientation
            Sets the orientation (an angle with respect to the
            origin) of the radial axis.
        range
            Defines the start and end point of this radial axis.
        showline
            Determines whether or not the line bounding this radial
            axis will be shown on the figure.
        showticklabels
            Determines whether or not the radial axis ticks will
            feature tick labels.
        tickcolor
            Sets the color of the tick lines on this radial axis.
        ticklen
            Sets the length of the tick lines on this radial axis.
        tickorientation
            Sets the orientation (from the paper perspective) of
            the radial axis tick labels.
        ticksuffix
            Sets the length of the tick lines on this radial axis.
        visible
            Determines whether or not this axis will be visible.
        """

    def __init__(
        self,
        arg=None,
        domain=None,
        endpadding=None,
        orientation=None,
        range=None,
        showline=None,
        showticklabels=None,
        tickcolor=None,
        ticklen=None,
        tickorientation=None,
        ticksuffix=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new RadialAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.RadialAxis
        domain
            Polar chart subplots are not supported yet. This key
            has currently no effect.
        endpadding

        orientation
            Sets the orientation (an angle with respect to the
            origin) of the radial axis.
        range
            Defines the start and end point of this radial axis.
        showline
            Determines whether or not the line bounding this radial
            axis will be shown on the figure.
        showticklabels
            Determines whether or not the radial axis ticks will
            feature tick labels.
        tickcolor
            Sets the color of the tick lines on this radial axis.
        ticklen
            Sets the length of the tick lines on this radial axis.
        tickorientation
            Sets the orientation (from the paper perspective) of
            the radial axis tick labels.
        ticksuffix
            Sets the length of the tick lines on this radial axis.
        visible
            Determines whether or not this axis will be visible.

        Returns
        -------
        RadialAxis
        """
        super(RadialAxis, self).__init__('radialaxis')

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
The first argument to the plotly.graph_objs.layout.RadialAxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.RadialAxis"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout import (radialaxis as v_radialaxis)

        # Initialize validators
        # ---------------------
        self._validators['domain'] = v_radialaxis.DomainValidator()
        self._validators['endpadding'] = v_radialaxis.EndpaddingValidator()
        self._validators['orientation'] = v_radialaxis.OrientationValidator()
        self._validators['range'] = v_radialaxis.RangeValidator()
        self._validators['showline'] = v_radialaxis.ShowlineValidator()
        self._validators['showticklabels'
                        ] = v_radialaxis.ShowticklabelsValidator()
        self._validators['tickcolor'] = v_radialaxis.TickcolorValidator()
        self._validators['ticklen'] = v_radialaxis.TicklenValidator()
        self._validators['tickorientation'
                        ] = v_radialaxis.TickorientationValidator()
        self._validators['ticksuffix'] = v_radialaxis.TicksuffixValidator()
        self._validators['visible'] = v_radialaxis.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('domain', None)
        self.domain = domain if domain is not None else _v
        _v = arg.pop('endpadding', None)
        self.endpadding = endpadding if endpadding is not None else _v
        _v = arg.pop('orientation', None)
        self.orientation = orientation if orientation is not None else _v
        _v = arg.pop('range', None)
        self.range = range if range is not None else _v
        _v = arg.pop('showline', None)
        self.showline = showline if showline is not None else _v
        _v = arg.pop('showticklabels', None)
        self.showticklabels = showticklabels if showticklabels is not None else _v
        _v = arg.pop('tickcolor', None)
        self.tickcolor = tickcolor if tickcolor is not None else _v
        _v = arg.pop('ticklen', None)
        self.ticklen = ticklen if ticklen is not None else _v
        _v = arg.pop('tickorientation', None)
        self.tickorientation = tickorientation if tickorientation is not None else _v
        _v = arg.pop('ticksuffix', None)
        self.ticksuffix = ticksuffix if ticksuffix is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
