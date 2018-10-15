from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Marker(BaseTraceHierarchyType):

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.choropleth.marker.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets themarker.linecolor. It accepts either a
                    specific color or an array of numbers that are
                    mapped to the colorscale relative to the max
                    and min values of the array or relative to
                    `marker.line.cmin` and `marker.line.cmax` if
                    set.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                width
                    Sets the width (in px) of the lines bounding
                    the marker points.
                widthsrc
                    Sets the source reference on plot.ly for  width
                    .

        Returns
        -------
        plotly.graph_objs.choropleth.marker.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the locations.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # opacitysrc
    # ----------
    @property
    def opacitysrc(self):
        """
        Sets the source reference on plot.ly for  opacity .
    
        The 'opacitysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['opacitysrc']

    @opacitysrc.setter
    def opacitysrc(self, val):
        self['opacitysrc'] = val

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
        line
            plotly.graph_objs.choropleth.marker.Line instance or
            dict with compatible properties
        opacity
            Sets the opacity of the locations.
        opacitysrc
            Sets the source reference on plot.ly for  opacity .
        """

    def __init__(
        self, arg=None, line=None, opacity=None, opacitysrc=None, **kwargs
    ):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.choropleth.Marker
        line
            plotly.graph_objs.choropleth.marker.Line instance or
            dict with compatible properties
        opacity
            Sets the opacity of the locations.
        opacitysrc
            Sets the source reference on plot.ly for  opacity .

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
The first argument to the plotly.graph_objs.choropleth.Marker 
constructor must be a dict or 
an instance of plotly.graph_objs.choropleth.Marker"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.choropleth import (marker as v_marker)

        # Initialize validators
        # ---------------------
        self._validators['line'] = v_marker.LineValidator()
        self._validators['opacity'] = v_marker.OpacityValidator()
        self._validators['opacitysrc'] = v_marker.OpacitysrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('line', None)
        self['line'] = line if line is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('opacitysrc', None)
        self['opacitysrc'] = opacitysrc if opacitysrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
