from plotly.basedatatypes import BaseTraceHierarchyType


class Projection(BaseTraceHierarchyType):

    # x
    # -
    @property
    def x(self):
        """
        The 'x' property is an instance of X
        that may be specified as:
          - An instance of plotly.graph_objs.scatter3d.projection.X
          - A dict of string/value properties that will be passed
            to the X constructor
    
            Supported dict properties:
                
                opacity
                    Sets the projection color.
                scale
                    Sets the scale factor determining the size of
                    the projection marker points.
                show
                    Sets whether or not projections are shown along
                    the x axis.

        Returns
        -------
        plotly.graph_objs.scatter3d.projection.X
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
          - An instance of plotly.graph_objs.scatter3d.projection.Y
          - A dict of string/value properties that will be passed
            to the Y constructor
    
            Supported dict properties:
                
                opacity
                    Sets the projection color.
                scale
                    Sets the scale factor determining the size of
                    the projection marker points.
                show
                    Sets whether or not projections are shown along
                    the y axis.

        Returns
        -------
        plotly.graph_objs.scatter3d.projection.Y
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
          - An instance of plotly.graph_objs.scatter3d.projection.Z
          - A dict of string/value properties that will be passed
            to the Z constructor
    
            Supported dict properties:
                
                opacity
                    Sets the projection color.
                scale
                    Sets the scale factor determining the size of
                    the projection marker points.
                show
                    Sets whether or not projections are shown along
                    the z axis.

        Returns
        -------
        plotly.graph_objs.scatter3d.projection.Z
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'scatter3d'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x
            plotly.graph_objs.scatter3d.projection.X instance or
            dict with compatible properties
        y
            plotly.graph_objs.scatter3d.projection.Y instance or
            dict with compatible properties
        z
            plotly.graph_objs.scatter3d.projection.Z instance or
            dict with compatible properties
        """

    def __init__(self, x=None, y=None, z=None, **kwargs):
        """
        Construct a new Projection object
        
        Parameters
        ----------
        x
            plotly.graph_objs.scatter3d.projection.X instance or
            dict with compatible properties
        y
            plotly.graph_objs.scatter3d.projection.Y instance or
            dict with compatible properties
        z
            plotly.graph_objs.scatter3d.projection.Z instance or
            dict with compatible properties

        Returns
        -------
        Projection
        """
        super(Projection, self).__init__('projection')

        # Import validators
        # -----------------
        from plotly.validators.scatter3d import (projection as v_projection)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_projection.XValidator()
        self._validators['y'] = v_projection.YValidator()
        self._validators['z'] = v_projection.ZValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.x = x
        self.y = y
        self.z = z

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
