from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Colorscale(BaseLayoutHierarchyType):

    # diverging
    # ---------
    @property
    def diverging(self):
        """
        Sets the default diverging colorscale. Note that
        `autocolorscale` must be true for this attribute to work.
    
        The 'diverging' property is a colorscale and may be
        specified as:
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis']

        Returns
        -------
        str
        """
        return self['diverging']

    @diverging.setter
    def diverging(self, val):
        self['diverging'] = val

    # sequential
    # ----------
    @property
    def sequential(self):
        """
        Sets the default sequential colorscale for positive values.
        Note that `autocolorscale` must be true for this attribute to
        work.
    
        The 'sequential' property is a colorscale and may be
        specified as:
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis']

        Returns
        -------
        str
        """
        return self['sequential']

    @sequential.setter
    def sequential(self, val):
        self['sequential'] = val

    # sequentialminus
    # ---------------
    @property
    def sequentialminus(self):
        """
        Sets the default sequential colorscale for negative values.
        Note that `autocolorscale` must be true for this attribute to
        work.
    
        The 'sequentialminus' property is a colorscale and may be
        specified as:
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis']

        Returns
        -------
        str
        """
        return self['sequentialminus']

    @sequentialminus.setter
    def sequentialminus(self, val):
        self['sequentialminus'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        diverging
            Sets the default diverging colorscale. Note that
            `autocolorscale` must be true for this attribute to
            work.
        sequential
            Sets the default sequential colorscale for positive
            values. Note that `autocolorscale` must be true for
            this attribute to work.
        sequentialminus
            Sets the default sequential colorscale for negative
            values. Note that `autocolorscale` must be true for
            this attribute to work.
        """

    def __init__(
        self,
        arg=None,
        diverging=None,
        sequential=None,
        sequentialminus=None,
        **kwargs
    ):
        """
        Construct a new Colorscale object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Colorscale
        diverging
            Sets the default diverging colorscale. Note that
            `autocolorscale` must be true for this attribute to
            work.
        sequential
            Sets the default sequential colorscale for positive
            values. Note that `autocolorscale` must be true for
            this attribute to work.
        sequentialminus
            Sets the default sequential colorscale for negative
            values. Note that `autocolorscale` must be true for
            this attribute to work.

        Returns
        -------
        Colorscale
        """
        super(Colorscale, self).__init__('colorscale')

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
The first argument to the plotly.graph_objs.layout.Colorscale 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Colorscale"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout import (colorscale as v_colorscale)

        # Initialize validators
        # ---------------------
        self._validators['diverging'] = v_colorscale.DivergingValidator()
        self._validators['sequential'] = v_colorscale.SequentialValidator()
        self._validators['sequentialminus'
                        ] = v_colorscale.SequentialminusValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('diverging', None)
        self['diverging'] = diverging if diverging is not None else _v
        _v = arg.pop('sequential', None)
        self['sequential'] = sequential if sequential is not None else _v
        _v = arg.pop('sequentialminus', None)
        self['sequentialminus'
            ] = sequentialminus if sequentialminus is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
