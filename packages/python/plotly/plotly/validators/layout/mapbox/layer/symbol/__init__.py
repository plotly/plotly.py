import _plotly_utils.basevalidators


class TextpositionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="textposition",
        parent_name="layout.mapbox.layer.symbol",
        **kwargs
    ):
        super(TextpositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop(
                "values",
                [
                    "top left",
                    "top center",
                    "top right",
                    "middle left",
                    "middle center",
                    "middle right",
                    "bottom left",
                    "bottom center",
                    "bottom right",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="textfont", parent_name="layout.mapbox.layer.symbol", **kwargs
    ):
        super(TextfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Textfont"),
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
                system. The Chart Studio Cloud (at
                https://chart-studio.plotly.com or on-premise)
                generates images on a server, where only a
                select number of fonts are installed and
                supported. These include "Arial", "Balto",
                "Courier New", "Droid Sans",, "Droid Serif",
                "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            size

""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="text", parent_name="layout.mapbox.layer.symbol", **kwargs
    ):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PlacementValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="placement",
        parent_name="layout.mapbox.layer.symbol",
        **kwargs
    ):
        super(PlacementValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["point", "line", "line-center"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class IconsizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="iconsize", parent_name="layout.mapbox.layer.symbol", **kwargs
    ):
        super(IconsizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class IconValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="icon", parent_name="layout.mapbox.layer.symbol", **kwargs
    ):
        super(IconValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
