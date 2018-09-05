import _plotly_utils.basevalidators


class AngularAxisValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='angularaxis', parent_name='layout', **kwargs
    ):
        super(AngularAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='AngularAxis',
            data_docs="""
            domain
                Polar chart subplots are not supported yet.
                This key has currently no effect.
            endpadding

            range
                Defines the start and end point of this angular
                axis.
            showline
                Determines whether or not the line bounding
                this angular axis will be shown on the figure.
            showticklabels
                Determines whether or not the angular axis
                ticks will feature tick labels.
            tickcolor
                Sets the color of the tick lines on this
                angular axis.
            ticklen
                Sets the length of the tick lines on this
                angular axis.
            tickorientation
                Sets the orientation (from the paper
                perspective) of the angular axis tick labels.
            ticksuffix
                Sets the length of the tick lines on this
                angular axis.
            visible
                Determines whether or not this axis will be
                visible.
""",
            **kwargs
        )
