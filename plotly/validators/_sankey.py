import _plotly_utils.basevalidators


class SankeyValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='sankey', parent_name='', **kwargs):
        super(SankeyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Sankey'),
            data_docs=kwargs.pop(
                'data_docs', """
            arrangement
                If value is `snap` (the default), the node
                arrangement is assisted by automatic snapping
                of elements to preserve space between nodes
                specified via `nodepad`. If value is
                `perpendicular`, the nodes can only move along
                a line perpendicular to the flow. If value is
                `freeform`, the nodes can freely move on the
                plane. If value is `fixed`, the nodes are
                stationary.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            domain
                plotly.graph_objs.sankey.Domain instance or
                dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired. Note that this attribute is superseded
                by `node.hoverinfo` and `node.hoverinfo` for
                nodes and links respectively.
            hoverlabel
                plotly.graph_objs.sankey.Hoverlabel instance or
                dict with compatible properties
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
            link
                The links of the Sankey plot.
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            node
                The nodes of the Sankey plot.
            opacity
                Sets the opacity of the trace.
            orientation
                Sets the orientation of the Sankey diagram.
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
                plotly.graph_objs.sankey.Stream instance or
                dict with compatible properties
            textfont
                Sets the font for node labels
            uid

            valueformat
                Sets the value formatting rule using d3
                formatting mini-language which is similar to
                those of Python. See https://github.com/d3/d3-f
                ormat/blob/master/README.md#locale_format
            valuesuffix
                Adds a unit to follow the value in the hover
                tooltip. Add a space if a separation is
                necessary from the value.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
"""
            ),
            **kwargs
        )
