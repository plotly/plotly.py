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


import _plotly_utils.basevalidators


class ScaleValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="scale", parent_name="layout.geo.projection", **kwargs
    ):
        super(ScaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RotationValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="rotation", parent_name="layout.geo.projection", **kwargs
    ):
        super(RotationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Rotation"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            lat
                Rotates the map along meridians (in degrees
                North).
            lon
                Rotates the map along parallels (in degrees
                East). Defaults to the center of the
                `lonaxis.range` values.
            roll
                Roll the map (in degrees) For example, a roll
                of 180 makes the map appear upside down.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ParallelsValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(
        self, plotly_name="parallels", parent_name="layout.geo.projection", **kwargs
    ):
        super(ParallelsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            items=kwargs.pop(
                "items",
                [
                    {"valType": "number", "editType": "plot"},
                    {"valType": "number", "editType": "plot"},
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
