import _plotly_utils.basevalidators


class HoverlabelValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='hoverlabel', parent_name='histogram2d', **kwargs
    ):
        super(HoverlabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Hoverlabel',
            data_docs="""
            bgcolor
                Sets the background color of the hover labels
                for this trace
            bgcolorsrc
                Sets the source reference on plot.ly for
                bgcolor .
            bordercolor
                Sets the border color of the hover labels for
                this trace.
            bordercolorsrc
                Sets the source reference on plot.ly for
                bordercolor .
            font
                Sets the font used in hover labels.
            namelength
                Sets the length (in number of characters) of
                the trace name in the hover labels for this
                trace. -1 shows the whole name regardless of
                length. 0-3 shows the first 0-3 characters, and
                an integer >3 will show the whole name if it is
                less than that many characters, but if it is
                longer, will truncate to `namelength - 3`
                characters and add an ellipsis.
            namelengthsrc
                Sets the source reference on plot.ly for
                namelength .
""",
            **kwargs
        )
