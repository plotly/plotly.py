import _plotly_utils.basevalidators as _bv


class OperationValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="operation", parent_name="contour.contours", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values",
                [
                    "=",
                    "<",
                    ">=",
                    ">",
                    "<=",
                    "[]",
                    "()",
                    "[)",
                    "(]",
                    "][",
                    ")(",
                    "](",
                    ")[",
                ],
            ),
            **kwargs,
        )
