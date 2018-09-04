from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Z(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the color of the contour lines.
    
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

    # highlight
    # ---------
    @property
    def highlight(self):
        """
        Determines whether or not contour lines about the z dimension
        are highlighted on hover.
    
        The 'highlight' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['highlight']

    @highlight.setter
    def highlight(self, val):
        self['highlight'] = val

    # highlightcolor
    # --------------
    @property
    def highlightcolor(self):
        """
        Sets the color of the highlighted contour lines.
    
        The 'highlightcolor' property is a color and may be specified as:
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
        return self['highlightcolor']

    @highlightcolor.setter
    def highlightcolor(self, val):
        self['highlightcolor'] = val

    # highlightwidth
    # --------------
    @property
    def highlightwidth(self):
        """
        Sets the width of the highlighted contour lines.
    
        The 'highlightwidth' property is a number and may be specified as:
          - An int or float in the interval [1, 16]

        Returns
        -------
        int|float
        """
        return self['highlightwidth']

    @highlightwidth.setter
    def highlightwidth(self, val):
        self['highlightwidth'] = val

    # project
    # -------
    @property
    def project(self):
        """
        The 'project' property is an instance of Project
        that may be specified as:
          - An instance of plotly.graph_objs.surface.contours.z.Project
          - A dict of string/value properties that will be passed
            to the Project constructor
    
            Supported dict properties:
                
                x
                    Determines whether or not these contour lines
                    are projected on the x plane. If `highlight` is
                    set to True (the default), the projected lines
                    are shown on hover. If `show` is set to True,
                    the projected lines are shown in permanence.
                y
                    Determines whether or not these contour lines
                    are projected on the y plane. If `highlight` is
                    set to True (the default), the projected lines
                    are shown on hover. If `show` is set to True,
                    the projected lines are shown in permanence.
                z
                    Determines whether or not these contour lines
                    are projected on the z plane. If `highlight` is
                    set to True (the default), the projected lines
                    are shown on hover. If `show` is set to True,
                    the projected lines are shown in permanence.

        Returns
        -------
        plotly.graph_objs.surface.contours.z.Project
        """
        return self['project']

    @project.setter
    def project(self, val):
        self['project'] = val

    # show
    # ----
    @property
    def show(self):
        """
        Determines whether or not contour lines about the z dimension
        are drawn.
    
        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['show']

    @show.setter
    def show(self, val):
        self['show'] = val

    # usecolormap
    # -----------
    @property
    def usecolormap(self):
        """
        An alternate to "color". Determines whether or not the contour
        lines are colored using the trace "colorscale".
    
        The 'usecolormap' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['usecolormap']

    @usecolormap.setter
    def usecolormap(self, val):
        self['usecolormap'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width of the contour lines.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [1, 16]

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
        return 'surface.contours'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the color of the contour lines.
        highlight
            Determines whether or not contour lines about the z
            dimension are highlighted on hover.
        highlightcolor
            Sets the color of the highlighted contour lines.
        highlightwidth
            Sets the width of the highlighted contour lines.
        project
            plotly.graph_objs.surface.contours.z.Project instance
            or dict with compatible properties
        show
            Determines whether or not contour lines about the z
            dimension are drawn.
        usecolormap
            An alternate to "color". Determines whether or not the
            contour lines are colored using the trace "colorscale".
        width
            Sets the width of the contour lines.
        """

    def __init__(
        self,
        arg=None,
        color=None,
        highlight=None,
        highlightcolor=None,
        highlightwidth=None,
        project=None,
        show=None,
        usecolormap=None,
        width=None,
        **kwargs
    ):
        """
        Construct a new Z object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.surface.contours.Z
        color
            Sets the color of the contour lines.
        highlight
            Determines whether or not contour lines about the z
            dimension are highlighted on hover.
        highlightcolor
            Sets the color of the highlighted contour lines.
        highlightwidth
            Sets the width of the highlighted contour lines.
        project
            plotly.graph_objs.surface.contours.z.Project instance
            or dict with compatible properties
        show
            Determines whether or not contour lines about the z
            dimension are drawn.
        usecolormap
            An alternate to "color". Determines whether or not the
            contour lines are colored using the trace "colorscale".
        width
            Sets the width of the contour lines.

        Returns
        -------
        Z
        """
        super(Z, self).__init__('z')

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
The first argument to the plotly.graph_objs.surface.contours.Z 
constructor must be a dict or 
an instance of plotly.graph_objs.surface.contours.Z"""
            )

        # Import validators
        # -----------------
        from plotly.validators.surface.contours import (z as v_z)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_z.ColorValidator()
        self._validators['highlight'] = v_z.HighlightValidator()
        self._validators['highlightcolor'] = v_z.HighlightcolorValidator()
        self._validators['highlightwidth'] = v_z.HighlightwidthValidator()
        self._validators['project'] = v_z.ProjectValidator()
        self._validators['show'] = v_z.ShowValidator()
        self._validators['usecolormap'] = v_z.UsecolormapValidator()
        self._validators['width'] = v_z.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('color', None)
        self.color = color if color is not None else _v
        _v = arg.pop('highlight', None)
        self.highlight = highlight if highlight is not None else _v
        _v = arg.pop('highlightcolor', None)
        self.highlightcolor = highlightcolor if highlightcolor is not None else _v
        _v = arg.pop('highlightwidth', None)
        self.highlightwidth = highlightwidth if highlightwidth is not None else _v
        _v = arg.pop('project', None)
        self.project = project if project is not None else _v
        _v = arg.pop('show', None)
        self.show = show if show is not None else _v
        _v = arg.pop('usecolormap', None)
        self.usecolormap = usecolormap if usecolormap is not None else _v
        _v = arg.pop('width', None)
        self.width = width if width is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
