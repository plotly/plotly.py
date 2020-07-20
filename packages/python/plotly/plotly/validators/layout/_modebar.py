import _plotly_utils.basevalidators


class ModebarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="modebar", parent_name="layout", **kwargs):
        super(ModebarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Modebar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            activecolor
                Sets the color of the active or hovered on
                icons in the modebar.
            bgcolor
                Sets the background color of the modebar.
            color
                Sets the color of the icons in the modebar.
            orientation
                Sets the orientation of the modebar.
            uirevision
                Controls persistence of user-driven changes
                related to the modebar, including `hovermode`,
                `dragmode`, and `showspikes` at both the root
                level and inside subplots. Defaults to
                `layout.uirevision`.
""",
            ),
            **kwargs
        )
