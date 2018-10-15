import _plotly_utils.basevalidators


class TableValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='table', parent_name='', **kwargs):
        super(TableValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Table'),
            data_docs=kwargs.pop(
                'data_docs', """
            cells
                plotly.graph_objs.table.Cells instance or dict
                with compatible properties
            columnorder
                Specifies the rendered order of the data
                columns; for example, a value `2` at position
                `0` means that column index `0` in the data
                will be rendered as the third column, as
                columns have an index base of zero.
            columnordersrc
                Sets the source reference on plot.ly for
                columnorder .
            columnwidth
                The width of columns expressed as a ratio.
                Columns fill the available width in proportion
                of their specified column widths.
            columnwidthsrc
                Sets the source reference on plot.ly for
                columnwidth .
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
                plotly.graph_objs.table.Domain instance or dict
                with compatible properties
            header
                plotly.graph_objs.table.Header instance or dict
                with compatible properties
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
                plotly.graph_objs.table.Hoverlabel instance or
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
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
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
                plotly.graph_objs.table.Stream instance or dict
                with compatible properties
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
