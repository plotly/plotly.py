import _plotly_utils.basevalidators


class RadialAxisValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='radialaxis', parent_name='layout', **kwargs
    ):
        super(RadialAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'RadialAxis'),
            data_docs=kwargs.pop(
                'data_docs', """
            domain
                Polar chart subplots are not supported yet.
                This key has currently no effect.
            endpadding
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots.
            orientation
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the
                orientation (an angle with respect to the
                origin) of the radial axis.
            range
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Defines the start
                and end point of this radial axis.
            showline
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not the line bounding this radial axis will
                be shown on the figure.
            showticklabels
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not the radial axis ticks will feature tick
                labels.
            tickcolor
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the color of
                the tick lines on this radial axis.
            ticklen
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the length of
                the tick lines on this radial axis.
            tickorientation
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the
                orientation (from the paper perspective) of the
                radial axis tick labels.
            ticksuffix
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Sets the length of
                the tick lines on this radial axis.
            visible
                Legacy polar charts are deprecated! Please
                switch to "polar" subplots. Determines whether
                or not this axis will be visible.
"""
            ),
            **kwargs
        )
