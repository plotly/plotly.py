from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Unselected(BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.scattercarpet.unselected.Marker
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
        plotly.graph_objs.scattercarpet.unselected.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # textfont
    # --------
    @property
    def textfont(self):
        """
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.scattercarpet.unselected.Textfont
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
            Supported dict properties:
                
                color
                    Sets the text font color of unselected points,
                    applied only when a selection exists.

        Returns
        -------
        plotly.graph_objs.scattercarpet.unselected.Textfont
        """
        return self['textfont']

    @textfont.setter
    def textfont(self, val):
        self['textfont'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'scattercarpet'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            plotly.graph_objs.scattercarpet.unselected.Marker
            instance or dict with compatible properties
        textfont
            plotly.graph_objs.scattercarpet.unselected.Textfont
            instance or dict with compatible properties
        """

    def __init__(self, arg=None, marker=None, textfont=None, **kwargs):
        """
        Construct a new Unselected object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.scattercarpet.Unselected
        marker
            plotly.graph_objs.scattercarpet.unselected.Marker
            instance or dict with compatible properties
        textfont
            plotly.graph_objs.scattercarpet.unselected.Textfont
            instance or dict with compatible properties

        Returns
        -------
        Unselected
        """
        super(Unselected, self).__init__('unselected')

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
The first argument to the plotly.graph_objs.scattercarpet.Unselected 
constructor must be a dict or 
an instance of plotly.graph_objs.scattercarpet.Unselected"""
            )

        # Import validators
        # -----------------
        from plotly.validators.scattercarpet import (
            unselected as v_unselected
        )

        # Initialize validators
        # ---------------------
        self._validators['marker'] = v_unselected.MarkerValidator()
        self._validators['textfont'] = v_unselected.TextfontValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('marker', None)
        self.marker = marker if marker is not None else _v
        _v = arg.pop('textfont', None)
        self.textfont = textfont if textfont is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
