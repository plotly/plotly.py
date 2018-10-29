import _plotly_utils.basevalidators


class HistogramValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='histogram', parent_name='', **kwargs):
        super(HistogramValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Histogram'),
            data_docs=kwargs.pop(
                'data_docs', """
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
            cumulative
                plotly.graph_objs.histogram.Cumulative instance
                or dict with compatible properties
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
                plotly.graph_objs.histogram.ErrorX instance or
                dict with compatible properties
            error_y
                plotly.graph_objs.histogram.ErrorY instance or
                dict with compatible properties
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
                plotly.graph_objs.histogram.Hoverlabel instance
                or dict with compatible properties
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
                plotly.graph_objs.histogram.Marker instance or
                dict with compatible properties
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
            orientation
                Sets the orientation of the bars. With "v"
                ("h"), the value of the each bar spans along
                the vertical (horizontal).
            selected
                plotly.graph_objs.histogram.Selected instance
                or dict with compatible properties
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
                plotly.graph_objs.histogram.Stream instance or
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

            unselected
                plotly.graph_objs.histogram.Unselected instance
                or dict with compatible properties
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
                plotly.graph_objs.histogram.XBins instance or
                dict with compatible properties
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
                plotly.graph_objs.histogram.YBins instance or
                dict with compatible properties
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
"""
            ),
            **kwargs
        )
