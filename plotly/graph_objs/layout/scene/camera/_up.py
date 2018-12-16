from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Up(BaseLayoutHierarchyType):

    # x
    # -
    @property
    def x(self):
        """
        The 'x' property is a number and may be specified as:
          - An int or float

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
        The 'y' property is a number and may be specified as:
          - An int or float

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
        The 'z' property is a number and may be specified as:
          - An int or float

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
        return 'layout.scene.camera'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x

        y

        z

        """

    def __init__(self, arg=None, x=None, y=None, z=None, **kwargs):
        """
        Construct a new Up object
        
        Sets the (x,y,z) components of the 'up' camera vector. This
        vector determines the up direction of this scene with respect
        to the page. The default is *{x: 0, y: 0, z: 1}* which means
        that the z axis points up.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.scene.camera.Up
        x

        y

        z


        Returns
        -------
        Up
        """
        super(Up, self).__init__('up')

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
The first argument to the plotly.graph_objs.layout.scene.camera.Up 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.scene.camera.Up"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout.scene.camera import (up as v_up)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_up.XValidator()
        self._validators['y'] = v_up.YValidator()
        self._validators['z'] = v_up.ZValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('x', None)
        self['x'] = x if x is not None else _v
        _v = arg.pop('y', None)
        self['y'] = y if y is not None else _v
        _v = arg.pop('z', None)
        self['z'] = z if z is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
