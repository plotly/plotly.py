import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="uirevision", parent_name="layout.modebar", **kwargs
    ):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OrientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="orientation", parent_name="layout.modebar", **kwargs
    ):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["v", "h"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="color", parent_name="layout.modebar", **kwargs):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="bgcolor", parent_name="layout.modebar", **kwargs):
        super(BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ActivecolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="activecolor", parent_name="layout.modebar", **kwargs
    ):
        super(ActivecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
