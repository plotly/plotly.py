import _plotly_utils.basevalidators


class TilingValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="tiling", parent_name="icicle", **kwargs):
        super(TilingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tiling"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            flip
                Determines if the positions obtained from
                solver are flipped on each axis.
            orientation
                Sets the orientation of the icicle. With "v"
                the icicle grows vertically. With "h" the
                icicle grows horizontally.
            pad
                Sets the inner padding (in px).
""",
            ),
            **kwargs
        )
