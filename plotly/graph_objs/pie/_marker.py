from plotly.basedatatypes import BaseTraceHierarchyType


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
        list, one-dimensional numpy array, or pandas Series

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
    
        The 'colorssrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

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

    def __init__(self, colors=None, colorssrc=None, line=None, **kwargs):
        """
        Construct a new Marker object
        
        Parameters
        ----------
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
        self.colors = colors
        self.colorssrc = colorssrc
        self.line = line

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
