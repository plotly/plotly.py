from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Diagonal(BaseTraceHierarchyType):

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not subplots on the diagonal are
        displayed.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'splom'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        visible
            Determines whether or not subplots on the diagonal are
            displayed.
        """

    def __init__(self, arg=None, visible=None, **kwargs):
        """
        Construct a new Diagonal object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.splom.Diagonal
        visible
            Determines whether or not subplots on the diagonal are
            displayed.

        Returns
        -------
        Diagonal
        """
        super(Diagonal, self).__init__('diagonal')

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
The first argument to the plotly.graph_objs.splom.Diagonal 
constructor must be a dict or 
an instance of plotly.graph_objs.splom.Diagonal"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.splom import (diagonal as v_diagonal)

        # Initialize validators
        # ---------------------
        self._validators['visible'] = v_diagonal.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
