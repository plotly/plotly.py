import _plotly_utils.basevalidators as _bv


class FacenormalsepsilonValidator(_bv.NumberValidator):
    def __init__(
        self,
        plotly_name="facenormalsepsilon",
        parent_name="streamtube.lighting",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
