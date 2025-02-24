from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Violin(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "violin"
    _valid_props = {
        "alignmentgroup",
        "bandwidth",
        "box",
        "customdata",
        "customdatasrc",
        "fillcolor",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hoveron",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "jitter",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "marker",
        "meanline",
        "meta",
        "metasrc",
        "name",
        "offsetgroup",
        "opacity",
        "orientation",
        "pointpos",
        "points",
        "quartilemethod",
        "scalegroup",
        "scalemode",
        "selected",
        "selectedpoints",
        "showlegend",
        "side",
        "span",
        "spanmode",
        "stream",
        "text",
        "textsrc",
        "type",
        "uid",
        "uirevision",
        "unselected",
        "visible",
        "width",
        "x",
        "x0",
        "xaxis",
        "xhoverformat",
        "xsrc",
        "y",
        "y0",
        "yaxis",
        "yhoverformat",
        "ysrc",
        "zorder",
    }

    @property
    def alignmentgroup(self):
        """
        Set several traces linked to the same position axis or matching
        axes to the same alignmentgroup. This controls whether bars
        compute their positional range dependently or independently.

        The 'alignmentgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["alignmentgroup"]

    @alignmentgroup.setter
    def alignmentgroup(self, val):
        self["alignmentgroup"] = val

    @property
    def bandwidth(self):
        """
        Sets the bandwidth used to compute the kernel density estimate.
        By default, the bandwidth is determined by Silverman's rule of
        thumb.

        The 'bandwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["bandwidth"]

    @bandwidth.setter
    def bandwidth(self, val):
        self["bandwidth"] = val

    @property
    def box(self):
        """
        The 'box' property is an instance of Box
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Box`
          - A dict of string/value properties that will be passed
            to the Box constructor

        Returns
        -------
        plotly.graph_objs.violin.Box
        """
        return self["box"]

    @box.setter
    def box(self, val):
        self["box"] = val

    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements

        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

    @property
    def customdatasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `customdata`.

        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    @property
    def fillcolor(self):
        """
        Sets the fill color. Defaults to a half-transparent variant of
        the line color, marker color, or marker line color, whichever
        is available.

        The 'fillcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self["fillcolor"]

    @fillcolor.setter
    def fillcolor(self, val):
        self["fillcolor"] = val

    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|NDArray
        """
        return self["hoverinfo"]

    @hoverinfo.setter
    def hoverinfo(self, val):
        self["hoverinfo"] = val

    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hoverinfo`.

        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hoverinfosrc"]

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self["hoverinfosrc"] = val

    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

        Returns
        -------
        plotly.graph_objs.violin.Hoverlabel
        """
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    @property
    def hoveron(self):
        """
        Do the hover effects highlight individual violins or sample
        points or the kernel density estimate or any combination of
        them?

        The 'hoveron' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['violins', 'points', 'kde'] joined with '+' characters
            (e.g. 'violins+points')
            OR exactly one of ['all'] (e.g. 'all')

        Returns
        -------
        Any
        """
        return self["hoveron"]

    @hoveron.setter
    def hoveron(self, val):
        self["hoveron"] = val

    @property
    def hovertemplate(self):
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. The variables available in `hovertemplate`
        are the ones emitted as event data described at this link
        https://plotly.com/javascript/plotlyjs-events/#event-data.
        Additionally, every attributes that can be specified per-point
        (the ones that are `arrayOk: true`) are available.  Anything
        contained in tag `<extra>` is displayed in the secondary box,
        for example "<extra>{fullData.name}</extra>". To hide the
        secondary box completely, use an empty tag `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|NDArray
        """
        return self["hovertemplate"]

    @hovertemplate.setter
    def hovertemplate(self, val):
        self["hovertemplate"] = val

    @property
    def hovertemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.

        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hovertemplatesrc"]

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self["hovertemplatesrc"] = val

    @property
    def hovertext(self):
        """
        Same as `text`.

        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|NDArray
        """
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

    @property
    def hovertextsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertext`.

        The 'hovertextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hovertextsrc"]

    @hovertextsrc.setter
    def hovertextsrc(self, val):
        self["hovertextsrc"] = val

    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.

        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["ids"]

    @ids.setter
    def ids(self, val):
        self["ids"] = val

    @property
    def idssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `ids`.

        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["idssrc"]

    @idssrc.setter
    def idssrc(self, val):
        self["idssrc"] = val

    @property
    def jitter(self):
        """
        Sets the amount of jitter in the sample points drawn. If 0, the
        sample points align along the distribution axis. If 1, the
        sample points are drawn in a random jitter of width equal to
        the width of the violins.

        The 'jitter' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["jitter"]

    @jitter.setter
    def jitter(self, val):
        self["jitter"] = val

    @property
    def legend(self):
        """
        Sets the reference to a legend to show this trace in.
        References to these legends are "legend", "legend2", "legend3",
        etc. Settings for these legends are set in the layout, under
        `layout.legend`, `layout.legend2`, etc.

        The 'legend' property is an identifier of a particular
        subplot, of type 'legend', that may be specified as the string 'legend'
        optionally followed by an integer >= 1
        (e.g. 'legend', 'legend1', 'legend2', 'legend3', etc.)

        Returns
        -------
        str
        """
        return self["legend"]

    @legend.setter
    def legend(self, val):
        self["legend"] = val

    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces and shapes part of
        the same legend group hide/show at the same time when toggling
        legend items.

        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["legendgroup"]

    @legendgroup.setter
    def legendgroup(self, val):
        self["legendgroup"] = val

    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

        Returns
        -------
        plotly.graph_objs.violin.Legendgrouptitle
        """
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

    @property
    def legendrank(self):
        """
        Sets the legend rank for this trace. Items and groups with
        smaller ranks are presented on top/left side while with
        "reversed" `legend.traceorder` they are on bottom/right side.
        The default legendrank is 1000, so that you can use ranks less
        than 1000 to place certain items before all unranked items, and
        ranks greater than 1000 to go after all unranked items. When
        having unranked or equal rank items shapes would be displayed
        after traces i.e. according to their order in data and layout.

        The 'legendrank' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["legendrank"]

    @legendrank.setter
    def legendrank(self, val):
        self["legendrank"] = val

    @property
    def legendwidth(self):
        """
        Sets the width (in px or fraction) of the legend for this
        trace.

        The 'legendwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["legendwidth"]

    @legendwidth.setter
    def legendwidth(self, val):
        self["legendwidth"] = val

    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.violin.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor

        Returns
        -------
        plotly.graph_objs.violin.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    @property
    def meanline(self):
        """
        The 'meanline' property is an instance of Meanline
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Meanline`
          - A dict of string/value properties that will be passed
            to the Meanline constructor

        Returns
        -------
        plotly.graph_objs.violin.Meanline
        """
        return self["meanline"]

    @meanline.setter
    def meanline(self, val):
        self["meanline"] = val

    @property
    def meta(self):
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.

        The 'meta' property accepts values of any type

        Returns
        -------
        Any|NDArray
        """
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

    @property
    def metasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `meta`.

        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

    @property
    def name(self):
        """
        Sets the trace name. The trace name appears as the legend item
        and on hover. For violin traces, the name will also be used for
        the position coordinate, if `x` and `x0` (`y` and `y0` if
        horizontal) are missing and the position axis is categorical.
        Note that the trace name is also used as a default value for
        attribute `scalegroup` (please see its description for
        details).

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    @property
    def offsetgroup(self):
        """
        Set several traces linked to the same position axis or matching
        axes to the same offsetgroup where bars of the same position
        coordinate will line up.

        The 'offsetgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["offsetgroup"]

    @offsetgroup.setter
    def offsetgroup(self, val):
        self["offsetgroup"] = val

    @property
    def opacity(self):
        """
        Sets the opacity of the trace.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    @property
    def orientation(self):
        """
        Sets the orientation of the violin(s). If "v" ("h"), the
        distribution is visualized along the vertical (horizontal).

        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    @property
    def pointpos(self):
        """
        Sets the position of the sample points in relation to the
        violins. If 0, the sample points are places over the center of
        the violins. Positive (negative) values correspond to positions
        to the right (left) for vertical violins and above (below) for
        horizontal violins.

        The 'pointpos' property is a number and may be specified as:
          - An int or float in the interval [-2, 2]

        Returns
        -------
        int|float
        """
        return self["pointpos"]

    @pointpos.setter
    def pointpos(self, val):
        self["pointpos"] = val

    @property
    def points(self):
        """
        If "outliers", only the sample points lying outside the
        whiskers are shown If "suspectedoutliers", the outlier points
        are shown and points either less than 4*Q1-3*Q3 or greater than
        4*Q3-3*Q1 are highlighted (see `outliercolor`) If "all", all
        sample points are shown If False, only the violins are shown
        with no sample points. Defaults to "suspectedoutliers" when
        `marker.outliercolor` or `marker.line.outliercolor` is set,
        otherwise defaults to "outliers".

        The 'points' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'outliers', 'suspectedoutliers', False]

        Returns
        -------
        Any
        """
        return self["points"]

    @points.setter
    def points(self, val):
        self["points"] = val

    @property
    def quartilemethod(self):
        """
        Sets the method used to compute the sample's Q1 and Q3
        quartiles. The "linear" method uses the 25th percentile for Q1
        and 75th percentile for Q3 as computed using method #10 (listed
        on http://jse.amstat.org/v14n3/langford.html). The "exclusive"
        method uses the median to divide the ordered dataset into two
        halves if the sample is odd, it does not include the median in
        either half - Q1 is then the median of the lower half and Q3
        the median of the upper half. The "inclusive" method also uses
        the median to divide the ordered dataset into two halves but if
        the sample is odd, it includes the median in both halves - Q1
        is then the median of the lower half and Q3 the median of the
        upper half.

        The 'quartilemethod' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'exclusive', 'inclusive']

        Returns
        -------
        Any
        """
        return self["quartilemethod"]

    @quartilemethod.setter
    def quartilemethod(self, val):
        self["quartilemethod"] = val

    @property
    def scalegroup(self):
        """
        If there are multiple violins that should be sized according to
        to some metric (see `scalemode`), link them by providing a non-
        empty group id here shared by every trace in the same group. If
        a violin's `width` is undefined, `scalegroup` will default to
        the trace's name. In this case, violins with the same names
        will be linked together

        The 'scalegroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["scalegroup"]

    @scalegroup.setter
    def scalegroup(self, val):
        self["scalegroup"] = val

    @property
    def scalemode(self):
        """
        Sets the metric by which the width of each violin is
        determined. "width" means each violin has the same (max) width
        "count" means the violins are scaled by the number of sample
        points making up each violin.

        The 'scalemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['width', 'count']

        Returns
        -------
        Any
        """
        return self["scalemode"]

    @scalemode.setter
    def scalemode(self, val):
        self["scalemode"] = val

    @property
    def selected(self):
        """
        The 'selected' property is an instance of Selected
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Selected`
          - A dict of string/value properties that will be passed
            to the Selected constructor

        Returns
        -------
        plotly.graph_objs.violin.Selected
        """
        return self["selected"]

    @selected.setter
    def selected(self, val):
        self["selected"] = val

    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.

        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["selectedpoints"]

    @selectedpoints.setter
    def selectedpoints(self, val):
        self["selectedpoints"] = val

    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.

        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    @property
    def side(self):
        """
        Determines on which side of the position value the density
        function making up one half of a violin is plotted. Useful when
        comparing two violin traces under "overlay" mode, where one
        trace has `side` set to "positive" and the other to "negative".

        The 'side' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['both', 'positive', 'negative']

        Returns
        -------
        Any
        """
        return self["side"]

    @side.setter
    def side(self, val):
        self["side"] = val

    @property
    def span(self):
        """
            Sets the span in data space for which the density function will
            be computed. Has an effect only when `spanmode` is set to
            "manual".

            The 'span' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'span[0]' property accepts values of any type
        (1) The 'span[1]' property accepts values of any type

            Returns
            -------
            list
        """
        return self["span"]

    @span.setter
    def span(self, val):
        self["span"] = val

    @property
    def spanmode(self):
        """
        Sets the method by which the span in data space where the
        density function will be computed. "soft" means the span goes
        from the sample's minimum value minus two bandwidths to the
        sample's maximum value plus two bandwidths. "hard" means the
        span goes from the sample's minimum to its maximum value. For
        custom span settings, use mode "manual" and fill in the `span`
        attribute.

        The 'spanmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['soft', 'hard', 'manual']

        Returns
        -------
        Any
        """
        return self["spanmode"]

    @spanmode.setter
    def spanmode(self, val):
        self["spanmode"] = val

    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

        Returns
        -------
        plotly.graph_objs.violin.Stream
        """
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    @property
    def text(self):
        """
        Sets the text elements associated with each sample value. If a
        single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        the this trace's (x,y) coordinates. To be seen, trace
        `hoverinfo` must contain a "text" flag.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|NDArray
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    @property
    def textsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `text`.

        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["textsrc"]

    @textsrc.setter
    def textsrc(self, val):
        self["textsrc"] = val

    @property
    def uid(self):
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.

        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["uid"]

    @uid.setter
    def uid(self, val):
        self["uid"] = val

    @property
    def uirevision(self):
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def unselected(self):
        """
        The 'unselected' property is an instance of Unselected
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.violin.Unselected`
          - A dict of string/value properties that will be passed
            to the Unselected constructor

        Returns
        -------
        plotly.graph_objs.violin.Unselected
        """
        return self["unselected"]

    @unselected.setter
    def unselected(self, val):
        self["unselected"] = val

    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).

        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def width(self):
        """
        Sets the width of the violin in data coordinates. If 0 (default
        value) the width is automatically selected based on the
        positions of other violin traces in the same subplot.

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

    @property
    def x(self):
        """
        Sets the x sample data or coordinates. See overview for more
        info.

        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    @property
    def x0(self):
        """
        Sets the x coordinate for single-box traces or the starting
        coordinate for multi-box traces set using q1/median/q3. See
        overview for more info.

        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["x0"]

    @x0.setter
    def x0(self, val):
        self["x0"] = val

    @property
    def xaxis(self):
        """
        Sets a reference between this trace's x coordinates and a 2D
        cartesian x axis. If "x" (the default value), the x coordinates
        refer to `layout.xaxis`. If "x2", the x coordinates refer to
        `layout.xaxis2`, and so on.

        The 'xaxis' property is an identifier of a particular
        subplot, of type 'x', that may be specified as the string 'x'
        optionally followed by an integer >= 1
        (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        str
        """
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

    @property
    def xhoverformat(self):
        """
        Sets the hover text formatting rulefor `x`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `xaxis.hoverformat`.

        The 'xhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["xhoverformat"]

    @xhoverformat.setter
    def xhoverformat(self, val):
        self["xhoverformat"] = val

    @property
    def xsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `x`.

        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["xsrc"]

    @xsrc.setter
    def xsrc(self, val):
        self["xsrc"] = val

    @property
    def y(self):
        """
        Sets the y sample data or coordinates. See overview for more
        info.

        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    @property
    def y0(self):
        """
        Sets the y coordinate for single-box traces or the starting
        coordinate for multi-box traces set using q1/median/q3. See
        overview for more info.

        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["y0"]

    @y0.setter
    def y0(self, val):
        self["y0"] = val

    @property
    def yaxis(self):
        """
        Sets a reference between this trace's y coordinates and a 2D
        cartesian y axis. If "y" (the default value), the y coordinates
        refer to `layout.yaxis`. If "y2", the y coordinates refer to
        `layout.yaxis2`, and so on.

        The 'yaxis' property is an identifier of a particular
        subplot, of type 'y', that may be specified as the string 'y'
        optionally followed by an integer >= 1
        (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        str
        """
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    @property
    def yhoverformat(self):
        """
        Sets the hover text formatting rulefor `y`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `yaxis.hoverformat`.

        The 'yhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["yhoverformat"]

    @yhoverformat.setter
    def yhoverformat(self, val):
        self["yhoverformat"] = val

    @property
    def ysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `y`.

        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["ysrc"]

    @ysrc.setter
    def ysrc(self, val):
        self["ysrc"] = val

    @property
    def zorder(self):
        """
        Sets the layer on which this trace is displayed, relative to
        other SVG traces on the same subplot. SVG traces with higher
        `zorder` appear in front of those with lower `zorder`.

        The 'zorder' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)

        Returns
        -------
        int
        """
        return self["zorder"]

    @zorder.setter
    def zorder(self, val):
        self["zorder"] = val

    @property
    def type(self):
        return self._props["type"]

    @property
    def _prop_descriptions(self):
        return """\
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        bandwidth
            Sets the bandwidth used to compute the kernel density
            estimate. By default, the bandwidth is determined by
            Silverman's rule of thumb.
        box
            :class:`plotly.graph_objects.violin.Box` instance or
            dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.violin.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual violins or
            sample points or the kernel density estimate or any
            combination of them?
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        jitter
            Sets the amount of jitter in the sample points drawn.
            If 0, the sample points align along the distribution
            axis. If 1, the sample points are drawn in a random
            jitter of width equal to the width of the violins.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.violin.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        line
            :class:`plotly.graph_objects.violin.Line` instance or
            dict with compatible properties
        marker
            :class:`plotly.graph_objects.violin.Marker` instance or
            dict with compatible properties
        meanline
            :class:`plotly.graph_objects.violin.Meanline` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover. For violin traces, the name
            will also be used for the position coordinate, if `x`
            and `x0` (`y` and `y0` if horizontal) are missing and
            the position axis is categorical. Note that the trace
            name is also used as a default value for attribute
            `scalegroup` (please see its description for details).
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the violin(s). If "v" ("h"),
            the distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the violins. If 0, the sample points are places over
            the center of the violins. Positive (negative) values
            correspond to positions to the right (left) for
            vertical violins and above (below) for horizontal
            violins.
        points
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the violins are shown with no sample
            points. Defaults to "suspectedoutliers" when
            `marker.outliercolor` or `marker.line.outliercolor` is
            set, otherwise defaults to "outliers".
        quartilemethod
            Sets the method used to compute the sample's Q1 and Q3
            quartiles. The "linear" method uses the 25th percentile
            for Q1 and 75th percentile for Q3 as computed using
            method #10 (listed on
            http://jse.amstat.org/v14n3/langford.html). The
            "exclusive" method uses the median to divide the
            ordered dataset into two halves if the sample is odd,
            it does not include the median in either half - Q1 is
            then the median of the lower half and Q3 the median of
            the upper half. The "inclusive" method also uses the
            median to divide the ordered dataset into two halves
            but if the sample is odd, it includes the median in
            both halves - Q1 is then the median of the lower half
            and Q3 the median of the upper half.
        scalegroup
            If there are multiple violins that should be sized
            according to to some metric (see `scalemode`), link
            them by providing a non-empty group id here shared by
            every trace in the same group. If a violin's `width` is
            undefined, `scalegroup` will default to the trace's
            name. In this case, violins with the same names will be
            linked together
        scalemode
            Sets the metric by which the width of each violin is
            determined. "width" means each violin has the same
            (max) width "count" means the violins are scaled by the
            number of sample points making up each violin.
        selected
            :class:`plotly.graph_objects.violin.Selected` instance
            or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        side
            Determines on which side of the position value the
            density function making up one half of a violin is
            plotted. Useful when comparing two violin traces under
            "overlay" mode, where one trace has `side` set to
            "positive" and the other to "negative".
        span
            Sets the span in data space for which the density
            function will be computed. Has an effect only when
            `spanmode` is set to "manual".
        spanmode
            Sets the method by which the span in data space where
            the density function will be computed. "soft" means the
            span goes from the sample's minimum value minus two
            bandwidths to the sample's maximum value plus two
            bandwidths. "hard" means the span goes from the
            sample's minimum to its maximum value. For custom span
            settings, use mode "manual" and fill in the `span`
            attribute.
        stream
            :class:`plotly.graph_objects.violin.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with each sample
            value. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.violin.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the width of the violin in data coordinates. If 0
            (default value) the width is automatically selected
            based on the positions of other violin traces in the
            same subplot.
        x
            Sets the x sample data or coordinates. See overview for
            more info.
        x0
            Sets the x coordinate for single-box traces or the
            starting coordinate for multi-box traces set using
            q1/median/q3. See overview for more info.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y sample data or coordinates. See overview for
            more info.
        y0
            Sets the y coordinate for single-box traces or the
            starting coordinate for multi-box traces set using
            q1/median/q3. See overview for more info.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        zorder
            Sets the layer on which this trace is displayed,
            relative to other SVG traces on the same subplot. SVG
            traces with higher `zorder` appear in front of those
            with lower `zorder`.
        """

    def __init__(
        self,
        arg=None,
        alignmentgroup: str | None = None,
        bandwidth: int | float | None = None,
        box: None | None = None,
        customdata: NDArray | None = None,
        customdatasrc: str | None = None,
        fillcolor: str | None = None,
        hoverinfo: Any | None = None,
        hoverinfosrc: str | None = None,
        hoverlabel: None | None = None,
        hoveron: Any | None = None,
        hovertemplate: str | None = None,
        hovertemplatesrc: str | None = None,
        hovertext: str | None = None,
        hovertextsrc: str | None = None,
        ids: NDArray | None = None,
        idssrc: str | None = None,
        jitter: int | float | None = None,
        legend: str | None = None,
        legendgroup: str | None = None,
        legendgrouptitle: None | None = None,
        legendrank: int | float | None = None,
        legendwidth: int | float | None = None,
        line: None | None = None,
        marker: None | None = None,
        meanline: None | None = None,
        meta: Any | None = None,
        metasrc: str | None = None,
        name: str | None = None,
        offsetgroup: str | None = None,
        opacity: int | float | None = None,
        orientation: Any | None = None,
        pointpos: int | float | None = None,
        points: Any | None = None,
        quartilemethod: Any | None = None,
        scalegroup: str | None = None,
        scalemode: Any | None = None,
        selected: None | None = None,
        selectedpoints: Any | None = None,
        showlegend: bool | None = None,
        side: Any | None = None,
        span: list | None = None,
        spanmode: Any | None = None,
        stream: None | None = None,
        text: str | None = None,
        textsrc: str | None = None,
        uid: str | None = None,
        uirevision: Any | None = None,
        unselected: None | None = None,
        visible: Any | None = None,
        width: int | float | None = None,
        x: NDArray | None = None,
        x0: Any | None = None,
        xaxis: str | None = None,
        xhoverformat: str | None = None,
        xsrc: str | None = None,
        y: NDArray | None = None,
        y0: Any | None = None,
        yaxis: str | None = None,
        yhoverformat: str | None = None,
        ysrc: str | None = None,
        zorder: int | None = None,
        **kwargs,
    ):
        """
        Construct a new Violin object

        In vertical (horizontal) violin plots, statistics are computed
        using `y` (`x`) values. By supplying an `x` (`y`) array, one
        violin per distinct x (y) value is drawn If no `x` (`y`) list
        is provided, a single violin is drawn. That violin position is
        then positioned with with `name` or with `x0` (`y0`) if
        provided.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Violin`
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        bandwidth
            Sets the bandwidth used to compute the kernel density
            estimate. By default, the bandwidth is determined by
            Silverman's rule of thumb.
        box
            :class:`plotly.graph_objects.violin.Box` instance or
            dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.violin.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual violins or
            sample points or the kernel density estimate or any
            combination of them?
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        jitter
            Sets the amount of jitter in the sample points drawn.
            If 0, the sample points align along the distribution
            axis. If 1, the sample points are drawn in a random
            jitter of width equal to the width of the violins.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.violin.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        line
            :class:`plotly.graph_objects.violin.Line` instance or
            dict with compatible properties
        marker
            :class:`plotly.graph_objects.violin.Marker` instance or
            dict with compatible properties
        meanline
            :class:`plotly.graph_objects.violin.Meanline` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover. For violin traces, the name
            will also be used for the position coordinate, if `x`
            and `x0` (`y` and `y0` if horizontal) are missing and
            the position axis is categorical. Note that the trace
            name is also used as a default value for attribute
            `scalegroup` (please see its description for details).
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the violin(s). If "v" ("h"),
            the distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the violins. If 0, the sample points are places over
            the center of the violins. Positive (negative) values
            correspond to positions to the right (left) for
            vertical violins and above (below) for horizontal
            violins.
        points
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the violins are shown with no sample
            points. Defaults to "suspectedoutliers" when
            `marker.outliercolor` or `marker.line.outliercolor` is
            set, otherwise defaults to "outliers".
        quartilemethod
            Sets the method used to compute the sample's Q1 and Q3
            quartiles. The "linear" method uses the 25th percentile
            for Q1 and 75th percentile for Q3 as computed using
            method #10 (listed on
            http://jse.amstat.org/v14n3/langford.html). The
            "exclusive" method uses the median to divide the
            ordered dataset into two halves if the sample is odd,
            it does not include the median in either half - Q1 is
            then the median of the lower half and Q3 the median of
            the upper half. The "inclusive" method also uses the
            median to divide the ordered dataset into two halves
            but if the sample is odd, it includes the median in
            both halves - Q1 is then the median of the lower half
            and Q3 the median of the upper half.
        scalegroup
            If there are multiple violins that should be sized
            according to to some metric (see `scalemode`), link
            them by providing a non-empty group id here shared by
            every trace in the same group. If a violin's `width` is
            undefined, `scalegroup` will default to the trace's
            name. In this case, violins with the same names will be
            linked together
        scalemode
            Sets the metric by which the width of each violin is
            determined. "width" means each violin has the same
            (max) width "count" means the violins are scaled by the
            number of sample points making up each violin.
        selected
            :class:`plotly.graph_objects.violin.Selected` instance
            or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        side
            Determines on which side of the position value the
            density function making up one half of a violin is
            plotted. Useful when comparing two violin traces under
            "overlay" mode, where one trace has `side` set to
            "positive" and the other to "negative".
        span
            Sets the span in data space for which the density
            function will be computed. Has an effect only when
            `spanmode` is set to "manual".
        spanmode
            Sets the method by which the span in data space where
            the density function will be computed. "soft" means the
            span goes from the sample's minimum value minus two
            bandwidths to the sample's maximum value plus two
            bandwidths. "hard" means the span goes from the
            sample's minimum to its maximum value. For custom span
            settings, use mode "manual" and fill in the `span`
            attribute.
        stream
            :class:`plotly.graph_objects.violin.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with each sample
            value. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.violin.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the width of the violin in data coordinates. If 0
            (default value) the width is automatically selected
            based on the positions of other violin traces in the
            same subplot.
        x
            Sets the x sample data or coordinates. See overview for
            more info.
        x0
            Sets the x coordinate for single-box traces or the
            starting coordinate for multi-box traces set using
            q1/median/q3. See overview for more info.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y sample data or coordinates. See overview for
            more info.
        y0
            Sets the y coordinate for single-box traces or the
            starting coordinate for multi-box traces set using
            q1/median/q3. See overview for more info.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        zorder
            Sets the layer on which this trace is displayed,
            relative to other SVG traces on the same subplot. SVG
            traces with higher `zorder` appear in front of those
            with lower `zorder`.

        Returns
        -------
        Violin
        """
        super().__init__("violin")
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
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Violin
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Violin`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("alignmentgroup", arg, alignmentgroup)
        self._init_provided("bandwidth", arg, bandwidth)
        self._init_provided("box", arg, box)
        self._init_provided("customdata", arg, customdata)
        self._init_provided("customdatasrc", arg, customdatasrc)
        self._init_provided("fillcolor", arg, fillcolor)
        self._init_provided("hoverinfo", arg, hoverinfo)
        self._init_provided("hoverinfosrc", arg, hoverinfosrc)
        self._init_provided("hoverlabel", arg, hoverlabel)
        self._init_provided("hoveron", arg, hoveron)
        self._init_provided("hovertemplate", arg, hovertemplate)
        self._init_provided("hovertemplatesrc", arg, hovertemplatesrc)
        self._init_provided("hovertext", arg, hovertext)
        self._init_provided("hovertextsrc", arg, hovertextsrc)
        self._init_provided("ids", arg, ids)
        self._init_provided("idssrc", arg, idssrc)
        self._init_provided("jitter", arg, jitter)
        self._init_provided("legend", arg, legend)
        self._init_provided("legendgroup", arg, legendgroup)
        self._init_provided("legendgrouptitle", arg, legendgrouptitle)
        self._init_provided("legendrank", arg, legendrank)
        self._init_provided("legendwidth", arg, legendwidth)
        self._init_provided("line", arg, line)
        self._init_provided("marker", arg, marker)
        self._init_provided("meanline", arg, meanline)
        self._init_provided("meta", arg, meta)
        self._init_provided("metasrc", arg, metasrc)
        self._init_provided("name", arg, name)
        self._init_provided("offsetgroup", arg, offsetgroup)
        self._init_provided("opacity", arg, opacity)
        self._init_provided("orientation", arg, orientation)
        self._init_provided("pointpos", arg, pointpos)
        self._init_provided("points", arg, points)
        self._init_provided("quartilemethod", arg, quartilemethod)
        self._init_provided("scalegroup", arg, scalegroup)
        self._init_provided("scalemode", arg, scalemode)
        self._init_provided("selected", arg, selected)
        self._init_provided("selectedpoints", arg, selectedpoints)
        self._init_provided("showlegend", arg, showlegend)
        self._init_provided("side", arg, side)
        self._init_provided("span", arg, span)
        self._init_provided("spanmode", arg, spanmode)
        self._init_provided("stream", arg, stream)
        self._init_provided("text", arg, text)
        self._init_provided("textsrc", arg, textsrc)
        self._init_provided("uid", arg, uid)
        self._init_provided("uirevision", arg, uirevision)
        self._init_provided("unselected", arg, unselected)
        self._init_provided("visible", arg, visible)
        self._init_provided("width", arg, width)
        self._init_provided("x", arg, x)
        self._init_provided("x0", arg, x0)
        self._init_provided("xaxis", arg, xaxis)
        self._init_provided("xhoverformat", arg, xhoverformat)
        self._init_provided("xsrc", arg, xsrc)
        self._init_provided("y", arg, y)
        self._init_provided("y0", arg, y0)
        self._init_provided("yaxis", arg, yaxis)
        self._init_provided("yhoverformat", arg, yhoverformat)
        self._init_provided("ysrc", arg, ysrc)
        self._init_provided("zorder", arg, zorder)

        self._props["type"] = "violin"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
