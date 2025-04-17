import _plotly_utils.basevalidators as _bv


class LabelaliasValidator(_bv.AnyValidator):
    def __init__(
        self,
        plotly_name="labelalias",
        parent_name="scatter3d.marker.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
