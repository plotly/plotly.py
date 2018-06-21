from plotly.basedatatypes import BaseLayoutHierarchyType


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

    def __init__(self, x=None, y=None, z=None, **kwargs):
        """
        Construct a new Up object
        
        Sets the (x,y,z) components of the 'up' camera vector. This
        vector determines the up direction of this scene with respect
        to the page. The default is *{x: 0, y: 0, z: 1}* which means
        that the z axis points up.

        Parameters
        ----------
        x

        y

        z


        Returns
        -------
        Up
        """
        super(Up, self).__init__('up')

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
        self.x = x
        self.y = y
        self.z = z

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
