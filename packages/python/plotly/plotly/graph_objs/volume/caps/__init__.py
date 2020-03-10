from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Z(_BaseTraceHierarchyType):

    # fill
    # ----
    @property
    def fill(self):
        """
        Sets the fill ratio of the `caps`. The default fill value of
        the `caps` is 1 meaning that they are entirely shaded. On the
        other hand Applying a `fill` ratio less than one would allow
        the creation of openings parallel to the edges.
    
        The 'fill' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    # show
    # ----
    @property
    def show(self):
        """
        Sets the fill ratio of the `slices`. The default fill value of
        the z `slices` is 1 meaning that they are entirely shaded. On
        the other hand Applying a `fill` ratio less than one would
        allow the creation of openings parallel to the edges.
    
        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["show"]

    @show.setter
    def show(self, val):
        self["show"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "volume.caps"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fill
            Sets the fill ratio of the `caps`. The default fill
            value of the `caps` is 1 meaning that they are entirely
            shaded. On the other hand Applying a `fill` ratio less
            than one would allow the creation of openings parallel
            to the edges.
        show
            Sets the fill ratio of the `slices`. The default fill
            value of the z `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        """

    def __init__(self, arg=None, fill=None, show=None, **kwargs):
        """
        Construct a new Z object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.volume.caps.Z`
        fill
            Sets the fill ratio of the `caps`. The default fill
            value of the `caps` is 1 meaning that they are entirely
            shaded. On the other hand Applying a `fill` ratio less
            than one would allow the creation of openings parallel
            to the edges.
        show
            Sets the fill ratio of the `slices`. The default fill
            value of the z `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.

        Returns
        -------
        Z
        """
        super(Z, self).__init__("z")

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
The first argument to the plotly.graph_objs.volume.caps.Z 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.volume.caps.Z`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.volume.caps import z as v_z

        # Initialize validators
        # ---------------------
        self._validators["fill"] = v_z.FillValidator()
        self._validators["show"] = v_z.ShowValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("fill", None)
        self["fill"] = fill if fill is not None else _v
        _v = arg.pop("show", None)
        self["show"] = show if show is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Y(_BaseTraceHierarchyType):

    # fill
    # ----
    @property
    def fill(self):
        """
        Sets the fill ratio of the `caps`. The default fill value of
        the `caps` is 1 meaning that they are entirely shaded. On the
        other hand Applying a `fill` ratio less than one would allow
        the creation of openings parallel to the edges.
    
        The 'fill' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    # show
    # ----
    @property
    def show(self):
        """
        Sets the fill ratio of the `slices`. The default fill value of
        the y `slices` is 1 meaning that they are entirely shaded. On
        the other hand Applying a `fill` ratio less than one would
        allow the creation of openings parallel to the edges.
    
        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["show"]

    @show.setter
    def show(self, val):
        self["show"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "volume.caps"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fill
            Sets the fill ratio of the `caps`. The default fill
            value of the `caps` is 1 meaning that they are entirely
            shaded. On the other hand Applying a `fill` ratio less
            than one would allow the creation of openings parallel
            to the edges.
        show
            Sets the fill ratio of the `slices`. The default fill
            value of the y `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        """

    def __init__(self, arg=None, fill=None, show=None, **kwargs):
        """
        Construct a new Y object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.volume.caps.Y`
        fill
            Sets the fill ratio of the `caps`. The default fill
            value of the `caps` is 1 meaning that they are entirely
            shaded. On the other hand Applying a `fill` ratio less
            than one would allow the creation of openings parallel
            to the edges.
        show
            Sets the fill ratio of the `slices`. The default fill
            value of the y `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.

        Returns
        -------
        Y
        """
        super(Y, self).__init__("y")

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
The first argument to the plotly.graph_objs.volume.caps.Y 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.volume.caps.Y`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.volume.caps import y as v_y

        # Initialize validators
        # ---------------------
        self._validators["fill"] = v_y.FillValidator()
        self._validators["show"] = v_y.ShowValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("fill", None)
        self["fill"] = fill if fill is not None else _v
        _v = arg.pop("show", None)
        self["show"] = show if show is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class X(_BaseTraceHierarchyType):

    # fill
    # ----
    @property
    def fill(self):
        """
        Sets the fill ratio of the `caps`. The default fill value of
        the `caps` is 1 meaning that they are entirely shaded. On the
        other hand Applying a `fill` ratio less than one would allow
        the creation of openings parallel to the edges.
    
        The 'fill' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    # show
    # ----
    @property
    def show(self):
        """
        Sets the fill ratio of the `slices`. The default fill value of
        the x `slices` is 1 meaning that they are entirely shaded. On
        the other hand Applying a `fill` ratio less than one would
        allow the creation of openings parallel to the edges.
    
        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["show"]

    @show.setter
    def show(self, val):
        self["show"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "volume.caps"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fill
            Sets the fill ratio of the `caps`. The default fill
            value of the `caps` is 1 meaning that they are entirely
            shaded. On the other hand Applying a `fill` ratio less
            than one would allow the creation of openings parallel
            to the edges.
        show
            Sets the fill ratio of the `slices`. The default fill
            value of the x `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        """

    def __init__(self, arg=None, fill=None, show=None, **kwargs):
        """
        Construct a new X object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.volume.caps.X`
        fill
            Sets the fill ratio of the `caps`. The default fill
            value of the `caps` is 1 meaning that they are entirely
            shaded. On the other hand Applying a `fill` ratio less
            than one would allow the creation of openings parallel
            to the edges.
        show
            Sets the fill ratio of the `slices`. The default fill
            value of the x `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.

        Returns
        -------
        X
        """
        super(X, self).__init__("x")

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
The first argument to the plotly.graph_objs.volume.caps.X 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.volume.caps.X`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.volume.caps import x as v_x

        # Initialize validators
        # ---------------------
        self._validators["fill"] = v_x.FillValidator()
        self._validators["show"] = v_x.ShowValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("fill", None)
        self["fill"] = fill if fill is not None else _v
        _v = arg.pop("show", None)
        self["show"] = show if show is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = ["X", "Y", "Z"]
