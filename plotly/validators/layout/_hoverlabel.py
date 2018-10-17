import _plotly_utils.basevalidators


class HoverlabelValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='hoverlabel', parent_name='layout', **kwargs
    ):
        super(HoverlabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Hoverlabel'),
            data_docs=kwargs.pop(
                'data_docs', """
            bgcolor
                Sets the background color of all hover labels
                on graph
            bordercolor
                Sets the border color of all hover labels on
                graph.
            font
                Sets the default hover label font used by all
                traces on the graph.
            namelength
                Sets the default length (in number of
                characters) of the trace name in the hover
                labels for all traces. -1 shows the whole name
                regardless of length. 0-3 shows the first 0-3
                characters, and an integer >3 will show the
                whole name if it is less than that many
                characters, but if it is longer, will truncate
                to `namelength - 3` characters and add an
                ellipsis.
"""
            ),
            **kwargs
        )
