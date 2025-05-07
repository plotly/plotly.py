#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ZValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="z", parent_name="layout.scene.camera.center", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "camera"),
            **kwargs,
        )
