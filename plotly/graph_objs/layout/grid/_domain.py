from plotly.basedatatypes import BaseLayoutHierarchyType


class Domain(BaseLayoutHierarchyType):

    # x
    # -
    @property
    def x(self):
        """
        Sets the horizontal domain of this grid subplot (in plot
        fraction). The first and last cells end exactly at the domain
        edges, with no grout around the edges.
    
        The 'x' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'x[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'x[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
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
        Sets the vertical domain of this grid subplot (in plot
        fraction). The first and last cells end exactly at the domain
        edges, with no grout around the edges.
    
        The 'y' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'y[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'y[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.grid'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x
            Sets the horizontal domain of this grid subplot (in
            plot fraction). The first and last cells end exactly at
            the domain edges, with no grout around the edges.
        y
            Sets the vertical domain of this grid subplot (in plot
            fraction). The first and last cells end exactly at the
            domain edges, with no grout around the edges.
        """

    def __init__(self, x=None, y=None, **kwargs):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        x
            Sets the horizontal domain of this grid subplot (in
            plot fraction). The first and last cells end exactly at
            the domain edges, with no grout around the edges.
        y
            Sets the vertical domain of this grid subplot (in plot
            fraction). The first and last cells end exactly at the
            domain edges, with no grout around the edges.

        Returns
        -------
        Domain
        """
        super(Domain, self).__init__('domain')

        # Import validators
        # -----------------
        from plotly.validators.layout.grid import (domain as v_domain)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_domain.XValidator()
        self._validators['y'] = v_domain.YValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.x = x
        self.y = y

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
