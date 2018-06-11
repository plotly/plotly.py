from plotly.basedatatypes import BaseTraceHierarchyType


class Increasing(BaseTraceHierarchyType):

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.ohlc.increasing.Line
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
        plotly.graph_objs.ohlc.increasing.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

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
            plotly.graph_objs.ohlc.increasing.Line instance or dict
            with compatible properties
        """

    def __init__(self, line=None, **kwargs):
        """
        Construct a new Increasing object
        
        Parameters
        ----------
        line
            plotly.graph_objs.ohlc.increasing.Line instance or dict
            with compatible properties

        Returns
        -------
        Increasing
        """
        super(Increasing, self).__init__('increasing')

        # Import validators
        # -----------------
        from plotly.validators.ohlc import (increasing as v_increasing)

        # Initialize validators
        # ---------------------
        self._validators['line'] = v_increasing.LineValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.line = line

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
