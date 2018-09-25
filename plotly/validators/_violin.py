import _plotly_utils.basevalidators


class ViolinValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='violin', parent_name='', **kwargs):
        super(ViolinValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Violin'),
            data_docs=kwargs.pop(
                'data_docs', """
            bandwidth
                Sets the bandwidth used to compute the kernel
                density estimate. By default, the bandwidth is
                determined by Silverman's rule of thumb.
            box
                plotly.graph_objs.violin.Box instance or dict
                with compatible properties
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
                plotly.graph_objs.violin.Hoverlabel instance or
                dict with compatible properties
            hoveron
                Do the hover effects highlight individual
                violins or sample points or the kernel density
                estimate or any combination of them?
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
                plotly.graph_objs.violin.Line instance or dict
                with compatible properties
            marker
                plotly.graph_objs.violin.Marker instance or
                dict with compatible properties
            meanline
                plotly.graph_objs.violin.Meanline instance or
                dict with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover. For box traces,
                the name will also be used for the position
                coordinate, if `x` and `x0` (`y` and `y0` if
                horizontal) are missing and the position axis
                is categorical
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
                no sample points
            scalegroup
                If there are multiple violins that should be
                sized according to to some metric (see
                `scalemode`), link them by providing a non-
                empty group id here shared by every trace in
                the same group.
            scalemode
                Sets the metric by which the width of each
                violin is determined."width" means each violin
                has the same (max) width*count* means the
                violins are scaled by the number of sample
                points makingup each violin.
            selected
                plotly.graph_objs.violin.Selected instance or
                dict with compatible properties
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
                plotly.graph_objs.violin.Stream instance or
                dict with compatible properties
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
                plotly.graph_objs.violin.Unselected instance or
                dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
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
            ysrc
                Sets the source reference on plot.ly for  y .
"""
            ),
            **kwargs
        )
