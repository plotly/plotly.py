from plotly.basedatatypes import BaseTraceHierarchyType


class Unselected(BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.violin.unselected.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of unselected points,
                    applied only when a selection exists.
                opacity
                    Sets the marker opacity of unselected points,
                    applied only when a selection exists.
                size
                    Sets the marker size of unselected points,
                    applied only when a selection exists.

        Returns
        -------
        plotly.graph_objs.violin.unselected.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'violin'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            plotly.graph_objs.violin.unselected.Marker instance or
            dict with compatible properties
        """

    def __init__(self, marker=None, **kwargs):
        """
        Construct a new Unselected object
        
        Parameters
        ----------
        marker
            plotly.graph_objs.violin.unselected.Marker instance or
            dict with compatible properties

        Returns
        -------
        Unselected
        """
        super(Unselected, self).__init__('unselected')

        # Import validators
        # -----------------
        from plotly.validators.violin import (unselected as v_unselected)

        # Initialize validators
        # ---------------------
        self._validators['marker'] = v_unselected.MarkerValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.marker = marker

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
