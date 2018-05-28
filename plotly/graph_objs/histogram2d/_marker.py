from plotly.basedatatypes import BaseTraceHierarchyType


class Marker(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the aggregation data.
    
        The 'color' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
        The 'colorsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'histogram2d'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the aggregation data.
        colorsrc
            Sets the source reference on plot.ly for  color .
        """

    def __init__(self, color=None, colorsrc=None, **kwargs):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        color
            Sets the aggregation data.
        colorsrc
            Sets the source reference on plot.ly for  color .

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__('marker')

        # Import validators
        # -----------------
        from plotly.validators.histogram2d import (marker as v_marker)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_marker.ColorValidator()
        self._validators['colorsrc'] = v_marker.ColorsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.color = color
        self.colorsrc = colorsrc

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
