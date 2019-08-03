import _plotly_utils.basevalidators


class ValueformatValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="valueformat", parent_name="indicator.delta", **kwargs
    ):
        super(ValueformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RelativeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="relative", parent_name="indicator.delta", **kwargs):
        super(RelativeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ReferenceValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="reference", parent_name="indicator.delta", **kwargs
    ):
        super(ReferenceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PositionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="position", parent_name="indicator.delta", **kwargs):
        super(PositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["top", "bottom", "left", "right"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class IncreasingValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="increasing", parent_name="indicator.delta", **kwargs
    ):
        super(IncreasingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Increasing"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color for increasing value.
            symbol
                Sets the symbol to display for increasing value
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="font", parent_name="indicator.delta", **kwargs):
        super(FontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Font"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The plotly service (at https://plot.ly
                or on-premise) generates images on a server,
                where only a select number of fonts are
                installed and supported. These include "Arial",
                "Balto", "Courier New", "Droid Sans",, "Droid
                Serif", "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            size

""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class DecreasingValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="decreasing", parent_name="indicator.delta", **kwargs
    ):
        super(DecreasingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Decreasing"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color for increasing value.
            symbol
                Sets the symbol to display for increasing value
""",
            ),
            **kwargs
        )
