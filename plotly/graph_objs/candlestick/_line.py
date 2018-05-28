from plotly.basedatatypes import BaseTraceHierarchyType


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

    def __init__(self, width=None, **kwargs):
        """
        Construct a new Line object
        
        Parameters
        ----------
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

        # Import validators
        # -----------------
        from plotly.validators.candlestick import (line as v_line)

        # Initialize validators
        # ---------------------
        self._validators['width'] = v_line.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.width = width

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
