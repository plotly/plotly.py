import _plotly_utils.basevalidators


class ScatterpolarValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='scatterpolar', parent_name='', **kwargs):
        super(ScatterpolarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Scatterpolar'),
            data_docs=kwargs.pop(
                'data_docs', """
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
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dr
                Sets the r coordinate step.
            dtheta
                Sets the theta coordinate step. By default, the
                `dtheta` step equals the subplot's period
                divided by the length of the `r` coordinates.
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". scatterpolar
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
                plotly.graph_objs.scatterpolar.Hoverlabel
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
                plotly.graph_objs.scatterpolar.Line instance or
                dict with compatible properties
            marker
                plotly.graph_objs.scatterpolar.Marker instance
                or dict with compatible properties
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover. If there are less than 20
                points and the trace is not stacked then the
                default is "lines+markers". Otherwise, "lines".
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            r
                Sets the radial coordinates
            r0
                Alternate to `r`. Builds a linear space of r
                coordinates. Use with `dr` where `r0` is the
                starting coordinate and `dr` the step.
            rsrc
                Sets the source reference on plot.ly for  r .
            selected
                plotly.graph_objs.scatterpolar.Selected
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
                plotly.graph_objs.scatterpolar.Stream instance
                or dict with compatible properties
            subplot
                Sets a reference between this trace's data
                coordinates and a polar subplot. If "polar"
                (the default value), the data refer to
                `layout.polar`. If "polar2", the data refer to
                `layout.polar2`, and so on.
            text
                Sets text elements associated with each (x,y)
                pair. If a single string, the same string
                appears over all the data points. If an array
                of string, the items are mapped in order to the
                this trace's (x,y) coordinates. If trace
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
            theta
                Sets the angular coordinates
            theta0
                Alternate to `theta`. Builds a linear space of
                theta coordinates. Use with `dtheta` where
                `theta0` is the starting coordinate and
                `dtheta` the step.
            thetasrc
                Sets the source reference on plot.ly for  theta
                .
            thetaunit
                Sets the unit of input "theta" values. Has an
                effect only when on "linear" angular axes.
            uid

            unselected
                plotly.graph_objs.scatterpolar.Unselected
                instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
"""
            ),
            **kwargs
        )
