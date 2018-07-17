from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Marker(BaseTraceHierarchyType):

    # colors
    # ------
    @property
    def colors(self):
        """
        Sets the color of each sector of this pie chart. If not
        specified, the default trace color set is used to pick the
        sector colors.
    
        The 'colors' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['colors']

    @colors.setter
    def colors(self, val):
        self['colors'] = val

    # colorssrc
    # ---------
    @property
    def colorssrc(self):
        """
        Sets the source reference on plot.ly for  colors .
    
        The 'colorssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['colorssrc']

    @colorssrc.setter
    def colorssrc(self, val):
        self['colorssrc'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.pie.marker.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the line enclosing each
                    sector.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                width
                    Sets the width (in px) of the line enclosing
                    each sector.
                widthsrc
                    Sets the source reference on plot.ly for  width
                    .

        Returns
        -------
        plotly.graph_objs.pie.marker.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'pie'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        colors
            Sets the color of each sector of this pie chart. If not
            specified, the default trace color set is used to pick
            the sector colors.
        colorssrc
            Sets the source reference on plot.ly for  colors .
        line
            plotly.graph_objs.pie.marker.Line instance or dict with
            compatible properties
        """

    def __init__(
        self, arg=None, colors=None, colorssrc=None, line=None, **kwargs
    ):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.pie.Marker
        colors
            Sets the color of each sector of this pie chart. If not
            specified, the default trace color set is used to pick
            the sector colors.
        colorssrc
            Sets the source reference on plot.ly for  colors .
        line
            plotly.graph_objs.pie.marker.Line instance or dict with
            compatible properties

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
The first argument to the plotly.graph_objs.pie.Marker 
constructor must be a dict or 
an instance of plotly.graph_objs.pie.Marker"""
            )

        # Import validators
        # -----------------
        from plotly.validators.pie import (marker as v_marker)

        # Initialize validators
        # ---------------------
        self._validators['colors'] = v_marker.ColorsValidator()
        self._validators['colorssrc'] = v_marker.ColorssrcValidator()
        self._validators['line'] = v_marker.LineValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('colors', None)
        self.colors = colors if colors is not None else _v
        _v = arg.pop('colorssrc', None)
        self.colorssrc = colorssrc if colorssrc is not None else _v
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
