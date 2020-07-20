import _plotly_utils.basevalidators


class DeltaValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="delta", parent_name="indicator", **kwargs):
        super(DeltaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Delta"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            decreasing
                :class:`plotly.graph_objects.indicator.delta.De
                creasing` instance or dict with compatible
                properties
            font
                Set the font used to display the delta
            increasing
                :class:`plotly.graph_objects.indicator.delta.In
                creasing` instance or dict with compatible
                properties
            position
                Sets the position of delta with respect to the
                number.
            reference
                Sets the reference value to compute the delta.
                By default, it is set to the current value.
            relative
                Show relative change
            valueformat
                Sets the value formatting rule using d3
                formatting mini-language which is similar to
                those of Python. See
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
""",
            ),
            **kwargs
        )
