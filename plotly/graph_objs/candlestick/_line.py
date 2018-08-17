from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Line(BaseTraceHierarchyType):

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width (in px) of line bounding the box(es). Note that
        this style setting can also be set per direction via
        `increasing.line.width` and `decreasing.line.width`.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'candlestick'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        width
            Sets the width (in px) of line bounding the box(es).
            Note that this style setting can also be set per
            direction via `increasing.line.width` and
            `decreasing.line.width`.
        """

    def __init__(self, arg=None, width=None, **kwargs):
        """
        Construct a new Line object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.candlestick.Line
        width
            Sets the width (in px) of line bounding the box(es).
            Note that this style setting can also be set per
            direction via `increasing.line.width` and
            `decreasing.line.width`.

        Returns
        -------
        Line
        """
        super(Line, self).__init__('line')

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
The first argument to the plotly.graph_objs.candlestick.Line 
constructor must be a dict or 
an instance of plotly.graph_objs.candlestick.Line"""
            )

        # Import validators
        # -----------------
        from plotly.validators.candlestick import (line as v_line)

        # Initialize validators
        # ---------------------
        self._validators['width'] = v_line.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('width', None)
        self.width = width if width is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
