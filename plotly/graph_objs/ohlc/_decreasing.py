from plotly.basedatatypes import BaseTraceHierarchyType


class Decreasing(BaseTraceHierarchyType):

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.ohlc.decreasing.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the line color.
                dash
                    Sets the dash style of lines. Set to a dash
                    type string (*solid*, *dot*, *dash*,
                    *longdash*, *dashdot*, or *longdashdot*) or a
                    dash length list in px (eg *5px,10px,2px,2px*).
                width
                    Sets the line width (in px).

        Returns
        -------
        plotly.graph_objs.ohlc.decreasing.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the segment name. The segment name appear as the legend
        item and on hover.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this segment
        is shown in the legend.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlegend']

    @showlegend.setter
    def showlegend(self, val):
        self['showlegend'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'ohlc'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        line
            plotly.graph_objs.ohlc.decreasing.Line instance or dict
            with compatible properties
        name
            Sets the segment name. The segment name appear as the
            legend item and on hover.
        showlegend
            Determines whether or not an item corresponding to this
            segment is shown in the legend.
        """

    def __init__(self, line=None, name=None, showlegend=None, **kwargs):
        """
        Construct a new Decreasing object
        
        Parameters
        ----------
        line
            plotly.graph_objs.ohlc.decreasing.Line instance or dict
            with compatible properties
        name
            Sets the segment name. The segment name appear as the
            legend item and on hover.
        showlegend
            Determines whether or not an item corresponding to this
            segment is shown in the legend.

        Returns
        -------
        Decreasing
        """
        super(Decreasing, self).__init__('decreasing')

        # Import validators
        # -----------------
        from plotly.validators.ohlc import (decreasing as v_decreasing)

        # Initialize validators
        # ---------------------
        self._validators['line'] = v_decreasing.LineValidator()
        self._validators['name'] = v_decreasing.NameValidator()
        self._validators['showlegend'] = v_decreasing.ShowlegendValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.line = line
        self.name = name
        self.showlegend = showlegend

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
