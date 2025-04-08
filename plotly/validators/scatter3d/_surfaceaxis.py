#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SurfaceaxisValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="surfaceaxis", parent_name="scatter3d", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", [-1, 0, 1, 2]),
            **kwargs,
        )
