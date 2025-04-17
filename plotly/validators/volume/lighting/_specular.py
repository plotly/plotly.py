import _plotly_utils.basevalidators as _bv


class SpecularValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="specular", parent_name="volume.lighting", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 2),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
