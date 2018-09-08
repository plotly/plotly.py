from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Selected(BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.box.selected.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of selected points.
                opacity
                    Sets the marker opacity of selected points.
                size
                    Sets the marker size of selected points.

        Returns
        -------
        plotly.graph_objs.box.selected.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'box'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            plotly.graph_objs.box.selected.Marker instance or dict
            with compatible properties
        """

    def __init__(self, arg=None, marker=None, **kwargs):
        """
        Construct a new Selected object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.box.Selected
        marker
            plotly.graph_objs.box.selected.Marker instance or dict
            with compatible properties

        Returns
        -------
        Selected
        """
        super(Selected, self).__init__('selected')

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
The first argument to the plotly.graph_objs.box.Selected 
constructor must be a dict or 
an instance of plotly.graph_objs.box.Selected"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.box import (selected as v_selected)

        # Initialize validators
        # ---------------------
        self._validators['marker'] = v_selected.MarkerValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('marker', None)
        self['marker'] = marker if marker is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
