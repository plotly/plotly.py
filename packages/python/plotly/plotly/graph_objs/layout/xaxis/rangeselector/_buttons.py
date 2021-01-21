from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Buttons(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout.xaxis.rangeselector"
    _path_str = "layout.xaxis.rangeselector.buttons"
    _valid_props = {""}

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, **kwargs):
        """
        Construct a new Buttons object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.xaxis.r
            angeselector.Buttons`

        Returns
        -------
        Buttons
        """
        super(Buttons, self).__init__("buttons")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.xaxis.rangeselector.Buttons 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.xaxis.rangeselector.Buttons`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
