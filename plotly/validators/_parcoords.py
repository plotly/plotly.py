import _plotly_utils.basevalidators


class ParcoordsValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='parcoords', parent_name='', **kwargs):
        super(ParcoordsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Parcoords'),
            data_docs=kwargs.pop(
                'data_docs', """
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            dimensions
                The dimensions (variables) of the parallel
                coordinates chart. 2..60 dimensions are
                supported.
            dimensiondefaults
                When used in a template (as layout.template.dat
                a.parcoords.dimensiondefaults), sets the
                default property values to use for elements of
                parcoords.dimensions
            domain
                plotly.graph_objs.parcoords.Domain instance or
                dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            labelfont
                Sets the font for the `dimension` labels.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                plotly.graph_objs.parcoords.Line instance or
                dict with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            rangefont
                Sets the font for the `dimension` range values.
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
                plotly.graph_objs.parcoords.Stream instance or
                dict with compatible properties
            tickfont
                Sets the font for the `dimension` tick values.
            uid

            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
"""
            ),
            **kwargs
        )
