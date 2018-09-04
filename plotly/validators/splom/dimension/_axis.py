import _plotly_utils.basevalidators


class AxisValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='axis', parent_name='splom.dimension', **kwargs
    ):
        super(AxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Axis',
            data_docs="""
            type
                Sets the axis type for this dimension's
                generated x and y axes. Note that the axis
                `type` values set in layout take precedence
                over this attribute.
""",
            **kwargs
        )
