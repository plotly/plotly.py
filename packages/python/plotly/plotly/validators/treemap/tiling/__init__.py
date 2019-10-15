import _plotly_utils.basevalidators


class SquarifyratioValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="squarifyratio", parent_name="treemap.tiling", **kwargs
    ):
        super(SquarifyratioValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PadValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="pad", parent_name="treemap.tiling", **kwargs):
        super(PadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PackingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="packing", parent_name="treemap.tiling", **kwargs):
        super(PackingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                ["squarify", "binary", "dice", "slice", "slice-dice", "dice-slice"],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FlipValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="flip", parent_name="treemap.tiling", **kwargs):
        super(FlipValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            flags=kwargs.pop("flags", ["x", "y"]),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
