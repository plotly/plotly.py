import _plotly_utils.basevalidators


class BoxValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='box', parent_name='', **kwargs):
        super(BoxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Box',
            data_docs="""
            boxmean
                If True, the mean of the box(es)' underlying
                distribution is drawn as a dashed line inside
                the box(es). If "sd" the standard deviation is
                also drawn.
            boxpoints
                If "outliers", only the sample points lying
                outside the whiskers are shown If
                "suspectedoutliers", the outlier points are
                shown and points either less than 4*Q1-3*Q3 or
                greater than 4*Q3-3*Q1 are highlighted (see
                `outliercolor`) If "all", all sample points are
                shown If False, only the box(es) are shown with
                no sample points
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
                plotly.graph_objs.box.Hoverlabel instance or
                dict with compatible properties
            hoveron
                Do the hover effects highlight individual boxes
                or sample points or both?
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
                plotly.graph_objs.box.Line instance or dict
                with compatible properties
            marker
                plotly.graph_objs.box.Marker instance or dict
                with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover. For box traces,
                the name will also be used for the position
                coordinate, if `x` and `x0` (`y` and `y0` if
                horizontal) are missing and the position axis
                is categorical
            notched
                Determines whether or not notches should be
                drawn.
            notchwidth
                Sets the width of the notches relative to the
                box' width. For example, with 0, the notches
                are as wide as the box(es).
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
            selected
                plotly.graph_objs.box.Selected instance or dict
                with compatible properties
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
                plotly.graph_objs.box.Stream instance or dict
                with compatible properties
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

            unselected
                plotly.graph_objs.box.Unselected instance or
                dict with compatible properties
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
                Sets the x sample data or coordinates. See
                overview for more info.
            x0
                Sets the x coordinate of the box. See overview
                for more info.
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
                Sets the y coordinate of the box. See overview
                for more info.
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
            **kwargs
        )
