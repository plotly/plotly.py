from plotly.basedatatypes import BaseLayoutHierarchyType


class Line(BaseLayoutHierarchyType):

    # width
    # -----
    @property
    def width(self):
        """
        Sets the line width. Has an effect only when `type` is set to
        *line*.
    
        The 'width' property is a number and may be specified as:
          - An int or float

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
        return 'layout.mapbox.layer'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        width
            Sets the line width. Has an effect only when `type` is
            set to *line*.
        """

    def __init__(self, width=None, **kwargs):
        """
        Construct a new Line object
        
        Parameters
        ----------
        width
            Sets the line width. Has an effect only when `type` is
            set to *line*.

        Returns
        -------
        Line
        """
        super(Line, self).__init__('line')

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import (line as v_line)

        # Initialize validators
        # ---------------------
        self._validators['width'] = v_line.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.width = width

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
