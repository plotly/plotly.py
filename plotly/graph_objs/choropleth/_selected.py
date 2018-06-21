from plotly.basedatatypes import BaseTraceHierarchyType


class Selected(BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.choropleth.selected.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                opacity
                    Sets the marker opacity of selected points.

        Returns
        -------
        plotly.graph_objs.choropleth.selected.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'choropleth'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            plotly.graph_objs.choropleth.selected.Marker instance
            or dict with compatible properties
        """

    def __init__(self, marker=None, **kwargs):
        """
        Construct a new Selected object
        
        Parameters
        ----------
        marker
            plotly.graph_objs.choropleth.selected.Marker instance
            or dict with compatible properties

        Returns
        -------
        Selected
        """
        super(Selected, self).__init__('selected')

        # Import validators
        # -----------------
        from plotly.validators.choropleth import (selected as v_selected)

        # Initialize validators
        # ---------------------
        self._validators['marker'] = v_selected.MarkerValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.marker = marker

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
