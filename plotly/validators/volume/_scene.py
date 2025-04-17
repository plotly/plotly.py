import _plotly_utils.basevalidators as _bv


class SceneValidator(_bv.SubplotidValidator):
    def __init__(self, plotly_name="scene", parent_name="volume", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            dflt=kwargs.pop("dflt", "scene"),
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            **kwargs,
        )
