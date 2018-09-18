import _plotly_utils.basevalidators


class PointcloudValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='pointcloud', parent_name='', **kwargs):
        super(PointcloudValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Pointcloud',
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
                plotly.graph_objs.pointcloud.Hoverlabel
                instance or dict with compatible properties
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
                plotly.graph_objs.pointcloud.Marker instance or
                dict with compatible properties
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
                plotly.graph_objs.pointcloud.Stream instance or
                dict with compatible properties
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
            **kwargs
        )
