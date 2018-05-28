from plotly.basedatatypes import BaseTraceHierarchyType


class Lightposition(BaseTraceHierarchyType):

    # x
    # -
    @property
    def x(self):
        """
        Numeric vector, representing the X coordinate for each vertex.
    
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-100000, 100000]

        Returns
        -------
        int|float
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
        Numeric vector, representing the Y coordinate for each vertex.
    
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-100000, 100000]

        Returns
        -------
        int|float
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
        Numeric vector, representing the Z coordinate for each vertex.
    
        The 'z' property is a number and may be specified as:
          - An int or float in the interval [-100000, 100000]

        Returns
        -------
        int|float
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'mesh3d'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x
            Numeric vector, representing the X coordinate for each
            vertex.
        y
            Numeric vector, representing the Y coordinate for each
            vertex.
        z
            Numeric vector, representing the Z coordinate for each
            vertex.
        """

    def __init__(self, x=None, y=None, z=None, **kwargs):
        """
        Construct a new Lightposition object
        
        Parameters
        ----------
        x
            Numeric vector, representing the X coordinate for each
            vertex.
        y
            Numeric vector, representing the Y coordinate for each
            vertex.
        z
            Numeric vector, representing the Z coordinate for each
            vertex.

        Returns
        -------
        Lightposition
        """
        super(Lightposition, self).__init__('lightposition')

        # Import validators
        # -----------------
        from plotly.validators.mesh3d import (lightposition as v_lightposition)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_lightposition.XValidator()
        self._validators['y'] = v_lightposition.YValidator()
        self._validators['z'] = v_lightposition.ZValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.x = x
        self.y = y
        self.z = z

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
