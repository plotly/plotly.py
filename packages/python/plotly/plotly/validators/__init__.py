import _plotly_utils.basevalidators


class LayoutValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="layout", parent_name="", **kwargs):
        super(LayoutValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Layout"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            angularaxis
                :class:`plotly.graph_objects.layout.AngularAxis
                ` instance or dict with compatible properties
            annotations
                A tuple of
                :class:`plotly.graph_objects.layout.Annotation`
                instances or dicts with compatible properties
            annotationdefaults
                When used in a template (as
                layout.template.layout.annotationdefaults),
                sets the default property values to use for
                elements of layout.annotations
            autosize
                Determines whether or not a layout width or
                height that has been left undefined by the user
                is initialized on each relayout. Note that,
                regardless of this attribute, an undefined
                layout width or height is always initialized on
                the first call to plot.
            bargap
                Sets the gap (in plot fraction) between bars of
                adjacent location coordinates.
            bargroupgap
                Sets the gap (in plot fraction) between bars of
                the same location coordinate.
            barmode
                Determines how bars at the same location
                coordinate are displayed on the graph. With
                "stack", the bars are stacked on top of one
                another With "relative", the bars are stacked
                on top of one another, with negative values
                below the axis, positive values above With
                "group", the bars are plotted next to one
                another centered around the shared location.
                With "overlay", the bars are plotted over one
                another, you might need to an "opacity" to see
                multiple bars.
            barnorm
                Sets the normalization for bar traces on the
                graph. With "fraction", the value of each bar
                is divided by the sum of all values at that
                location coordinate. "percent" is the same but
                multiplied by 100 to show percentages.
            boxgap
                Sets the gap (in plot fraction) between boxes
                of adjacent location coordinates. Has no effect
                on traces that have "width" set.
            boxgroupgap
                Sets the gap (in plot fraction) between boxes
                of the same location coordinate. Has no effect
                on traces that have "width" set.
            boxmode
                Determines how boxes at the same location
                coordinate are displayed on the graph. If
                "group", the boxes are plotted next to one
                another centered around the shared location. If
                "overlay", the boxes are plotted over one
                another, you might need to set "opacity" to see
                them multiple boxes. Has no effect on traces
                that have "width" set.
            calendar
                Sets the default calendar system to use for
                interpreting and displaying dates throughout
                the plot.
            clickmode
                Determines the mode of single click
                interactions. "event" is the default value and
                emits the `plotly_click` event. In addition
                this mode emits the `plotly_selected` event in
                drag modes "lasso" and "select", but with no
                event data attached (kept for compatibility
                reasons). The "select" flag enables selecting
                single data points via click. This mode also
                supports persistent selections, meaning that
                pressing Shift while clicking, adds to /
                subtracts from an existing selection. "select"
                with `hovermode`: "x" can be confusing,
                consider explicitly setting `hovermode`:
                "closest" when using this feature. Selection
                events are sent accordingly as long as "event"
                flag is set as well. When the "event" flag is
                missing, `plotly_click` and `plotly_selected`
                events are not fired.
            coloraxis
                :class:`plotly.graph_objects.layout.Coloraxis`
                instance or dict with compatible properties
            colorscale
                :class:`plotly.graph_objects.layout.Colorscale`
                instance or dict with compatible properties
            colorway
                Sets the default trace colors.
            datarevision
                If provided, a changed value tells
                `Plotly.react` that one or more data arrays has
                changed. This way you can modify arrays in-
                place rather than making a complete new copy
                for an incremental change. If NOT provided,
                `Plotly.react` assumes that data arrays are
                being treated as immutable, thus any data array
                with a different identity from its predecessor
                contains new data.
            direction
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the direction
                corresponding to positive angles in legacy
                polar charts.
            dragmode
                Determines the mode of drag interactions.
                "select" and "lasso" apply only to scatter
                traces with markers or text. "orbit" and
                "turntable" apply only to 3D scenes.
            editrevision
                Controls persistence of user-driven changes in
                `editable: true` configuration, other than
                trace names and axis titles. Defaults to
                `layout.uirevision`.
            extendfunnelareacolors
                If `true`, the funnelarea slice colors (whether
                given by `funnelareacolorway` or inherited from
                `colorway`) will be extended to three times its
                original length by first repeating every color
                20% lighter then each color 20% darker. This is
                intended to reduce the likelihood of reusing
                the same color when you have many slices, but
                you can set `false` to disable. Colors provided
                in the trace, using `marker.colors`, are never
                extended.
            extendpiecolors
                If `true`, the pie slice colors (whether given
                by `piecolorway` or inherited from `colorway`)
                will be extended to three times its original
                length by first repeating every color 20%
                lighter then each color 20% darker. This is
                intended to reduce the likelihood of reusing
                the same color when you have many slices, but
                you can set `false` to disable. Colors provided
                in the trace, using `marker.colors`, are never
                extended.
            extendsunburstcolors
                If `true`, the sunburst slice colors (whether
                given by `sunburstcolorway` or inherited from
                `colorway`) will be extended to three times its
                original length by first repeating every color
                20% lighter then each color 20% darker. This is
                intended to reduce the likelihood of reusing
                the same color when you have many slices, but
                you can set `false` to disable. Colors provided
                in the trace, using `marker.colors`, are never
                extended.
            extendtreemapcolors
                If `true`, the treemap slice colors (whether
                given by `treemapcolorway` or inherited from
                `colorway`) will be extended to three times its
                original length by first repeating every color
                20% lighter then each color 20% darker. This is
                intended to reduce the likelihood of reusing
                the same color when you have many slices, but
                you can set `false` to disable. Colors provided
                in the trace, using `marker.colors`, are never
                extended.
            font
                Sets the global font. Note that fonts used in
                traces and other layout components inherit from
                the global font.
            funnelareacolorway
                Sets the default funnelarea slice colors.
                Defaults to the main `colorway` used for trace
                colors. If you specify a new list here it can
                still be extended with lighter and darker
                colors, see `extendfunnelareacolors`.
            funnelgap
                Sets the gap (in plot fraction) between bars of
                adjacent location coordinates.
            funnelgroupgap
                Sets the gap (in plot fraction) between bars of
                the same location coordinate.
            funnelmode
                Determines how bars at the same location
                coordinate are displayed on the graph. With
                "stack", the bars are stacked on top of one
                another With "group", the bars are plotted next
                to one another centered around the shared
                location. With "overlay", the bars are plotted
                over one another, you might need to an
                "opacity" to see multiple bars.
            geo
                :class:`plotly.graph_objects.layout.Geo`
                instance or dict with compatible properties
            grid
                :class:`plotly.graph_objects.layout.Grid`
                instance or dict with compatible properties
            height
                Sets the plot's height (in px).
            hiddenlabels
                hiddenlabels is the funnelarea & pie chart
                analog of visible:'legendonly' but it can
                contain many labels, and can simultaneously
                hide slices from several pies/funnelarea charts
            hiddenlabelssrc
                Sets the source reference on plot.ly for
                hiddenlabels .
            hidesources
                Determines whether or not a text link citing
                the data source is placed at the bottom-right
                cored of the figure. Has only an effect only on
                graphs that have been generated via forked
                graphs from the plotly service (at
                https://plot.ly or on-premise).
            hoverdistance
                Sets the default distance (in pixels) to look
                for data to add hover labels (-1 means no
                cutoff, 0 means no looking for data). This is
                only a real distance for hovering on point-like
                objects, like scatter points. For area-like
                objects (bars, scatter fills, etc) hovering is
                on inside the area and off outside, but these
                objects will not supersede hover on point-like
                objects in case of conflict.
            hoverlabel
                :class:`plotly.graph_objects.layout.Hoverlabel`
                instance or dict with compatible properties
            hovermode
                Determines the mode of hover interactions. If
                `clickmode` includes the "select" flag,
                `hovermode` defaults to "closest". If
                `clickmode` lacks the "select" flag, it
                defaults to "x" or "y" (depending on the
                trace's `orientation` value) for plots based on
                cartesian coordinates. For anything else the
                default value is "closest".
            images
                A tuple of
                :class:`plotly.graph_objects.layout.Image`
                instances or dicts with compatible properties
            imagedefaults
                When used in a template (as
                layout.template.layout.imagedefaults), sets the
                default property values to use for elements of
                layout.images
            legend
                :class:`plotly.graph_objects.layout.Legend`
                instance or dict with compatible properties
            mapbox
                :class:`plotly.graph_objects.layout.Mapbox`
                instance or dict with compatible properties
            margin
                :class:`plotly.graph_objects.layout.Margin`
                instance or dict with compatible properties
            meta
                Assigns extra meta information that can be used
                in various `text` attributes. Attributes such
                as the graph, axis and colorbar `title.text`,
                annotation `text` `trace.name` in legend items,
                `rangeselector`, `updatemenus` and `sliders`
                `label` text all support `meta`. One can access
                `meta` fields using template strings:
                `%{meta[i]}` where `i` is the index of the
                `meta` item in question. `meta` can also be an
                object for example `{key: value}` which can be
                accessed %{meta[key]}.
            metasrc
                Sets the source reference on plot.ly for  meta
                .
            modebar
                :class:`plotly.graph_objects.layout.Modebar`
                instance or dict with compatible properties
            orientation
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Rotates the entire
                polar by the given angle in legacy polar
                charts.
            paper_bgcolor
                Sets the background color of the paper where
                the graph is drawn.
            piecolorway
                Sets the default pie slice colors. Defaults to
                the main `colorway` used for trace colors. If
                you specify a new list here it can still be
                extended with lighter and darker colors, see
                `extendpiecolors`.
            plot_bgcolor
                Sets the background color of the plotting area
                in-between x and y axes.
            polar
                :class:`plotly.graph_objects.layout.Polar`
                instance or dict with compatible properties
            radialaxis
                :class:`plotly.graph_objects.layout.RadialAxis`
                instance or dict with compatible properties
            scene
                :class:`plotly.graph_objects.layout.Scene`
                instance or dict with compatible properties
            selectdirection
                When "dragmode" is set to "select", this limits
                the selection of the drag to horizontal,
                vertical or diagonal. "h" only allows
                horizontal selection, "v" only vertical, "d"
                only diagonal and "any" sets no limit.
            selectionrevision
                Controls persistence of user-driven changes in
                selected points from all traces.
            separators
                Sets the decimal and thousand separators. For
                example, *. * puts a '.' before decimals and a
                space between thousands. In English locales,
                dflt is ".," but other locales may alter this
                default.
            shapes
                A tuple of
                :class:`plotly.graph_objects.layout.Shape`
                instances or dicts with compatible properties
            shapedefaults
                When used in a template (as
                layout.template.layout.shapedefaults), sets the
                default property values to use for elements of
                layout.shapes
            showlegend
                Determines whether or not a legend is drawn.
                Default is `true` if there is a trace to show
                and any of these: a) Two or more traces would
                by default be shown in the legend. b) One pie
                trace is shown in the legend. c) One trace is
                explicitly given with `showlegend: true`.
            sliders
                A tuple of
                :class:`plotly.graph_objects.layout.Slider`
                instances or dicts with compatible properties
            sliderdefaults
                When used in a template (as
                layout.template.layout.sliderdefaults), sets
                the default property values to use for elements
                of layout.sliders
            spikedistance
                Sets the default distance (in pixels) to look
                for data to draw spikelines to (-1 means no
                cutoff, 0 means no looking for data). As with
                hoverdistance, distance does not apply to area-
                like objects. In addition, some objects can be
                hovered on but will not generate spikelines,
                such as scatter fills.
            sunburstcolorway
                Sets the default sunburst slice colors.
                Defaults to the main `colorway` used for trace
                colors. If you specify a new list here it can
                still be extended with lighter and darker
                colors, see `extendsunburstcolors`.
            template
                Default attributes to be applied to the plot.
                This should be a dict with format: `{'layout':
                layoutTemplate, 'data': {trace_type:
                [traceTemplate, ...], ...}}` where
                `layoutTemplate` is a dict matching the
                structure of `figure.layout` and
                `traceTemplate` is a dict matching the
                structure of the trace with type `trace_type`
                (e.g. 'scatter'). Alternatively, this may be
                specified as an instance of
                plotly.graph_objs.layout.Template.  Trace
                templates are applied cyclically to traces of
                each type. Container arrays (eg `annotations`)
                have special handling: An object ending in
                `defaults` (eg `annotationdefaults`) is applied
                to each array item. But if an item has a
                `templateitemname` key we look in the template
                array for an item with matching `name` and
                apply that instead. If no matching `name` is
                found we mark the item invisible. Any named
                template item not referenced is appended to the
                end of the array, so this can be used to add a
                watermark annotation or a logo image, for
                example. To omit one of these items on the
                plot, make an item with matching
                `templateitemname` and `visible: false`.
            ternary
                :class:`plotly.graph_objects.layout.Ternary`
                instance or dict with compatible properties
            title
                :class:`plotly.graph_objects.layout.Title`
                instance or dict with compatible properties
            titlefont
                Deprecated: Please use layout.title.font
                instead. Sets the title font. Note that the
                title's font used to be customized by the now
                deprecated `titlefont` attribute.
            transition
                Sets transition options used during
                Plotly.react updates.
            treemapcolorway
                Sets the default treemap slice colors. Defaults
                to the main `colorway` used for trace colors.
                If you specify a new list here it can still be
                extended with lighter and darker colors, see
                `extendtreemapcolors`.
            uirevision
                Used to allow user interactions with the plot
                to persist after `Plotly.react` calls that are
                unaware of these interactions. If `uirevision`
                is omitted, or if it is given and it changed
                from the previous `Plotly.react` call, the
                exact new figure is used. If `uirevision` is
                truthy and did NOT change, any attribute that
                has been affected by user interactions and did
                not receive a different value in the new figure
                will keep the interaction value.
                `layout.uirevision` attribute serves as the
                default for `uirevision` attributes in various
                sub-containers. For finer control you can set
                these sub-attributes directly. For example, if
                your app separately controls the data on the x
                and y axes you might set
                `xaxis.uirevision=*time*` and
                `yaxis.uirevision=*cost*`. Then if only the y
                data is changed, you can update
                `yaxis.uirevision=*quantity*` and the y axis
                range will reset but the x axis range will
                retain any user-driven zoom.
            uniformtext
                :class:`plotly.graph_objects.layout.Uniformtext
                ` instance or dict with compatible properties
            updatemenus
                A tuple of
                :class:`plotly.graph_objects.layout.Updatemenu`
                instances or dicts with compatible properties
            updatemenudefaults
                When used in a template (as
                layout.template.layout.updatemenudefaults),
                sets the default property values to use for
                elements of layout.updatemenus
            violingap
                Sets the gap (in plot fraction) between violins
                of adjacent location coordinates. Has no effect
                on traces that have "width" set.
            violingroupgap
                Sets the gap (in plot fraction) between violins
                of the same location coordinate. Has no effect
                on traces that have "width" set.
            violinmode
                Determines how violins at the same location
                coordinate are displayed on the graph. If
                "group", the violins are plotted next to one
                another centered around the shared location. If
                "overlay", the violins are plotted over one
                another, you might need to set "opacity" to see
                them multiple violins. Has no effect on traces
                that have "width" set.
            waterfallgap
                Sets the gap (in plot fraction) between bars of
                adjacent location coordinates.
            waterfallgroupgap
                Sets the gap (in plot fraction) between bars of
                the same location coordinate.
            waterfallmode
                Determines how bars at the same location
                coordinate are displayed on the graph. With
                "group", the bars are plotted next to one
                another centered around the shared location.
                With "overlay", the bars are plotted over one
                another, you might need to an "opacity" to see
                multiple bars.
            width
                Sets the plot's width (in px).
            xaxis
                :class:`plotly.graph_objects.layout.XAxis`
                instance or dict with compatible properties
            yaxis
                :class:`plotly.graph_objects.layout.YAxis`
                instance or dict with compatible properties
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class WaterfallValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="waterfall", parent_name="", **kwargs):
        super(WaterfallValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Waterfall"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            alignmentgroup
                Set several traces linked to the same position
                axis or matching axes to the same
                alignmentgroup. This controls whether bars
                compute their positional range dependently or
                independently.
            base
                Sets where the bar base is drawn (in position
                axis units).
            cliponaxis
                Determines whether the text nodes are clipped
                about the subplot axes. To show the text nodes
                above axis lines and tick labels, make sure to
                set `xaxis.layer` and `yaxis.layer` to *below
                traces*.
            connector
                :class:`plotly.graph_objects.waterfall.Connecto
                r` instance or dict with compatible properties
            constraintext
                Constrain the size of text inside or outside a
                bar to be no larger than the bar itself.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            decreasing
                :class:`plotly.graph_objects.waterfall.Decreasi
                ng` instance or dict with compatible properties
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.waterfall.Hoverlab
                el` instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `initial`, `delta` and `final`.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (x,y) pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            increasing
                :class:`plotly.graph_objects.waterfall.Increasi
                ng` instance or dict with compatible properties
            insidetextanchor
                Determines if texts are kept at center or
                start/end points in `textposition` "inside"
                mode.
            insidetextfont
                Sets the font used for `text` lying inside the
                bar.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            measure
                An array containing types of values. By default
                the values are considered as 'relative'.
                However; it is possible to use 'total' to
                compute the sums. Also 'absolute' could be
                applied to reset the computed total or to
                declare an initial value where needed.
            measuresrc
                Sets the source reference on plot.ly for
                measure .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            offset
                Shifts the position where the bar is drawn (in
                position axis units). In "group" barmode,
                traces that set "offset" will be excluded and
                drawn in "overlay" mode instead.
            offsetgroup
                Set several traces linked to the same position
                axis or matching axes to the same offsetgroup
                where bars of the same position coordinate will
                line up.
            offsetsrc
                Sets the source reference on plot.ly for
                offset .
            opacity
                Sets the opacity of the trace.
            orientation
                Sets the orientation of the bars. With "v"
                ("h"), the value of the each bar spans along
                the vertical (horizontal).
            outsidetextfont
                Sets the font used for `text` lying outside the
                bar.
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.waterfall.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textangle
                Sets the angle of the tick labels with respect
                to the bar. For example, a `tickangle` of -90
                draws the tick labels vertically. With "auto"
                the texts may automatically be rotated to fit
                with the maximum size in bars.
            textfont
                Sets the font used for `text`.
            textinfo
                Determines which trace information appear on
                the graph. In the case of having multiple
                waterfalls, totals are computed separately (per
                trace).
            textposition
                Specifies the location of the `text`. "inside"
                positions `text` inside, next to the bar end
                (rotated and scaled if needed). "outside"
                positions `text` outside, next to the bar end
                (scaled if needed), unless there is another bar
                stacked on this one, then the text gets pushed
                inside. "auto" tries to position `text` inside
                the bar, but if the bar is too small and no bar
                is stacked on this one the text is moved
                outside.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `initial`, `delta`,
                `final` and `label`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
            totals
                :class:`plotly.graph_objects.waterfall.Totals`
                instance or dict with compatible properties
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
            width
                Sets the bar width (in position axis units).
            widthsrc
                Sets the source reference on plot.ly for  width
                .
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
            xsrc
                Sets the source reference on plot.ly for  x .
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
            ysrc
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class VolumeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="volume", parent_name="", **kwargs):
        super(VolumeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Volume"),
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
            caps
                :class:`plotly.graph_objects.volume.Caps`
                instance or dict with compatible properties
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                `value`) or the bounds set in `cmin` and `cmax`
                Defaults to `false` when `cmin` and `cmax` are
                set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as `value` and if
                set, `cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `cmin` and/or `cmax` to be equidistant
                to this point. Value should have the same units
                as `value`. Has no effect when `cauto` is
                `false`.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as `value` and if
                set, `cmax` must be set as well.
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
                :class:`plotly.graph_objects.volume.ColorBar`
                instance or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)'], [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            contour
                :class:`plotly.graph_objects.volume.Contour`
                instance or dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            flatshading
                Determines whether or not normal smoothing is
                applied to the meshes, creating meshes with an
                angular, low-poly look via flat reflections.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.volume.Hoverlabel`
                instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            isomax
                Sets the maximum boundary for iso-surface plot.
            isomin
                Sets the minimum boundary for iso-surface plot.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                :class:`plotly.graph_objects.volume.Lighting`
                instance or dict with compatible properties
            lightposition
                :class:`plotly.graph_objects.volume.Lightpositi
                on` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface. Please note
                that in the case of using high `opacity` values
                for example a value greater than or equal to
                0.5 on two surfaces (and 0.25 with four
                surfaces), an overlay of multiple transparent
                surfaces may not perfectly be sorted in depth
                by the webgl API. This behavior may be improved
                in the near future and is subject to change.
            opacityscale
                Sets the opacityscale. The opacityscale must be
                an array containing arrays mapping a normalized
                value to an opacity value. At minimum, a
                mapping for the lowest (0) and highest (1)
                values are required. For example, `[[0, 1],
                [0.5, 0.2], [1, 1]]` means that higher/lower
                values would have higher opacity values and
                those in the middle would be more transparent
                Alternatively, `opacityscale` may be a palette
                name string of the following list: 'min',
                'max', 'extremes' and 'uniform'. The default is
                'uniform'.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            slices
                :class:`plotly.graph_objects.volume.Slices`
                instance or dict with compatible properties
            spaceframe
                :class:`plotly.graph_objects.volume.Spaceframe`
                instance or dict with compatible properties
            stream
                :class:`plotly.graph_objects.volume.Stream`
                instance or dict with compatible properties
            surface
                :class:`plotly.graph_objects.volume.Surface`
                instance or dict with compatible properties
            text
                Sets the text elements associated with the
                vertices. If trace `hoverinfo` contains a
                "text" flag and "hovertext" is not set, these
                elements will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            value
                Sets the 4th dimension (value) of the vertices.
            valuesrc
                Sets the source reference on plot.ly for  value
                .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the X coordinates of the vertices on X
                axis.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the Y coordinates of the vertices on Y
                axis.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the Z coordinates of the vertices on Z
                axis.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ViolinValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="violin", parent_name="", **kwargs):
        super(ViolinValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Violin"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            alignmentgroup
                Set several traces linked to the same position
                axis or matching axes to the same
                alignmentgroup. This controls whether bars
                compute their positional range dependently or
                independently.
            bandwidth
                Sets the bandwidth used to compute the kernel
                density estimate. By default, the bandwidth is
                determined by Silverman's rule of thumb.
            box
                :class:`plotly.graph_objects.violin.Box`
                instance or dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.violin.Hoverlabel`
                instance or dict with compatible properties
            hoveron
                Do the hover effects highlight individual
                violins or sample points or the kernel density
                estimate or any combination of them?
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            jitter
                Sets the amount of jitter in the sample points
                drawn. If 0, the sample points align along the
                distribution axis. If 1, the sample points are
                drawn in a random jitter of width equal to the
                width of the violins.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.violin.Line`
                instance or dict with compatible properties
            marker
                :class:`plotly.graph_objects.violin.Marker`
                instance or dict with compatible properties
            meanline
                :class:`plotly.graph_objects.violin.Meanline`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover. For violin
                traces, the name will also be used for the
                position coordinate, if `x` and `x0` (`y` and
                `y0` if horizontal) are missing and the
                position axis is categorical. Note that the
                trace name is also used as a default value for
                attribute `scalegroup` (please see its
                description for details).
            offsetgroup
                Set several traces linked to the same position
                axis or matching axes to the same offsetgroup
                where bars of the same position coordinate will
                line up.
            opacity
                Sets the opacity of the trace.
            orientation
                Sets the orientation of the violin(s). If "v"
                ("h"), the distribution is visualized along the
                vertical (horizontal).
            pointpos
                Sets the position of the sample points in
                relation to the violins. If 0, the sample
                points are places over the center of the
                violins. Positive (negative) values correspond
                to positions to the right (left) for vertical
                violins and above (below) for horizontal
                violins.
            points
                If "outliers", only the sample points lying
                outside the whiskers are shown If
                "suspectedoutliers", the outlier points are
                shown and points either less than 4*Q1-3*Q3 or
                greater than 4*Q3-3*Q1 are highlighted (see
                `outliercolor`) If "all", all sample points are
                shown If False, only the violins are shown with
                no sample points. Defaults to
                "suspectedoutliers" when `marker.outliercolor`
                or `marker.line.outliercolor` is set, otherwise
                defaults to "outliers".
            scalegroup
                If there are multiple violins that should be
                sized according to to some metric (see
                `scalemode`), link them by providing a non-
                empty group id here shared by every trace in
                the same group. If a violin's `width` is
                undefined, `scalegroup` will default to the
                trace's name. In this case, violins with the
                same names will be linked together
            scalemode
                Sets the metric by which the width of each
                violin is determined."width" means each violin
                has the same (max) width*count* means the
                violins are scaled by the number of sample
                points makingup each violin.
            selected
                :class:`plotly.graph_objects.violin.Selected`
                instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            side
                Determines on which side of the position value
                the density function making up one half of a
                violin is plotted. Useful when comparing two
                violin traces under "overlay" mode, where one
                trace has `side` set to "positive" and the
                other to "negative".
            span
                Sets the span in data space for which the
                density function will be computed. Has an
                effect only when `spanmode` is set to "manual".
            spanmode
                Sets the method by which the span in data space
                where the density function will be computed.
                "soft" means the span goes from the sample's
                minimum value minus two bandwidths to the
                sample's maximum value plus two bandwidths.
                "hard" means the span goes from the sample's
                minimum to its maximum value. For custom span
                settings, use mode "manual" and fill in the
                `span` attribute.
            stream
                :class:`plotly.graph_objects.violin.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with each
                sample value. If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to the this trace's (x,y) coordinates. To be
                seen, trace `hoverinfo` must contain a "text"
                flag.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            unselected
                :class:`plotly.graph_objects.violin.Unselected`
                instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            width
                Sets the width of the violin in data
                coordinates. If 0 (default value) the width is
                automatically selected based on the positions
                of other violin traces in the same subplot.
            x
                Sets the x sample data or coordinates. See
                overview for more info.
            x0
                Sets the x coordinate for single-box traces or
                the starting coordinate for multi-box traces
                set using q1/median/q3. See overview for more
                info.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y sample data or coordinates. See
                overview for more info.
            y0
                Sets the y coordinate for single-box traces or
                the starting coordinate for multi-box traces
                set using q1/median/q3. See overview for more
                info.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            ysrc
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TreemapValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="treemap", parent_name="", **kwargs):
        super(TreemapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Treemap"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            branchvalues
                Determines how the items in `values` are
                summed. When set to "total", items in `values`
                are taken to be value of all its descendants.
                When set to "remainder", items in `values`
                corresponding to the root and the branches
                sectors are taken to be the extra part not part
                of the sum of the values at their leaves.
            count
                Determines default for `values` when it is not
                provided, by inferring a 1 for each of the
                "leaves" and/or "branches", otherwise 0.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            domain
                :class:`plotly.graph_objects.treemap.Domain`
                instance or dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.treemap.Hoverlabel
                ` instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `currentPath`, `root`, `entry`,
                `percentRoot`, `percentEntry` and
                `percentParent`. Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                sector. If a single string, the same string
                appears for all data points. If an array of
                string, the items are mapped in order of this
                trace's sectors. To be seen, trace `hoverinfo`
                must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            insidetextfont
                Sets the font used for `textinfo` lying inside
                the sector.
            labels
                Sets the labels of each of the sectors.
            labelssrc
                Sets the source reference on plot.ly for
                labels .
            level
                Sets the level from which this trace hierarchy
                is rendered. Set `level` to `''` to start from
                the root node in the hierarchy. Must be an "id"
                if `ids` is filled in, otherwise plotly
                attempts to find a matching item in `labels`.
            marker
                :class:`plotly.graph_objects.treemap.Marker`
                instance or dict with compatible properties
            maxdepth
                Sets the number of rendered sectors from any
                given `level`. Set `maxdepth` to "-1" to render
                all the levels in the hierarchy.
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            outsidetextfont
                Sets the font used for `textinfo` lying outside
                the sector. This option refers to the root of
                the hierarchy presented on top left corner of a
                treemap graph. Please note that if a hierarchy
                has multiple root nodes, this option won't have
                any effect and `insidetextfont` would be used.
            parents
                Sets the parent sectors for each of the
                sectors. Empty string items '' are understood
                to reference the root node in the hierarchy. If
                `ids` is filled, `parents` items are understood
                to be "ids" themselves. When `ids` is not set,
                plotly attempts to find matching items in
                `labels`, but beware they must be unique.
            parentssrc
                Sets the source reference on plot.ly for
                parents .
            pathbar
                :class:`plotly.graph_objects.treemap.Pathbar`
                instance or dict with compatible properties
            stream
                :class:`plotly.graph_objects.treemap.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each sector.
                If trace `textinfo` contains a "text" flag,
                these elements will be seen on the chart. If
                trace `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the font used for `textinfo`.
            textinfo
                Determines which trace information appear on
                the graph.
            textposition
                Sets the positions of the `text` elements.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `currentPath`, `root`,
                `entry`, `percentRoot`, `percentEntry`,
                `percentParent`, `label` and `value`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
            tiling
                :class:`plotly.graph_objects.treemap.Tiling`
                instance or dict with compatible properties
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
            values
                Sets the values associated with each of the
                sectors. Use with `branchvalues` to determine
                how the values are summed.
            valuessrc
                Sets the source reference on plot.ly for
                values .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TableValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="table", parent_name="", **kwargs):
        super(TableValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Table"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            cells
                :class:`plotly.graph_objects.table.Cells`
                instance or dict with compatible properties
            columnorder
                Specifies the rendered order of the data
                columns; for example, a value `2` at position
                `0` means that column index `0` in the data
                will be rendered as the third column, as
                columns have an index base of zero.
            columnordersrc
                Sets the source reference on plot.ly for
                columnorder .
            columnwidth
                The width of columns expressed as a ratio.
                Columns fill the available width in proportion
                of their specified column widths.
            columnwidthsrc
                Sets the source reference on plot.ly for
                columnwidth .
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            domain
                :class:`plotly.graph_objects.table.Domain`
                instance or dict with compatible properties
            header
                :class:`plotly.graph_objects.table.Header`
                instance or dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.table.Hoverlabel`
                instance or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            stream
                :class:`plotly.graph_objects.table.Stream`
                instance or dict with compatible properties
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
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SurfaceValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="surface", parent_name="", **kwargs):
        super(SurfaceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Surface"),
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
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here z
                or surfacecolor) or the bounds set in `cmin`
                and `cmax`  Defaults to `false` when `cmin` and
                `cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as z or surfacecolor
                and if set, `cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `cmin` and/or `cmax` to be equidistant
                to this point. Value should have the same units
                as z or surfacecolor. Has no effect when
                `cauto` is `false`.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as z or surfacecolor
                and if set, `cmax` must be set as well.
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
                :class:`plotly.graph_objects.surface.ColorBar`
                instance or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)'], [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the `z` data are filled in.
            contours
                :class:`plotly.graph_objects.surface.Contours`
                instance or dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            hidesurface
                Determines whether or not a surface is drawn.
                For example, set `hidesurface` to False
                `contours.x.show` to True and `contours.y.show`
                to True to draw a wire frame plot.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.surface.Hoverlabel
                ` instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                :class:`plotly.graph_objects.surface.Lighting`
                instance or dict with compatible properties
            lightposition
                :class:`plotly.graph_objects.surface.Lightposit
                ion` instance or dict with compatible
                properties
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface. Please note
                that in the case of using high `opacity` values
                for example a value greater than or equal to
                0.5 on two surfaces (and 0.25 with four
                surfaces), an overlay of multiple transparent
                surfaces may not perfectly be sorted in depth
                by the webgl API. This behavior may be improved
                in the near future and is subject to change.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            stream
                :class:`plotly.graph_objects.surface.Stream`
                instance or dict with compatible properties
            surfacecolor
                Sets the surface color values, used for setting
                a color scale independent of `z`.
            surfacecolorsrc
                Sets the source reference on plot.ly for
                surfacecolor .
            text
                Sets the text elements associated with each z
                value. If trace `hoverinfo` contains a "text"
                flag and "hovertext" is not set, these elements
                will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y coordinates.
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the z coordinates.
            zcalendar
                Sets the calendar system to use with `z` date
                data.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SunburstValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="sunburst", parent_name="", **kwargs):
        super(SunburstValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Sunburst"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            branchvalues
                Determines how the items in `values` are
                summed. When set to "total", items in `values`
                are taken to be value of all its descendants.
                When set to "remainder", items in `values`
                corresponding to the root and the branches
                sectors are taken to be the extra part not part
                of the sum of the values at their leaves.
            count
                Determines default for `values` when it is not
                provided, by inferring a 1 for each of the
                "leaves" and/or "branches", otherwise 0.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            domain
                :class:`plotly.graph_objects.sunburst.Domain`
                instance or dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.sunburst.Hoverlabe
                l` instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `currentPath`, `root`, `entry`,
                `percentRoot`, `percentEntry` and
                `percentParent`. Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                sector. If a single string, the same string
                appears for all data points. If an array of
                string, the items are mapped in order of this
                trace's sectors. To be seen, trace `hoverinfo`
                must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            insidetextfont
                Sets the font used for `textinfo` lying inside
                the sector.
            insidetextorientation
                Controls the orientation of the text inside
                chart sectors. When set to "auto", text may be
                oriented in any direction in order to be as big
                as possible in the middle of a sector. The
                "horizontal" option orients text to be parallel
                with the bottom of the chart, and may make text
                smaller in order to achieve that goal. The
                "radial" option orients text along the radius
                of the sector. The "tangential" option orients
                text perpendicular to the radius of the sector.
            labels
                Sets the labels of each of the sectors.
            labelssrc
                Sets the source reference on plot.ly for
                labels .
            leaf
                :class:`plotly.graph_objects.sunburst.Leaf`
                instance or dict with compatible properties
            level
                Sets the level from which this trace hierarchy
                is rendered. Set `level` to `''` to start from
                the root node in the hierarchy. Must be an "id"
                if `ids` is filled in, otherwise plotly
                attempts to find a matching item in `labels`.
            marker
                :class:`plotly.graph_objects.sunburst.Marker`
                instance or dict with compatible properties
            maxdepth
                Sets the number of rendered sectors from any
                given `level`. Set `maxdepth` to "-1" to render
                all the levels in the hierarchy.
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            outsidetextfont
                Sets the font used for `textinfo` lying outside
                the sector. This option refers to the root of
                the hierarchy presented at the center of a
                sunburst graph. Please note that if a hierarchy
                has multiple root nodes, this option won't have
                any effect and `insidetextfont` would be used.
            parents
                Sets the parent sectors for each of the
                sectors. Empty string items '' are understood
                to reference the root node in the hierarchy. If
                `ids` is filled, `parents` items are understood
                to be "ids" themselves. When `ids` is not set,
                plotly attempts to find matching items in
                `labels`, but beware they must be unique.
            parentssrc
                Sets the source reference on plot.ly for
                parents .
            stream
                :class:`plotly.graph_objects.sunburst.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each sector.
                If trace `textinfo` contains a "text" flag,
                these elements will be seen on the chart. If
                trace `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the font used for `textinfo`.
            textinfo
                Determines which trace information appear on
                the graph.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `currentPath`, `root`,
                `entry`, `percentRoot`, `percentEntry`,
                `percentParent`, `label` and `value`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
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
            values
                Sets the values associated with each of the
                sectors. Use with `branchvalues` to determine
                how the values are summed.
            valuessrc
                Sets the source reference on plot.ly for
                values .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class StreamtubeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="streamtube", parent_name="", **kwargs):
        super(StreamtubeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Streamtube"),
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
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                u/v/w norm) or the bounds set in `cmin` and
                `cmax`  Defaults to `false` when `cmin` and
                `cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as u/v/w norm and if
                set, `cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `cmin` and/or `cmax` to be equidistant
                to this point. Value should have the same units
                as u/v/w norm. Has no effect when `cauto` is
                `false`.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as u/v/w norm and if
                set, `cmax` must be set as well.
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
                :class:`plotly.graph_objects.streamtube.ColorBa
                r` instance or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)'], [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.streamtube.Hoverla
                bel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `tubex`, `tubey`, `tubez`, `tubeu`,
                `tubev`, `tubew`, `norm` and `divergence`.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                :class:`plotly.graph_objects.streamtube.Lightin
                g` instance or dict with compatible properties
            lightposition
                :class:`plotly.graph_objects.streamtube.Lightpo
                sition` instance or dict with compatible
                properties
            maxdisplayed
                The maximum number of displayed segments in a
                streamtube.
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface. Please note
                that in the case of using high `opacity` values
                for example a value greater than or equal to
                0.5 on two surfaces (and 0.25 with four
                surfaces), an overlay of multiple transparent
                surfaces may not perfectly be sorted in depth
                by the webgl API. This behavior may be improved
                in the near future and is subject to change.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            sizeref
                The scaling factor for the streamtubes. The
                default is 1, which avoids two max divergence
                tubes from touching at adjacent starting
                positions.
            starts
                :class:`plotly.graph_objects.streamtube.Starts`
                instance or dict with compatible properties
            stream
                :class:`plotly.graph_objects.streamtube.Stream`
                instance or dict with compatible properties
            text
                Sets a text element associated with this trace.
                If trace `hoverinfo` contains a "text" flag,
                this text element will be seen in all hover
                labels. Note that streamtube traces do not
                support array `text` values.
            u
                Sets the x components of the vector field.
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
            usrc
                Sets the source reference on plot.ly for  u .
            v
                Sets the y components of the vector field.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            vsrc
                Sets the source reference on plot.ly for  v .
            w
                Sets the z components of the vector field.
            wsrc
                Sets the source reference on plot.ly for  w .
            x
                Sets the x coordinates of the vector field.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y coordinates of the vector field.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the z coordinates of the vector field.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SplomValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="splom", parent_name="", **kwargs):
        super(SplomValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Splom"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            diagonal
                :class:`plotly.graph_objects.splom.Diagonal`
                instance or dict with compatible properties
            dimensions
                A tuple of
                :class:`plotly.graph_objects.splom.Dimension`
                instances or dicts with compatible properties
            dimensiondefaults
                When used in a template (as
                layout.template.data.splom.dimensiondefaults),
                sets the default property values to use for
                elements of splom.dimensions
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.splom.Hoverlabel`
                instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.splom.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                :class:`plotly.graph_objects.splom.Selected`
                instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showlowerhalf
                Determines whether or not subplots on the lower
                half from the diagonal are displayed.
            showupperhalf
                Determines whether or not subplots on the upper
                half from the diagonal are displayed.
            stream
                :class:`plotly.graph_objects.splom.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each (x,y)
                pair to appear on hover. If a single string,
                the same string appears over all the data
                points. If an array of string, the items are
                mapped in order to the this trace's (x,y)
                coordinates.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            unselected
                :class:`plotly.graph_objects.splom.Unselected`
                instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            xaxes
                Sets the list of x axes corresponding to
                dimensions of this splom trace. By default, a
                splom will match the first N xaxes where N is
                the number of input dimensions. Note that, in
                case where `diagonal.visible` is false and
                `showupperhalf` or `showlowerhalf` is false,
                this splom trace will generate one less x-axis
                and one less y-axis.
            yaxes
                Sets the list of y axes corresponding to
                dimensions of this splom trace. By default, a
                splom will match the first N yaxes where N is
                the number of input dimensions. Note that, in
                case where `diagonal.visible` is false and
                `showupperhalf` or `showlowerhalf` is false,
                this splom trace will generate one less x-axis
                and one less y-axis.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScatterternaryValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scatterternary", parent_name="", **kwargs):
        super(ScatterternaryValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatterternary"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            a
                Sets the quantity of component `a` in each data
                point. If `a`, `b`, and `c` are all provided,
                they need not be normalized, only the relative
                values matter. If only two arrays are provided
                they must be normalized to match
                `ternary<i>.sum`.
            asrc
                Sets the source reference on plot.ly for  a .
            b
                Sets the quantity of component `a` in each data
                point. If `a`, `b`, and `c` are all provided,
                they need not be normalized, only the relative
                values matter. If only two arrays are provided
                they must be normalized to match
                `ternary<i>.sum`.
            bsrc
                Sets the source reference on plot.ly for  b .
            c
                Sets the quantity of component `a` in each data
                point. If `a`, `b`, and `c` are all provided,
                they need not be normalized, only the relative
                values matter. If only two arrays are provided
                they must be normalized to match
                `ternary<i>.sum`.
            cliponaxis
                Determines whether or not markers and text
                nodes are clipped about the subplot axes. To
                show markers and text nodes above axis lines
                and tick labels, make sure to set `xaxis.layer`
                and `yaxis.layer` to *below traces*.
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            csrc
                Sets the source reference on plot.ly for  c .
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". scatterternary
                has a subset of the options available to
                scatter. "toself" connects the endpoints of the
                trace (or each segment of the trace if it has
                gaps) into a closed shape. "tonext" fills the
                space between two traces if one completely
                encloses the other (eg consecutive contour
                lines), and behaves like "toself" if there is
                no trace before it. "tonext" should not be used
                if one trace does not enclose the other.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scatterternary.Hov
                erlabel` instance or dict with compatible
                properties
            hoveron
                Do the hover effects highlight individual
                points (markers or line points) or do they
                highlight filled regions? If the fill is
                "toself" or "tonext" and there are no markers
                or text, then the default is "fills", otherwise
                it is "points".
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (a,b,c) point. If a single string, the same
                string appears over all the data points. If an
                array of strings, the items are mapped in order
                to the the data points in (a,b,c). To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scatterternary.Lin
                e` instance or dict with compatible properties
            marker
                :class:`plotly.graph_objects.scatterternary.Mar
                ker` instance or dict with compatible
                properties
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                :class:`plotly.graph_objects.scatterternary.Sel
                ected` instance or dict with compatible
                properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scatterternary.Str
                eam` instance or dict with compatible
                properties
            subplot
                Sets a reference between this trace's data
                coordinates and a ternary subplot. If "ternary"
                (the default value), the data refer to
                `layout.ternary`. If "ternary2", the data refer
                to `layout.ternary2`, and so on.
            sum
                The number each triplet should sum to, if only
                two of `a`, `b`, and `c` are provided. This
                overrides `ternary<i>.sum` to normalize this
                specific trace, but does not affect the values
                displayed on the axes. 0 (or missing) means to
                use ternary<i>.sum
            text
                Sets text elements associated with each (a,b,c)
                point. If a single string, the same string
                appears over all the data points. If an array
                of strings, the items are mapped in order to
                the the data points in (a,b,c). If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the text font.
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `a`, `b`, `c` and `text`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
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
            unselected
                :class:`plotly.graph_objects.scatterternary.Uns
                elected` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScatterpolarglValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scatterpolargl", parent_name="", **kwargs):
        super(ScatterpolarglValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatterpolargl"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dr
                Sets the r coordinate step.
            dtheta
                Sets the theta coordinate step. By default, the
                `dtheta` step equals the subplot's period
                divided by the length of the `r` coordinates.
            fill
                Sets the area to fill with a solid color.
                Defaults to "none" unless this trace is
                stacked, then it gets "tonexty" ("tonextx") if
                `orientation` is "v" ("h") Use with `fillcolor`
                if not "none". "tozerox" and "tozeroy" fill to
                x=0 and y=0 respectively. "tonextx" and
                "tonexty" fill between the endpoints of this
                trace and the endpoints of the trace before it,
                connecting those endpoints with straight lines
                (to make a stacked area graph); if there is no
                trace before it, they behave like "tozerox" and
                "tozeroy". "toself" connects the endpoints of
                the trace (or each segment of the trace if it
                has gaps) into a closed shape. "tonext" fills
                the space between two traces if one completely
                encloses the other (eg consecutive contour
                lines), and behaves like "toself" if there is
                no trace before it. "tonext" should not be used
                if one trace does not enclose the other. Traces
                in a `stackgroup` will only fill to (or be
                filled to) other traces in the same group. With
                multiple `stackgroup`s or some traces stacked
                and some not, if fill-linked traces are not
                already consecutive, the later ones will be
                pushed down in the drawing order.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scatterpolargl.Hov
                erlabel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (x,y) pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scatterpolargl.Lin
                e` instance or dict with compatible properties
            marker
                :class:`plotly.graph_objects.scatterpolargl.Mar
                ker` instance or dict with compatible
                properties
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            r
                Sets the radial coordinates
            r0
                Alternate to `r`. Builds a linear space of r
                coordinates. Use with `dr` where `r0` is the
                starting coordinate and `dr` the step.
            rsrc
                Sets the source reference on plot.ly for  r .
            selected
                :class:`plotly.graph_objects.scatterpolargl.Sel
                ected` instance or dict with compatible
                properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scatterpolargl.Str
                eam` instance or dict with compatible
                properties
            subplot
                Sets a reference between this trace's data
                coordinates and a polar subplot. If "polar"
                (the default value), the data refer to
                `layout.polar`. If "polar2", the data refer to
                `layout.polar2`, and so on.
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the text font.
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `r`, `theta` and `text`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
            theta
                Sets the angular coordinates
            theta0
                Alternate to `theta`. Builds a linear space of
                theta coordinates. Use with `dtheta` where
                `theta0` is the starting coordinate and
                `dtheta` the step.
            thetasrc
                Sets the source reference on plot.ly for  theta
                .
            thetaunit
                Sets the unit of input "theta" values. Has an
                effect only when on "linear" angular axes.
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
            unselected
                :class:`plotly.graph_objects.scatterpolargl.Uns
                elected` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScatterpolarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scatterpolar", parent_name="", **kwargs):
        super(ScatterpolarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatterpolar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            cliponaxis
                Determines whether or not markers and text
                nodes are clipped about the subplot axes. To
                show markers and text nodes above axis lines
                and tick labels, make sure to set `xaxis.layer`
                and `yaxis.layer` to *below traces*.
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dr
                Sets the r coordinate step.
            dtheta
                Sets the theta coordinate step. By default, the
                `dtheta` step equals the subplot's period
                divided by the length of the `r` coordinates.
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". scatterpolar
                has a subset of the options available to
                scatter. "toself" connects the endpoints of the
                trace (or each segment of the trace if it has
                gaps) into a closed shape. "tonext" fills the
                space between two traces if one completely
                encloses the other (eg consecutive contour
                lines), and behaves like "toself" if there is
                no trace before it. "tonext" should not be used
                if one trace does not enclose the other.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scatterpolar.Hover
                label` instance or dict with compatible
                properties
            hoveron
                Do the hover effects highlight individual
                points (markers or line points) or do they
                highlight filled regions? If the fill is
                "toself" or "tonext" and there are no markers
                or text, then the default is "fills", otherwise
                it is "points".
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (x,y) pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scatterpolar.Line`
                instance or dict with compatible properties
            marker
                :class:`plotly.graph_objects.scatterpolar.Marke
                r` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            r
                Sets the radial coordinates
            r0
                Alternate to `r`. Builds a linear space of r
                coordinates. Use with `dr` where `r0` is the
                starting coordinate and `dr` the step.
            rsrc
                Sets the source reference on plot.ly for  r .
            selected
                :class:`plotly.graph_objects.scatterpolar.Selec
                ted` instance or dict with compatible
                properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scatterpolar.Strea
                m` instance or dict with compatible properties
            subplot
                Sets a reference between this trace's data
                coordinates and a polar subplot. If "polar"
                (the default value), the data refer to
                `layout.polar`. If "polar2", the data refer to
                `layout.polar2`, and so on.
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the text font.
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `r`, `theta` and `text`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
            theta
                Sets the angular coordinates
            theta0
                Alternate to `theta`. Builds a linear space of
                theta coordinates. Use with `dtheta` where
                `theta0` is the starting coordinate and
                `dtheta` the step.
            thetasrc
                Sets the source reference on plot.ly for  theta
                .
            thetaunit
                Sets the unit of input "theta" values. Has an
                effect only when on "linear" angular axes.
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
            unselected
                :class:`plotly.graph_objects.scatterpolar.Unsel
                ected` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScattermapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattermapbox", parent_name="", **kwargs):
        super(ScattermapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattermapbox"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            below
                Determines if this scattermapbox trace's layers
                are to be inserted before the layer with the
                specified ID. By default, scattermapbox layers
                are inserted above all the base layers. To
                place the scattermapbox layers above every
                other layer, set `below` to "''".
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". "toself"
                connects the endpoints of the trace (or each
                segment of the trace if it has gaps) into a
                closed shape.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scattermapbox.Hove
                rlabel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (lon,lat) pair If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to the this trace's (lon,lat) coordinates. To
                be seen, trace `hoverinfo` must contain a
                "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            lat
                Sets the latitude coordinates (in degrees
                North).
            latsrc
                Sets the source reference on plot.ly for  lat .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scattermapbox.Line
                ` instance or dict with compatible properties
            lon
                Sets the longitude coordinates (in degrees
                East).
            lonsrc
                Sets the source reference on plot.ly for  lon .
            marker
                :class:`plotly.graph_objects.scattermapbox.Mark
                er` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover.
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                :class:`plotly.graph_objects.scattermapbox.Sele
                cted` instance or dict with compatible
                properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scattermapbox.Stre
                am` instance or dict with compatible properties
            subplot
                Sets a reference between this trace's data
                coordinates and a mapbox subplot. If "mapbox"
                (the default value), the data refer to
                `layout.mapbox`. If "mapbox2", the data refer
                to `layout.mapbox2`, and so on.
            text
                Sets text elements associated with each
                (lon,lat) pair If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to the this trace's (lon,lat) coordinates. If
                trace `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the icon text font
                (color=mapbox.layer.paint.text-color,
                size=mapbox.layer.layout.text-size). Has an
                effect only when `type` is set to "symbol".
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `lat`, `lon` and `text`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
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
            unselected
                :class:`plotly.graph_objects.scattermapbox.Unse
                lected` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScatterglValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattergl", parent_name="", **kwargs):
        super(ScatterglValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattergl"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            error_x
                :class:`plotly.graph_objects.scattergl.ErrorX`
                instance or dict with compatible properties
            error_y
                :class:`plotly.graph_objects.scattergl.ErrorY`
                instance or dict with compatible properties
            fill
                Sets the area to fill with a solid color.
                Defaults to "none" unless this trace is
                stacked, then it gets "tonexty" ("tonextx") if
                `orientation` is "v" ("h") Use with `fillcolor`
                if not "none". "tozerox" and "tozeroy" fill to
                x=0 and y=0 respectively. "tonextx" and
                "tonexty" fill between the endpoints of this
                trace and the endpoints of the trace before it,
                connecting those endpoints with straight lines
                (to make a stacked area graph); if there is no
                trace before it, they behave like "tozerox" and
                "tozeroy". "toself" connects the endpoints of
                the trace (or each segment of the trace if it
                has gaps) into a closed shape. "tonext" fills
                the space between two traces if one completely
                encloses the other (eg consecutive contour
                lines), and behaves like "toself" if there is
                no trace before it. "tonext" should not be used
                if one trace does not enclose the other. Traces
                in a `stackgroup` will only fill to (or be
                filled to) other traces in the same group. With
                multiple `stackgroup`s or some traces stacked
                and some not, if fill-linked traces are not
                already consecutive, the later ones will be
                pushed down in the drawing order.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scattergl.Hoverlab
                el` instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (x,y) pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scattergl.Line`
                instance or dict with compatible properties
            marker
                :class:`plotly.graph_objects.scattergl.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace.
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                :class:`plotly.graph_objects.scattergl.Selected
                ` instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scattergl.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the text font.
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
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
            unselected
                :class:`plotly.graph_objects.scattergl.Unselect
                ed` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  x .
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
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScattergeoValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattergeo", parent_name="", **kwargs):
        super(ScattergeoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattergeo"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            featureidkey
                Sets the key in GeoJSON features which is used
                as id to match the items included in the
                `locations` array. Only has an effect when
                `geojson` is set. Support nested property, for
                example "properties.name".
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". "toself"
                connects the endpoints of the trace (or each
                segment of the trace if it has gaps) into a
                closed shape.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            geo
                Sets a reference between this trace's
                geospatial coordinates and a geographic map. If
                "geo" (the default value), the geospatial
                coordinates refer to `layout.geo`. If "geo2",
                the geospatial coordinates refer to
                `layout.geo2`, and so on.
            geojson
                Sets optional GeoJSON data associated with this
                trace. If not given, the features on the base
                map are used when `locations` is set. It can be
                set as a valid GeoJSON object or as a URL
                string. Note that we only accept GeoJSONs of
                type "FeatureCollection" or "Feature" with
                geometries of type "Polygon" or "MultiPolygon".
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scattergeo.Hoverla
                bel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (lon,lat) pair or item in `locations`. If a
                single string, the same string appears over all
                the data points. If an array of string, the
                items are mapped in order to the this trace's
                (lon,lat) or `locations` coordinates. To be
                seen, trace `hoverinfo` must contain a "text"
                flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            lat
                Sets the latitude coordinates (in degrees
                North).
            latsrc
                Sets the source reference on plot.ly for  lat .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scattergeo.Line`
                instance or dict with compatible properties
            locationmode
                Determines the set of locations used to match
                entries in `locations` to regions on the map.
                Values "ISO-3", "USA-states", *country names*
                correspond to features on the base map and
                value "geojson-id" corresponds to features from
                a custom GeoJSON linked to the `geojson`
                attribute.
            locations
                Sets the coordinates via location IDs or names.
                Coordinates correspond to the centroid of each
                location given. See `locationmode` for more
                info.
            locationssrc
                Sets the source reference on plot.ly for
                locations .
            lon
                Sets the longitude coordinates (in degrees
                East).
            lonsrc
                Sets the source reference on plot.ly for  lon .
            marker
                :class:`plotly.graph_objects.scattergeo.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                :class:`plotly.graph_objects.scattergeo.Selecte
                d` instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scattergeo.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each
                (lon,lat) pair or item in `locations`. If a
                single string, the same string appears over all
                the data points. If an array of string, the
                items are mapped in order to the this trace's
                (lon,lat) or `locations` coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the text font.
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `lat`, `lon`, `location`
                and `text`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
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
            unselected
                :class:`plotly.graph_objects.scattergeo.Unselec
                ted` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScattercarpetValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattercarpet", parent_name="", **kwargs):
        super(ScattercarpetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattercarpet"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            a
                Sets the a-axis coordinates.
            asrc
                Sets the source reference on plot.ly for  a .
            b
                Sets the b-axis coordinates.
            bsrc
                Sets the source reference on plot.ly for  b .
            carpet
                An identifier for this carpet, so that
                `scattercarpet` and `contourcarpet` traces can
                specify a carpet plot on which they lie
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". scatterternary
                has a subset of the options available to
                scatter. "toself" connects the endpoints of the
                trace (or each segment of the trace if it has
                gaps) into a closed shape. "tonext" fills the
                space between two traces if one completely
                encloses the other (eg consecutive contour
                lines), and behaves like "toself" if there is
                no trace before it. "tonext" should not be used
                if one trace does not enclose the other.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scattercarpet.Hove
                rlabel` instance or dict with compatible
                properties
            hoveron
                Do the hover effects highlight individual
                points (markers or line points) or do they
                highlight filled regions? If the fill is
                "toself" or "tonext" and there are no markers
                or text, then the default is "fills", otherwise
                it is "points".
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (a,b) point. If a single string, the same
                string appears over all the data points. If an
                array of strings, the items are mapped in order
                to the the data points in (a,b). To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scattercarpet.Line
                ` instance or dict with compatible properties
            marker
                :class:`plotly.graph_objects.scattercarpet.Mark
                er` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                :class:`plotly.graph_objects.scattercarpet.Sele
                cted` instance or dict with compatible
                properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scattercarpet.Stre
                am` instance or dict with compatible properties
            text
                Sets text elements associated with each (a,b)
                point. If a single string, the same string
                appears over all the data points. If an array
                of strings, the items are mapped in order to
                the the data points in (a,b). If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the text font.
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `a`, `b` and `text`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
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
            unselected
                :class:`plotly.graph_objects.scattercarpet.Unse
                lected` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class Scatter3dValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scatter3d", parent_name="", **kwargs):
        super(Scatter3dValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatter3d"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            error_x
                :class:`plotly.graph_objects.scatter3d.ErrorX`
                instance or dict with compatible properties
            error_y
                :class:`plotly.graph_objects.scatter3d.ErrorY`
                instance or dict with compatible properties
            error_z
                :class:`plotly.graph_objects.scatter3d.ErrorZ`
                instance or dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scatter3d.Hoverlab
                el` instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets text elements associated with each (x,y,z)
                triplet. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y,z) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scatter3d.Line`
                instance or dict with compatible properties
            marker
                :class:`plotly.graph_objects.scatter3d.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            projection
                :class:`plotly.graph_objects.scatter3d.Projecti
                on` instance or dict with compatible properties
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scatter3d.Stream`
                instance or dict with compatible properties
            surfaceaxis
                If "-1", the scatter points are not fill with a
                surface If 0, 1, 2, the scatter points are
                filled with a Delaunay surface about the x, y,
                z respectively.
            surfacecolor
                Sets the surface fill color.
            text
                Sets text elements associated with each (x,y,z)
                triplet. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y,z) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                :class:`plotly.graph_objects.scatter3d.Textfont
                ` instance or dict with compatible properties
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
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
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y coordinates.
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the z coordinates.
            zcalendar
                Sets the calendar system to use with `z` date
                data.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScatterValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scatter", parent_name="", **kwargs):
        super(ScatterValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatter"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            cliponaxis
                Determines whether or not markers and text
                nodes are clipped about the subplot axes. To
                show markers and text nodes above axis lines
                and tick labels, make sure to set `xaxis.layer`
                and `yaxis.layer` to *below traces*.
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            error_x
                :class:`plotly.graph_objects.scatter.ErrorX`
                instance or dict with compatible properties
            error_y
                :class:`plotly.graph_objects.scatter.ErrorY`
                instance or dict with compatible properties
            fill
                Sets the area to fill with a solid color.
                Defaults to "none" unless this trace is
                stacked, then it gets "tonexty" ("tonextx") if
                `orientation` is "v" ("h") Use with `fillcolor`
                if not "none". "tozerox" and "tozeroy" fill to
                x=0 and y=0 respectively. "tonextx" and
                "tonexty" fill between the endpoints of this
                trace and the endpoints of the trace before it,
                connecting those endpoints with straight lines
                (to make a stacked area graph); if there is no
                trace before it, they behave like "tozerox" and
                "tozeroy". "toself" connects the endpoints of
                the trace (or each segment of the trace if it
                has gaps) into a closed shape. "tonext" fills
                the space between two traces if one completely
                encloses the other (eg consecutive contour
                lines), and behaves like "toself" if there is
                no trace before it. "tonext" should not be used
                if one trace does not enclose the other. Traces
                in a `stackgroup` will only fill to (or be
                filled to) other traces in the same group. With
                multiple `stackgroup`s or some traces stacked
                and some not, if fill-linked traces are not
                already consecutive, the later ones will be
                pushed down in the drawing order.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            groupnorm
                Only relevant when `stackgroup` is used, and
                only the first `groupnorm` found in the
                `stackgroup` will be used - including if
                `visible` is "legendonly" but not if it is
                `false`. Sets the normalization for the sum of
                this `stackgroup`. With "fraction", the value
                of each trace at each location is divided by
                the sum of all trace values at that location.
                "percent" is the same but multiplied by 100 to
                show percentages. If there are multiple
                subplots, or multiple `stackgroup`s on one
                subplot, each will be normalized within its own
                set.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.scatter.Hoverlabel
                ` instance or dict with compatible properties
            hoveron
                Do the hover effects highlight individual
                points (markers or line points) or do they
                highlight filled regions? If the fill is
                "toself" or "tonext" and there are no markers
                or text, then the default is "fills", otherwise
                it is "points".
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (x,y) pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.scatter.Line`
                instance or dict with compatible properties
            marker
                :class:`plotly.graph_objects.scatter.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            orientation
                Only relevant when `stackgroup` is used, and
                only the first `orientation` found in the
                `stackgroup` will be used - including if
                `visible` is "legendonly" but not if it is
                `false`. Sets the stacking direction. With "v"
                ("h"), the y (x) values of subsequent traces
                are added. Also affects the default value of
                `fill`.
            r
                r coordinates in scatter traces are
                deprecated!Please switch to the "scatterpolar"
                trace type.Sets the radial coordinatesfor
                legacy polar chart only.
            rsrc
                Sets the source reference on plot.ly for  r .
            selected
                :class:`plotly.graph_objects.scatter.Selected`
                instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stackgaps
                Only relevant when `stackgroup` is used, and
                only the first `stackgaps` found in the
                `stackgroup` will be used - including if
                `visible` is "legendonly" but not if it is
                `false`. Determines how we handle locations at
                which other traces in this group have data but
                this one does not. With *infer zero* we insert
                a zero at these locations. With "interpolate"
                we linearly interpolate between existing
                values, and extrapolate a constant beyond the
                existing values.
            stackgroup
                Set several scatter traces (on the same
                subplot) to the same stackgroup in order to add
                their y values (or their x values if
                `orientation` is "h"). If blank or omitted this
                trace will not be stacked. Stacking also turns
                `fill` on by default, using "tonexty"
                ("tonextx") if `orientation` is "h" ("v") and
                sets the default `mode` to "lines" irrespective
                of point count. You can only stack on a numeric
                (linear or log) axis. Traces in a `stackgroup`
                will only fill to (or be filled to) other
                traces in the same group. With multiple
                `stackgroup`s or some traces stacked and some
                not, if fill-linked traces are not already
                consecutive, the later ones will be pushed down
                in the drawing order.
            stream
                :class:`plotly.graph_objects.scatter.Stream`
                instance or dict with compatible properties
            t
                t coordinates in scatter traces are
                deprecated!Please switch to the "scatterpolar"
                trace type.Sets the angular coordinatesfor
                legacy polar chart only.
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the text font.
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
            tsrc
                Sets the source reference on plot.ly for  t .
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
            unselected
                :class:`plotly.graph_objects.scatter.Unselected
                ` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  x .
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
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SankeyValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="sankey", parent_name="", **kwargs):
        super(SankeyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Sankey"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            arrangement
                If value is `snap` (the default), the node
                arrangement is assisted by automatic snapping
                of elements to preserve space between nodes
                specified via `nodepad`. If value is
                `perpendicular`, the nodes can only move along
                a line perpendicular to the flow. If value is
                `freeform`, the nodes can freely move on the
                plane. If value is `fixed`, the nodes are
                stationary.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            domain
                :class:`plotly.graph_objects.sankey.Domain`
                instance or dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired. Note that this attribute is superseded
                by `node.hoverinfo` and `node.hoverinfo` for
                nodes and links respectively.
            hoverlabel
                :class:`plotly.graph_objects.sankey.Hoverlabel`
                instance or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            link
                The links of the Sankey plot.
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            node
                The nodes of the Sankey plot.
            orientation
                Sets the orientation of the Sankey diagram.
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            stream
                :class:`plotly.graph_objects.sankey.Stream`
                instance or dict with compatible properties
            textfont
                Sets the font for node labels
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
            valueformat
                Sets the value formatting rule using d3
                formatting mini-language which is similar to
                those of Python. See
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
            valuesuffix
                Adds a unit to follow the value in the hover
                tooltip. Add a space if a separation is
                necessary from the value.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class PointcloudValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="pointcloud", parent_name="", **kwargs):
        super(PointcloudValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Pointcloud"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.pointcloud.Hoverla
                bel` instance or dict with compatible
                properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            indices
                A sequential value, 0..n, supply it to avoid
                creating this array inside plotting. If
                specified, it must be a typed `Int32Array`
                array. Its length must be equal to or greater
                than the number of points. For the best
                performance and memory use, create one large
                `indices` typed array that is guaranteed to be
                at least as long as the largest number of
                points during use, and reuse it on each
                `Plotly.restyle()` call.
            indicessrc
                Sets the source reference on plot.ly for
                indices .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.pointcloud.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.pointcloud.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xbounds
                Specify `xbounds` in the shape of `[xMin, xMax]
                to avoid looping through the `xy` typed array.
                Use it in conjunction with `xy` and `ybounds`
                for the performance benefits.
            xboundssrc
                Sets the source reference on plot.ly for
                xbounds .
            xsrc
                Sets the source reference on plot.ly for  x .
            xy
                Faster alternative to specifying `x` and `y`
                separately. If supplied, it must be a typed
                `Float32Array` array that represents points
                such that `xy[i * 2] = x[i]` and `xy[i * 2 + 1]
                = y[i]`
            xysrc
                Sets the source reference on plot.ly for  xy .
            y
                Sets the y coordinates.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            ybounds
                Specify `ybounds` in the shape of `[yMin, yMax]
                to avoid looping through the `xy` typed array.
                Use it in conjunction with `xy` and `xbounds`
                for the performance benefits.
            yboundssrc
                Sets the source reference on plot.ly for
                ybounds .
            ysrc
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class PieValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="pie", parent_name="", **kwargs):
        super(PieValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Pie"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            automargin
                Determines whether outside text labels can push
                the margins.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            direction
                Specifies the direction at which succeeding
                sectors follow one another.
            dlabel
                Sets the label step. See `label0` for more
                info.
            domain
                :class:`plotly.graph_objects.pie.Domain`
                instance or dict with compatible properties
            hole
                Sets the fraction of the radius to cut out of
                the pie. Use this to make a donut chart.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.pie.Hoverlabel`
                instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `label`, `color`, `value`, `percent`
                and `text`. Anything contained in tag `<extra>`
                is displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                sector. If a single string, the same string
                appears for all data points. If an array of
                string, the items are mapped in order of this
                trace's sectors. To be seen, trace `hoverinfo`
                must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            insidetextfont
                Sets the font used for `textinfo` lying inside
                the sector.
            insidetextorientation
                Controls the orientation of the text inside
                chart sectors. When set to "auto", text may be
                oriented in any direction in order to be as big
                as possible in the middle of a sector. The
                "horizontal" option orients text to be parallel
                with the bottom of the chart, and may make text
                smaller in order to achieve that goal. The
                "radial" option orients text along the radius
                of the sector. The "tangential" option orients
                text perpendicular to the radius of the sector.
            label0
                Alternate to `labels`. Builds a numeric set of
                labels. Use with `dlabel` where `label0` is the
                starting label and `dlabel` the step.
            labels
                Sets the sector labels. If `labels` entries are
                duplicated, we sum associated `values` or
                simply count occurrences if `values` is not
                provided. For other array attributes (including
                color) we use the first non-empty entry among
                all occurrences of the label.
            labelssrc
                Sets the source reference on plot.ly for
                labels .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.pie.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            outsidetextfont
                Sets the font used for `textinfo` lying outside
                the sector.
            pull
                Sets the fraction of larger radius to pull the
                sectors out from the center. This can be a
                constant to pull all slices apart from each
                other equally or an array to highlight one or
                more slices.
            pullsrc
                Sets the source reference on plot.ly for  pull
                .
            rotation
                Instead of the first slice starting at 12
                o'clock, rotate to some other angle.
            scalegroup
                If there are multiple pie charts that should be
                sized according to their totals, link them by
                providing a non-empty group id here shared by
                every trace in the same group.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            sort
                Determines whether or not the sectors are
                reordered from largest to smallest.
            stream
                :class:`plotly.graph_objects.pie.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each sector.
                If trace `textinfo` contains a "text" flag,
                these elements will be seen on the chart. If
                trace `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the font used for `textinfo`.
            textinfo
                Determines which trace information appear on
                the graph.
            textposition
                Specifies the location of the `textinfo`.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `label`, `color`, `value`,
                `percent` and `text`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
            title
                :class:`plotly.graph_objects.pie.Title`
                instance or dict with compatible properties
            titlefont
                Deprecated: Please use pie.title.font instead.
                Sets the font used for `title`. Note that the
                title's font used to be set by the now
                deprecated `titlefont` attribute.
            titleposition
                Deprecated: Please use pie.title.position
                instead. Specifies the location of the `title`.
                Note that the title's position used to be set
                by the now deprecated `titleposition`
                attribute.
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
            values
                Sets the values of the sectors. If omitted, we
                count occurrences of each label.
            valuessrc
                Sets the source reference on plot.ly for
                values .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ParcoordsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="parcoords", parent_name="", **kwargs):
        super(ParcoordsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Parcoords"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dimensions
                The dimensions (variables) of the parallel
                coordinates chart. 2..60 dimensions are
                supported.
            dimensiondefaults
                When used in a template (as layout.template.dat
                a.parcoords.dimensiondefaults), sets the
                default property values to use for elements of
                parcoords.dimensions
            domain
                :class:`plotly.graph_objects.parcoords.Domain`
                instance or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            labelangle
                Sets the angle of the labels with respect to
                the horizontal. For example, a `tickangle` of
                -90 draws the labels vertically. Tilted labels
                with "labelangle" may be positioned better
                inside margins when `labelposition` is set to
                "bottom".
            labelfont
                Sets the font for the `dimension` labels.
            labelside
                Specifies the location of the `label`. "top"
                positions labels above, next to the title
                "bottom" positions labels below the graph
                Tilted labels with "labelangle" may be
                positioned better inside margins when
                `labelposition` is set to "bottom".
            line
                :class:`plotly.graph_objects.parcoords.Line`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            rangefont
                Sets the font for the `dimension` range values.
            stream
                :class:`plotly.graph_objects.parcoords.Stream`
                instance or dict with compatible properties
            tickfont
                Sets the font for the `dimension` tick values.
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
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ParcatsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="parcats", parent_name="", **kwargs):
        super(ParcatsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Parcats"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            arrangement
                Sets the drag interaction mode for categories
                and dimensions. If `perpendicular`, the
                categories can only move along a line
                perpendicular to the paths. If `freeform`, the
                categories can freely move on the plane. If
                `fixed`, the categories and dimensions are
                stationary.
            bundlecolors
                Sort paths so that like colors are bundled
                together within each category.
            counts
                The number of observations represented by each
                state. Defaults to 1 so that each state
                represents one observation
            countssrc
                Sets the source reference on plot.ly for
                counts .
            dimensions
                The dimensions (variables) of the parallel
                categories diagram.
            dimensiondefaults
                When used in a template (as layout.template.dat
                a.parcats.dimensiondefaults), sets the default
                property values to use for elements of
                parcats.dimensions
            domain
                :class:`plotly.graph_objects.parcats.Domain`
                instance or dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoveron
                Sets the hover interaction mode for the parcats
                diagram. If `category`, hover interaction take
                place per category. If `color`, hover
                interactions take place per color per category.
                If `dimension`, hover interactions take place
                across all categories per dimension.
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `count`, `probability`, `category`,
                `categorycount`, `colorcount` and
                `bandcolorcount`. Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            labelfont
                Sets the font for the `dimension` labels.
            line
                :class:`plotly.graph_objects.parcats.Line`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            sortpaths
                Sets the path sorting algorithm. If `forward`,
                sort paths based on dimension categories from
                left to right. If `backward`, sort paths based
                on dimensions categories from right to left.
            stream
                :class:`plotly.graph_objects.parcats.Stream`
                instance or dict with compatible properties
            tickfont
                Sets the font for the `category` labels.
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
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class OhlcValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="ohlc", parent_name="", **kwargs):
        super(OhlcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Ohlc"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            close
                Sets the close values.
            closesrc
                Sets the source reference on plot.ly for  close
                .
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            decreasing
                :class:`plotly.graph_objects.ohlc.Decreasing`
                instance or dict with compatible properties
            high
                Sets the high values.
            highsrc
                Sets the source reference on plot.ly for  high
                .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.ohlc.Hoverlabel`
                instance or dict with compatible properties
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            increasing
                :class:`plotly.graph_objects.ohlc.Increasing`
                instance or dict with compatible properties
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.ohlc.Line`
                instance or dict with compatible properties
            low
                Sets the low values.
            lowsrc
                Sets the source reference on plot.ly for  low .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            open
                Sets the open values.
            opensrc
                Sets the source reference on plot.ly for  open
                .
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.ohlc.Stream`
                instance or dict with compatible properties
            text
                Sets hover text elements associated with each
                sample point. If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to this trace's sample points.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            tickwidth
                Sets the width of the open/close tick marks
                relative to the "x" minimal interval.
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
                Sets the x coordinates. If absent, linear
                coordinate will be generated.
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
                Sets the source reference on plot.ly for  x .
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class Mesh3dValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="mesh3d", parent_name="", **kwargs):
        super(Mesh3dValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Mesh3d"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            alphahull
                Determines how the mesh surface triangles are
                derived from the set of vertices (points)
                represented by the `x`, `y` and `z` arrays, if
                the `i`, `j`, `k` arrays are not supplied. For
                general use of `mesh3d` it is preferred that
                `i`, `j`, `k` are supplied. If "-1", Delaunay
                triangulation is used, which is mainly suitable
                if the mesh is a single, more or less layer
                surface that is perpendicular to
                `delaunayaxis`. In case the `delaunayaxis`
                intersects the mesh surface at more than one
                point it will result triangles that are very
                long in the dimension of `delaunayaxis`. If
                ">0", the alpha-shape algorithm is used. In
                this case, the positive `alphahull` value
                signals the use of the alpha-shape algorithm,
                _and_ its value acts as the parameter for the
                mesh fitting. If 0,  the convex-hull algorithm
                is used. It is suitable for convex bodies or if
                the intention is to enclose the `x`, `y` and
                `z` point set into a convex hull.
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                `intensity`) or the bounds set in `cmin` and
                `cmax`  Defaults to `false` when `cmin` and
                `cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as `intensity` and
                if set, `cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `cmin` and/or `cmax` to be equidistant
                to this point. Value should have the same units
                as `intensity`. Has no effect when `cauto` is
                `false`.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as `intensity` and
                if set, `cmax` must be set as well.
            color
                Sets the color of the whole mesh
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
                :class:`plotly.graph_objects.mesh3d.ColorBar`
                instance or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)'], [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            contour
                :class:`plotly.graph_objects.mesh3d.Contour`
                instance or dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            delaunayaxis
                Sets the Delaunay axis, which is the axis that
                is perpendicular to the surface of the Delaunay
                triangulation. It has an effect if `i`, `j`,
                `k` are not provided and `alphahull` is set to
                indicate Delaunay triangulation.
            facecolor
                Sets the color of each face Overrides "color"
                and "vertexcolor".
            facecolorsrc
                Sets the source reference on plot.ly for
                facecolor .
            flatshading
                Determines whether or not normal smoothing is
                applied to the meshes, creating meshes with an
                angular, low-poly look via flat reflections.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.mesh3d.Hoverlabel`
                instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            i
                A vector of vertex indices, i.e. integer values
                between 0 and the length of the vertex vectors,
                representing the "first" vertex of a triangle.
                For example, `{i[m], j[m], k[m]}` together
                represent face m (triangle m) in the mesh,
                where `i[m] = n` points to the triplet `{x[n],
                y[n], z[n]}` in the vertex arrays. Therefore,
                each element in `i` represents a point in
                space, which is the first vertex of a triangle.
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            intensity
                Sets the intensity values for vertices or cells
                as defined by `intensitymode`. It can be used
                for plotting fields on meshes.
            intensitymode
                Determines the source of `intensity` values.
            intensitysrc
                Sets the source reference on plot.ly for
                intensity .
            isrc
                Sets the source reference on plot.ly for  i .
            j
                A vector of vertex indices, i.e. integer values
                between 0 and the length of the vertex vectors,
                representing the "second" vertex of a triangle.
                For example, `{i[m], j[m], k[m]}`  together
                represent face m (triangle m) in the mesh,
                where `j[m] = n` points to the triplet `{x[n],
                y[n], z[n]}` in the vertex arrays. Therefore,
                each element in `j` represents a point in
                space, which is the second vertex of a
                triangle.
            jsrc
                Sets the source reference on plot.ly for  j .
            k
                A vector of vertex indices, i.e. integer values
                between 0 and the length of the vertex vectors,
                representing the "third" vertex of a triangle.
                For example, `{i[m], j[m], k[m]}` together
                represent face m (triangle m) in the mesh,
                where `k[m] = n` points to the triplet  `{x[n],
                y[n], z[n]}` in the vertex arrays. Therefore,
                each element in `k` represents a point in
                space, which is the third vertex of a triangle.
            ksrc
                Sets the source reference on plot.ly for  k .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                :class:`plotly.graph_objects.mesh3d.Lighting`
                instance or dict with compatible properties
            lightposition
                :class:`plotly.graph_objects.mesh3d.Lightpositi
                on` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface. Please note
                that in the case of using high `opacity` values
                for example a value greater than or equal to
                0.5 on two surfaces (and 0.25 with four
                surfaces), an overlay of multiple transparent
                surfaces may not perfectly be sorted in depth
                by the webgl API. This behavior may be improved
                in the near future and is subject to change.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            stream
                :class:`plotly.graph_objects.mesh3d.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with the
                vertices. If trace `hoverinfo` contains a
                "text" flag and "hovertext" is not set, these
                elements will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            vertexcolor
                Sets the color of each vertex Overrides
                "color". While Red, green and blue colors are
                in the range of 0 and 255; in the case of
                having vertex color data in RGBA format, the
                alpha color should be normalized to be between
                0 and 1.
            vertexcolorsrc
                Sets the source reference on plot.ly for
                vertexcolor .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the X coordinates of the vertices. The nth
                element of vectors `x`, `y` and `z` jointly
                represent the X, Y and Z coordinates of the nth
                vertex.
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the Y coordinates of the vertices. The nth
                element of vectors `x`, `y` and `z` jointly
                represent the X, Y and Z coordinates of the nth
                vertex.
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the Z coordinates of the vertices. The nth
                element of vectors `x`, `y` and `z` jointly
                represent the X, Y and Z coordinates of the nth
                vertex.
            zcalendar
                Sets the calendar system to use with `z` date
                data.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class IsosurfaceValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="isosurface", parent_name="", **kwargs):
        super(IsosurfaceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Isosurface"),
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
            caps
                :class:`plotly.graph_objects.isosurface.Caps`
                instance or dict with compatible properties
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                `value`) or the bounds set in `cmin` and `cmax`
                Defaults to `false` when `cmin` and `cmax` are
                set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as `value` and if
                set, `cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `cmin` and/or `cmax` to be equidistant
                to this point. Value should have the same units
                as `value`. Has no effect when `cauto` is
                `false`.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as `value` and if
                set, `cmax` must be set as well.
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
                :class:`plotly.graph_objects.isosurface.ColorBa
                r` instance or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)'], [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            contour
                :class:`plotly.graph_objects.isosurface.Contour
                ` instance or dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            flatshading
                Determines whether or not normal smoothing is
                applied to the meshes, creating meshes with an
                angular, low-poly look via flat reflections.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.isosurface.Hoverla
                bel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            isomax
                Sets the maximum boundary for iso-surface plot.
            isomin
                Sets the minimum boundary for iso-surface plot.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                :class:`plotly.graph_objects.isosurface.Lightin
                g` instance or dict with compatible properties
            lightposition
                :class:`plotly.graph_objects.isosurface.Lightpo
                sition` instance or dict with compatible
                properties
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface. Please note
                that in the case of using high `opacity` values
                for example a value greater than or equal to
                0.5 on two surfaces (and 0.25 with four
                surfaces), an overlay of multiple transparent
                surfaces may not perfectly be sorted in depth
                by the webgl API. This behavior may be improved
                in the near future and is subject to change.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            slices
                :class:`plotly.graph_objects.isosurface.Slices`
                instance or dict with compatible properties
            spaceframe
                :class:`plotly.graph_objects.isosurface.Spacefr
                ame` instance or dict with compatible
                properties
            stream
                :class:`plotly.graph_objects.isosurface.Stream`
                instance or dict with compatible properties
            surface
                :class:`plotly.graph_objects.isosurface.Surface
                ` instance or dict with compatible properties
            text
                Sets the text elements associated with the
                vertices. If trace `hoverinfo` contains a
                "text" flag and "hovertext" is not set, these
                elements will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            value
                Sets the 4th dimension (value) of the vertices.
            valuesrc
                Sets the source reference on plot.ly for  value
                .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the X coordinates of the vertices on X
                axis.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the Y coordinates of the vertices on Y
                axis.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the Z coordinates of the vertices on Z
                axis.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class IndicatorValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="indicator", parent_name="", **kwargs):
        super(IndicatorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Indicator"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            align
                Sets the horizontal alignment of the `text`
                within the box. Note that this attribute has no
                effect if an angular gauge is displayed: in
                this case, it is always centered
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            delta
                :class:`plotly.graph_objects.indicator.Delta`
                instance or dict with compatible properties
            domain
                :class:`plotly.graph_objects.indicator.Domain`
                instance or dict with compatible properties
            gauge
                The gauge of the Indicator plot.
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
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
                Sets the source reference on plot.ly for  meta
                .
            mode
                Determines how the value is displayed on the
                graph. `number` displays the value numerically
                in text. `delta` displays the difference to a
                reference value in text. Finally, `gauge`
                displays the value graphically on an axis.
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            number
                :class:`plotly.graph_objects.indicator.Number`
                instance or dict with compatible properties
            stream
                :class:`plotly.graph_objects.indicator.Stream`
                instance or dict with compatible properties
            title
                :class:`plotly.graph_objects.indicator.Title`
                instance or dict with compatible properties
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
            value
                Sets the number to be displayed.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ImageValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="image", parent_name="", **kwargs):
        super(ImageValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Image"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            colormodel
                Color model used to map the numerical color
                components described in `z` into colors.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Set the pixel's horizontal size.
            dy
                Set the pixel's vertical size
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.image.Hoverlabel`
                instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `z`, `color` and `colormodel`.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            stream
                :class:`plotly.graph_objects.image.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with each z
                value.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            x0
                Set the image's x position.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            y0
                Set the image's y position.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            z
                A 2-dimensional array in which each element is
                an array of 3 or 4 numbers representing a
                color.
            zmax
                Array defining the higher bound for each color
                component. Note that the default value will
                depend on the colormodel. For the `rgb`
                colormodel, it is [255, 255, 255]. For the
                `rgba` colormodel, it is [255, 255, 255, 1].
                For the `hsl` colormodel, it is [360, 100,
                100]. For the `hsla` colormodel, it is [360,
                100, 100, 1].
            zmin
                Array defining the lower bound for each color
                component. Note that the default value will
                depend on the colormodel. For the `rgb`
                colormodel, it is [0, 0, 0]. For the `rgba`
                colormodel, it is [0, 0, 0, 0]. For the `hsl`
                colormodel, it is [0, 0, 0]. For the `hsla`
                colormodel, it is [0, 0, 0, 0].
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class Histogram2dContourValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="histogram2dcontour", parent_name="", **kwargs):
        super(Histogram2dContourValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Histogram2dContour"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autobinx
                Obsolete: since v1.42 each bin attribute is
                auto-determined separately and `autobinx` is
                not needed. However, we accept `autobinx: true`
                or `false` and will update `xbins` accordingly
                before deleting `autobinx` from the trace.
            autobiny
                Obsolete: since v1.42 each bin attribute is
                auto-determined separately and `autobiny` is
                not needed. However, we accept `autobiny: true`
                or `false` and will update `ybins` accordingly
                before deleting `autobiny` from the trace.
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
            bingroup
                Set the `xbingroup` and `ybingroup` default
                prefix For example, setting a `bingroup` of 1
                on two histogram2d traces will make them their
                x-bins and y-bins match separately.
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
                :class:`plotly.graph_objects.histogram2dcontour
                .ColorBar` instance or dict with compatible
                properties
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
            contours
                :class:`plotly.graph_objects.histogram2dcontour
                .Contours` instance or dict with compatible
                properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            histfunc
                Specifies the binning function used for this
                histogram trace. If "count", the histogram
                values are computed by counting the number of
                values lying inside each bin. If "sum", "avg",
                "min", "max", the histogram values are computed
                using the sum, the average, the minimum or the
                maximum of the values lying inside each bin
                respectively.
            histnorm
                Specifies the type of normalization used for
                this histogram trace. If "", the span of each
                bar corresponds to the number of occurrences
                (i.e. the number of data points lying inside
                the bins). If "percent" / "probability", the
                span of each bar corresponds to the percentage
                / fraction of occurrences with respect to the
                total number of sample points (here, the sum of
                all bin HEIGHTS equals 100% / 1). If "density",
                the span of each bar corresponds to the number
                of occurrences in a bin divided by the size of
                the bin interval (here, the sum of all bin
                AREAS equals the total number of sample
                points). If *probability density*, the area of
                each bar corresponds to the probability that an
                event will fall into the corresponding bin
                (here, the sum of all bin AREAS equals 1).
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.histogram2dcontour
                .Hoverlabel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variable `z` Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.histogram2dcontour
                .Line` instance or dict with compatible
                properties
            marker
                :class:`plotly.graph_objects.histogram2dcontour
                .Marker` instance or dict with compatible
                properties
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            nbinsx
                Specifies the maximum number of desired bins.
                This value will be used in an algorithm that
                will decide the optimal bin size such that the
                histogram best visualizes the distribution of
                the data. Ignored if `xbins.size` is provided.
            nbinsy
                Specifies the maximum number of desired bins.
                This value will be used in an algorithm that
                will decide the optimal bin size such that the
                histogram best visualizes the distribution of
                the data. Ignored if `ybins.size` is provided.
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
                :class:`plotly.graph_objects.histogram2dcontour
                .Stream` instance or dict with compatible
                properties
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
                Sets the sample data to be binned on the x
                axis.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xbingroup
                Set a group of histogram traces which will have
                compatible x-bin settings. Using `xbingroup`,
                histogram2d and histogram2dcontour traces  (on
                axes of the same axis type) can have compatible
                x-bin settings. Note that the same `xbingroup`
                value can be used to set (1D) histogram
                `bingroup`
            xbins
                :class:`plotly.graph_objects.histogram2dcontour
                .XBins` instance or dict with compatible
                properties
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the sample data to be binned on the y
                axis.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            ybingroup
                Set a group of histogram traces which will have
                compatible y-bin settings. Using `ybingroup`,
                histogram2d and histogram2dcontour traces  (on
                axes of the same axis type) can have compatible
                y-bin settings. Note that the same `ybingroup`
                value can be used to set (1D) histogram
                `bingroup`
            ybins
                :class:`plotly.graph_objects.histogram2dcontour
                .YBins` instance or dict with compatible
                properties
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the aggregation data.
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
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class Histogram2dValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="histogram2d", parent_name="", **kwargs):
        super(Histogram2dValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Histogram2d"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autobinx
                Obsolete: since v1.42 each bin attribute is
                auto-determined separately and `autobinx` is
                not needed. However, we accept `autobinx: true`
                or `false` and will update `xbins` accordingly
                before deleting `autobinx` from the trace.
            autobiny
                Obsolete: since v1.42 each bin attribute is
                auto-determined separately and `autobiny` is
                not needed. However, we accept `autobiny: true`
                or `false` and will update `ybins` accordingly
                before deleting `autobiny` from the trace.
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            bingroup
                Set the `xbingroup` and `ybingroup` default
                prefix For example, setting a `bingroup` of 1
                on two histogram2d traces will make them their
                x-bins and y-bins match separately.
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
                :class:`plotly.graph_objects.histogram2d.ColorB
                ar` instance or dict with compatible properties
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
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            histfunc
                Specifies the binning function used for this
                histogram trace. If "count", the histogram
                values are computed by counting the number of
                values lying inside each bin. If "sum", "avg",
                "min", "max", the histogram values are computed
                using the sum, the average, the minimum or the
                maximum of the values lying inside each bin
                respectively.
            histnorm
                Specifies the type of normalization used for
                this histogram trace. If "", the span of each
                bar corresponds to the number of occurrences
                (i.e. the number of data points lying inside
                the bins). If "percent" / "probability", the
                span of each bar corresponds to the percentage
                / fraction of occurrences with respect to the
                total number of sample points (here, the sum of
                all bin HEIGHTS equals 100% / 1). If "density",
                the span of each bar corresponds to the number
                of occurrences in a bin divided by the size of
                the bin interval (here, the sum of all bin
                AREAS equals the total number of sample
                points). If *probability density*, the area of
                each bar corresponds to the probability that an
                event will fall into the corresponding bin
                (here, the sum of all bin AREAS equals 1).
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.histogram2d.Hoverl
                abel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variable `z` Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.histogram2d.Marker
                ` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            nbinsx
                Specifies the maximum number of desired bins.
                This value will be used in an algorithm that
                will decide the optimal bin size such that the
                histogram best visualizes the distribution of
                the data. Ignored if `xbins.size` is provided.
            nbinsy
                Specifies the maximum number of desired bins.
                This value will be used in an algorithm that
                will decide the optimal bin size such that the
                histogram best visualizes the distribution of
                the data. Ignored if `ybins.size` is provided.
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
                :class:`plotly.graph_objects.histogram2d.Stream
                ` instance or dict with compatible properties
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
                Sets the sample data to be binned on the x
                axis.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xbingroup
                Set a group of histogram traces which will have
                compatible x-bin settings. Using `xbingroup`,
                histogram2d and histogram2dcontour traces  (on
                axes of the same axis type) can have compatible
                x-bin settings. Note that the same `xbingroup`
                value can be used to set (1D) histogram
                `bingroup`
            xbins
                :class:`plotly.graph_objects.histogram2d.XBins`
                instance or dict with compatible properties
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xgap
                Sets the horizontal gap (in pixels) between
                bricks.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the sample data to be binned on the y
                axis.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            ybingroup
                Set a group of histogram traces which will have
                compatible y-bin settings. Using `ybingroup`,
                histogram2d and histogram2dcontour traces  (on
                axes of the same axis type) can have compatible
                y-bin settings. Note that the same `ybingroup`
                value can be used to set (1D) histogram
                `bingroup`
            ybins
                :class:`plotly.graph_objects.histogram2d.YBins`
                instance or dict with compatible properties
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ygap
                Sets the vertical gap (in pixels) between
                bricks.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the aggregation data.
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
            zsmooth
                Picks a smoothing algorithm use to smooth `z`
                data.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HistogramValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="histogram", parent_name="", **kwargs):
        super(HistogramValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Histogram"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            alignmentgroup
                Set several traces linked to the same position
                axis or matching axes to the same
                alignmentgroup. This controls whether bars
                compute their positional range dependently or
                independently.
            autobinx
                Obsolete: since v1.42 each bin attribute is
                auto-determined separately and `autobinx` is
                not needed. However, we accept `autobinx: true`
                or `false` and will update `xbins` accordingly
                before deleting `autobinx` from the trace.
            autobiny
                Obsolete: since v1.42 each bin attribute is
                auto-determined separately and `autobiny` is
                not needed. However, we accept `autobiny: true`
                or `false` and will update `ybins` accordingly
                before deleting `autobiny` from the trace.
            bingroup
                Set a group of histogram traces which will have
                compatible bin settings. Note that traces on
                the same subplot and with the same
                "orientation" under `barmode` "stack",
                "relative" and "group" are forced into the same
                bingroup, Using `bingroup`, traces under
                `barmode` "overlay" and on different axes (of
                the same axis type) can have compatible bin
                settings. Note that histogram and histogram2d*
                trace can share the same `bingroup`
            cumulative
                :class:`plotly.graph_objects.histogram.Cumulati
                ve` instance or dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            error_x
                :class:`plotly.graph_objects.histogram.ErrorX`
                instance or dict with compatible properties
            error_y
                :class:`plotly.graph_objects.histogram.ErrorY`
                instance or dict with compatible properties
            histfunc
                Specifies the binning function used for this
                histogram trace. If "count", the histogram
                values are computed by counting the number of
                values lying inside each bin. If "sum", "avg",
                "min", "max", the histogram values are computed
                using the sum, the average, the minimum or the
                maximum of the values lying inside each bin
                respectively.
            histnorm
                Specifies the type of normalization used for
                this histogram trace. If "", the span of each
                bar corresponds to the number of occurrences
                (i.e. the number of data points lying inside
                the bins). If "percent" / "probability", the
                span of each bar corresponds to the percentage
                / fraction of occurrences with respect to the
                total number of sample points (here, the sum of
                all bin HEIGHTS equals 100% / 1). If "density",
                the span of each bar corresponds to the number
                of occurrences in a bin divided by the size of
                the bin interval (here, the sum of all bin
                AREAS equals the total number of sample
                points). If *probability density*, the area of
                each bar corresponds to the probability that an
                event will fall into the corresponding bin
                (here, the sum of all bin AREAS equals 1).
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.histogram.Hoverlab
                el` instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variable `binNumber` Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.histogram.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            nbinsx
                Specifies the maximum number of desired bins.
                This value will be used in an algorithm that
                will decide the optimal bin size such that the
                histogram best visualizes the distribution of
                the data. Ignored if `xbins.size` is provided.
            nbinsy
                Specifies the maximum number of desired bins.
                This value will be used in an algorithm that
                will decide the optimal bin size such that the
                histogram best visualizes the distribution of
                the data. Ignored if `ybins.size` is provided.
            offsetgroup
                Set several traces linked to the same position
                axis or matching axes to the same offsetgroup
                where bars of the same position coordinate will
                line up.
            opacity
                Sets the opacity of the trace.
            orientation
                Sets the orientation of the bars. With "v"
                ("h"), the value of the each bar spans along
                the vertical (horizontal).
            selected
                :class:`plotly.graph_objects.histogram.Selected
                ` instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.histogram.Stream`
                instance or dict with compatible properties
            text
                Sets hover text elements associated with each
                bar. If a single string, the same string
                appears over all bars. If an array of string,
                the items are mapped in order to the this
                trace's coordinates.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            unselected
                :class:`plotly.graph_objects.histogram.Unselect
                ed` instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the sample data to be binned on the x
                axis.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xbins
                :class:`plotly.graph_objects.histogram.XBins`
                instance or dict with compatible properties
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the sample data to be binned on the y
                axis.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            ybins
                :class:`plotly.graph_objects.histogram.YBins`
                instance or dict with compatible properties
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HeatmapglValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="heatmapgl", parent_name="", **kwargs):
        super(HeatmapglValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Heatmapgl"),
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
                :class:`plotly.graph_objects.heatmapgl.ColorBar
                ` instance or dict with compatible properties
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
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.heatmapgl.Hoverlab
                el` instance or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            reversescale
                Reverses the color mapping if true. If true,
                `zmin` will correspond to the last color in the
                array and `zmax` will correspond to the first
                color.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            stream
                :class:`plotly.graph_objects.heatmapgl.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with each z
                value.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            xsrc
                Sets the source reference on plot.ly for  x .
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
            ysrc
                Sets the source reference on plot.ly for  y .
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
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HeatmapValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="heatmap", parent_name="", **kwargs):
        super(HeatmapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Heatmap"),
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
                :class:`plotly.graph_objects.heatmap.ColorBar`
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
                dimensional array and `zsmooth` is not false;
                otherwise it is defaulted to false.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.heatmap.Hoverlabel
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
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
                :class:`plotly.graph_objects.heatmap.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with each z
                value.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            xgap
                Sets the horizontal gap (in pixels) between
                bricks.
            xsrc
                Sets the source reference on plot.ly for  x .
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
            ygap
                Sets the vertical gap (in pixels) between
                bricks.
            ysrc
                Sets the source reference on plot.ly for  y .
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
            zsmooth
                Picks a smoothing algorithm use to smooth `z`
                data.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FunnelareaValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="funnelarea", parent_name="", **kwargs):
        super(FunnelareaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Funnelarea"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            aspectratio
                Sets the ratio between height and width
            baseratio
                Sets the ratio between bottom length and
                maximum top length.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dlabel
                Sets the label step. See `label0` for more
                info.
            domain
                :class:`plotly.graph_objects.funnelarea.Domain`
                instance or dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.funnelarea.Hoverla
                bel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `label`, `color`, `value`, `text` and
                `percent`. Anything contained in tag `<extra>`
                is displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                sector. If a single string, the same string
                appears for all data points. If an array of
                string, the items are mapped in order of this
                trace's sectors. To be seen, trace `hoverinfo`
                must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            insidetextfont
                Sets the font used for `textinfo` lying inside
                the sector.
            label0
                Alternate to `labels`. Builds a numeric set of
                labels. Use with `dlabel` where `label0` is the
                starting label and `dlabel` the step.
            labels
                Sets the sector labels. If `labels` entries are
                duplicated, we sum associated `values` or
                simply count occurrences if `values` is not
                provided. For other array attributes (including
                color) we use the first non-empty entry among
                all occurrences of the label.
            labelssrc
                Sets the source reference on plot.ly for
                labels .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.funnelarea.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            scalegroup
                If there are multiple funnelareas that should
                be sized according to their totals, link them
                by providing a non-empty group id here shared
                by every trace in the same group.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.funnelarea.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each sector.
                If trace `textinfo` contains a "text" flag,
                these elements will be seen on the chart. If
                trace `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the font used for `textinfo`.
            textinfo
                Determines which trace information appear on
                the graph.
            textposition
                Specifies the location of the `textinfo`.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `label`, `color`, `value`,
                `text` and `percent`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
            title
                :class:`plotly.graph_objects.funnelarea.Title`
                instance or dict with compatible properties
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
            values
                Sets the values of the sectors. If omitted, we
                count occurrences of each label.
            valuessrc
                Sets the source reference on plot.ly for
                values .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FunnelValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="funnel", parent_name="", **kwargs):
        super(FunnelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Funnel"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            alignmentgroup
                Set several traces linked to the same position
                axis or matching axes to the same
                alignmentgroup. This controls whether bars
                compute their positional range dependently or
                independently.
            cliponaxis
                Determines whether the text nodes are clipped
                about the subplot axes. To show the text nodes
                above axis lines and tick labels, make sure to
                set `xaxis.layer` and `yaxis.layer` to *below
                traces*.
            connector
                :class:`plotly.graph_objects.funnel.Connector`
                instance or dict with compatible properties
            constraintext
                Constrain the size of text inside or outside a
                bar to be no larger than the bar itself.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.funnel.Hoverlabel`
                instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `percentInitial`, `percentPrevious`
                and `percentTotal`. Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (x,y) pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            insidetextanchor
                Determines if texts are kept at center or
                start/end points in `textposition` "inside"
                mode.
            insidetextfont
                Sets the font used for `text` lying inside the
                bar.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.funnel.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            offset
                Shifts the position where the bar is drawn (in
                position axis units). In "group" barmode,
                traces that set "offset" will be excluded and
                drawn in "overlay" mode instead.
            offsetgroup
                Set several traces linked to the same position
                axis or matching axes to the same offsetgroup
                where bars of the same position coordinate will
                line up.
            opacity
                Sets the opacity of the trace.
            orientation
                Sets the orientation of the funnels. With "v"
                ("h"), the value of the each bar spans along
                the vertical (horizontal). By default funnels
                are tend to be oriented horizontally; unless
                only "y" array is presented or orientation is
                set to "v". Also regarding graphs including
                only 'horizontal' funnels, "autorange" on the
                "y-axis" are set to "reversed".
            outsidetextfont
                Sets the font used for `text` lying outside the
                bar.
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.funnel.Stream`
                instance or dict with compatible properties
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textangle
                Sets the angle of the tick labels with respect
                to the bar. For example, a `tickangle` of -90
                draws the tick labels vertically. With "auto"
                the texts may automatically be rotated to fit
                with the maximum size in bars.
            textfont
                Sets the font used for `text`.
            textinfo
                Determines which trace information appear on
                the graph. In the case of having multiple
                funnels, percentages & totals are computed
                separately (per trace).
            textposition
                Specifies the location of the `text`. "inside"
                positions `text` inside, next to the bar end
                (rotated and scaled if needed). "outside"
                positions `text` outside, next to the bar end
                (scaled if needed), unless there is another bar
                stacked on this one, then the text gets pushed
                inside. "auto" tries to position `text` inside
                the bar, but if the bar is too small and no bar
                is stacked on this one the text is moved
                outside.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `percentInitial`,
                `percentPrevious`, `percentTotal`, `label` and
                `value`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
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
            width
                Sets the bar width (in position axis units).
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
            xsrc
                Sets the source reference on plot.ly for  x .
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
            ysrc
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class DensitymapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="densitymapbox", parent_name="", **kwargs):
        super(DensitymapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Densitymapbox"),
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
            below
                Determines if the densitymapbox trace will be
                inserted before the layer with the specified
                ID. By default, densitymapbox traces are placed
                below the first layer of type symbol If set to
                '', the layer will be inserted above every
                existing layer.
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
                :class:`plotly.graph_objects.densitymapbox.Colo
                rBar` instance or dict with compatible
                properties
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
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.densitymapbox.Hove
                rlabel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (lon,lat) pair If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to the this trace's (lon,lat) coordinates. To
                be seen, trace `hoverinfo` must contain a
                "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            lat
                Sets the latitude coordinates (in degrees
                North).
            latsrc
                Sets the source reference on plot.ly for  lat .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lon
                Sets the longitude coordinates (in degrees
                East).
            lonsrc
                Sets the source reference on plot.ly for  lon .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            radius
                Sets the radius of influence of one `lon` /
                `lat` point in pixels. Increasing the value
                makes the densitymapbox trace smoother, but
                less detailed.
            radiussrc
                Sets the source reference on plot.ly for
                radius .
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
                :class:`plotly.graph_objects.densitymapbox.Stre
                am` instance or dict with compatible properties
            subplot
                Sets a reference between this trace's data
                coordinates and a mapbox subplot. If "mapbox"
                (the default value), the data refer to
                `layout.mapbox`. If "mapbox2", the data refer
                to `layout.mapbox2`, and so on.
            text
                Sets text elements associated with each
                (lon,lat) pair If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to the this trace's (lon,lat) coordinates. If
                trace `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            z
                Sets the points' weight. For example, a value
                of 10 would be equivalent to having 10 points
                of weight 1 in the same spot
            zauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `z`) or the bounds set in `zmin` and `zmax`
                Defaults to `false` when `zmin` and `zmax` are
                set by the user.
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
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ContourcarpetValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="contourcarpet", parent_name="", **kwargs):
        super(ContourcarpetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Contourcarpet"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            a
                Sets the x coordinates.
            a0
                Alternate to `x`. Builds a linear space of x
                coordinates. Use with `dx` where `x0` is the
                starting coordinate and `dx` the step.
            asrc
                Sets the source reference on plot.ly for  a .
            atype
                If "array", the heatmap's x coordinates are
                given by "x" (the default behavior when `x` is
                provided). If "scaled", the heatmap's x
                coordinates are given by "x0" and "dx" (the
                default behavior when `x` is not provided).
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
            b
                Sets the y coordinates.
            b0
                Alternate to `y`. Builds a linear space of y
                coordinates. Use with `dy` where `y0` is the
                starting coordinate and `dy` the step.
            bsrc
                Sets the source reference on plot.ly for  b .
            btype
                If "array", the heatmap's y coordinates are
                given by "y" (the default behavior when `y` is
                provided) If "scaled", the heatmap's y
                coordinates are given by "y0" and "dy" (the
                default behavior when `y` is not provided)
            carpet
                The `carpet` of the carpet axes on which this
                contour trace lies
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
                :class:`plotly.graph_objects.contourcarpet.Colo
                rBar` instance or dict with compatible
                properties
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
            contours
                :class:`plotly.graph_objects.contourcarpet.Cont
                ours` instance or dict with compatible
                properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            da
                Sets the x coordinate step. See `x0` for more
                info.
            db
                Sets the y coordinate step. See `y0` for more
                info.
            fillcolor
                Sets the fill color if `contours.type` is
                "constraint". Defaults to a half-transparent
                variant of the line color, marker color, or
                marker line color, whichever is available.
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.contourcarpet.Line
                ` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  meta
                .
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
                :class:`plotly.graph_objects.contourcarpet.Stre
                am` instance or dict with compatible properties
            text
                Sets the text elements associated with each z
                value.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            z
                Sets the z data.
            zauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `z`) or the bounds set in `zmin` and `zmax`
                Defaults to `false` when `zmin` and `zmax` are
                set by the user.
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
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


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
                Sets the source reference on plot.ly for
                customdata .
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
                Sets the source reference on plot.ly for
                hoverinfo .
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
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
                Sets the source reference on plot.ly for  meta
                .
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
                Sets the source reference on plot.ly for  text
                .
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
                Sets the source reference on plot.ly for  x .
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
                Sets the source reference on plot.ly for  y .
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
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ConeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="cone", parent_name="", **kwargs):
        super(ConeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Cone"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            anchor
                Sets the cones' anchor with respect to their
                x/y/z positions. Note that "cm" denote the
                cone's center of mass which corresponds to 1/4
                from the tail to tip.
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                u/v/w norm) or the bounds set in `cmin` and
                `cmax`  Defaults to `false` when `cmin` and
                `cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as u/v/w norm and if
                set, `cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `cmin` and/or `cmax` to be equidistant
                to this point. Value should have the same units
                as u/v/w norm. Has no effect when `cauto` is
                `false`.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as u/v/w norm and if
                set, `cmax` must be set as well.
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
                :class:`plotly.graph_objects.cone.ColorBar`
                instance or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)'], [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.cone.Hoverlabel`
                instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variable `norm` Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                :class:`plotly.graph_objects.cone.Lighting`
                instance or dict with compatible properties
            lightposition
                :class:`plotly.graph_objects.cone.Lightposition
                ` instance or dict with compatible properties
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface. Please note
                that in the case of using high `opacity` values
                for example a value greater than or equal to
                0.5 on two surfaces (and 0.25 with four
                surfaces), an overlay of multiple transparent
                surfaces may not perfectly be sorted in depth
                by the webgl API. This behavior may be improved
                in the near future and is subject to change.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            sizemode
                Determines whether `sizeref` is set as a
                "scaled" (i.e unitless) scalar (normalized by
                the max u/v/w norm in the vector field) or as
                "absolute" value (in the same units as the
                vector field).
            sizeref
                Adjusts the cone size scaling. The size of the
                cones is determined by their u/v/w norm
                multiplied a factor and `sizeref`. This factor
                (computed internally) corresponds to the
                minimum "time" to travel across two successive
                x/y/z positions at the average velocity of
                those two successive positions. All cones in a
                given trace use the same factor. With
                `sizemode` set to "scaled", `sizeref` is
                unitless, its default value is 0.5 With
                `sizemode` set to "absolute", `sizeref` has the
                same units as the u/v/w vector field, its the
                default value is half the sample's maximum
                vector norm.
            stream
                :class:`plotly.graph_objects.cone.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with the
                cones. If trace `hoverinfo` contains a "text"
                flag and "hovertext" is not set, these elements
                will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            u
                Sets the x components of the vector field.
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
            usrc
                Sets the source reference on plot.ly for  u .
            v
                Sets the y components of the vector field.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            vsrc
                Sets the source reference on plot.ly for  v .
            w
                Sets the z components of the vector field.
            wsrc
                Sets the source reference on plot.ly for  w .
            x
                Sets the x coordinates of the vector field and
                of the displayed cones.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y coordinates of the vector field and
                of the displayed cones.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the z coordinates of the vector field and
                of the displayed cones.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ChoroplethmapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="choroplethmapbox", parent_name="", **kwargs):
        super(ChoroplethmapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Choroplethmapbox"),
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
            below
                Determines if the choropleth polygons will be
                inserted before the layer with the specified
                ID. By default, choroplethmapbox traces are
                placed above the water layers. If set to '',
                the layer will be inserted above every existing
                layer.
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
                :class:`plotly.graph_objects.choroplethmapbox.C
                olorBar` instance or dict with compatible
                properties
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
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            featureidkey
                Sets the key in GeoJSON features which is used
                as id to match the items included in the
                `locations` array. Support nested property, for
                example "properties.name".
            geojson
                Sets the GeoJSON data associated with this
                trace. It can be set as a valid GeoJSON object
                or as a URL string. Note that we only accept
                GeoJSONs of type "FeatureCollection" or
                "Feature" with geometries of type "Polygon" or
                "MultiPolygon".
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.choroplethmapbox.H
                overlabel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variable `properties` Anything contained in tag
                `<extra>` is displayed in the secondary box,
                for example "<extra>{fullData.name}</extra>".
                To hide the secondary box completely, use an
                empty tag `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            locations
                Sets which features found in "geojson" to plot
                using their feature `id` field.
            locationssrc
                Sets the source reference on plot.ly for
                locations .
            marker
                :class:`plotly.graph_objects.choroplethmapbox.M
                arker` instance or dict with compatible
                properties
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            reversescale
                Reverses the color mapping if true. If true,
                `zmin` will correspond to the last color in the
                array and `zmax` will correspond to the first
                color.
            selected
                :class:`plotly.graph_objects.choroplethmapbox.S
                elected` instance or dict with compatible
                properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            stream
                :class:`plotly.graph_objects.choroplethmapbox.S
                tream` instance or dict with compatible
                properties
            subplot
                Sets a reference between this trace's data
                coordinates and a mapbox subplot. If "mapbox"
                (the default value), the data refer to
                `layout.mapbox`. If "mapbox2", the data refer
                to `layout.mapbox2`, and so on.
            text
                Sets the text elements associated with each
                location.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            unselected
                :class:`plotly.graph_objects.choroplethmapbox.U
                nselected` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            z
                Sets the color values.
            zauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `z`) or the bounds set in `zmin` and `zmax`
                Defaults to `false` when `zmin` and `zmax` are
                set by the user.
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
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ChoroplethValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="choropleth", parent_name="", **kwargs):
        super(ChoroplethValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Choropleth"),
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
                :class:`plotly.graph_objects.choropleth.ColorBa
                r` instance or dict with compatible properties
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
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            featureidkey
                Sets the key in GeoJSON features which is used
                as id to match the items included in the
                `locations` array. Only has an effect when
                `geojson` is set. Support nested property, for
                example "properties.name".
            geo
                Sets a reference between this trace's
                geospatial coordinates and a geographic map. If
                "geo" (the default value), the geospatial
                coordinates refer to `layout.geo`. If "geo2",
                the geospatial coordinates refer to
                `layout.geo2`, and so on.
            geojson
                Sets optional GeoJSON data associated with this
                trace. If not given, the features on the base
                map are used. It can be set as a valid GeoJSON
                object or as a URL string. Note that we only
                accept GeoJSONs of type "FeatureCollection" or
                "Feature" with geometries of type "Polygon" or
                "MultiPolygon".
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.choropleth.Hoverla
                bel` instance or dict with compatible
                properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            locationmode
                Determines the set of locations used to match
                entries in `locations` to regions on the map.
                Values "ISO-3", "USA-states", *country names*
                correspond to features on the base map and
                value "geojson-id" corresponds to features from
                a custom GeoJSON linked to the `geojson`
                attribute.
            locations
                Sets the coordinates via location IDs or names.
                See `locationmode` for more info.
            locationssrc
                Sets the source reference on plot.ly for
                locations .
            marker
                :class:`plotly.graph_objects.choropleth.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            reversescale
                Reverses the color mapping if true. If true,
                `zmin` will correspond to the last color in the
                array and `zmax` will correspond to the first
                color.
            selected
                :class:`plotly.graph_objects.choropleth.Selecte
                d` instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            stream
                :class:`plotly.graph_objects.choropleth.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with each
                location.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            unselected
                :class:`plotly.graph_objects.choropleth.Unselec
                ted` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            z
                Sets the color values.
            zauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `z`) or the bounds set in `zmin` and `zmax`
                Defaults to `false` when `zmin` and `zmax` are
                set by the user.
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
                Sets the source reference on plot.ly for  z .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CarpetValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="carpet", parent_name="", **kwargs):
        super(CarpetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Carpet"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            a
                An array containing values of the first
                parameter value
            a0
                Alternate to `a`. Builds a linear space of a
                coordinates. Use with `da` where `a0` is the
                starting coordinate and `da` the step.
            aaxis
                :class:`plotly.graph_objects.carpet.Aaxis`
                instance or dict with compatible properties
            asrc
                Sets the source reference on plot.ly for  a .
            b
                A two dimensional array of y coordinates at
                each carpet point.
            b0
                Alternate to `b`. Builds a linear space of a
                coordinates. Use with `db` where `b0` is the
                starting coordinate and `db` the step.
            baxis
                :class:`plotly.graph_objects.carpet.Baxis`
                instance or dict with compatible properties
            bsrc
                Sets the source reference on plot.ly for  b .
            carpet
                An identifier for this carpet, so that
                `scattercarpet` and `contourcarpet` traces can
                specify a carpet plot on which they lie
            cheaterslope
                The shift applied to each successive row of
                data in creating a cheater plot. Only used if
                `x` is been ommitted.
            color
                Sets default for all colors associated with
                this axis all at once: line, font, tick, and
                grid colors. Grid color is lightened by
                blending this with the plot background
                Individual pieces can override this.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            da
                Sets the a coordinate step. See `a0` for more
                info.
            db
                Sets the b coordinate step. See `b0` for more
                info.
            font
                The default font used for axis & tick labels on
                this carpet
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            stream
                :class:`plotly.graph_objects.carpet.Stream`
                instance or dict with compatible properties
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
                A two dimensional array of x coordinates at
                each carpet point. If ommitted, the plot is a
                cheater plot and the xaxis is hidden by
                default.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                A two dimensional array of y coordinates at
                each carpet point.
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            ysrc
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CandlestickValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="candlestick", parent_name="", **kwargs):
        super(CandlestickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Candlestick"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            close
                Sets the close values.
            closesrc
                Sets the source reference on plot.ly for  close
                .
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            decreasing
                :class:`plotly.graph_objects.candlestick.Decrea
                sing` instance or dict with compatible
                properties
            high
                Sets the high values.
            highsrc
                Sets the source reference on plot.ly for  high
                .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.candlestick.Hoverl
                abel` instance or dict with compatible
                properties
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            increasing
                :class:`plotly.graph_objects.candlestick.Increa
                sing` instance or dict with compatible
                properties
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.candlestick.Line`
                instance or dict with compatible properties
            low
                Sets the low values.
            lowsrc
                Sets the source reference on plot.ly for  low .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            open
                Sets the open values.
            opensrc
                Sets the source reference on plot.ly for  open
                .
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.candlestick.Stream
                ` instance or dict with compatible properties
            text
                Sets hover text elements associated with each
                sample point. If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to this trace's sample points.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            whiskerwidth
                Sets the width of the whiskers relative to the
                box' width. For example, with 1, the whiskers
                are as wide as the box(es).
            x
                Sets the x coordinates. If absent, linear
                coordinate will be generated.
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
                Sets the source reference on plot.ly for  x .
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BoxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="box", parent_name="", **kwargs):
        super(BoxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Box"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            alignmentgroup
                Set several traces linked to the same position
                axis or matching axes to the same
                alignmentgroup. This controls whether bars
                compute their positional range dependently or
                independently.
            boxmean
                If True, the mean of the box(es)' underlying
                distribution is drawn as a dashed line inside
                the box(es). If "sd" the standard deviation is
                also drawn. Defaults to True when `mean` is
                set. Defaults to "sd" when `sd` is set
                Otherwise defaults to False.
            boxpoints
                If "outliers", only the sample points lying
                outside the whiskers are shown If
                "suspectedoutliers", the outlier points are
                shown and points either less than 4*Q1-3*Q3 or
                greater than 4*Q3-3*Q1 are highlighted (see
                `outliercolor`) If "all", all sample points are
                shown If False, only the box(es) are shown with
                no sample points Defaults to
                "suspectedoutliers" when `marker.outliercolor`
                or `marker.line.outliercolor` is set. Defaults
                to "all" under the q1/median/q3 signature.
                Otherwise defaults to "outliers".
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step for multi-box traces
                set using q1/median/q3.
            dy
                Sets the y coordinate step for multi-box traces
                set using q1/median/q3.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.box.Hoverlabel`
                instance or dict with compatible properties
            hoveron
                Do the hover effects highlight individual boxes
                or sample points or both?
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            jitter
                Sets the amount of jitter in the sample points
                drawn. If 0, the sample points align along the
                distribution axis. If 1, the sample points are
                drawn in a random jitter of width equal to the
                width of the box(es).
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`plotly.graph_objects.box.Line` instance
                or dict with compatible properties
            lowerfence
                Sets the lower fence values. There should be as
                many items as the number of boxes desired. This
                attribute has effect only under the
                q1/median/q3 signature. If `lowerfence` is not
                provided but a sample (in `y` or `x`) is set,
                we compute the lower as the last sample point
                below 1.5 times the IQR.
            lowerfencesrc
                Sets the source reference on plot.ly for
                lowerfence .
            marker
                :class:`plotly.graph_objects.box.Marker`
                instance or dict with compatible properties
            mean
                Sets the mean values. There should be as many
                items as the number of boxes desired. This
                attribute has effect only under the
                q1/median/q3 signature. If `mean` is not
                provided but a sample (in `y` or `x`) is set,
                we compute the mean for each box using the
                sample values.
            meansrc
                Sets the source reference on plot.ly for  mean
                .
            median
                Sets the median values. There should be as many
                items as the number of boxes desired.
            mediansrc
                Sets the source reference on plot.ly for
                median .
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover. For box traces,
                the name will also be used for the position
                coordinate, if `x` and `x0` (`y` and `y0` if
                horizontal) are missing and the position axis
                is categorical
            notched
                Determines whether or not notches are drawn.
                Notches displays a confidence interval around
                the median. We compute the confidence interval
                as median +/- 1.57 * IQR / sqrt(N), where IQR
                is the interquartile range and N is the sample
                size. If two boxes' notches do not overlap
                there is 95% confidence their medians differ.
                See https://sites.google.com/site/davidsstatist
                ics/home/notched-box-plots for more info.
                Defaults to False unless `notchwidth` or
                `notchspan` is set.
            notchspan
                Sets the notch span from the boxes' `median`
                values. There should be as many items as the
                number of boxes desired. This attribute has
                effect only under the q1/median/q3 signature.
                If `notchspan` is not provided but a sample (in
                `y` or `x`) is set, we compute it as 1.57 * IQR
                / sqrt(N), where N is the sample size.
            notchspansrc
                Sets the source reference on plot.ly for
                notchspan .
            notchwidth
                Sets the width of the notches relative to the
                box' width. For example, with 0, the notches
                are as wide as the box(es).
            offsetgroup
                Set several traces linked to the same position
                axis or matching axes to the same offsetgroup
                where bars of the same position coordinate will
                line up.
            opacity
                Sets the opacity of the trace.
            orientation
                Sets the orientation of the box(es). If "v"
                ("h"), the distribution is visualized along the
                vertical (horizontal).
            pointpos
                Sets the position of the sample points in
                relation to the box(es). If 0, the sample
                points are places over the center of the
                box(es). Positive (negative) values correspond
                to positions to the right (left) for vertical
                boxes and above (below) for horizontal boxes
            q1
                Sets the Quartile 1 values. There should be as
                many items as the number of boxes desired.
            q1src
                Sets the source reference on plot.ly for  q1 .
            q3
                Sets the Quartile 3 values. There should be as
                many items as the number of boxes desired.
            q3src
                Sets the source reference on plot.ly for  q3 .
            quartilemethod
                Sets the method used to compute the sample's Q1
                and Q3 quartiles. The "linear" method uses the
                25th percentile for Q1 and 75th percentile for
                Q3 as computed using method #10 (listed on http
                ://www.amstat.org/publications/jse/v14n3/langfo
                rd.html). The "exclusive" method uses the
                median to divide the ordered dataset into two
                halves if the sample is odd, it does not
                include the median in either half - Q1 is then
                the median of the lower half and Q3 the median
                of the upper half. The "inclusive" method also
                uses the median to divide the ordered dataset
                into two halves but if the sample is odd, it
                includes the median in both halves - Q1 is then
                the median of the lower half and Q3 the median
                of the upper half.
            sd
                Sets the standard deviation values. There
                should be as many items as the number of boxes
                desired. This attribute has effect only under
                the q1/median/q3 signature. If `sd` is not
                provided but a sample (in `y` or `x`) is set,
                we compute the standard deviation for each box
                using the sample values.
            sdsrc
                Sets the source reference on plot.ly for  sd .
            selected
                :class:`plotly.graph_objects.box.Selected`
                instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.box.Stream`
                instance or dict with compatible properties
            text
                Sets the text elements associated with each
                sample value. If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to the this trace's (x,y) coordinates. To be
                seen, trace `hoverinfo` must contain a "text"
                flag.
            textsrc
                Sets the source reference on plot.ly for  text
                .
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
            unselected
                :class:`plotly.graph_objects.box.Unselected`
                instance or dict with compatible properties
            upperfence
                Sets the upper fence values. There should be as
                many items as the number of boxes desired. This
                attribute has effect only under the
                q1/median/q3 signature. If `upperfence` is not
                provided but a sample (in `y` or `x`) is set,
                we compute the lower as the last sample point
                above 1.5 times the IQR.
            upperfencesrc
                Sets the source reference on plot.ly for
                upperfence .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            whiskerwidth
                Sets the width of the whiskers relative to the
                box' width. For example, with 1, the whiskers
                are as wide as the box(es).
            width
                Sets the width of the box in data coordinate If
                0 (default value) the width is automatically
                selected based on the positions of other box
                traces in the same subplot.
            x
                Sets the x sample data or coordinates. See
                overview for more info.
            x0
                Sets the x coordinate for single-box traces or
                the starting coordinate for multi-box traces
                set using q1/median/q3. See overview for more
                info.
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
                Sets the source reference on plot.ly for  x .
            y
                Sets the y sample data or coordinates. See
                overview for more info.
            y0
                Sets the y coordinate for single-box traces or
                the starting coordinate for multi-box traces
                set using q1/median/q3. See overview for more
                info.
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
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BarpolarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="barpolar", parent_name="", **kwargs):
        super(BarpolarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Barpolar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            base
                Sets where the bar base is drawn (in radial
                axis units). In "stack" barmode, traces that
                set "base" will be excluded and drawn in
                "overlay" mode instead.
            basesrc
                Sets the source reference on plot.ly for  base
                .
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dr
                Sets the r coordinate step.
            dtheta
                Sets the theta coordinate step. By default, the
                `dtheta` step equals the subplot's period
                divided by the length of the `r` coordinates.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.barpolar.Hoverlabe
                l` instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.barpolar.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            offset
                Shifts the angular position where the bar is
                drawn (in "thetatunit" units).
            offsetsrc
                Sets the source reference on plot.ly for
                offset .
            opacity
                Sets the opacity of the trace.
            r
                Sets the radial coordinates
            r0
                Alternate to `r`. Builds a linear space of r
                coordinates. Use with `dr` where `r0` is the
                starting coordinate and `dr` the step.
            rsrc
                Sets the source reference on plot.ly for  r .
            selected
                :class:`plotly.graph_objects.barpolar.Selected`
                instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.barpolar.Stream`
                instance or dict with compatible properties
            subplot
                Sets a reference between this trace's data
                coordinates and a polar subplot. If "polar"
                (the default value), the data refer to
                `layout.polar`. If "polar2", the data refer to
                `layout.polar2`, and so on.
            text
                Sets hover text elements associated with each
                bar. If a single string, the same string
                appears over all bars. If an array of string,
                the items are mapped in order to the this
                trace's coordinates.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            theta
                Sets the angular coordinates
            theta0
                Alternate to `theta`. Builds a linear space of
                theta coordinates. Use with `dtheta` where
                `theta0` is the starting coordinate and
                `dtheta` the step.
            thetasrc
                Sets the source reference on plot.ly for  theta
                .
            thetaunit
                Sets the unit of input "theta" values. Has an
                effect only when on "linear" angular axes.
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
            unselected
                :class:`plotly.graph_objects.barpolar.Unselecte
                d` instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            width
                Sets the bar angular width (in "thetaunit"
                units).
            widthsrc
                Sets the source reference on plot.ly for  width
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="bar", parent_name="", **kwargs):
        super(BarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Bar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            alignmentgroup
                Set several traces linked to the same position
                axis or matching axes to the same
                alignmentgroup. This controls whether bars
                compute their positional range dependently or
                independently.
            base
                Sets where the bar base is drawn (in position
                axis units). In "stack" or "relative" barmode,
                traces that set "base" will be excluded and
                drawn in "overlay" mode instead.
            basesrc
                Sets the source reference on plot.ly for  base
                .
            cliponaxis
                Determines whether the text nodes are clipped
                about the subplot axes. To show the text nodes
                above axis lines and tick labels, make sure to
                set `xaxis.layer` and `yaxis.layer` to *below
                traces*.
            constraintext
                Constrain the size of text inside or outside a
                bar to be no larger than the bar itself.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dx
                Sets the x coordinate step. See `x0` for more
                info.
            dy
                Sets the y coordinate step. See `y0` for more
                info.
            error_x
                :class:`plotly.graph_objects.bar.ErrorX`
                instance or dict with compatible properties
            error_y
                :class:`plotly.graph_objects.bar.ErrorY`
                instance or dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.bar.Hoverlabel`
                instance or dict with compatible properties
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
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `value` and `label`. Anything
                contained in tag `<extra>` is displayed in the
                secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            hovertext
                Sets hover text elements associated with each
                (x,y) pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. To be seen,
                trace `hoverinfo` must contain a "text" flag.
            hovertextsrc
                Sets the source reference on plot.ly for
                hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            insidetextanchor
                Determines if texts are kept at center or
                start/end points in `textposition` "inside"
                mode.
            insidetextfont
                Sets the font used for `text` lying inside the
                bar.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.bar.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            offset
                Shifts the position where the bar is drawn (in
                position axis units). In "group" barmode,
                traces that set "offset" will be excluded and
                drawn in "overlay" mode instead.
            offsetgroup
                Set several traces linked to the same position
                axis or matching axes to the same offsetgroup
                where bars of the same position coordinate will
                line up.
            offsetsrc
                Sets the source reference on plot.ly for
                offset .
            opacity
                Sets the opacity of the trace.
            orientation
                Sets the orientation of the bars. With "v"
                ("h"), the value of the each bar spans along
                the vertical (horizontal).
            outsidetextfont
                Sets the font used for `text` lying outside the
                bar.
            r
                r coordinates in scatter traces are
                deprecated!Please switch to the "scatterpolar"
                trace type.Sets the radial coordinatesfor
                legacy polar chart only.
            rsrc
                Sets the source reference on plot.ly for  r .
            selected
                :class:`plotly.graph_objects.bar.Selected`
                instance or dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.bar.Stream`
                instance or dict with compatible properties
            t
                t coordinates in scatter traces are
                deprecated!Please switch to the "scatterpolar"
                trace type.Sets the angular coordinatesfor
                legacy polar chart only.
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textangle
                Sets the angle of the tick labels with respect
                to the bar. For example, a `tickangle` of -90
                draws the tick labels vertically. With "auto"
                the texts may automatically be rotated to fit
                with the maximum size in bars.
            textfont
                Sets the font used for `text`.
            textposition
                Specifies the location of the `text`. "inside"
                positions `text` inside, next to the bar end
                (rotated and scaled if needed). "outside"
                positions `text` outside, next to the bar end
                (scaled if needed), unless there is another bar
                stacked on this one, then the text gets pushed
                inside. "auto" tries to position `text` inside
                the bar, but if the bar is too small and no bar
                is stacked on this one the text is moved
                outside.
            textpositionsrc
                Sets the source reference on plot.ly for
                textposition .
            textsrc
                Sets the source reference on plot.ly for  text
                .
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. Dates are
                formatted using d3-time-format's syntax
                %{variable|d3-time-format}, for example "Day:
                %{2019-01-01|%A}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                for details on the date formatting syntax.
                Every attributes that can be specified per-
                point (the ones that are `arrayOk: true`) are
                available. variables `value` and `label`.
            texttemplatesrc
                Sets the source reference on plot.ly for
                texttemplate .
            tsrc
                Sets the source reference on plot.ly for  t .
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
            unselected
                :class:`plotly.graph_objects.bar.Unselected`
                instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            width
                Sets the bar width (in position axis units).
            widthsrc
                Sets the source reference on plot.ly for  width
                .
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
                Sets the source reference on plot.ly for  x .
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
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class AreaValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="area", parent_name="", **kwargs):
        super(AreaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Area"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                :class:`plotly.graph_objects.area.Hoverlabel`
                instance or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                :class:`plotly.graph_objects.area.Marker`
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
                Sets the source reference on plot.ly for  meta
                .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            r
                Area traces are deprecated! Please switch to
                the "barpolar" trace type. Sets the radial
                coordinates for legacy polar chart only.
            rsrc
                Sets the source reference on plot.ly for  r .
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.area.Stream`
                instance or dict with compatible properties
            t
                Area traces are deprecated! Please switch to
                the "barpolar" trace type. Sets the angular
                coordinates for legacy polar chart only.
            tsrc
                Sets the source reference on plot.ly for  t .
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
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FramesValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="frames", parent_name="", **kwargs):
        super(FramesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Frame"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            baseframe
                The name of the frame into which this frame's
                properties are merged before applying. This is
                used to unify properties and avoid needing to
                specify the same values for the same properties
                in multiple frames.
            data
                A list of traces this frame modifies. The
                format is identical to the normal trace
                definition.
            group
                An identifier that specifies the group to which
                the frame belongs, used by animate to select a
                subset of frames.
            layout
                Layout properties which this frame modifies.
                The format is identical to the normal layout
                definition.
            name
                A label by which to identify the frame
            traces
                A list of trace indices that identify the
                respective traces in the data attribute
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class DataValidator(_plotly_utils.basevalidators.BaseDataValidator):
    def __init__(self, plotly_name="data", parent_name="", **kwargs):

        super(DataValidator, self).__init__(
            class_strs_map={
                "area": "Area",
                "bar": "Bar",
                "barpolar": "Barpolar",
                "box": "Box",
                "candlestick": "Candlestick",
                "carpet": "Carpet",
                "choropleth": "Choropleth",
                "choroplethmapbox": "Choroplethmapbox",
                "cone": "Cone",
                "contour": "Contour",
                "contourcarpet": "Contourcarpet",
                "densitymapbox": "Densitymapbox",
                "funnel": "Funnel",
                "funnelarea": "Funnelarea",
                "heatmap": "Heatmap",
                "heatmapgl": "Heatmapgl",
                "histogram": "Histogram",
                "histogram2d": "Histogram2d",
                "histogram2dcontour": "Histogram2dContour",
                "image": "Image",
                "indicator": "Indicator",
                "isosurface": "Isosurface",
                "mesh3d": "Mesh3d",
                "ohlc": "Ohlc",
                "parcats": "Parcats",
                "parcoords": "Parcoords",
                "pie": "Pie",
                "pointcloud": "Pointcloud",
                "sankey": "Sankey",
                "scatter": "Scatter",
                "scatter3d": "Scatter3d",
                "scattercarpet": "Scattercarpet",
                "scattergeo": "Scattergeo",
                "scattergl": "Scattergl",
                "scattermapbox": "Scattermapbox",
                "scatterpolar": "Scatterpolar",
                "scatterpolargl": "Scatterpolargl",
                "scatterternary": "Scatterternary",
                "splom": "Splom",
                "streamtube": "Streamtube",
                "sunburst": "Sunburst",
                "surface": "Surface",
                "table": "Table",
                "treemap": "Treemap",
                "violin": "Violin",
                "volume": "Volume",
                "waterfall": "Waterfall",
            },
            plotly_name=plotly_name,
            parent_name=parent_name,
            **kwargs
        )
