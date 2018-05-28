from plotly.basedatatypes import BaseTraceHierarchyType


class Contours(BaseTraceHierarchyType):

    # x
    # -
    @property
    def x(self):
        """
        The 'x' property is an instance of X
        that may be specified as:
          - An instance of plotly.graph_objs.surface.contours.X
          - A dict of string/value properties that will be passed
            to the X constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the contour lines.
                highlight
                    Determines whether or not contour lines about
                    the x dimension are highlighted on hover.
                highlightcolor
                    Sets the color of the highlighted contour
                    lines.
                highlightwidth
                    Sets the width of the highlighted contour
                    lines.
                project
                    plotly.graph_objs.surface.contours.x.Project
                    instance or dict with compatible properties
                show
                    Determines whether or not contour lines about
                    the x dimension are drawn.
                usecolormap
                    An alternate to *color*. Determines whether or
                    not the contour lines are colored using the
                    trace *colorscale*.
                width
                    Sets the width of the contour lines.

        Returns
        -------
        plotly.graph_objs.surface.contours.X
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # y
    # -
    @property
    def y(self):
        """
        The 'y' property is an instance of Y
        that may be specified as:
          - An instance of plotly.graph_objs.surface.contours.Y
          - A dict of string/value properties that will be passed
            to the Y constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the contour lines.
                highlight
                    Determines whether or not contour lines about
                    the y dimension are highlighted on hover.
                highlightcolor
                    Sets the color of the highlighted contour
                    lines.
                highlightwidth
                    Sets the width of the highlighted contour
                    lines.
                project
                    plotly.graph_objs.surface.contours.y.Project
                    instance or dict with compatible properties
                show
                    Determines whether or not contour lines about
                    the y dimension are drawn.
                usecolormap
                    An alternate to *color*. Determines whether or
                    not the contour lines are colored using the
                    trace *colorscale*.
                width
                    Sets the width of the contour lines.

        Returns
        -------
        plotly.graph_objs.surface.contours.Y
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # z
    # -
    @property
    def z(self):
        """
        The 'z' property is an instance of Z
        that may be specified as:
          - An instance of plotly.graph_objs.surface.contours.Z
          - A dict of string/value properties that will be passed
            to the Z constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the contour lines.
                highlight
                    Determines whether or not contour lines about
                    the z dimension are highlighted on hover.
                highlightcolor
                    Sets the color of the highlighted contour
                    lines.
                highlightwidth
                    Sets the width of the highlighted contour
                    lines.
                project
                    plotly.graph_objs.surface.contours.z.Project
                    instance or dict with compatible properties
                show
                    Determines whether or not contour lines about
                    the z dimension are drawn.
                usecolormap
                    An alternate to *color*. Determines whether or
                    not the contour lines are colored using the
                    trace *colorscale*.
                width
                    Sets the width of the contour lines.

        Returns
        -------
        plotly.graph_objs.surface.contours.Z
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'surface'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x
            plotly.graph_objs.surface.contours.X instance or dict
            with compatible properties
        y
            plotly.graph_objs.surface.contours.Y instance or dict
            with compatible properties
        z
            plotly.graph_objs.surface.contours.Z instance or dict
            with compatible properties
        """

    def __init__(self, x=None, y=None, z=None, **kwargs):
        """
        Construct a new Contours object
        
        Parameters
        ----------
        x
            plotly.graph_objs.surface.contours.X instance or dict
            with compatible properties
        y
            plotly.graph_objs.surface.contours.Y instance or dict
            with compatible properties
        z
            plotly.graph_objs.surface.contours.Z instance or dict
            with compatible properties

        Returns
        -------
        Contours
        """
        super(Contours, self).__init__('contours')

        # Import validators
        # -----------------
        from plotly.validators.surface import (contours as v_contours)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_contours.XValidator()
        self._validators['y'] = v_contours.YValidator()
        self._validators['z'] = v_contours.ZValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.x = x
        self.y = y
        self.z = z

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
