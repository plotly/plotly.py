from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Treemap(_BaseTraceType):

    _parent_path_str = ""
    _path_str = "treemap"
    _valid_props = {
        "branchvalues",
        "count",
        "customdata",
        "customdatasrc",
        "domain",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "insidetextfont",
        "labels",
        "labelssrc",
        "legend",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "level",
        "marker",
        "maxdepth",
        "meta",
        "metasrc",
        "name",
        "opacity",
        "outsidetextfont",
        "parents",
        "parentssrc",
        "pathbar",
        "root",
        "sort",
        "stream",
        "text",
        "textfont",
        "textinfo",
        "textposition",
        "textsrc",
        "texttemplate",
        "texttemplatesrc",
        "tiling",
        "type",
        "uid",
        "uirevision",
        "values",
        "valuessrc",
        "visible",
    }

    @property
    def branchvalues(self):
        """
        Determines how the items in `values` are summed. When set to
        "total", items in `values` are taken to be value of all its
        descendants. When set to "remainder", items in `values`
        corresponding to the root and the branches sectors are taken to
        be the extra part not part of the sum of the values at their
        leaves.

        The 'branchvalues' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['remainder', 'total']

        Returns
        -------
        Any
        """
        return self["branchvalues"]

    @branchvalues.setter
    def branchvalues(self, val):
        self["branchvalues"] = val

    @property
    def count(self):
        """
        Determines default for `values` when it is not provided, by
        inferring a 1 for each of the "leaves" and/or "branches",
        otherwise 0.

        The 'count' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['branches', 'leaves'] joined with '+' characters
            (e.g. 'branches+leaves')

        Returns
        -------
        Any
        """
        return self["count"]

    @count.setter
    def count(self, val):
        self["count"] = val

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
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

        Returns
        -------
        plotly.graph_objs.treemap.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['label', 'text', 'value', 'name', 'current path', 'percent root', 'percent entry', 'percent parent'] joined with '+' characters
            (e.g. 'label+text')
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
          - An instance of :class:`plotly.graph_objs.treemap.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

        Returns
        -------
        plotly.graph_objs.treemap.Hoverlabel
        """
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

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
        (the ones that are `arrayOk: true`) are available. Finally, the
        template string has access to variables `currentPath`, `root`,
        `entry`, `percentRoot`, `percentEntry` and `percentParent`.
        Anything contained in tag `<extra>` is displayed in the
        secondary box, for example "<extra>{fullData.name}</extra>". To
        hide the secondary box completely, use an empty tag
        `<extra></extra>`.

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
        Sets hover text elements associated with each sector. If a
        single string, the same string appears for all data points. If
        an array of string, the items are mapped in order of this
        trace's sectors. To be seen, trace `hoverinfo` must contain a
        "text" flag.

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
    def insidetextfont(self):
        """
        Sets the font used for `textinfo` lying inside the sector.

        The 'insidetextfont' property is an instance of Insidetextfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Insidetextfont`
          - A dict of string/value properties that will be passed
            to the Insidetextfont constructor

        Returns
        -------
        plotly.graph_objs.treemap.Insidetextfont
        """
        return self["insidetextfont"]

    @insidetextfont.setter
    def insidetextfont(self, val):
        self["insidetextfont"] = val

    @property
    def labels(self):
        """
        Sets the labels of each of the sectors.

        The 'labels' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["labels"]

    @labels.setter
    def labels(self, val):
        self["labels"] = val

    @property
    def labelssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `labels`.

        The 'labelssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["labelssrc"]

    @labelssrc.setter
    def labelssrc(self, val):
        self["labelssrc"] = val

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
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

        Returns
        -------
        plotly.graph_objs.treemap.Legendgrouptitle
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
    def level(self):
        """
        Sets the level from which this trace hierarchy is rendered. Set
        `level` to `''` to start from the root node in the hierarchy.
        Must be an "id" if `ids` is filled in, otherwise plotly
        attempts to find a matching item in `labels`.

        The 'level' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["level"]

    @level.setter
    def level(self, val):
        self["level"] = val

    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor

        Returns
        -------
        plotly.graph_objs.treemap.Marker
        """
        return self["marker"]

    @marker.setter
    def marker(self, val):
        self["marker"] = val

    @property
    def maxdepth(self):
        """
        Sets the number of rendered sectors from any given `level`. Set
        `maxdepth` to "-1" to render all the levels in the hierarchy.

        The 'maxdepth' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)

        Returns
        -------
        int
        """
        return self["maxdepth"]

    @maxdepth.setter
    def maxdepth(self, val):
        self["maxdepth"] = val

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
        and on hover.

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
    def outsidetextfont(self):
        """
        Sets the font used for `textinfo` lying outside the sector.
        This option refers to the root of the hierarchy presented on
        top left corner of a treemap graph. Please note that if a
        hierarchy has multiple root nodes, this option won't have any
        effect and `insidetextfont` would be used.

        The 'outsidetextfont' property is an instance of Outsidetextfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Outsidetextfont`
          - A dict of string/value properties that will be passed
            to the Outsidetextfont constructor

        Returns
        -------
        plotly.graph_objs.treemap.Outsidetextfont
        """
        return self["outsidetextfont"]

    @outsidetextfont.setter
    def outsidetextfont(self, val):
        self["outsidetextfont"] = val

    @property
    def parents(self):
        """
        Sets the parent sectors for each of the sectors. Empty string
        items '' are understood to reference the root node in the
        hierarchy. If `ids` is filled, `parents` items are understood
        to be "ids" themselves. When `ids` is not set, plotly attempts
        to find matching items in `labels`, but beware they must be
        unique.

        The 'parents' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["parents"]

    @parents.setter
    def parents(self, val):
        self["parents"] = val

    @property
    def parentssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `parents`.

        The 'parentssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["parentssrc"]

    @parentssrc.setter
    def parentssrc(self, val):
        self["parentssrc"] = val

    @property
    def pathbar(self):
        """
        The 'pathbar' property is an instance of Pathbar
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Pathbar`
          - A dict of string/value properties that will be passed
            to the Pathbar constructor

        Returns
        -------
        plotly.graph_objs.treemap.Pathbar
        """
        return self["pathbar"]

    @pathbar.setter
    def pathbar(self, val):
        self["pathbar"] = val

    @property
    def root(self):
        """
        The 'root' property is an instance of Root
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Root`
          - A dict of string/value properties that will be passed
            to the Root constructor

        Returns
        -------
        plotly.graph_objs.treemap.Root
        """
        return self["root"]

    @root.setter
    def root(self, val):
        self["root"] = val

    @property
    def sort(self):
        """
        Determines whether or not the sectors are reordered from
        largest to smallest.

        The 'sort' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["sort"]

    @sort.setter
    def sort(self, val):
        self["sort"] = val

    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

        Returns
        -------
        plotly.graph_objs.treemap.Stream
        """
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    @property
    def text(self):
        """
        Sets text elements associated with each sector. If trace
        `textinfo` contains a "text" flag, these elements will be seen
        on the chart. If trace `hoverinfo` contains a "text" flag and
        "hovertext" is not set, these elements will be seen in the
        hover labels.

        The 'text' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    @property
    def textfont(self):
        """
        Sets the font used for `textinfo`.

        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Textfont`
          - A dict of string/value properties that will be passed
            to the Textfont constructor

        Returns
        -------
        plotly.graph_objs.treemap.Textfont
        """
        return self["textfont"]

    @textfont.setter
    def textfont(self, val):
        self["textfont"] = val

    @property
    def textinfo(self):
        """
        Determines which trace information appear on the graph.

        The 'textinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['label', 'text', 'value', 'current path', 'percent root', 'percent entry', 'percent parent'] joined with '+' characters
            (e.g. 'label+text')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self["textinfo"]

    @textinfo.setter
    def textinfo(self, val):
        self["textinfo"] = val

    @property
    def textposition(self):
        """
        Sets the positions of the `text` elements.

        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle left',
                'middle center', 'middle right', 'bottom left', 'bottom
                center', 'bottom right']

        Returns
        -------
        Any
        """
        return self["textposition"]

    @textposition.setter
    def textposition(self, val):
        self["textposition"] = val

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
    def texttemplate(self):
        """
        Template string used for rendering the information text that
        appear on points. Note that this will override `textinfo`.
        Variables are inserted using %{variable}, for example "y:
        %{y}". Numbers are formatted using d3-format's syntax
        %{variable:d3-format}, for example "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. Every attributes that can be specified per-
        point (the ones that are `arrayOk: true`) are available.
        Finally, the template string has access to variables
        `currentPath`, `root`, `entry`, `percentRoot`, `percentEntry`,
        `percentParent`, `label` and `value`.

        The 'texttemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|NDArray
        """
        return self["texttemplate"]

    @texttemplate.setter
    def texttemplate(self, val):
        self["texttemplate"] = val

    @property
    def texttemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `texttemplate`.

        The 'texttemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["texttemplatesrc"]

    @texttemplatesrc.setter
    def texttemplatesrc(self, val):
        self["texttemplatesrc"] = val

    @property
    def tiling(self):
        """
        The 'tiling' property is an instance of Tiling
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.treemap.Tiling`
          - A dict of string/value properties that will be passed
            to the Tiling constructor

        Returns
        -------
        plotly.graph_objs.treemap.Tiling
        """
        return self["tiling"]

    @tiling.setter
    def tiling(self, val):
        self["tiling"] = val

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
    def values(self):
        """
        Sets the values associated with each of the sectors. Use with
        `branchvalues` to determine how the values are summed.

        The 'values' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self["values"]

    @values.setter
    def values(self, val):
        self["values"] = val

    @property
    def valuessrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `values`.

        The 'valuessrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["valuessrc"]

    @valuessrc.setter
    def valuessrc(self, val):
        self["valuessrc"] = val

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
    def type(self):
        return self._props["type"]

    @property
    def _prop_descriptions(self):
        return """\
        branchvalues
            Determines how the items in `values` are summed. When
            set to "total", items in `values` are taken to be value
            of all its descendants. When set to "remainder", items
            in `values` corresponding to the root and the branches
            sectors are taken to be the extra part not part of the
            sum of the values at their leaves.
        count
            Determines default for `values` when it is not
            provided, by inferring a 1 for each of the "leaves"
            and/or "branches", otherwise 0.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        domain
            :class:`plotly.graph_objects.treemap.Domain` instance
            or dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.treemap.Hoverlabel`
            instance or dict with compatible properties
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
            are available. Finally, the template string has access
            to variables `currentPath`, `root`, `entry`,
            `percentRoot`, `percentEntry` and `percentParent`.
            Anything contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
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
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        labels
            Sets the labels of each of the sectors.
        labelssrc
            Sets the source reference on Chart Studio Cloud for
            `labels`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgrouptitle
            :class:`plotly.graph_objects.treemap.Legendgrouptitle`
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
        level
            Sets the level from which this trace hierarchy is
            rendered. Set `level` to `''` to start from the root
            node in the hierarchy. Must be an "id" if `ids` is
            filled in, otherwise plotly attempts to find a matching
            item in `labels`.
        marker
            :class:`plotly.graph_objects.treemap.Marker` instance
            or dict with compatible properties
        maxdepth
            Sets the number of rendered sectors from any given
            `level`. Set `maxdepth` to "-1" to render all the
            levels in the hierarchy.
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
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            sector. This option refers to the root of the hierarchy
            presented on top left corner of a treemap graph. Please
            note that if a hierarchy has multiple root nodes, this
            option won't have any effect and `insidetextfont` would
            be used.
        parents
            Sets the parent sectors for each of the sectors. Empty
            string items '' are understood to reference the root
            node in the hierarchy. If `ids` is filled, `parents`
            items are understood to be "ids" themselves. When `ids`
            is not set, plotly attempts to find matching items in
            `labels`, but beware they must be unique.
        parentssrc
            Sets the source reference on Chart Studio Cloud for
            `parents`.
        pathbar
            :class:`plotly.graph_objects.treemap.Pathbar` instance
            or dict with compatible properties
        root
            :class:`plotly.graph_objects.treemap.Root` instance or
            dict with compatible properties
        sort
            Determines whether or not the sectors are reordered
            from largest to smallest.
        stream
            :class:`plotly.graph_objects.treemap.Stream` instance
            or dict with compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Sets the positions of the `text` elements.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. Every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `currentPath`, `root`, `entry`,
            `percentRoot`, `percentEntry`, `percentParent`, `label`
            and `value`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `texttemplate`.
        tiling
            :class:`plotly.graph_objects.treemap.Tiling` instance
            or dict with compatible properties
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
        values
            Sets the values associated with each of the sectors.
            Use with `branchvalues` to determine how the values are
            summed.
        valuessrc
            Sets the source reference on Chart Studio Cloud for
            `values`.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        """

    def __init__(
        self,
        arg=None,
        branchvalues: Any | None = None,
        count: Any | None = None,
        customdata: NDArray | None = None,
        customdatasrc: str | None = None,
        domain: None | None = None,
        hoverinfo: Any | None = None,
        hoverinfosrc: str | None = None,
        hoverlabel: None | None = None,
        hovertemplate: str | None = None,
        hovertemplatesrc: str | None = None,
        hovertext: str | None = None,
        hovertextsrc: str | None = None,
        ids: NDArray | None = None,
        idssrc: str | None = None,
        insidetextfont: None | None = None,
        labels: NDArray | None = None,
        labelssrc: str | None = None,
        legend: str | None = None,
        legendgrouptitle: None | None = None,
        legendrank: int | float | None = None,
        legendwidth: int | float | None = None,
        level: Any | None = None,
        marker: None | None = None,
        maxdepth: int | None = None,
        meta: Any | None = None,
        metasrc: str | None = None,
        name: str | None = None,
        opacity: int | float | None = None,
        outsidetextfont: None | None = None,
        parents: NDArray | None = None,
        parentssrc: str | None = None,
        pathbar: None | None = None,
        root: None | None = None,
        sort: bool | None = None,
        stream: None | None = None,
        text: NDArray | None = None,
        textfont: None | None = None,
        textinfo: Any | None = None,
        textposition: Any | None = None,
        textsrc: str | None = None,
        texttemplate: str | None = None,
        texttemplatesrc: str | None = None,
        tiling: None | None = None,
        uid: str | None = None,
        uirevision: Any | None = None,
        values: NDArray | None = None,
        valuessrc: str | None = None,
        visible: Any | None = None,
        **kwargs,
    ):
        """
        Construct a new Treemap object

        Visualize hierarchal data from leaves (and/or outer branches)
        towards root with rectangles. The treemap sectors are
        determined by the entries in "labels" or "ids" and in
        "parents".

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Treemap`
        branchvalues
            Determines how the items in `values` are summed. When
            set to "total", items in `values` are taken to be value
            of all its descendants. When set to "remainder", items
            in `values` corresponding to the root and the branches
            sectors are taken to be the extra part not part of the
            sum of the values at their leaves.
        count
            Determines default for `values` when it is not
            provided, by inferring a 1 for each of the "leaves"
            and/or "branches", otherwise 0.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        domain
            :class:`plotly.graph_objects.treemap.Domain` instance
            or dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.treemap.Hoverlabel`
            instance or dict with compatible properties
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
            are available. Finally, the template string has access
            to variables `currentPath`, `root`, `entry`,
            `percentRoot`, `percentEntry` and `percentParent`.
            Anything contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
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
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        labels
            Sets the labels of each of the sectors.
        labelssrc
            Sets the source reference on Chart Studio Cloud for
            `labels`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgrouptitle
            :class:`plotly.graph_objects.treemap.Legendgrouptitle`
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
        level
            Sets the level from which this trace hierarchy is
            rendered. Set `level` to `''` to start from the root
            node in the hierarchy. Must be an "id" if `ids` is
            filled in, otherwise plotly attempts to find a matching
            item in `labels`.
        marker
            :class:`plotly.graph_objects.treemap.Marker` instance
            or dict with compatible properties
        maxdepth
            Sets the number of rendered sectors from any given
            `level`. Set `maxdepth` to "-1" to render all the
            levels in the hierarchy.
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
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            sector. This option refers to the root of the hierarchy
            presented on top left corner of a treemap graph. Please
            note that if a hierarchy has multiple root nodes, this
            option won't have any effect and `insidetextfont` would
            be used.
        parents
            Sets the parent sectors for each of the sectors. Empty
            string items '' are understood to reference the root
            node in the hierarchy. If `ids` is filled, `parents`
            items are understood to be "ids" themselves. When `ids`
            is not set, plotly attempts to find matching items in
            `labels`, but beware they must be unique.
        parentssrc
            Sets the source reference on Chart Studio Cloud for
            `parents`.
        pathbar
            :class:`plotly.graph_objects.treemap.Pathbar` instance
            or dict with compatible properties
        root
            :class:`plotly.graph_objects.treemap.Root` instance or
            dict with compatible properties
        sort
            Determines whether or not the sectors are reordered
            from largest to smallest.
        stream
            :class:`plotly.graph_objects.treemap.Stream` instance
            or dict with compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Sets the positions of the `text` elements.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. Every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. Finally, the template string has access
            to variables `currentPath`, `root`, `entry`,
            `percentRoot`, `percentEntry`, `percentParent`, `label`
            and `value`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `texttemplate`.
        tiling
            :class:`plotly.graph_objects.treemap.Tiling` instance
            or dict with compatible properties
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
        values
            Sets the values associated with each of the sectors.
            Use with `branchvalues` to determine how the values are
            summed.
        valuessrc
            Sets the source reference on Chart Studio Cloud for
            `values`.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Treemap
        """
        super().__init__("treemap")
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
The first argument to the plotly.graph_objs.Treemap
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Treemap`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("branchvalues", arg, branchvalues)
        self._init_provided("count", arg, count)
        self._init_provided("customdata", arg, customdata)
        self._init_provided("customdatasrc", arg, customdatasrc)
        self._init_provided("domain", arg, domain)
        self._init_provided("hoverinfo", arg, hoverinfo)
        self._init_provided("hoverinfosrc", arg, hoverinfosrc)
        self._init_provided("hoverlabel", arg, hoverlabel)
        self._init_provided("hovertemplate", arg, hovertemplate)
        self._init_provided("hovertemplatesrc", arg, hovertemplatesrc)
        self._init_provided("hovertext", arg, hovertext)
        self._init_provided("hovertextsrc", arg, hovertextsrc)
        self._init_provided("ids", arg, ids)
        self._init_provided("idssrc", arg, idssrc)
        self._init_provided("insidetextfont", arg, insidetextfont)
        self._init_provided("labels", arg, labels)
        self._init_provided("labelssrc", arg, labelssrc)
        self._init_provided("legend", arg, legend)
        self._init_provided("legendgrouptitle", arg, legendgrouptitle)
        self._init_provided("legendrank", arg, legendrank)
        self._init_provided("legendwidth", arg, legendwidth)
        self._init_provided("level", arg, level)
        self._init_provided("marker", arg, marker)
        self._init_provided("maxdepth", arg, maxdepth)
        self._init_provided("meta", arg, meta)
        self._init_provided("metasrc", arg, metasrc)
        self._init_provided("name", arg, name)
        self._init_provided("opacity", arg, opacity)
        self._init_provided("outsidetextfont", arg, outsidetextfont)
        self._init_provided("parents", arg, parents)
        self._init_provided("parentssrc", arg, parentssrc)
        self._init_provided("pathbar", arg, pathbar)
        self._init_provided("root", arg, root)
        self._init_provided("sort", arg, sort)
        self._init_provided("stream", arg, stream)
        self._init_provided("text", arg, text)
        self._init_provided("textfont", arg, textfont)
        self._init_provided("textinfo", arg, textinfo)
        self._init_provided("textposition", arg, textposition)
        self._init_provided("textsrc", arg, textsrc)
        self._init_provided("texttemplate", arg, texttemplate)
        self._init_provided("texttemplatesrc", arg, texttemplatesrc)
        self._init_provided("tiling", arg, tiling)
        self._init_provided("uid", arg, uid)
        self._init_provided("uirevision", arg, uirevision)
        self._init_provided("values", arg, values)
        self._init_provided("valuessrc", arg, valuessrc)
        self._init_provided("visible", arg, visible)

        self._props["type"] = "treemap"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
