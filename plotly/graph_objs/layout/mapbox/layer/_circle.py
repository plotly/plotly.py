from plotly.basedatatypes import BaseLayoutHierarchyType


class Circle(BaseLayoutHierarchyType):

    # radius
    # ------
    @property
    def radius(self):
        """
        Sets the circle radius. Has an effect only when `type` is set
        to *circle*.
    
        The 'radius' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['radius']

    @radius.setter
    def radius(self, val):
        self['radius'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.mapbox.layer'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        radius
            Sets the circle radius. Has an effect only when `type`
            is set to *circle*.
        """

    def __init__(self, radius=None, **kwargs):
        """
        Construct a new Circle object
        
        Parameters
        ----------
        radius
            Sets the circle radius. Has an effect only when `type`
            is set to *circle*.

        Returns
        -------
        Circle
        """
        super(Circle, self).__init__('circle')

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import (circle as v_circle)

        # Initialize validators
        # ---------------------
        self._validators['radius'] = v_circle.RadiusValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.radius = radius

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
