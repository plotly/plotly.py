import _plotly_utils.basevalidators


class RadialAxisValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='radialaxis', parent_name='layout', **kwargs
    ):
        super(RadialAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='RadialAxis',
            data_docs="""
            domain
                Polar chart subplots are not supported yet.
                This key has currently no effect.
            endpadding

            orientation
                Sets the orientation (an angle with respect to
                the origin) of the radial axis.
            range
                Defines the start and end point of this radial
                axis.
            showline
                Determines whether or not the line bounding
                this radial axis will be shown on the figure.
            showticklabels
                Determines whether or not the radial axis ticks
                will feature tick labels.
            tickcolor
                Sets the color of the tick lines on this radial
                axis.
            ticklen
                Sets the length of the tick lines on this
                radial axis.
            tickorientation
                Sets the orientation (from the paper
                perspective) of the radial axis tick labels.
            ticksuffix
                Sets the length of the tick lines on this
                radial axis.
            visible
                Determines whether or not this axis will be
                visible.
""",
            **kwargs
        )
