import _plotly_utils.basevalidators as _bv


class XcalendarValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="xcalendar", parent_name="ohlc", **kwargs):
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
