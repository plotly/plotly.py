from plotly.basedatatypes import BaseTraceHierarchyType


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

    def __init__(self, visible=None, **kwargs):
        """
        Construct a new Diagonal object
        
        Parameters
        ----------
        visible
            Determines whether or not subplots on the diagonal are
            displayed.

        Returns
        -------
        Diagonal
        """
        super(Diagonal, self).__init__('diagonal')

        # Import validators
        # -----------------
        from plotly.validators.splom import (diagonal as v_diagonal)

        # Initialize validators
        # ---------------------
        self._validators['visible'] = v_diagonal.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.visible = visible

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
