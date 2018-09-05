import _plotly_utils.basevalidators


class ScatterternaryValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='scatterternary', parent_name='', **kwargs):
        super(ScatterternaryValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Scatterternary',
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
            c
                Sets the quantity of component `a` in each data
                point. If `a`, `b`, and `c` are all provided,
                they need not be normalized, only the relative
                values matter. If only two arrays are provided
                they must be normalized to match
                `ternary<i>.sum`.
            cliponaxis
                Determines whether or not markers and text
                nodes are clipped about the subplot axes. To
                show markers and text nodes above axis lines
                and tick labels, make sure to set `xaxis.layer`
                and `yaxis.layer` to *below traces*.
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            csrc
                Sets the source reference on plot.ly for  c .
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
                plotly.graph_objs.scatterternary.Hoverlabel
                instance or dict with compatible properties
            hoveron
                Do the hover effects highlight individual
                points (markers or line points) or do they
                highlight filled regions? If the fill is
                "toself" or "tonext" and there are no markers
                or text, then the default is "fills", otherwise
                it is "points".
            hovertext
                Sets hover text elements associated with each
                (a,b,c) point. If a single string, the same
                string appears over all the data points. If an
                array of strings, the items are mapped in order
                to the the data points in (a,b,c). To be seen,
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
                plotly.graph_objs.scatterternary.Line instance
                or dict with compatible properties
            marker
                plotly.graph_objs.scatterternary.Marker
                instance or dict with compatible properties
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
                plotly.graph_objs.scatterternary.Selected
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
                plotly.graph_objs.scatterternary.Stream
                instance or dict with compatible properties
            subplot
                Sets a reference between this trace's data
                coordinates and a ternary subplot. If "ternary"
                (the default value), the data refer to
                `layout.ternary`. If "ternary2", the data refer
                to `layout.ternary2`, and so on.
            sum
                The number each triplet should sum to, if only
                two of `a`, `b`, and `c` are provided. This
                overrides `ternary<i>.sum` to normalize this
                specific trace, but does not affect the values
                displayed on the axes. 0 (or missing) means to
                use ternary<i>.sum
            text
                Sets text elements associated with each (a,b,c)
                point. If a single string, the same string
                appears over all the data points. If an array
                of strings, the items are mapped in order to
                the the data points in (a,b,c). If trace
                `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
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
                plotly.graph_objs.scatterternary.Unselected
                instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            **kwargs
        )
