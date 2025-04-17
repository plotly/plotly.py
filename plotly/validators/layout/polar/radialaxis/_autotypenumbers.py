import _plotly_utils.basevalidators as _bv


class AutotypenumbersValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="autotypenumbers",
        parent_name="layout.polar.radialaxis",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["convert types", "strict"]),
            **kwargs,
        )
