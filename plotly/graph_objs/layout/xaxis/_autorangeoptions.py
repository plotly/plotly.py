#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Autorangeoptions(_BaseLayoutHierarchyType):
    _parent_path_str = "layout.xaxis"
    _path_str = "layout.xaxis.autorangeoptions"
    _valid_props = {"clipmax", "clipmin", "include", "maxallowed", "minallowed"}

    @property
    def clipmax(self):
        """
        Clip autorange maximum if it goes beyond this value. Has no
        effect when `autorangeoptions.maxallowed` is provided.

        The 'clipmax' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["clipmax"]

    @clipmax.setter
    def clipmax(self, val):
        self["clipmax"] = val

    @property
    def clipmin(self):
        """
        Clip autorange minimum if it goes beyond this value. Has no
        effect when `autorangeoptions.minallowed` is provided.

        The 'clipmin' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["clipmin"]

    @clipmin.setter
    def clipmin(self, val):
        self["clipmin"] = val

    @property
    def include(self):
        """
        Extends the autorange to include this value or array of values,
        even when they fall outside the data range. Has no effect on
        endpoints set by `autorangeoptions.minallowed` or
        `autorangeoptions.maxallowed`. Subject to
        `autorangeoptions.clipmin` and `autorangeoptions.clipmax`.

        The 'include' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["include"]

    @include.setter
    def include(self, val):
        self["include"] = val

    @property
    def maxallowed(self):
        """
        Use this value exactly as autorange maximum.

        The 'maxallowed' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["maxallowed"]

    @maxallowed.setter
    def maxallowed(self, val):
        self["maxallowed"] = val

    @property
    def minallowed(self):
        """
        Use this value exactly as autorange minimum.

        The 'minallowed' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["minallowed"]

    @minallowed.setter
    def minallowed(self, val):
        self["minallowed"] = val

    @property
    def _prop_descriptions(self):
        return """\
        clipmax
            Clip autorange maximum if it goes beyond this value.
            Has no effect when `autorangeoptions.maxallowed` is
            provided.
        clipmin
            Clip autorange minimum if it goes beyond this value.
            Has no effect when `autorangeoptions.minallowed` is
            provided.
        include
            Extends the autorange to include this value or array of
            values, even when they fall outside the data range. Has
            no effect on endpoints set by
            `autorangeoptions.minallowed` or
            `autorangeoptions.maxallowed`. Subject to
            `autorangeoptions.clipmin` and
            `autorangeoptions.clipmax`.
        maxallowed
            Use this value exactly as autorange maximum.
        minallowed
            Use this value exactly as autorange minimum.
        """

    def __init__(
        self,
        arg=None,
        clipmax=None,
        clipmin=None,
        include=None,
        maxallowed=None,
        minallowed=None,
        **kwargs,
    ):
        """
        Construct a new Autorangeoptions object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.xaxis.A
            utorangeoptions`
        clipmax
            Clip autorange maximum if it goes beyond this value.
            Has no effect when `autorangeoptions.maxallowed` is
            provided.
        clipmin
            Clip autorange minimum if it goes beyond this value.
            Has no effect when `autorangeoptions.minallowed` is
            provided.
        include
            Extends the autorange to include this value or array of
            values, even when they fall outside the data range. Has
            no effect on endpoints set by
            `autorangeoptions.minallowed` or
            `autorangeoptions.maxallowed`. Subject to
            `autorangeoptions.clipmin` and
            `autorangeoptions.clipmax`.
        maxallowed
            Use this value exactly as autorange maximum.
        minallowed
            Use this value exactly as autorange minimum.

        Returns
        -------
        Autorangeoptions
        """
        super().__init__("autorangeoptions")
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
The first argument to the plotly.graph_objs.layout.xaxis.Autorangeoptions
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.xaxis.Autorangeoptions`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("clipmax", arg, clipmax)
        self._set_property("clipmin", arg, clipmin)
        self._set_property("include", arg, include)
        self._set_property("maxallowed", arg, maxallowed)
        self._set_property("minallowed", arg, minallowed)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
