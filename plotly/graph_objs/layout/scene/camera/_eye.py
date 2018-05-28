from plotly.basedatatypes import BaseLayoutHierarchyType


class Eye(BaseLayoutHierarchyType):

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
        Construct a new Eye object
        
        Sets the (x,y,z) components of the 'eye' camera vector. This
        vector determines the view point about the origin of this
        scene.

        Parameters
        ----------
        x

        y

        z


        Returns
        -------
        Eye
        """
        super(Eye, self).__init__('eye')

        # Import validators
        # -----------------
        from plotly.validators.layout.scene.camera import (eye as v_eye)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_eye.XValidator()
        self._validators['y'] = v_eye.YValidator()
        self._validators['z'] = v_eye.ZValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.x = x
        self.y = y
        self.z = z

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
