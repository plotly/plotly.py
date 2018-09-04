import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='line', parent_name='layout.mapbox.layer', **kwargs
    ):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Line',
            data_docs="""
            width
                Sets the line width. Has an effect only when
                `type` is set to "line".
""",
            **kwargs
        )
