#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ZcalendarValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="zcalendar", parent_name="surface", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values",
                [
                    "chinese",
                    "coptic",
                    "discworld",
                    "ethiopian",
                    "gregorian",
                    "hebrew",
                    "islamic",
                    "jalali",
                    "julian",
                    "mayan",
                    "nanakshahi",
                    "nepali",
                    "persian",
                    "taiwan",
                    "thai",
                    "ummalqura",
                ],
            ),
            **kwargs,
        )
