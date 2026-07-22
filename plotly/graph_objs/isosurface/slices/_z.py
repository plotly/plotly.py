#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Z(_BaseTraceHierarchyType):
    _parent_path_str = "isosurface.slices"
    _path_str = "isosurface.slices.z"
    _valid_props = {"fill", "locations", "show"}

    @property
    def fill(self):
        """
        Sets the fill ratio of the `slices`. The default fill value of
        the `slices` is 1 meaning that they are entirely shaded. On the
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

    @property
    def locations(self):
        """
        Specifies the location(s) of slices on the axis. When not
        specified slices would be created for all points of the axis z
        except start and end.

        The 'locations' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["locations"]

    @locations.setter
    def locations(self, val):
        self["locations"] = val

    @property
    def show(self):
        """
        Determines whether or not slice planes about the z dimension
        are drawn.

        The 'show' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        return self["show"]

    @show.setter
    def show(self, val):
        self["show"] = val

    @property
    def _prop_descriptions(self):
        return """\
        fill
            Sets the fill ratio of the `slices`. The default fill
            value of the `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        locations
            Specifies the location(s) of slices on the axis. When
            not specified slices would be created for all points of
            the axis z except start and end.
        show
            Determines whether or not slice planes about the z
            dimension are drawn.
        """

    def __init__(self, arg=None, fill=None, locations=None, show=None, **kwargs):
        """
        Construct a new Z object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.isosurface.slices.Z`
        fill
            Sets the fill ratio of the `slices`. The default fill
            value of the `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        locations
            Specifies the location(s) of slices on the axis. When
            not specified slices would be created for all points of
            the axis z except start and end.
        show
            Determines whether or not slice planes about the z
            dimension are drawn.

        Returns
        -------
        Z
        """
        super().__init__("z")
        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.isosurface.slices.Z
constructor must be a dict or
an instance of :class:`plotly.graph_objs.isosurface.slices.Z`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("fill", arg, fill)
        self._set_property("locations", arg, locations)
        self._set_property("show", arg, show)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
