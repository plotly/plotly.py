import _plotly_utils.basevalidators as _bv


class CalendarValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="calendar", parent_name="layout.yaxis", **kwargs):
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
