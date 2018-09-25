import _plotly_utils.basevalidators


class CandlestickValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='candlestick', parent_name='', **kwargs):
        super(CandlestickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Candlestick'),
            data_docs=kwargs.pop(
                'data_docs', """
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
                plotly.graph_objs.candlestick.Decreasing
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
                plotly.graph_objs.candlestick.Hoverlabel
                instance or dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            increasing
                plotly.graph_objs.candlestick.Increasing
                instance or dict with compatible properties
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                plotly.graph_objs.candlestick.Line instance or
                dict with compatible properties
            low
                Sets the low values.
            lowsrc
                Sets the source reference on plot.ly for  low .
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
                plotly.graph_objs.candlestick.Stream instance
                or dict with compatible properties
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
"""
            ),
            **kwargs
        )
