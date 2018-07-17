from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Marker(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the aggregation data.
    
        The 'color' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

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
    
        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

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
        return 'histogram2dcontour'

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

    def __init__(self, arg=None, color=None, colorsrc=None, **kwargs):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.histogram2dcontour.Marker
        color
            Sets the aggregation data.
        colorsrc
            Sets the source reference on plot.ly for  color .

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__('marker')

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
The first argument to the plotly.graph_objs.histogram2dcontour.Marker 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram2dcontour.Marker"""
            )

        # Import validators
        # -----------------
        from plotly.validators.histogram2dcontour import (marker as v_marker)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_marker.ColorValidator()
        self._validators['colorsrc'] = v_marker.ColorsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('color', None)
        self.color = color if color is not None else _v
        _v = arg.pop('colorsrc', None)
        self.colorsrc = colorsrc if colorsrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
