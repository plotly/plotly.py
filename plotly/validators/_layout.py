import _plotly_utils.basevalidators


class LayoutValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='layout', parent_name='', **kwargs):
        super(LayoutValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Layout'),
            data_docs=kwargs.pop(
                'data_docs', """
            angularaxis
                plotly.graph_objs.layout.AngularAxis instance
                or dict with compatible properties
            annotations
                plotly.graph_objs.layout.Annotation instance or
                dict with compatible properties
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
                of adjacent location coordinates.
            boxgroupgap
                Sets the gap (in plot fraction) between boxes
                of the same location coordinate.
            boxmode
                Determines how boxes at the same location
                coordinate are displayed on the graph. If
                "group", the boxes are plotted next to one
                another centered around the shared location. If
                "overlay", the boxes are plotted over one
                another, you might need to set "opacity" to see
                them multiple boxes.
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
            font
                Sets the global font. Note that fonts used in
                traces and other layout components inherit from
                the global font.
            geo
                plotly.graph_objs.layout.Geo instance or dict
                with compatible properties
            grid
                plotly.graph_objs.layout.Grid instance or dict
                with compatible properties
            height
                Sets the plot's height (in px).
            hiddenlabels

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
                plotly.graph_objs.layout.Hoverlabel instance or
                dict with compatible properties
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
                plotly.graph_objs.layout.Image instance or dict
                with compatible properties
            imagedefaults
                When used in a template (as
                layout.template.layout.imagedefaults), sets the
                default property values to use for elements of
                layout.images
            legend
                plotly.graph_objs.layout.Legend instance or
                dict with compatible properties
            mapbox
                plotly.graph_objs.layout.Mapbox instance or
                dict with compatible properties
            margin
                plotly.graph_objs.layout.Margin instance or
                dict with compatible properties
            modebar
                plotly.graph_objs.layout.Modebar instance or
                dict with compatible properties
            orientation
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Rotates the entire
                polar by the given angle in legacy polar
                charts.
            paper_bgcolor
                Sets the color of paper where the graph is
                drawn.
            piecolorway
                Sets the default pie slice colors. Defaults to
                the main `colorway` used for trace colors. If
                you specify a new list here it can still be
                extended with lighter and darker colors, see
                `extendpiecolors`.
            plot_bgcolor
                Sets the color of plotting area in-between x
                and y axes.
            polar
                plotly.graph_objs.layout.Polar instance or dict
                with compatible properties
            radialaxis
                plotly.graph_objs.layout.RadialAxis instance or
                dict with compatible properties
            scene
                plotly.graph_objs.layout.Scene instance or dict
                with compatible properties
            selectdirection
                When "dragmode" is set to "select", this limits
                the selection of the drag to horizontal,
                vertical or diagonal. "h" only allows
                horizontal selection, "v" only vertical, "d"
                only diagonal and "any" sets no limit.
            separators
                Sets the decimal and thousand separators. For
                example, *. * puts a '.' before decimals and a
                space between thousands. In English locales,
                dflt is ".," but other locales may alter this
                default.
            shapes
                plotly.graph_objs.layout.Shape instance or dict
                with compatible properties
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
                plotly.graph_objs.layout.Slider instance or
                dict with compatible properties
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
                plotly.graph_objs.layout.Ternary instance or
                dict with compatible properties
            title
                Sets the plot's title.
            titlefont
                Sets the title font.
            updatemenus
                plotly.graph_objs.layout.Updatemenu instance or
                dict with compatible properties
            updatemenudefaults
                When used in a template (as
                layout.template.layout.updatemenudefaults),
                sets the default property values to use for
                elements of layout.updatemenus
            violingap
                Sets the gap (in plot fraction) between violins
                of adjacent location coordinates.
            violingroupgap
                Sets the gap (in plot fraction) between violins
                of the same location coordinate.
            violinmode
                Determines how violins at the same location
                coordinate are displayed on the graph. If
                "group", the violins are plotted next to one
                another centered around the shared location. If
                "overlay", the violins are plotted over one
                another, you might need to set "opacity" to see
                them multiple violins.
            width
                Sets the plot's width (in px).
            xaxis
                plotly.graph_objs.layout.XAxis instance or dict
                with compatible properties
            yaxis
                plotly.graph_objs.layout.YAxis instance or dict
                with compatible properties
"""
            ),
            **kwargs
        )
