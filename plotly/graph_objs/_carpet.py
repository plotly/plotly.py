

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Carpet(_BaseTraceType):

    # class properties
    # --------------------
    _parent_path_str = ''
    _path_str = 'carpet'
    _valid_props = {"a", "a0", "aaxis", "asrc", "b", "b0", "baxis", "bsrc", "carpet", "cheaterslope", "color", "customdata", "customdatasrc", "da", "db", "font", "ids", "idssrc", "legend", "legendgrouptitle", "legendrank", "legendwidth", "meta", "metasrc", "name", "opacity", "stream", "type", "uid", "uirevision", "visible", "x", "xaxis", "xsrc", "y", "yaxis", "ysrc", "zorder"}

    # a
    # -
    @property
    def a(self):
        """
        An array containing values of the first parameter value

        The 'a' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self['a']

    @a.setter
    def a(self, val):
        self['a'] = val

    # a0
    # --
    @property
    def a0(self):
        """
        Alternate to `a`. Builds a linear space of a coordinates. Use
        with `da` where `a0` is the starting coordinate and `da` the
        step.

        The 'a0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['a0']

    @a0.setter
    def a0(self, val):
        self['a0'] = val

    # aaxis
    # -----
    @property
    def aaxis(self):
        """
        The 'aaxis' property is an instance of Aaxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.carpet.Aaxis`
          - A dict of string/value properties that will be passed
            to the Aaxis constructor

        Returns
        -------
        plotly.graph_objs.carpet.Aaxis
        """
        return self['aaxis']

    @aaxis.setter
    def aaxis(self, val):
        self['aaxis'] = val

    # asrc
    # ----
    @property
    def asrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `a`.

        The 'asrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['asrc']

    @asrc.setter
    def asrc(self, val):
        self['asrc'] = val

    # b
    # -
    @property
    def b(self):
        """
        A two dimensional array of y coordinates at each carpet point.

        The 'b' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self['b']

    @b.setter
    def b(self, val):
        self['b'] = val

    # b0
    # --
    @property
    def b0(self):
        """
        Alternate to `b`. Builds a linear space of a coordinates. Use
        with `db` where `b0` is the starting coordinate and `db` the
        step.

        The 'b0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['b0']

    @b0.setter
    def b0(self, val):
        self['b0'] = val

    # baxis
    # -----
    @property
    def baxis(self):
        """
        The 'baxis' property is an instance of Baxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.carpet.Baxis`
          - A dict of string/value properties that will be passed
            to the Baxis constructor

        Returns
        -------
        plotly.graph_objs.carpet.Baxis
        """
        return self['baxis']

    @baxis.setter
    def baxis(self, val):
        self['baxis'] = val

    # bsrc
    # ----
    @property
    def bsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `b`.

        The 'bsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['bsrc']

    @bsrc.setter
    def bsrc(self, val):
        self['bsrc'] = val

    # carpet
    # ------
    @property
    def carpet(self):
        """
        An identifier for this carpet, so that `scattercarpet` and
        `contourcarpet` traces can specify a carpet plot on which they
        lie

        The 'carpet' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['carpet']

    @carpet.setter
    def carpet(self, val):
        self['carpet'] = val

    # cheaterslope
    # ------------
    @property
    def cheaterslope(self):
        """
        The shift applied to each successive row of data in creating a
        cheater plot. Only used if `x` is been omitted.

        The 'cheaterslope' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cheaterslope']

    @cheaterslope.setter
    def cheaterslope(self, val):
        self['cheaterslope'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets default for all colors associated with this axis all at
        once: line, font, tick, and grid colors. Grid color is
        lightened by blending this with the plot background Individual
        pieces can override this.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # customdata
    # ----------
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
        return self['customdata']

    @customdata.setter
    def customdata(self, val):
        self['customdata'] = val

    # customdatasrc
    # -------------
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
        return self['customdatasrc']

    @customdatasrc.setter
    def customdatasrc(self, val):
        self['customdatasrc'] = val

    # da
    # --
    @property
    def da(self):
        """
        Sets the a coordinate step. See `a0` for more info.

        The 'da' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['da']

    @da.setter
    def da(self, val):
        self['da'] = val

    # db
    # --
    @property
    def db(self):
        """
        Sets the b coordinate step. See `b0` for more info.

        The 'db' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['db']

    @db.setter
    def db(self, val):
        self['db'] = val

    # font
    # ----
    @property
    def font(self):
        """
        The default font used for axis & tick labels on this carpet

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.carpet.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.carpet.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # ids
    # ---
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
        return self['ids']

    @ids.setter
    def ids(self, val):
        self['ids'] = val

    # idssrc
    # ------
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
        return self['idssrc']

    @idssrc.setter
    def idssrc(self, val):
        self['idssrc'] = val

    # legend
    # ------
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
        return self['legend']

    @legend.setter
    def legend(self, val):
        self['legend'] = val

    # legendgrouptitle
    # ----------------
    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.carpet.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

        Returns
        -------
        plotly.graph_objs.carpet.Legendgrouptitle
        """
        return self['legendgrouptitle']

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self['legendgrouptitle'] = val

    # legendrank
    # ----------
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
        return self['legendrank']

    @legendrank.setter
    def legendrank(self, val):
        self['legendrank'] = val

    # legendwidth
    # -----------
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
        return self['legendwidth']

    @legendwidth.setter
    def legendwidth(self, val):
        self['legendwidth'] = val

    # meta
    # ----
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
        return self['meta']

    @meta.setter
    def meta(self, val):
        self['meta'] = val

    # metasrc
    # -------
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
        return self['metasrc']

    @metasrc.setter
    def metasrc(self, val):
        self['metasrc'] = val

    # name
    # ----
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
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # opacity
    # -------
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
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.carpet.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

        Returns
        -------
        plotly.graph_objs.carpet.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # uid
    # ---
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
        return self['uid']

    @uid.setter
    def uid(self, val):
        self['uid'] = val

    # uirevision
    # ----------
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
        return self['uirevision']

    @uirevision.setter
    def uirevision(self, val):
        self['uirevision'] = val

    # visible
    # -------
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
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # x
    # -
    @property
    def x(self):
        """
        A two dimensional array of x coordinates at each carpet point.
        If omitted, the plot is a cheater plot and the xaxis is hidden
        by default.

        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xaxis
    # -----
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
        return self['xaxis']

    @xaxis.setter
    def xaxis(self, val):
        self['xaxis'] = val

    # xsrc
    # ----
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
        return self['xsrc']

    @xsrc.setter
    def xsrc(self, val):
        self['xsrc'] = val

    # y
    # -
    @property
    def y(self):
        """
        A two dimensional array of y coordinates at each carpet point.

        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yaxis
    # -----
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
        return self['yaxis']

    @yaxis.setter
    def yaxis(self, val):
        self['yaxis'] = val

    # ysrc
    # ----
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
        return self['ysrc']

    @ysrc.setter
    def ysrc(self, val):
        self['ysrc'] = val

    # zorder
    # ------
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
        return self['zorder']

    @zorder.setter
    def zorder(self, val):
        self['zorder'] = val

    # type
    # ----
    @property
    def type(self):
        return self._props['type']

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        a
            An array containing values of the first parameter value
        a0
            Alternate to `a`. Builds a linear space of a
            coordinates. Use with `da` where `a0` is the starting
            coordinate and `da` the step.
        aaxis
            :class:`plotly.graph_objects.carpet.Aaxis` instance or
            dict with compatible properties
        asrc
            Sets the source reference on Chart Studio Cloud for
            `a`.
        b
            A two dimensional array of y coordinates at each carpet
            point.
        b0
            Alternate to `b`. Builds a linear space of a
            coordinates. Use with `db` where `b0` is the starting
            coordinate and `db` the step.
        baxis
            :class:`plotly.graph_objects.carpet.Baxis` instance or
            dict with compatible properties
        bsrc
            Sets the source reference on Chart Studio Cloud for
            `b`.
        carpet
            An identifier for this carpet, so that `scattercarpet`
            and `contourcarpet` traces can specify a carpet plot on
            which they lie
        cheaterslope
            The shift applied to each successive row of data in
            creating a cheater plot. Only used if `x` is been
            omitted.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        da
            Sets the a coordinate step. See `a0` for more info.
        db
            Sets the b coordinate step. See `b0` for more info.
        font
            The default font used for axis & tick labels on this
            carpet
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgrouptitle
            :class:`plotly.graph_objects.carpet.Legendgrouptitle`
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
        stream
            :class:`plotly.graph_objects.carpet.Stream` instance or
            dict with compatible properties
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
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            A two dimensional array of x coordinates at each carpet
            point. If omitted, the plot is a cheater plot and the
            xaxis is hidden by default.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            A two dimensional array of y coordinates at each carpet
            point.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        zorder
            Sets the layer on which this trace is displayed,
            relative to other SVG traces on the same subplot. SVG
            traces with higher `zorder` appear in front of those
            with lower `zorder`.
        """
    def __init__(self,
            arg=None,
            a: NDArray|None = None,
            a0: int|float|None = None,
            aaxis: None|None = None,
            asrc: str|None = None,
            b: NDArray|None = None,
            b0: int|float|None = None,
            baxis: None|None = None,
            bsrc: str|None = None,
            carpet: str|None = None,
            cheaterslope: int|float|None = None,
            color: str|None = None,
            customdata: NDArray|None = None,
            customdatasrc: str|None = None,
            da: int|float|None = None,
            db: int|float|None = None,
            font: None|None = None,
            ids: NDArray|None = None,
            idssrc: str|None = None,
            legend: str|None = None,
            legendgrouptitle: None|None = None,
            legendrank: int|float|None = None,
            legendwidth: int|float|None = None,
            meta: Any|None = None,
            metasrc: str|None = None,
            name: str|None = None,
            opacity: int|float|None = None,
            stream: None|None = None,
            uid: str|None = None,
            uirevision: Any|None = None,
            visible: Any|None = None,
            x: NDArray|None = None,
            xaxis: str|None = None,
            xsrc: str|None = None,
            y: NDArray|None = None,
            yaxis: str|None = None,
            ysrc: str|None = None,
            zorder: int|None = None,
            **kwargs
        ):
        """
        Construct a new Carpet object

        The data describing carpet axis layout is set in `y` and
        (optionally) also `x`. If only `y` is present, `x` the plot is
        interpreted as a cheater plot and is filled in using the `y`
        values. `x` and `y` may either be 2D arrays matching with each
        dimension matching that of `a` and `b`, or they may be 1D
        arrays with total length equal to that of `a` and `b`.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Carpet`
        a
            An array containing values of the first parameter value
        a0
            Alternate to `a`. Builds a linear space of a
            coordinates. Use with `da` where `a0` is the starting
            coordinate and `da` the step.
        aaxis
            :class:`plotly.graph_objects.carpet.Aaxis` instance or
            dict with compatible properties
        asrc
            Sets the source reference on Chart Studio Cloud for
            `a`.
        b
            A two dimensional array of y coordinates at each carpet
            point.
        b0
            Alternate to `b`. Builds a linear space of a
            coordinates. Use with `db` where `b0` is the starting
            coordinate and `db` the step.
        baxis
            :class:`plotly.graph_objects.carpet.Baxis` instance or
            dict with compatible properties
        bsrc
            Sets the source reference on Chart Studio Cloud for
            `b`.
        carpet
            An identifier for this carpet, so that `scattercarpet`
            and `contourcarpet` traces can specify a carpet plot on
            which they lie
        cheaterslope
            The shift applied to each successive row of data in
            creating a cheater plot. Only used if `x` is been
            omitted.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        da
            Sets the a coordinate step. See `a0` for more info.
        db
            Sets the b coordinate step. See `b0` for more info.
        font
            The default font used for axis & tick labels on this
            carpet
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgrouptitle
            :class:`plotly.graph_objects.carpet.Legendgrouptitle`
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
        stream
            :class:`plotly.graph_objects.carpet.Stream` instance or
            dict with compatible properties
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
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            A two dimensional array of x coordinates at each carpet
            point. If omitted, the plot is a cheater plot and the
            xaxis is hidden by default.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            A two dimensional array of y coordinates at each carpet
            point.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
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
        Carpet
        """
        super().__init__('carpet')
        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
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
            raise ValueError("""\
The first argument to the plotly.graph_objs.Carpet
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Carpet`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('a', arg, a)
        self._init_provided('a0', arg, a0)
        self._init_provided('aaxis', arg, aaxis)
        self._init_provided('asrc', arg, asrc)
        self._init_provided('b', arg, b)
        self._init_provided('b0', arg, b0)
        self._init_provided('baxis', arg, baxis)
        self._init_provided('bsrc', arg, bsrc)
        self._init_provided('carpet', arg, carpet)
        self._init_provided('cheaterslope', arg, cheaterslope)
        self._init_provided('color', arg, color)
        self._init_provided('customdata', arg, customdata)
        self._init_provided('customdatasrc', arg, customdatasrc)
        self._init_provided('da', arg, da)
        self._init_provided('db', arg, db)
        self._init_provided('font', arg, font)
        self._init_provided('ids', arg, ids)
        self._init_provided('idssrc', arg, idssrc)
        self._init_provided('legend', arg, legend)
        self._init_provided('legendgrouptitle', arg, legendgrouptitle)
        self._init_provided('legendrank', arg, legendrank)
        self._init_provided('legendwidth', arg, legendwidth)
        self._init_provided('meta', arg, meta)
        self._init_provided('metasrc', arg, metasrc)
        self._init_provided('name', arg, name)
        self._init_provided('opacity', arg, opacity)
        self._init_provided('stream', arg, stream)
        self._init_provided('uid', arg, uid)
        self._init_provided('uirevision', arg, uirevision)
        self._init_provided('visible', arg, visible)
        self._init_provided('x', arg, x)
        self._init_provided('xaxis', arg, xaxis)
        self._init_provided('xsrc', arg, xsrc)
        self._init_provided('y', arg, y)
        self._init_provided('yaxis', arg, yaxis)
        self._init_provided('ysrc', arg, ysrc)
        self._init_provided('zorder', arg, zorder)

        # Read-only literals
        # ------------------

        self._props['type'] = 'carpet'
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
