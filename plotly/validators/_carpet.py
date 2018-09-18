import _plotly_utils.basevalidators


class CarpetValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='carpet', parent_name='', **kwargs):
        super(CarpetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Carpet',
            data_docs="""
            a
                An array containing values of the first
                parameter value
            a0
                Alternate to `a`. Builds a linear space of a
                coordinates. Use with `da` where `a0` is the
                starting coordinate and `da` the step.
            aaxis
                plotly.graph_objs.carpet.Aaxis instance or dict
                with compatible properties
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
                plotly.graph_objs.carpet.Baxis instance or dict
                with compatible properties
            bsrc
                Sets the source reference on plot.ly for  b .
            carpet
                An identifier for this carpet, so that
                `scattercarpet` and `scattercontour` traces can
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
                plotly.graph_objs.carpet.Hoverlabel instance or
                dict with compatible properties
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
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
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
                plotly.graph_objs.carpet.Stream instance or
                dict with compatible properties
            uid

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
            **kwargs
        )
