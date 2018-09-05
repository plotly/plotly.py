from plotly.basedatatypes import BaseTraceHierarchyType
import copy


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
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
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

    def __init__(self, arg=None, line=None, **kwargs):
        """
        Construct a new Increasing object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.ohlc.Increasing
        line
            plotly.graph_objs.ohlc.increasing.Line instance or dict
            with compatible properties

        Returns
        -------
        Increasing
        """
        super(Increasing, self).__init__('increasing')

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
The first argument to the plotly.graph_objs.ohlc.Increasing 
constructor must be a dict or 
an instance of plotly.graph_objs.ohlc.Increasing"""
            )

        # Import validators
        # -----------------
        from plotly.validators.ohlc import (increasing as v_increasing)

        # Initialize validators
        # ---------------------
        self._validators['line'] = v_increasing.LineValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
