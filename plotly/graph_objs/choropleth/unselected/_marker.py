from plotly.basedatatypes import BaseTraceHierarchyType


class Marker(BaseTraceHierarchyType):

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the marker opacity of unselected points, applied only when
        a selection exists.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'choropleth.unselected'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        opacity
            Sets the marker opacity of unselected points, applied
            only when a selection exists.
        """

    def __init__(self, opacity=None, **kwargs):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        opacity
            Sets the marker opacity of unselected points, applied
            only when a selection exists.

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__('marker')

        # Import validators
        # -----------------
        from plotly.validators.choropleth.unselected import (
            marker as v_marker
        )

        # Initialize validators
        # ---------------------
        self._validators['opacity'] = v_marker.OpacityValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.opacity = opacity

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
