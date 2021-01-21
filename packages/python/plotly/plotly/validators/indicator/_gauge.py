import _plotly_utils.basevalidators


class GaugeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="gauge", parent_name="indicator", **kwargs):
        super(GaugeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Gauge"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            axis
                :class:`plotly.graph_objects.indicator.gauge.Ax
                is` instance or dict with compatible properties
            bar
                Set the appearance of the gauge's value
            bgcolor
                Sets the gauge background color.
            bordercolor
                Sets the color of the border enclosing the
                gauge.
            borderwidth
                Sets the width (in px) of the border enclosing
                the gauge.
            shape
                Set the shape of the gauge
            steps
                :class:`plotly.graph_objects.indicator.gauge.St
                eps` instance or dict with compatible
                properties
            threshold
                :class:`plotly.graph_objects.indicator.gauge.Th
                reshold` instance or dict with compatible
                properties
""",
            ),
            **kwargs
        )
