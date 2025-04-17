import _plotly_utils.basevalidators as _bv


class ColoringValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="coloring",
        parent_name="histogram2dcontour.contours",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["fill", "heatmap", "lines", "none"]),
            **kwargs,
        )
