import _plotly_utils.basevalidators


class StartsValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='starts', parent_name='streamtube', **kwargs
    ):
        super(StartsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Starts',
            data_docs="""
            x
                Sets the x components of the starting position
                of the streamtubes
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y components of the starting position
                of the streamtubes
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the z components of the starting position
                of the streamtubes
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            **kwargs
        )
