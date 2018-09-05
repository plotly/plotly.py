import _plotly_utils.basevalidators


class XBinsValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='xbins', parent_name='histogram2d', **kwargs
    ):
        super(XBinsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='XBins',
            data_docs="""
            end
                Sets the end value for the x axis bins.
            size
                Sets the step in-between value each x axis bin.
            start
                Sets the starting value for the x axis bins.
""",
            **kwargs
        )
