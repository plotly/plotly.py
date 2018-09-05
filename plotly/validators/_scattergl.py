import _plotly_utils.basevalidators


class ScatterglValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='scattergl', parent_name='', **kwargs):
        super(ScatterglValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Scattergl',
            data_docs="""
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
                plotly.graph_objs.scattergl.ErrorX instance or
                dict with compatible properties
            error_y
                plotly.graph_objs.scattergl.ErrorY instance or
                dict with compatible properties
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". "tozerox" and
                "tozeroy" fill to x=0 and y=0 respectively.
                "tonextx" and "tonexty" fill between the
                endpoints of this trace and the endpoints of
                the trace before it, connecting those endpoints
                with straight lines (to make a stacked area
                graph); if there is no trace before it, they
                behave like "tozerox" and "tozeroy". "toself"
                connects the endpoints of the trace (or each
                segment of the trace if it has gaps) into a
                closed shape. "tonext" fills the space between
                two traces if one completely encloses the other
                (eg consecutive contour lines), and behaves
                like "toself" if there is no trace before it.
                "tonext" should not be used if one trace does
                not enclose the other.
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
                plotly.graph_objs.scattergl.Hoverlabel instance
                or dict with compatible properties
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
                plotly.graph_objs.scattergl.Line instance or
                dict with compatible properties
            marker
                plotly.graph_objs.scattergl.Marker instance or
                dict with compatible properties
            mode
                Determines the drawing mode for this scatter
                trace.
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                plotly.graph_objs.scattergl.Selected instance
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
                plotly.graph_objs.scattergl.Stream instance or
                dict with compatible properties
            text
                Sets text elements associated with each (x,y)
                pair to appear on hover. If a single string,
                the same string appears over all the data
                points. If an array of string, the items are
                mapped in order to the this trace's (x,y)
                coordinates.
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
            uid

            unselected
                plotly.graph_objs.scattergl.Unselected instance
                or dict with compatible properties
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
            **kwargs
        )
