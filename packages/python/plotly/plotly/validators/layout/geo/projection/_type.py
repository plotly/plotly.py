import _plotly_utils.basevalidators


class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="type", parent_name="layout.geo.projection", **kwargs
    ):
        super(TypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                [
                    "equirectangular",
                    "mercator",
                    "orthographic",
                    "natural earth",
                    "kavrayskiy7",
                    "miller",
                    "robinson",
                    "eckert4",
                    "azimuthal equal area",
                    "azimuthal equidistant",
                    "conic equal area",
                    "conic conformal",
                    "conic equidistant",
                    "gnomonic",
                    "stereographic",
                    "mollweide",
                    "hammer",
                    "transverse mercator",
                    "albers usa",
                    "winkel tripel",
                    "aitoff",
                    "sinusoidal",
                ],
            ),
            **kwargs
        )
