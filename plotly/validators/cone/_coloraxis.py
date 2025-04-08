#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ColoraxisValidator(_bv.SubplotidValidator):
    def __init__(self, plotly_name="coloraxis", parent_name="cone", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            dflt=kwargs.pop("dflt", None),
            edit_type=kwargs.pop("edit_type", "calc"),
            regex=kwargs.pop("regex", "/^coloraxis([2-9]|[1-9][0-9]+)?$/"),
            **kwargs,
        )
