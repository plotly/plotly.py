import _plotly_utils.basevalidators as _bv


class TextinfoValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="textinfo", parent_name="sunburst", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop(
                "flags",
                [
                    "label",
                    "text",
                    "value",
                    "current path",
                    "percent root",
                    "percent entry",
                    "percent parent",
                ],
            ),
            **kwargs,
        )
