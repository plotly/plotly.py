#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class FamilyValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="family", parent_name="carpet.legendgrouptitle.font", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            no_blank=kwargs.pop("no_blank", True),
            strict=kwargs.pop("strict", True),
            **kwargs,
        )
