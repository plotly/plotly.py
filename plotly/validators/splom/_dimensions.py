import _plotly_utils.basevalidators


class DimensionsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):

    def __init__(
        self, plotly_name='dimensions', parent_name='splom', **kwargs
    ):
        super(DimensionsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Dimension',
            data_docs="""
            label
                Sets the label corresponding to this splom
                dimension.
            values
                Sets the dimension values to be plotted.
            valuessrc
                Sets the source reference on plot.ly for
                values .
            visible
                Determines whether or not this dimension is
                shown on the graph. Note that even visible
                false dimension contribute to the default grid
                generate by this splom trace.""",
            **kwargs
        )
