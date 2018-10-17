import _plotly_utils.basevalidators


class BarpolarValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='barpolar', parent_name='', **kwargs):
        super(BarpolarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Barpolar'),
            data_docs=kwargs.pop(
                'data_docs', """
            base
                Sets where the bar base is drawn (in radial
                axis units). In "stack" barmode, traces that
                set "base" will be excluded and drawn in
                "overlay" mode instead.
            basesrc
                Sets the source reference on plot.ly for  base
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
            dr
                Sets the r coordinate step.
            dtheta
                Sets the theta coordinate step. By default, the
                `dtheta` step equals the subplot's period
                divided by the length of the `r` coordinates.
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
                plotly.graph_objs.barpolar.Hoverlabel instance
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
                plotly.graph_objs.barpolar.Marker instance or
                dict with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            offset
                Shifts the angular position where the bar is
                drawn (in "thetatunit" units).
            offsetsrc
                Sets the source reference on plot.ly for
                offset .
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
                plotly.graph_objs.barpolar.Selected instance or
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
            stream
                plotly.graph_objs.barpolar.Stream instance or
                dict with compatible properties
            subplot
                Sets a reference between this trace's data
                coordinates and a polar subplot. If "polar"
                (the default value), the data refer to
                `layout.polar`. If "polar2", the data refer to
                `layout.polar2`, and so on.
            text
                Sets hover text elements associated with each
                bar. If a single string, the same string
                appears over all bars. If an array of string,
                the items are mapped in order to the this
                trace's coordinates.
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
                plotly.graph_objs.barpolar.Unselected instance
                or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            width
                Sets the bar angular width (in "thetaunit"
                units).
            widthsrc
                Sets the source reference on plot.ly for  width
                .
"""
            ),
            **kwargs
        )
