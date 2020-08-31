import _plotly_utils.basevalidators


class ContourValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="contour", parent_name="", **kwargs):
        super(ContourValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Contour"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            autocontour
                Determines whether or not the contour level
                attributes are picked by an algorithm. If True,
                the number of contour levels can be set in
                `ncontours`. If False, set the contour level
                attributes in `contours`.
            coloraxis
                Sets a reference to a shared color axis.
                References to these shared color axes are
                "coloraxis", "coloraxis2", "coloraxis3", etc.
                Settings for these shared color axes are set in
                the layout, under `layout.coloraxis`,
                `layout.coloraxis2`, etc. Note that multiple
                color scales can be linked to the same color
                axis.
            colorbar
                :class:`plotly.graph_objects.contour.ColorBar`
                instance or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)'], [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`zmin` and
                `zmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the `z` data are filled in.
                It is defaulted to true if `z` is a one
                dimensional array otherwise it is defaulted to
                false.
            contours
                :class:`plotly.graph_objects.contour.Contours`
                instance or dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on Chart Studio Cloud
                for  customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            fillcolor
                Sets the fill color if `contours.type` is
                "constraint". Defaults to a half-transparent
                variant of the line color, marker color, or
                marker line color, whichever is available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on Chart Studio Cloud
                for  hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.contour.Hoverlabel
                ` instance or dict with compatible properties
            hoverongaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the `z` data have hover
                labels associated with them.
            hovertemplate
                Template string used for rendering the
                information that appear on hover box. Note that
                this will override `hoverinfo`. Variables are
                inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-time-
                format#locale_format for details on the date
                formatting syntax. The variables available in
                `hovertemplate` are the ones emitted as event
                data described at this link
                https://plotly.com/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on Chart Studio Cloud
                for  hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on Chart Studio Cloud
                for  hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on Chart Studio Cloud
                for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.contour.Line`
                instance or dict with compatible properties
            meta
                Assigns extra meta information associated with
                this trace that can be used in various text
                attributes. Attributes such as trace `name`,
                graph, axis and colorbar `title.text`,
                annotation `text` `rangeselector`,
                `updatemenues` and `sliders` `label` text all
                support `meta`. To access the trace `meta`
                values in an attribute in the same trace,
                simply use `%{meta[i]}` where `i` is the index
                or key of the `meta` item in question. To
                access trace `meta` in layout attributes, use
                `%{data[n[.meta[i]}` where `i` is the index or
                key of the `meta` and `n` is the trace index.
            metasrc
                Sets the source reference on Chart Studio Cloud
                for  meta .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            ncontours
                Sets the maximum number of contour levels. The
                actual number of contours will be chosen
                automatically to be less than or equal to the
                value of `ncontours`. Has an effect only if
                `autocontour` is True or if `contours.size` is
                missing.
            opacity
                Sets the opacity of the trace.
            reversescale
                Reverses the color mapping if true. If true,
                `zmin` will correspond to the last color in the
                array and `zmax` will correspond to the first
                color.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            stream
                :class:`plotly.graph_objects.contour.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with each z
                value.
            textsrc
                Sets the source reference on Chart Studio Cloud
                for  text .
            transpose
                Transposes the z data.
            uid
                Assign an id to this trace, Use this to provide
                object constancy between traces during
                animations and transitions.
            uirevision
                Controls persistence of some user-driven
                changes to the trace: `constraintrange` in
                `parcoords` traces, as well as some `editable:
                true` modifications such as `name` and
                `colorbar.title`. Defaults to
                `layout.uirevision`. Note that other user-
                driven trace attribute changes are controlled
                by `layout` attributes: `trace.visible` is
                controlled by `layout.legend.uirevision`,
                `selectedpoints` is controlled by
                `layout.selectionrevision`, and
                `colorbar.(x|y)` (accessible with `config:
                {editable: true}`) is controlled by
                `layout.editrevision`. Trace changes are
                tracked by `uid`, which only falls back on
                trace index if no `uid` is provided. So if your
                app can add/remove traces before the end of the
                `data` array, such that the same trace has a
                different index, you can still preserve user-
                driven changes if you give each trace a `uid`
                that stays with it as it moves.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the x coordinates.
            x0
                Alternate to `x`. Builds a linear space of x
                coordinates. Use with `dx` where `x0` is the
                starting coordinate and `dx` the step.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on Chart Studio Cloud
                for  x .
            xtype
                If "array", the heatmap's x coordinates are
                given by "x" (the default behavior when `x` is
                provided). If "scaled", the heatmap's x
                coordinates are given by "x0" and "dx" (the
                default behavior when `x` is not provided).
            y
                Sets the y coordinates.
            y0
                Alternate to `y`. Builds a linear space of y
                coordinates. Use with `dy` where `y0` is the
                starting coordinate and `dy` the step.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on Chart Studio Cloud
                for  y .
            ytype
                If "array", the heatmap's y coordinates are
                given by "y" (the default behavior when `y` is
                provided) If "scaled", the heatmap's y
                coordinates are given by "y0" and "dy" (the
                default behavior when `y` is not provided)
            z
                Sets the z data.
            zauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `z`) or the bounds set in `zmin` and `zmax`
                Defaults to `false` when `zmin` and `zmax` are
                set by the user.
            zhoverformat
                Sets the hover text formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. See:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
            zmax
                Sets the upper bound of the color domain. Value
                should have the same units as in `z` and if
                set, `zmin` must be set as well.
            zmid
                Sets the mid-point of the color domain by
                scaling `zmin` and/or `zmax` to be equidistant
                to this point. Value should have the same units
                as in `z`. Has no effect when `zauto` is
                `false`.
            zmin
                Sets the lower bound of the color domain. Value
                should have the same units as in `z` and if
                set, `zmax` must be set as well.
            zsrc
                Sets the source reference on Chart Studio Cloud
                for  z .
""",
            ),
            **kwargs
        )
