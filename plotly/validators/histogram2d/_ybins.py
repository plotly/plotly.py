import _plotly_utils.basevalidators


class YBinsValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='ybins', parent_name='histogram2d', **kwargs
    ):
        super(YBinsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='YBins',
            data_docs="""
            end
                Sets the end value for the y axis bins.
            size
                Sets the step in-between value each y axis bin.
            start
                Sets the starting value for the y axis bins.
""",
            **kwargs
        )
