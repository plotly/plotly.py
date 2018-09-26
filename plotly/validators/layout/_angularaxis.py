import _plotly_utils.basevalidators


class AngularAxisValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='angularaxis', parent_name='layout', **kwargs
    ):
        super(AngularAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'AngularAxis'),
            data_docs=kwargs.pop(
                'data_docs', """
            domain
                Polar chart subplots are not supported yet.
                This key has currently no effect.
            endpadding
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots.
            range
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Defines the start
                and end point of this angular axis.
            showline
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not the line bounding this angular axis will
                be shown on the figure.
            showticklabels
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not the angular axis ticks will feature tick
                labels.
            tickcolor
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the color of
                the tick lines on this angular axis.
            ticklen
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the length of
                the tick lines on this angular axis.
            tickorientation
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the
                orientation (from the paper perspective) of the
                angular axis tick labels.
            ticksuffix
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the length of
                the tick lines on this angular axis.
            visible
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not this axis will be visible.
"""
            ),
            **kwargs
        )
