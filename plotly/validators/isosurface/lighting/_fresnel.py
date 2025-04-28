#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class FresnelValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="fresnel", parent_name="isosurface.lighting", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 5),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
