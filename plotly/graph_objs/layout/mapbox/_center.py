from plotly.basedatatypes import BaseLayoutHierarchyType


class Center(BaseLayoutHierarchyType):

    # lat
    # ---
    @property
    def lat(self):
        """
        Sets the latitude of the center of the map (in degrees North).
    
        The 'lat' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['lat']

    @lat.setter
    def lat(self, val):
        self['lat'] = val

    # lon
    # ---
    @property
    def lon(self):
        """
        Sets the longitude of the center of the map (in degrees East).
    
        The 'lon' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['lon']

    @lon.setter
    def lon(self, val):
        self['lon'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.mapbox'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        lat
            Sets the latitude of the center of the map (in degrees
            North).
        lon
            Sets the longitude of the center of the map (in degrees
            East).
        """

    def __init__(self, lat=None, lon=None, **kwargs):
        """
        Construct a new Center object
        
        Parameters
        ----------
        lat
            Sets the latitude of the center of the map (in degrees
            North).
        lon
            Sets the longitude of the center of the map (in degrees
            East).

        Returns
        -------
        Center
        """
        super(Center, self).__init__('center')

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox import (center as v_center)

        # Initialize validators
        # ---------------------
        self._validators['lat'] = v_center.LatValidator()
        self._validators['lon'] = v_center.LonValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.lat = lat
        self.lon = lon

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
