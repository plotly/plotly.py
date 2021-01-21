from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Tickformatstops(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "scattergl.marker.colorbar"
    _path_str = "scattergl.marker.colorbar.tickformatstops"
    _valid_props = {""}

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(self, arg=None, **kwargs):
        """
        Construct a new Tickformatstops object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.scattergl.mark
            er.colorbar.Tickformatstops`

        Returns
        -------
        Tickformatstops
        """
        super(Tickformatstops, self).__init__("tickformatstops")

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
The first argument to the plotly.graph_objs.scattergl.marker.colorbar.Tickformatstops 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.scattergl.marker.colorbar.Tickformatstops`"""
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
