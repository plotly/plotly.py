from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class YBins(_BaseTraceHierarchyType):

    # end
    # ---
    @property
    def end(self):
        """
        Sets the end value for the y axis bins. The last bin may not
        end exactly at this value, we increment the bin edge by `size`
        from `start` until we reach or exceed `end`. Defaults to the
        maximum data value. Like `start`, for dates use a date string,
        and for category data `end` is based on the category serial
        numbers.
    
        The 'end' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["end"]

    @end.setter
    def end(self, val):
        self["end"] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the size of each y axis bin. Default behavior: If `nbinsy`
        is 0 or omitted, we choose a nice round bin size such that the
        number of bins is about the same as the typical number of
        samples in each bin. If `nbinsy` is provided, we choose a nice
        round bin size giving no more than that many bins. For date
        data, use milliseconds or "M<n>" for months, as in
        `axis.dtick`. For category data, the number of categories to
        bin together (always defaults to 1). If multiple non-overlaying
        histograms share a subplot, the first explicit `size` is used
        and all others discarded. If no `size` is provided,the sample
        data from all traces is combined to determine `size` as
        described above.
    
        The 'size' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # start
    # -----
    @property
    def start(self):
        """
        Sets the starting value for the y axis bins. Defaults to the
        minimum data value, shifted down if necessary to make nice
        round values and to remove ambiguous bin edges. For example, if
        most of the data is integers we shift the bin edges 0.5 down,
        so a `size` of 5 would have a default `start` of -0.5, so it is
        clear that 0-4 are in the first bin, 5-9 in the second, but
        continuous data gets a start of 0 and bins [0,5), [5,10) etc.
        Dates behave similarly, and `start` should be a date string.
        For category data, `start` is based on the category serial
        numbers, and defaults to -0.5. If multiple non-overlaying
        histograms share a subplot, the first explicit `start` is used
        exactly and all others are shifted down (if necessary) to
        differ from that one by an integer number of bins.
    
        The 'start' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["start"]

    @start.setter
    def start(self, val):
        self["start"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        end
            Sets the end value for the y axis bins. The last bin
            may not end exactly at this value, we increment the bin
            edge by `size` from `start` until we reach or exceed
            `end`. Defaults to the maximum data value. Like
            `start`, for dates use a date string, and for category
            data `end` is based on the category serial numbers.
        size
            Sets the size of each y axis bin. Default behavior: If
            `nbinsy` is 0 or omitted, we choose a nice round bin
            size such that the number of bins is about the same as
            the typical number of samples in each bin. If `nbinsy`
            is provided, we choose a nice round bin size giving no
            more than that many bins. For date data, use
            milliseconds or "M<n>" for months, as in `axis.dtick`.
            For category data, the number of categories to bin
            together (always defaults to 1). If multiple non-
            overlaying histograms share a subplot, the first
            explicit `size` is used and all others discarded. If no
            `size` is provided,the sample data from all traces is
            combined to determine `size` as described above.
        start
            Sets the starting value for the y axis bins. Defaults
            to the minimum data value, shifted down if necessary to
            make nice round values and to remove ambiguous bin
            edges. For example, if most of the data is integers we
            shift the bin edges 0.5 down, so a `size` of 5 would
            have a default `start` of -0.5, so it is clear that 0-4
            are in the first bin, 5-9 in the second, but continuous
            data gets a start of 0 and bins [0,5), [5,10) etc.
            Dates behave similarly, and `start` should be a date
            string. For category data, `start` is based on the
            category serial numbers, and defaults to -0.5. If
            multiple non-overlaying histograms share a subplot, the
            first explicit `start` is used exactly and all others
            are shifted down (if necessary) to differ from that one
            by an integer number of bins.
        """

    def __init__(self, arg=None, end=None, size=None, start=None, **kwargs):
        """
        Construct a new YBins object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.YBins
        end
            Sets the end value for the y axis bins. The last bin
            may not end exactly at this value, we increment the bin
            edge by `size` from `start` until we reach or exceed
            `end`. Defaults to the maximum data value. Like
            `start`, for dates use a date string, and for category
            data `end` is based on the category serial numbers.
        size
            Sets the size of each y axis bin. Default behavior: If
            `nbinsy` is 0 or omitted, we choose a nice round bin
            size such that the number of bins is about the same as
            the typical number of samples in each bin. If `nbinsy`
            is provided, we choose a nice round bin size giving no
            more than that many bins. For date data, use
            milliseconds or "M<n>" for months, as in `axis.dtick`.
            For category data, the number of categories to bin
            together (always defaults to 1). If multiple non-
            overlaying histograms share a subplot, the first
            explicit `size` is used and all others discarded. If no
            `size` is provided,the sample data from all traces is
            combined to determine `size` as described above.
        start
            Sets the starting value for the y axis bins. Defaults
            to the minimum data value, shifted down if necessary to
            make nice round values and to remove ambiguous bin
            edges. For example, if most of the data is integers we
            shift the bin edges 0.5 down, so a `size` of 5 would
            have a default `start` of -0.5, so it is clear that 0-4
            are in the first bin, 5-9 in the second, but continuous
            data gets a start of 0 and bins [0,5), [5,10) etc.
            Dates behave similarly, and `start` should be a date
            string. For category data, `start` is based on the
            category serial numbers, and defaults to -0.5. If
            multiple non-overlaying histograms share a subplot, the
            first explicit `start` is used exactly and all others
            are shifted down (if necessary) to differ from that one
            by an integer number of bins.

        Returns
        -------
        YBins
        """
        super(YBins, self).__init__("ybins")

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
The first argument to the plotly.graph_objs.histogram.YBins 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.YBins"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import ybins as v_ybins

        # Initialize validators
        # ---------------------
        self._validators["end"] = v_ybins.EndValidator()
        self._validators["size"] = v_ybins.SizeValidator()
        self._validators["start"] = v_ybins.StartValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("end", None)
        self["end"] = end if end is not None else _v
        _v = arg.pop("size", None)
        self["size"] = size if size is not None else _v
        _v = arg.pop("start", None)
        self["start"] = start if start is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class XBins(_BaseTraceHierarchyType):

    # end
    # ---
    @property
    def end(self):
        """
        Sets the end value for the x axis bins. The last bin may not
        end exactly at this value, we increment the bin edge by `size`
        from `start` until we reach or exceed `end`. Defaults to the
        maximum data value. Like `start`, for dates use a date string,
        and for category data `end` is based on the category serial
        numbers.
    
        The 'end' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["end"]

    @end.setter
    def end(self, val):
        self["end"] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the size of each x axis bin. Default behavior: If `nbinsx`
        is 0 or omitted, we choose a nice round bin size such that the
        number of bins is about the same as the typical number of
        samples in each bin. If `nbinsx` is provided, we choose a nice
        round bin size giving no more than that many bins. For date
        data, use milliseconds or "M<n>" for months, as in
        `axis.dtick`. For category data, the number of categories to
        bin together (always defaults to 1). If multiple non-overlaying
        histograms share a subplot, the first explicit `size` is used
        and all others discarded. If no `size` is provided,the sample
        data from all traces is combined to determine `size` as
        described above.
    
        The 'size' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # start
    # -----
    @property
    def start(self):
        """
        Sets the starting value for the x axis bins. Defaults to the
        minimum data value, shifted down if necessary to make nice
        round values and to remove ambiguous bin edges. For example, if
        most of the data is integers we shift the bin edges 0.5 down,
        so a `size` of 5 would have a default `start` of -0.5, so it is
        clear that 0-4 are in the first bin, 5-9 in the second, but
        continuous data gets a start of 0 and bins [0,5), [5,10) etc.
        Dates behave similarly, and `start` should be a date string.
        For category data, `start` is based on the category serial
        numbers, and defaults to -0.5. If multiple non-overlaying
        histograms share a subplot, the first explicit `start` is used
        exactly and all others are shifted down (if necessary) to
        differ from that one by an integer number of bins.
    
        The 'start' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["start"]

    @start.setter
    def start(self, val):
        self["start"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        end
            Sets the end value for the x axis bins. The last bin
            may not end exactly at this value, we increment the bin
            edge by `size` from `start` until we reach or exceed
            `end`. Defaults to the maximum data value. Like
            `start`, for dates use a date string, and for category
            data `end` is based on the category serial numbers.
        size
            Sets the size of each x axis bin. Default behavior: If
            `nbinsx` is 0 or omitted, we choose a nice round bin
            size such that the number of bins is about the same as
            the typical number of samples in each bin. If `nbinsx`
            is provided, we choose a nice round bin size giving no
            more than that many bins. For date data, use
            milliseconds or "M<n>" for months, as in `axis.dtick`.
            For category data, the number of categories to bin
            together (always defaults to 1). If multiple non-
            overlaying histograms share a subplot, the first
            explicit `size` is used and all others discarded. If no
            `size` is provided,the sample data from all traces is
            combined to determine `size` as described above.
        start
            Sets the starting value for the x axis bins. Defaults
            to the minimum data value, shifted down if necessary to
            make nice round values and to remove ambiguous bin
            edges. For example, if most of the data is integers we
            shift the bin edges 0.5 down, so a `size` of 5 would
            have a default `start` of -0.5, so it is clear that 0-4
            are in the first bin, 5-9 in the second, but continuous
            data gets a start of 0 and bins [0,5), [5,10) etc.
            Dates behave similarly, and `start` should be a date
            string. For category data, `start` is based on the
            category serial numbers, and defaults to -0.5. If
            multiple non-overlaying histograms share a subplot, the
            first explicit `start` is used exactly and all others
            are shifted down (if necessary) to differ from that one
            by an integer number of bins.
        """

    def __init__(self, arg=None, end=None, size=None, start=None, **kwargs):
        """
        Construct a new XBins object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.XBins
        end
            Sets the end value for the x axis bins. The last bin
            may not end exactly at this value, we increment the bin
            edge by `size` from `start` until we reach or exceed
            `end`. Defaults to the maximum data value. Like
            `start`, for dates use a date string, and for category
            data `end` is based on the category serial numbers.
        size
            Sets the size of each x axis bin. Default behavior: If
            `nbinsx` is 0 or omitted, we choose a nice round bin
            size such that the number of bins is about the same as
            the typical number of samples in each bin. If `nbinsx`
            is provided, we choose a nice round bin size giving no
            more than that many bins. For date data, use
            milliseconds or "M<n>" for months, as in `axis.dtick`.
            For category data, the number of categories to bin
            together (always defaults to 1). If multiple non-
            overlaying histograms share a subplot, the first
            explicit `size` is used and all others discarded. If no
            `size` is provided,the sample data from all traces is
            combined to determine `size` as described above.
        start
            Sets the starting value for the x axis bins. Defaults
            to the minimum data value, shifted down if necessary to
            make nice round values and to remove ambiguous bin
            edges. For example, if most of the data is integers we
            shift the bin edges 0.5 down, so a `size` of 5 would
            have a default `start` of -0.5, so it is clear that 0-4
            are in the first bin, 5-9 in the second, but continuous
            data gets a start of 0 and bins [0,5), [5,10) etc.
            Dates behave similarly, and `start` should be a date
            string. For category data, `start` is based on the
            category serial numbers, and defaults to -0.5. If
            multiple non-overlaying histograms share a subplot, the
            first explicit `start` is used exactly and all others
            are shifted down (if necessary) to differ from that one
            by an integer number of bins.

        Returns
        -------
        XBins
        """
        super(XBins, self).__init__("xbins")

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
The first argument to the plotly.graph_objs.histogram.XBins 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.XBins"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import xbins as v_xbins

        # Initialize validators
        # ---------------------
        self._validators["end"] = v_xbins.EndValidator()
        self._validators["size"] = v_xbins.SizeValidator()
        self._validators["start"] = v_xbins.StartValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("end", None)
        self["end"] = end if end is not None else _v
        _v = arg.pop("size", None)
        self["size"] = size if size is not None else _v
        _v = arg.pop("start", None)
        self["start"] = start if start is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Unselected(_BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.unselected.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of unselected points,
                    applied only when a selection exists.
                opacity
                    Sets the marker opacity of unselected points,
                    applied only when a selection exists.

        Returns
        -------
        plotly.graph_objs.histogram.unselected.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    # textfont
    # --------
    @property
    def textfont(self):
        """
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.unselected.Textfont
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
            Supported dict properties:
                
                color
                    Sets the text font color of unselected points,
                    applied only when a selection exists.

        Returns
        -------
        plotly.graph_objs.histogram.unselected.Textfont
        """
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            plotly.graph_objects.histogram.unselected.Marker
            instance or dict with compatible properties
        textfont
            plotly.graph_objects.histogram.unselected.Textfont
            instance or dict with compatible properties
        """

    def __init__(self, arg=None, marker=None, textfont=None, **kwargs):
        """
        Construct a new Unselected object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.Unselected
        marker
            plotly.graph_objects.histogram.unselected.Marker
            instance or dict with compatible properties
        textfont
            plotly.graph_objects.histogram.unselected.Textfont
            instance or dict with compatible properties

        Returns
        -------
        Unselected
        """
        super(Unselected, self).__init__("unselected")

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
The first argument to the plotly.graph_objs.histogram.Unselected 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.Unselected"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import unselected as v_unselected

        # Initialize validators
        # ---------------------
        self._validators["marker"] = v_unselected.MarkerValidator()
        self._validators["textfont"] = v_unselected.TextfontValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("marker", None)
        self["marker"] = marker if marker is not None else _v
        _v = arg.pop("textfont", None)
        self["textfont"] = textfont if textfont is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Stream(_BaseTraceHierarchyType):

    # maxpoints
    # ---------
    @property
    def maxpoints(self):
        """
        Sets the maximum number of points to keep on the plots from an
        incoming stream. If `maxpoints` is set to 50, only the newest
        50 points will be displayed on the plot.
    
        The 'maxpoints' property is a number and may be specified as:
          - An int or float in the interval [0, 10000]

        Returns
        -------
        int|float
        """
        return self["maxpoints"]

    @maxpoints.setter
    def maxpoints(self, val):
        self["maxpoints"] = val

    # token
    # -----
    @property
    def token(self):
        """
        The stream id number links a data trace on a plot with a
        stream. See https://plot.ly/settings for more details.
    
        The 'token' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["token"]

    @token.setter
    def token(self, val):
        self["token"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.
        """

    def __init__(self, arg=None, maxpoints=None, token=None, **kwargs):
        """
        Construct a new Stream object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.Stream
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.

        Returns
        -------
        Stream
        """
        super(Stream, self).__init__("stream")

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
The first argument to the plotly.graph_objs.histogram.Stream 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.Stream"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import stream as v_stream

        # Initialize validators
        # ---------------------
        self._validators["maxpoints"] = v_stream.MaxpointsValidator()
        self._validators["token"] = v_stream.TokenValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("maxpoints", None)
        self["maxpoints"] = maxpoints if maxpoints is not None else _v
        _v = arg.pop("token", None)
        self["token"] = token if token is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Selected(_BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.selected.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of selected points.
                opacity
                    Sets the marker opacity of selected points.

        Returns
        -------
        plotly.graph_objs.histogram.selected.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    # textfont
    # --------
    @property
    def textfont(self):
        """
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.selected.Textfont
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
            Supported dict properties:
                
                color
                    Sets the text font color of selected points.

        Returns
        -------
        plotly.graph_objs.histogram.selected.Textfont
        """
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            plotly.graph_objects.histogram.selected.Marker instance
            or dict with compatible properties
        textfont
            plotly.graph_objects.histogram.selected.Textfont
            instance or dict with compatible properties
        """

    def __init__(self, arg=None, marker=None, textfont=None, **kwargs):
        """
        Construct a new Selected object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.Selected
        marker
            plotly.graph_objects.histogram.selected.Marker instance
            or dict with compatible properties
        textfont
            plotly.graph_objects.histogram.selected.Textfont
            instance or dict with compatible properties

        Returns
        -------
        Selected
        """
        super(Selected, self).__init__("selected")

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
The first argument to the plotly.graph_objs.histogram.Selected 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.Selected"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import selected as v_selected

        # Initialize validators
        # ---------------------
        self._validators["marker"] = v_selected.MarkerValidator()
        self._validators["textfont"] = v_selected.TextfontValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("marker", None)
        self["marker"] = marker if marker is not None else _v
        _v = arg.pop("textfont", None)
        self["textfont"] = textfont if textfont is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `marker.colorscale`. Has an effect only if in `marker.color`is
        set to a numerical array. In case `colorscale` is unspecified
        or `autocolorscale` is true, the default  palette will be
        chosen according to whether numbers in the `color` array are
        all positive, all negative or mixed.
    
        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autocolorscale"]

    @autocolorscale.setter
    def autocolorscale(self, val):
        self["autocolorscale"] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here in `marker.color`) or the
        bounds set in `marker.cmin` and `marker.cmax`  Has an effect
        only if in `marker.color`is set to a numerical array. Defaults
        to `false` when `marker.cmin` and `marker.cmax` are set by the
        user.
    
        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["cauto"]

    @cauto.setter
    def cauto(self, val):
        self["cauto"] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Sets the upper bound of the color domain. Has an effect only if
        in `marker.color`is set to a numerical array. Value should have
        the same units as in `marker.color` and if set, `marker.cmin`
        must be set as well.
    
        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmax"]

    @cmax.setter
    def cmax(self, val):
        self["cmax"] = val

    # cmid
    # ----
    @property
    def cmid(self):
        """
        Sets the mid-point of the color domain by scaling `marker.cmin`
        and/or `marker.cmax` to be equidistant to this point. Has an
        effect only if in `marker.color`is set to a numerical array.
        Value should have the same units as in `marker.color`. Has no
        effect when `marker.cauto` is `false`.
    
        The 'cmid' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmid"]

    @cmid.setter
    def cmid(self, val):
        self["cmid"] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Sets the lower bound of the color domain. Has an effect only if
        in `marker.color`is set to a numerical array. Value should have
        the same units as in `marker.color` and if set, `marker.cmax`
        must be set as well.
    
        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmin"]

    @cmin.setter
    def cmin(self, val):
        self["cmin"] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets themarkercolor. It accepts either a specific color or an
        array of numbers that are mapped to the colorscale relative to
        the max and min values of the array or relative to
        `marker.cmin` and `marker.cmax` if set.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
          - A number that will be interpreted as a color
            according to histogram.marker.colorscale
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # coloraxis
    # ---------
    @property
    def coloraxis(self):
        """
        Sets a reference to a shared color axis. References to these
        shared color axes are "coloraxis", "coloraxis2", "coloraxis3",
        etc. Settings for these shared color axes are set in the
        layout, under `layout.coloraxis`, `layout.coloraxis2`, etc.
        Note that multiple color scales can be linked to the same color
        axis.
    
        The 'coloraxis' property is an identifier of a particular
        subplot, of type 'coloraxis', that may be specified as the string 'coloraxis'
        optionally followed by an integer >= 1
        (e.g. 'coloraxis', 'coloraxis1', 'coloraxis2', 'coloraxis3', etc.)

        Returns
        -------
        str
        """
        return self["coloraxis"]

    @coloraxis.setter
    def coloraxis(self, val):
        self["coloraxis"] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.marker.ColorBar
          - A dict of string/value properties that will be passed
            to the ColorBar constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the color of padded area.
                bordercolor
                    Sets the axis line color.
                borderwidth
                    Sets the width (in px) or the border enclosing
                    this color bar.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to "log" and "date"
                    axes. If the axis `type` is "log", then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. "log"
                    has several special values; "L<f>", where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use "D1" (all
                    digits) or "D2" (only 2 and 5). `tick0` is
                    ignored for "D1" and "D2". If the axis `type`
                    is "date", then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. "date" also has special values
                    "M<n>" gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to "2000-01-15" and `dtick` to "M3". To
                    set ticks every 4 years, set `dtick` to "M48"
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If "none", it appears as
                    1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                    "power", 1x10^9 (with 9 in a super script). If
                    "SI", 1G. If "B", 1B.
                len
                    Sets the length of the color bar This measure
                    excludes the padding of both ends. That is, the
                    color bar length is this length minus the
                    padding on both ends.
                lenmode
                    Determines whether this color bar's length
                    (i.e. the measure in the color variation
                    direction) is set in units of plot "fraction"
                    or in *pixels. Use `len` to set the value.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                outlinecolor
                    Sets the axis line color.
                outlinewidth
                    Sets the width (in px) of the axis line.
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If "all", all tick labels are displayed with a
                    prefix. If "first", only the first tick is
                    displayed with a prefix. If "last", only the
                    last tick is displayed with a suffix. If
                    "none", tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                thickness
                    Sets the thickness of the color bar This
                    measure excludes the size of the padding, ticks
                    and labels.
                thicknessmode
                    Determines whether this color bar's thickness
                    (i.e. the measure in the constant color
                    direction) is set in units of plot "fraction"
                    or in "pixels". Use `thickness` to set the
                    value.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    "log", then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is "date", it should be a date
                    string, like date data. If the axis `type` is
                    "category", it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the color bar's tick label font
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see:
                    https://github.com/d3/d3-3.x-api-
                    reference/blob/master/Formatting.md#d3_format
                    And for dates see:
                    https://github.com/d3/d3-3.x-api-
                    reference/blob/master/Time-Formatting.md#format
                    We add one item to d3's date formatter: "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                tickformatstops
                    A tuple of plotly.graph_objects.histogram.marke
                    r.colorbar.Tickformatstop instances or dicts
                    with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.dat
                    a.histogram.marker.colorbar.tickformatstopdefau
                    lts), sets the default property values to use
                    for elements of
                    histogram.marker.colorbar.tickformatstops
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If "auto",
                    the number of ticks is set via `nticks`. If
                    "linear", the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` ("linear" is the default
                    value if `tick0` and `dtick` are provided). If
                    "array", the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    ("array" is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    "", this axis' ticks are not drawn. If
                    "outside" ("inside"), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to "array". Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to "array". Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    plotly.graph_objects.histogram.marker.colorbar.
                    Title instance or dict with compatible
                    properties
                titlefont
                    Deprecated: Please use
                    histogram.marker.colorbar.title.font instead.
                    Sets this color bar's title font. Note that the
                    title's font used to be set by the now
                    deprecated `titlefont` attribute.
                titleside
                    Deprecated: Please use
                    histogram.marker.colorbar.title.side instead.
                    Determines the location of color bar's title
                    with respect to the color bar. Note that the
                    title's location used to be set by the now
                    deprecated `titleside` attribute.
                x
                    Sets the x position of the color bar (in plot
                    fraction).
                xanchor
                    Sets this color bar's horizontal position
                    anchor. This anchor binds the `x` position to
                    the "left", "center" or "right" of the color
                    bar.
                xpad
                    Sets the amount of padding (in px) along the x
                    direction.
                y
                    Sets the y position of the color bar (in plot
                    fraction).
                yanchor
                    Sets this color bar's vertical position anchor
                    This anchor binds the `y` position to the
                    "top", "middle" or "bottom" of the color bar.
                ypad
                    Sets the amount of padding (in px) along the y
                    direction.

        Returns
        -------
        plotly.graph_objs.histogram.marker.ColorBar
        """
        return self["colorbar"]

    @colorbar.setter
    def colorbar(self, val):
        self["colorbar"] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. Has an effect only if in `marker.color`is
        set to a numerical array. The colorscale must be an array
        containing arrays mapping a normalized value to an rgb, rgba,
        hex, hsl, hsv, or named color string. At minimum, a mapping for
        the lowest (0) and highest (1) values are required. For
        example, `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To
        control the bounds of the colorscale in color space,
        use`marker.cmin` and `marker.cmax`. Alternatively, `colorscale`
        may be a palette name string of the following list: Greys,YlGnB
        u,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland
        ,Jet,Hot,Blackbody,Earth,Electric,Viridis,Cividis.
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
                 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
                 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
                 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
                 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
                 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
                 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd'].
            Appending '_r' to a named colorscale reverses it.

        Returns
        -------
        str
        """
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["colorsrc"]

    @colorsrc.setter
    def colorsrc(self, val):
        self["colorsrc"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.marker.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                autocolorscale
                    Determines whether the colorscale is a default
                    palette (`autocolorscale: true`) or the palette
                    determined by `marker.line.colorscale`. Has an
                    effect only if in `marker.line.color`is set to
                    a numerical array. In case `colorscale` is
                    unspecified or `autocolorscale` is true, the
                    default  palette will be chosen according to
                    whether numbers in the `color` array are all
                    positive, all negative or mixed.
                cauto
                    Determines whether or not the color domain is
                    computed with respect to the input data (here
                    in `marker.line.color`) or the bounds set in
                    `marker.line.cmin` and `marker.line.cmax`  Has
                    an effect only if in `marker.line.color`is set
                    to a numerical array. Defaults to `false` when
                    `marker.line.cmin` and `marker.line.cmax` are
                    set by the user.
                cmax
                    Sets the upper bound of the color domain. Has
                    an effect only if in `marker.line.color`is set
                    to a numerical array. Value should have the
                    same units as in `marker.line.color` and if
                    set, `marker.line.cmin` must be set as well.
                cmid
                    Sets the mid-point of the color domain by
                    scaling `marker.line.cmin` and/or
                    `marker.line.cmax` to be equidistant to this
                    point. Has an effect only if in
                    `marker.line.color`is set to a numerical array.
                    Value should have the same units as in
                    `marker.line.color`. Has no effect when
                    `marker.line.cauto` is `false`.
                cmin
                    Sets the lower bound of the color domain. Has
                    an effect only if in `marker.line.color`is set
                    to a numerical array. Value should have the
                    same units as in `marker.line.color` and if
                    set, `marker.line.cmax` must be set as well.
                color
                    Sets themarker.linecolor. It accepts either a
                    specific color or an array of numbers that are
                    mapped to the colorscale relative to the max
                    and min values of the array or relative to
                    `marker.line.cmin` and `marker.line.cmax` if
                    set.
                coloraxis
                    Sets a reference to a shared color axis.
                    References to these shared color axes are
                    "coloraxis", "coloraxis2", "coloraxis3", etc.
                    Settings for these shared color axes are set in
                    the layout, under `layout.coloraxis`,
                    `layout.coloraxis2`, etc. Note that multiple
                    color scales can be linked to the same color
                    axis.
                colorscale
                    Sets the colorscale. Has an effect only if in
                    `marker.line.color`is set to a numerical array.
                    The colorscale must be an array containing
                    arrays mapping a normalized value to an rgb,
                    rgba, hex, hsl, hsv, or named color string. At
                    minimum, a mapping for the lowest (0) and
                    highest (1) values are required. For example,
                    `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
                    To control the bounds of the colorscale in
                    color space, use`marker.line.cmin` and
                    `marker.line.cmax`. Alternatively, `colorscale`
                    may be a palette name string of the following
                    list: Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,R
                    eds,Blues,Picnic,Rainbow,Portland,Jet,Hot,Black
                    body,Earth,Electric,Viridis,Cividis.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                reversescale
                    Reverses the color mapping if true. Has an
                    effect only if in `marker.line.color`is set to
                    a numerical array. If true, `marker.line.cmin`
                    will correspond to the last color in the array
                    and `marker.line.cmax` will correspond to the
                    first color.
                width
                    Sets the width (in px) of the lines bounding
                    the marker points.
                widthsrc
                    Sets the source reference on plot.ly for  width
                    .

        Returns
        -------
        plotly.graph_objs.histogram.marker.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the bars.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # opacitysrc
    # ----------
    @property
    def opacitysrc(self):
        """
        Sets the source reference on plot.ly for  opacity .
    
        The 'opacitysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["opacitysrc"]

    @opacitysrc.setter
    def opacitysrc(self, val):
        self["opacitysrc"] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. Has an effect only if in
        `marker.color`is set to a numerical array. If true,
        `marker.cmin` will correspond to the last color in the array
        and `marker.cmax` will correspond to the first color.
    
        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["reversescale"]

    @reversescale.setter
    def reversescale(self, val):
        self["reversescale"] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace. Has an effect only if in `marker.color`is set to a
        numerical array.
    
        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showscale"]

    @showscale.setter
    def showscale(self, val):
        self["showscale"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `marker.colorscale`. Has an effect only if in
            `marker.color`is set to a numerical array. In case
            `colorscale` is unspecified or `autocolorscale` is
            true, the default  palette will be chosen according to
            whether numbers in the `color` array are all positive,
            all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `marker.color`)
            or the bounds set in `marker.cmin` and `marker.cmax`
            Has an effect only if in `marker.color`is set to a
            numerical array. Defaults to `false` when `marker.cmin`
            and `marker.cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Has an effect
            only if in `marker.color`is set to a numerical array.
            Value should have the same units as in `marker.color`
            and if set, `marker.cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `marker.cmin` and/or `marker.cmax` to be equidistant to
            this point. Has an effect only if in `marker.color`is
            set to a numerical array. Value should have the same
            units as in `marker.color`. Has no effect when
            `marker.cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Has an effect
            only if in `marker.color`is set to a numerical array.
            Value should have the same units as in `marker.color`
            and if set, `marker.cmax` must be set as well.
        color
            Sets themarkercolor. It accepts either a specific color
            or an array of numbers that are mapped to the
            colorscale relative to the max and min values of the
            array or relative to `marker.cmin` and `marker.cmax` if
            set.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objects.histogram.marker.ColorBar instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. Has an effect only if in
            `marker.color`is set to a numerical array. The
            colorscale must be an array containing arrays mapping a
            normalized value to an rgb, rgba, hex, hsl, hsv, or
            named color string. At minimum, a mapping for the
            lowest (0) and highest (1) values are required. For
            example, `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
            To control the bounds of the colorscale in color space,
            use`marker.cmin` and `marker.cmax`. Alternatively,
            `colorscale` may be a palette name string of the
            following list: Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu
            ,Reds,Blues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,E
            arth,Electric,Viridis,Cividis.
        colorsrc
            Sets the source reference on plot.ly for  color .
        line
            plotly.graph_objects.histogram.marker.Line instance or
            dict with compatible properties
        opacity
            Sets the opacity of the bars.
        opacitysrc
            Sets the source reference on plot.ly for  opacity .
        reversescale
            Reverses the color mapping if true. Has an effect only
            if in `marker.color`is set to a numerical array. If
            true, `marker.cmin` will correspond to the last color
            in the array and `marker.cmax` will correspond to the
            first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace. Has an effect only if in `marker.color`is
            set to a numerical array.
        """

    def __init__(
        self,
        arg=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        color=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        colorsrc=None,
        line=None,
        opacity=None,
        opacitysrc=None,
        reversescale=None,
        showscale=None,
        **kwargs
    ):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.Marker
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `marker.colorscale`. Has an effect only if in
            `marker.color`is set to a numerical array. In case
            `colorscale` is unspecified or `autocolorscale` is
            true, the default  palette will be chosen according to
            whether numbers in the `color` array are all positive,
            all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `marker.color`)
            or the bounds set in `marker.cmin` and `marker.cmax`
            Has an effect only if in `marker.color`is set to a
            numerical array. Defaults to `false` when `marker.cmin`
            and `marker.cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Has an effect
            only if in `marker.color`is set to a numerical array.
            Value should have the same units as in `marker.color`
            and if set, `marker.cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `marker.cmin` and/or `marker.cmax` to be equidistant to
            this point. Has an effect only if in `marker.color`is
            set to a numerical array. Value should have the same
            units as in `marker.color`. Has no effect when
            `marker.cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Has an effect
            only if in `marker.color`is set to a numerical array.
            Value should have the same units as in `marker.color`
            and if set, `marker.cmax` must be set as well.
        color
            Sets themarkercolor. It accepts either a specific color
            or an array of numbers that are mapped to the
            colorscale relative to the max and min values of the
            array or relative to `marker.cmin` and `marker.cmax` if
            set.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            plotly.graph_objects.histogram.marker.ColorBar instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. Has an effect only if in
            `marker.color`is set to a numerical array. The
            colorscale must be an array containing arrays mapping a
            normalized value to an rgb, rgba, hex, hsl, hsv, or
            named color string. At minimum, a mapping for the
            lowest (0) and highest (1) values are required. For
            example, `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
            To control the bounds of the colorscale in color space,
            use`marker.cmin` and `marker.cmax`. Alternatively,
            `colorscale` may be a palette name string of the
            following list: Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu
            ,Reds,Blues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,E
            arth,Electric,Viridis,Cividis.
        colorsrc
            Sets the source reference on plot.ly for  color .
        line
            plotly.graph_objects.histogram.marker.Line instance or
            dict with compatible properties
        opacity
            Sets the opacity of the bars.
        opacitysrc
            Sets the source reference on plot.ly for  opacity .
        reversescale
            Reverses the color mapping if true. Has an effect only
            if in `marker.color`is set to a numerical array. If
            true, `marker.cmin` will correspond to the last color
            in the array and `marker.cmax` will correspond to the
            first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace. Has an effect only if in `marker.color`is
            set to a numerical array.

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__("marker")

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
The first argument to the plotly.graph_objs.histogram.Marker 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.Marker"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import marker as v_marker

        # Initialize validators
        # ---------------------
        self._validators["autocolorscale"] = v_marker.AutocolorscaleValidator()
        self._validators["cauto"] = v_marker.CautoValidator()
        self._validators["cmax"] = v_marker.CmaxValidator()
        self._validators["cmid"] = v_marker.CmidValidator()
        self._validators["cmin"] = v_marker.CminValidator()
        self._validators["color"] = v_marker.ColorValidator()
        self._validators["coloraxis"] = v_marker.ColoraxisValidator()
        self._validators["colorbar"] = v_marker.ColorBarValidator()
        self._validators["colorscale"] = v_marker.ColorscaleValidator()
        self._validators["colorsrc"] = v_marker.ColorsrcValidator()
        self._validators["line"] = v_marker.LineValidator()
        self._validators["opacity"] = v_marker.OpacityValidator()
        self._validators["opacitysrc"] = v_marker.OpacitysrcValidator()
        self._validators["reversescale"] = v_marker.ReversescaleValidator()
        self._validators["showscale"] = v_marker.ShowscaleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("autocolorscale", None)
        self["autocolorscale"] = autocolorscale if autocolorscale is not None else _v
        _v = arg.pop("cauto", None)
        self["cauto"] = cauto if cauto is not None else _v
        _v = arg.pop("cmax", None)
        self["cmax"] = cmax if cmax is not None else _v
        _v = arg.pop("cmid", None)
        self["cmid"] = cmid if cmid is not None else _v
        _v = arg.pop("cmin", None)
        self["cmin"] = cmin if cmin is not None else _v
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("coloraxis", None)
        self["coloraxis"] = coloraxis if coloraxis is not None else _v
        _v = arg.pop("colorbar", None)
        self["colorbar"] = colorbar if colorbar is not None else _v
        _v = arg.pop("colorscale", None)
        self["colorscale"] = colorscale if colorscale is not None else _v
        _v = arg.pop("colorsrc", None)
        self["colorsrc"] = colorsrc if colorsrc is not None else _v
        _v = arg.pop("line", None)
        self["line"] = line if line is not None else _v
        _v = arg.pop("opacity", None)
        self["opacity"] = opacity if opacity is not None else _v
        _v = arg.pop("opacitysrc", None)
        self["opacitysrc"] = opacitysrc if opacitysrc is not None else _v
        _v = arg.pop("reversescale", None)
        self["reversescale"] = reversescale if reversescale is not None else _v
        _v = arg.pop("showscale", None)
        self["showscale"] = showscale if showscale is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Hoverlabel(_BaseTraceHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the text content within hover
        label box. Has an effect only if the hover label text spans
        more two or more lines
    
        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'right', 'auto']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    # alignsrc
    # --------
    @property
    def alignsrc(self):
        """
        Sets the source reference on plot.ly for  align .
    
        The 'alignsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["alignsrc"]

    @alignsrc.setter
    def alignsrc(self, val):
        self["alignsrc"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the hover labels for this trace
    
        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bgcolorsrc
    # ----------
    @property
    def bgcolorsrc(self):
        """
        Sets the source reference on plot.ly for  bgcolor .
    
        The 'bgcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["bgcolorsrc"]

    @bgcolorsrc.setter
    def bgcolorsrc(self, val):
        self["bgcolorsrc"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the border color of the hover labels for this trace.
    
        The 'bordercolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # bordercolorsrc
    # --------------
    @property
    def bordercolorsrc(self):
        """
        Sets the source reference on plot.ly for  bordercolor .
    
        The 'bordercolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["bordercolorsrc"]

    @bordercolorsrc.setter
    def bordercolorsrc(self, val):
        self["bordercolorsrc"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font used in hover labels.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.hoverlabel.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include "Arial",
                    "Balto", "Courier New", "Droid Sans",, "Droid
                    Serif", "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                familysrc
                    Sets the source reference on plot.ly for
                    family .
                size
    
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .

        Returns
        -------
        plotly.graph_objs.histogram.hoverlabel.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # namelength
    # ----------
    @property
    def namelength(self):
        """
        Sets the default length (in number of characters) of the trace
        name in the hover labels for all traces. -1 shows the whole
        name regardless of length. 0-3 shows the first 0-3 characters,
        and an integer >3 will show the whole name if it is less than
        that many characters, but if it is longer, will truncate to
        `namelength - 3` characters and add an ellipsis.
    
        The 'namelength' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [-1, 9223372036854775807]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|numpy.ndarray
        """
        return self["namelength"]

    @namelength.setter
    def namelength(self, val):
        self["namelength"] = val

    # namelengthsrc
    # -------------
    @property
    def namelengthsrc(self):
        """
        Sets the source reference on plot.ly for  namelength .
    
        The 'namelengthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["namelengthsrc"]

    @namelengthsrc.setter
    def namelengthsrc(self, val):
        self["namelengthsrc"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        alignsrc
            Sets the source reference on plot.ly for  align .
        bgcolor
            Sets the background color of the hover labels for this
            trace
        bgcolorsrc
            Sets the source reference on plot.ly for  bgcolor .
        bordercolor
            Sets the border color of the hover labels for this
            trace.
        bordercolorsrc
            Sets the source reference on plot.ly for  bordercolor .
        font
            Sets the font used in hover labels.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.
        namelengthsrc
            Sets the source reference on plot.ly for  namelength .
        """

    def __init__(
        self,
        arg=None,
        align=None,
        alignsrc=None,
        bgcolor=None,
        bgcolorsrc=None,
        bordercolor=None,
        bordercolorsrc=None,
        font=None,
        namelength=None,
        namelengthsrc=None,
        **kwargs
    ):
        """
        Construct a new Hoverlabel object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.Hoverlabel
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        alignsrc
            Sets the source reference on plot.ly for  align .
        bgcolor
            Sets the background color of the hover labels for this
            trace
        bgcolorsrc
            Sets the source reference on plot.ly for  bgcolor .
        bordercolor
            Sets the border color of the hover labels for this
            trace.
        bordercolorsrc
            Sets the source reference on plot.ly for  bordercolor .
        font
            Sets the font used in hover labels.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.
        namelengthsrc
            Sets the source reference on plot.ly for  namelength .

        Returns
        -------
        Hoverlabel
        """
        super(Hoverlabel, self).__init__("hoverlabel")

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
The first argument to the plotly.graph_objs.histogram.Hoverlabel 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.Hoverlabel"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import hoverlabel as v_hoverlabel

        # Initialize validators
        # ---------------------
        self._validators["align"] = v_hoverlabel.AlignValidator()
        self._validators["alignsrc"] = v_hoverlabel.AlignsrcValidator()
        self._validators["bgcolor"] = v_hoverlabel.BgcolorValidator()
        self._validators["bgcolorsrc"] = v_hoverlabel.BgcolorsrcValidator()
        self._validators["bordercolor"] = v_hoverlabel.BordercolorValidator()
        self._validators["bordercolorsrc"] = v_hoverlabel.BordercolorsrcValidator()
        self._validators["font"] = v_hoverlabel.FontValidator()
        self._validators["namelength"] = v_hoverlabel.NamelengthValidator()
        self._validators["namelengthsrc"] = v_hoverlabel.NamelengthsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("align", None)
        self["align"] = align if align is not None else _v
        _v = arg.pop("alignsrc", None)
        self["alignsrc"] = alignsrc if alignsrc is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bgcolorsrc", None)
        self["bgcolorsrc"] = bgcolorsrc if bgcolorsrc is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("bordercolorsrc", None)
        self["bordercolorsrc"] = bordercolorsrc if bordercolorsrc is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("namelength", None)
        self["namelength"] = namelength if namelength is not None else _v
        _v = arg.pop("namelengthsrc", None)
        self["namelengthsrc"] = namelengthsrc if namelengthsrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class ErrorY(_BaseTraceHierarchyType):

    # array
    # -----
    @property
    def array(self):
        """
        Sets the data corresponding the length of each error bar.
        Values are plotted relative to the underlying data.
    
        The 'array' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["array"]

    @array.setter
    def array(self, val):
        self["array"] = val

    # arrayminus
    # ----------
    @property
    def arrayminus(self):
        """
        Sets the data corresponding the length of each error bar in the
        bottom (left) direction for vertical (horizontal) bars Values
        are plotted relative to the underlying data.
    
        The 'arrayminus' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["arrayminus"]

    @arrayminus.setter
    def arrayminus(self, val):
        self["arrayminus"] = val

    # arrayminussrc
    # -------------
    @property
    def arrayminussrc(self):
        """
        Sets the source reference on plot.ly for  arrayminus .
    
        The 'arrayminussrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["arrayminussrc"]

    @arrayminussrc.setter
    def arrayminussrc(self, val):
        self["arrayminussrc"] = val

    # arraysrc
    # --------
    @property
    def arraysrc(self):
        """
        Sets the source reference on plot.ly for  array .
    
        The 'arraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["arraysrc"]

    @arraysrc.setter
    def arraysrc(self, val):
        self["arraysrc"] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the stoke color of the error bars.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # symmetric
    # ---------
    @property
    def symmetric(self):
        """
        Determines whether or not the error bars have the same length
        in both direction (top/bottom for vertical bars, left/right for
        horizontal bars.
    
        The 'symmetric' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["symmetric"]

    @symmetric.setter
    def symmetric(self, val):
        self["symmetric"] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        Sets the thickness (in px) of the error bars.
    
        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    # traceref
    # --------
    @property
    def traceref(self):
        """
        The 'traceref' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["traceref"]

    @traceref.setter
    def traceref(self, val):
        self["traceref"] = val

    # tracerefminus
    # -------------
    @property
    def tracerefminus(self):
        """
        The 'tracerefminus' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["tracerefminus"]

    @tracerefminus.setter
    def tracerefminus(self, val):
        self["tracerefminus"] = val

    # type
    # ----
    @property
    def type(self):
        """
        Determines the rule used to generate the error bars. If
        *constant`, the bar lengths are of a constant value. Set this
        constant in `value`. If "percent", the bar lengths correspond
        to a percentage of underlying data. Set this percentage in
        `value`. If "sqrt", the bar lengths correspond to the sqaure of
        the underlying data. If "data", the bar lengths are set with
        data set `array`.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['percent', 'constant', 'sqrt', 'data']

        Returns
        -------
        Any
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    # value
    # -----
    @property
    def value(self):
        """
        Sets the value of either the percentage (if `type` is set to
        "percent") or the constant (if `type` is set to "constant")
        corresponding to the lengths of the error bars.
    
        The 'value' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["value"]

    @value.setter
    def value(self, val):
        self["value"] = val

    # valueminus
    # ----------
    @property
    def valueminus(self):
        """
        Sets the value of either the percentage (if `type` is set to
        "percent") or the constant (if `type` is set to "constant")
        corresponding to the lengths of the error bars in the bottom
        (left) direction for vertical (horizontal) bars
    
        The 'valueminus' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["valueminus"]

    @valueminus.setter
    def valueminus(self, val):
        self["valueminus"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this set of error bars is visible.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width (in px) of the cross-bar at both ends of the
        error bars.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on plot.ly for  arrayminus .
        arraysrc
            Sets the source reference on plot.ly for  array .
        color
            Sets the stoke color of the error bars.
        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            *constant`, the bar lengths are of a constant value.
            Set this constant in `value`. If "percent", the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If "sqrt", the bar
            lengths correspond to the sqaure of the underlying
            data. If "data", the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.
        """

    def __init__(
        self,
        arg=None,
        array=None,
        arrayminus=None,
        arrayminussrc=None,
        arraysrc=None,
        color=None,
        symmetric=None,
        thickness=None,
        traceref=None,
        tracerefminus=None,
        type=None,
        value=None,
        valueminus=None,
        visible=None,
        width=None,
        **kwargs
    ):
        """
        Construct a new ErrorY object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.ErrorY
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on plot.ly for  arrayminus .
        arraysrc
            Sets the source reference on plot.ly for  array .
        color
            Sets the stoke color of the error bars.
        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            *constant`, the bar lengths are of a constant value.
            Set this constant in `value`. If "percent", the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If "sqrt", the bar
            lengths correspond to the sqaure of the underlying
            data. If "data", the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.

        Returns
        -------
        ErrorY
        """
        super(ErrorY, self).__init__("error_y")

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
The first argument to the plotly.graph_objs.histogram.ErrorY 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.ErrorY"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import error_y as v_error_y

        # Initialize validators
        # ---------------------
        self._validators["array"] = v_error_y.ArrayValidator()
        self._validators["arrayminus"] = v_error_y.ArrayminusValidator()
        self._validators["arrayminussrc"] = v_error_y.ArrayminussrcValidator()
        self._validators["arraysrc"] = v_error_y.ArraysrcValidator()
        self._validators["color"] = v_error_y.ColorValidator()
        self._validators["symmetric"] = v_error_y.SymmetricValidator()
        self._validators["thickness"] = v_error_y.ThicknessValidator()
        self._validators["traceref"] = v_error_y.TracerefValidator()
        self._validators["tracerefminus"] = v_error_y.TracerefminusValidator()
        self._validators["type"] = v_error_y.TypeValidator()
        self._validators["value"] = v_error_y.ValueValidator()
        self._validators["valueminus"] = v_error_y.ValueminusValidator()
        self._validators["visible"] = v_error_y.VisibleValidator()
        self._validators["width"] = v_error_y.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("array", None)
        self["array"] = array if array is not None else _v
        _v = arg.pop("arrayminus", None)
        self["arrayminus"] = arrayminus if arrayminus is not None else _v
        _v = arg.pop("arrayminussrc", None)
        self["arrayminussrc"] = arrayminussrc if arrayminussrc is not None else _v
        _v = arg.pop("arraysrc", None)
        self["arraysrc"] = arraysrc if arraysrc is not None else _v
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("symmetric", None)
        self["symmetric"] = symmetric if symmetric is not None else _v
        _v = arg.pop("thickness", None)
        self["thickness"] = thickness if thickness is not None else _v
        _v = arg.pop("traceref", None)
        self["traceref"] = traceref if traceref is not None else _v
        _v = arg.pop("tracerefminus", None)
        self["tracerefminus"] = tracerefminus if tracerefminus is not None else _v
        _v = arg.pop("type", None)
        self["type"] = type if type is not None else _v
        _v = arg.pop("value", None)
        self["value"] = value if value is not None else _v
        _v = arg.pop("valueminus", None)
        self["valueminus"] = valueminus if valueminus is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("width", None)
        self["width"] = width if width is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class ErrorX(_BaseTraceHierarchyType):

    # array
    # -----
    @property
    def array(self):
        """
        Sets the data corresponding the length of each error bar.
        Values are plotted relative to the underlying data.
    
        The 'array' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["array"]

    @array.setter
    def array(self, val):
        self["array"] = val

    # arrayminus
    # ----------
    @property
    def arrayminus(self):
        """
        Sets the data corresponding the length of each error bar in the
        bottom (left) direction for vertical (horizontal) bars Values
        are plotted relative to the underlying data.
    
        The 'arrayminus' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["arrayminus"]

    @arrayminus.setter
    def arrayminus(self, val):
        self["arrayminus"] = val

    # arrayminussrc
    # -------------
    @property
    def arrayminussrc(self):
        """
        Sets the source reference on plot.ly for  arrayminus .
    
        The 'arrayminussrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["arrayminussrc"]

    @arrayminussrc.setter
    def arrayminussrc(self, val):
        self["arrayminussrc"] = val

    # arraysrc
    # --------
    @property
    def arraysrc(self):
        """
        Sets the source reference on plot.ly for  array .
    
        The 'arraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["arraysrc"]

    @arraysrc.setter
    def arraysrc(self, val):
        self["arraysrc"] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the stoke color of the error bars.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # copy_ystyle
    # -----------
    @property
    def copy_ystyle(self):
        """
        The 'copy_ystyle' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["copy_ystyle"]

    @copy_ystyle.setter
    def copy_ystyle(self, val):
        self["copy_ystyle"] = val

    # symmetric
    # ---------
    @property
    def symmetric(self):
        """
        Determines whether or not the error bars have the same length
        in both direction (top/bottom for vertical bars, left/right for
        horizontal bars.
    
        The 'symmetric' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["symmetric"]

    @symmetric.setter
    def symmetric(self, val):
        self["symmetric"] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        Sets the thickness (in px) of the error bars.
    
        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    # traceref
    # --------
    @property
    def traceref(self):
        """
        The 'traceref' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["traceref"]

    @traceref.setter
    def traceref(self, val):
        self["traceref"] = val

    # tracerefminus
    # -------------
    @property
    def tracerefminus(self):
        """
        The 'tracerefminus' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["tracerefminus"]

    @tracerefminus.setter
    def tracerefminus(self, val):
        self["tracerefminus"] = val

    # type
    # ----
    @property
    def type(self):
        """
        Determines the rule used to generate the error bars. If
        *constant`, the bar lengths are of a constant value. Set this
        constant in `value`. If "percent", the bar lengths correspond
        to a percentage of underlying data. Set this percentage in
        `value`. If "sqrt", the bar lengths correspond to the sqaure of
        the underlying data. If "data", the bar lengths are set with
        data set `array`.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['percent', 'constant', 'sqrt', 'data']

        Returns
        -------
        Any
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    # value
    # -----
    @property
    def value(self):
        """
        Sets the value of either the percentage (if `type` is set to
        "percent") or the constant (if `type` is set to "constant")
        corresponding to the lengths of the error bars.
    
        The 'value' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["value"]

    @value.setter
    def value(self, val):
        self["value"] = val

    # valueminus
    # ----------
    @property
    def valueminus(self):
        """
        Sets the value of either the percentage (if `type` is set to
        "percent") or the constant (if `type` is set to "constant")
        corresponding to the lengths of the error bars in the bottom
        (left) direction for vertical (horizontal) bars
    
        The 'valueminus' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["valueminus"]

    @valueminus.setter
    def valueminus(self, val):
        self["valueminus"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this set of error bars is visible.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width (in px) of the cross-bar at both ends of the
        error bars.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on plot.ly for  arrayminus .
        arraysrc
            Sets the source reference on plot.ly for  array .
        color
            Sets the stoke color of the error bars.
        copy_ystyle

        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            *constant`, the bar lengths are of a constant value.
            Set this constant in `value`. If "percent", the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If "sqrt", the bar
            lengths correspond to the sqaure of the underlying
            data. If "data", the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.
        """

    def __init__(
        self,
        arg=None,
        array=None,
        arrayminus=None,
        arrayminussrc=None,
        arraysrc=None,
        color=None,
        copy_ystyle=None,
        symmetric=None,
        thickness=None,
        traceref=None,
        tracerefminus=None,
        type=None,
        value=None,
        valueminus=None,
        visible=None,
        width=None,
        **kwargs
    ):
        """
        Construct a new ErrorX object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.ErrorX
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on plot.ly for  arrayminus .
        arraysrc
            Sets the source reference on plot.ly for  array .
        color
            Sets the stoke color of the error bars.
        copy_ystyle

        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            *constant`, the bar lengths are of a constant value.
            Set this constant in `value`. If "percent", the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If "sqrt", the bar
            lengths correspond to the sqaure of the underlying
            data. If "data", the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to "percent") or the constant (if `type` is set to
            "constant") corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.

        Returns
        -------
        ErrorX
        """
        super(ErrorX, self).__init__("error_x")

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
The first argument to the plotly.graph_objs.histogram.ErrorX 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.ErrorX"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import error_x as v_error_x

        # Initialize validators
        # ---------------------
        self._validators["array"] = v_error_x.ArrayValidator()
        self._validators["arrayminus"] = v_error_x.ArrayminusValidator()
        self._validators["arrayminussrc"] = v_error_x.ArrayminussrcValidator()
        self._validators["arraysrc"] = v_error_x.ArraysrcValidator()
        self._validators["color"] = v_error_x.ColorValidator()
        self._validators["copy_ystyle"] = v_error_x.CopyYstyleValidator()
        self._validators["symmetric"] = v_error_x.SymmetricValidator()
        self._validators["thickness"] = v_error_x.ThicknessValidator()
        self._validators["traceref"] = v_error_x.TracerefValidator()
        self._validators["tracerefminus"] = v_error_x.TracerefminusValidator()
        self._validators["type"] = v_error_x.TypeValidator()
        self._validators["value"] = v_error_x.ValueValidator()
        self._validators["valueminus"] = v_error_x.ValueminusValidator()
        self._validators["visible"] = v_error_x.VisibleValidator()
        self._validators["width"] = v_error_x.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("array", None)
        self["array"] = array if array is not None else _v
        _v = arg.pop("arrayminus", None)
        self["arrayminus"] = arrayminus if arrayminus is not None else _v
        _v = arg.pop("arrayminussrc", None)
        self["arrayminussrc"] = arrayminussrc if arrayminussrc is not None else _v
        _v = arg.pop("arraysrc", None)
        self["arraysrc"] = arraysrc if arraysrc is not None else _v
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("copy_ystyle", None)
        self["copy_ystyle"] = copy_ystyle if copy_ystyle is not None else _v
        _v = arg.pop("symmetric", None)
        self["symmetric"] = symmetric if symmetric is not None else _v
        _v = arg.pop("thickness", None)
        self["thickness"] = thickness if thickness is not None else _v
        _v = arg.pop("traceref", None)
        self["traceref"] = traceref if traceref is not None else _v
        _v = arg.pop("tracerefminus", None)
        self["tracerefminus"] = tracerefminus if tracerefminus is not None else _v
        _v = arg.pop("type", None)
        self["type"] = type if type is not None else _v
        _v = arg.pop("value", None)
        self["value"] = value if value is not None else _v
        _v = arg.pop("valueminus", None)
        self["valueminus"] = valueminus if valueminus is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("width", None)
        self["width"] = width if width is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Cumulative(_BaseTraceHierarchyType):

    # currentbin
    # ----------
    @property
    def currentbin(self):
        """
        Only applies if cumulative is enabled. Sets whether the current
        bin is included, excluded, or has half of its value included in
        the current cumulative value. "include" is the default for
        compatibility with various other tools, however it introduces a
        half-bin bias to the results. "exclude" makes the opposite
        half-bin bias, and "half" removes it.
    
        The 'currentbin' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['include', 'exclude', 'half']

        Returns
        -------
        Any
        """
        return self["currentbin"]

    @currentbin.setter
    def currentbin(self, val):
        self["currentbin"] = val

    # direction
    # ---------
    @property
    def direction(self):
        """
        Only applies if cumulative is enabled. If "increasing"
        (default) we sum all prior bins, so the result increases from
        left to right. If "decreasing" we sum later bins so the result
        decreases from left to right.
    
        The 'direction' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['increasing', 'decreasing']

        Returns
        -------
        Any
        """
        return self["direction"]

    @direction.setter
    def direction(self, val):
        self["direction"] = val

    # enabled
    # -------
    @property
    def enabled(self):
        """
        If true, display the cumulative distribution by summing the
        binned values. Use the `direction` and `centralbin` attributes
        to tune the accumulation method. Note: in this mode, the
        "density" `histnorm` settings behave the same as their
        equivalents without "density": "" and "density" both rise to
        the number of data points, and "probability" and *probability
        density* both rise to the number of sample points.
    
        The 'enabled' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["enabled"]

    @enabled.setter
    def enabled(self, val):
        self["enabled"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "histogram"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        currentbin
            Only applies if cumulative is enabled. Sets whether the
            current bin is included, excluded, or has half of its
            value included in the current cumulative value.
            "include" is the default for compatibility with various
            other tools, however it introduces a half-bin bias to
            the results. "exclude" makes the opposite half-bin
            bias, and "half" removes it.
        direction
            Only applies if cumulative is enabled. If "increasing"
            (default) we sum all prior bins, so the result
            increases from left to right. If "decreasing" we sum
            later bins so the result decreases from left to right.
        enabled
            If true, display the cumulative distribution by summing
            the binned values. Use the `direction` and `centralbin`
            attributes to tune the accumulation method. Note: in
            this mode, the "density" `histnorm` settings behave the
            same as their equivalents without "density": "" and
            "density" both rise to the number of data points, and
            "probability" and *probability density* both rise to
            the number of sample points.
        """

    def __init__(
        self, arg=None, currentbin=None, direction=None, enabled=None, **kwargs
    ):
        """
        Construct a new Cumulative object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.Cumulative
        currentbin
            Only applies if cumulative is enabled. Sets whether the
            current bin is included, excluded, or has half of its
            value included in the current cumulative value.
            "include" is the default for compatibility with various
            other tools, however it introduces a half-bin bias to
            the results. "exclude" makes the opposite half-bin
            bias, and "half" removes it.
        direction
            Only applies if cumulative is enabled. If "increasing"
            (default) we sum all prior bins, so the result
            increases from left to right. If "decreasing" we sum
            later bins so the result decreases from left to right.
        enabled
            If true, display the cumulative distribution by summing
            the binned values. Use the `direction` and `centralbin`
            attributes to tune the accumulation method. Note: in
            this mode, the "density" `histnorm` settings behave the
            same as their equivalents without "density": "" and
            "density" both rise to the number of data points, and
            "probability" and *probability density* both rise to
            the number of sample points.

        Returns
        -------
        Cumulative
        """
        super(Cumulative, self).__init__("cumulative")

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
The first argument to the plotly.graph_objs.histogram.Cumulative 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.Cumulative"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.histogram import cumulative as v_cumulative

        # Initialize validators
        # ---------------------
        self._validators["currentbin"] = v_cumulative.CurrentbinValidator()
        self._validators["direction"] = v_cumulative.DirectionValidator()
        self._validators["enabled"] = v_cumulative.EnabledValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("currentbin", None)
        self["currentbin"] = currentbin if currentbin is not None else _v
        _v = arg.pop("direction", None)
        self["direction"] = direction if direction is not None else _v
        _v = arg.pop("enabled", None)
        self["enabled"] = enabled if enabled is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = [
    "Cumulative",
    "ErrorX",
    "ErrorY",
    "Hoverlabel",
    "Marker",
    "Selected",
    "Stream",
    "Unselected",
    "XBins",
    "YBins",
    "hoverlabel",
    "marker",
    "selected",
    "unselected",
]

from plotly.graph_objs.histogram import unselected
from plotly.graph_objs.histogram import selected
from plotly.graph_objs.histogram import marker
from plotly.graph_objs.histogram import hoverlabel
