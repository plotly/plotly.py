import _plotly_utils.basevalidators as _bv


class TextinfoValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="textinfo", parent_name="funnel", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "plot"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop(
                "flags",
                [
                    "label",
                    "text",
                    "percent initial",
                    "percent previous",
                    "percent total",
                    "value",
                ],
            ),
            **kwargs,
        )
