import _plotly_utils.basevalidators


class ScattercarpetValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='scattercarpet', parent_name='', **kwargs):
        super(ScattercarpetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Scattercarpet',
            data_docs="""
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
            carpet
                An identifier for this carpet, so that
                `scattercarpet` and `scattercontour` traces can
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
                plotly.graph_objs.scattercarpet.Hoverlabel
                instance or dict with compatible properties
            hoveron
                Do the hover effects highlight individual
                points (markers or line points) or do they
                highlight filled regions? If the fill is
                "toself" or "tonext" and there are no markers
                or text, then the default is "fills", otherwise
                it is "points".
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
                plotly.graph_objs.scattercarpet.Line instance
                or dict with compatible properties
            marker
                plotly.graph_objs.scattercarpet.Marker instance
                or dict with compatible properties
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points, then the default is "lines+markers".
                Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                plotly.graph_objs.scattercarpet.Selected
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
                plotly.graph_objs.scattercarpet.Stream instance
                or dict with compatible properties
            text
                Sets text elements associated with each (a,b,c)
                point. If a single string, the same string
                appears over all the data points. If an array
                of strings, the items are mapped in order to
                the the data points in (a,b,c).
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
                plotly.graph_objs.scattercarpet.Unselected
                instance or dict with compatible properties
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
            **kwargs
        )
