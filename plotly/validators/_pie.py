import _plotly_utils.basevalidators


class PieValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='pie', parent_name='', **kwargs):
        super(PieValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Pie',
            data_docs="""
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
                plotly.graph_objs.pie.Domain instance or dict
                with compatible properties
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
                plotly.graph_objs.pie.Hoverlabel instance or
                dict with compatible properties
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
                the pie.
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
                plotly.graph_objs.pie.Marker instance or dict
                with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            outsidetextfont
                Sets the font used for `textinfo` lying outside
                the pie.
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
                If there are multiple pies that should be sized
                according to their totals, link them by
                providing a non-empty group id here shared by
                every trace in the same group.
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
            sort
                Determines whether or not the sectors are
                reordered from largest to smallest.
            stream
                plotly.graph_objs.pie.Stream instance or dict
                with compatible properties
            text
                Sets text elements associated with each sector.
                If trace `textinfo` contains a "text" flag,
                these elements will seen on the chart. If trace
                `hoverinfo` contains a "text" flag and
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
            uid

            values
                Sets the values of the sectors of this pie
                chart. If omitted, we count occurrences of each
                label.
            valuessrc
                Sets the source reference on plot.ly for
                values .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            **kwargs
        )
