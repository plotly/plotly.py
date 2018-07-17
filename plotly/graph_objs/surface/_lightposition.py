from plotly.basedatatypes import BaseTraceHierarchyType
import copy


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
        return 'surface'

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

    def __init__(self, arg=None, x=None, y=None, z=None, **kwargs):
        """
        Construct a new Lightposition object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.surface.Lightposition
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
The first argument to the plotly.graph_objs.surface.Lightposition 
constructor must be a dict or 
an instance of plotly.graph_objs.surface.Lightposition"""
            )

        # Import validators
        # -----------------
        from plotly.validators.surface import (
            lightposition as v_lightposition
        )

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_lightposition.XValidator()
        self._validators['y'] = v_lightposition.YValidator()
        self._validators['z'] = v_lightposition.ZValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('x', None)
        self.x = x if x is not None else _v
        _v = arg.pop('y', None)
        self.y = y if y is not None else _v
        _v = arg.pop('z', None)
        self.z = z if z is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
