import _plotly_utils.basevalidators


class WidthsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="widthsrc", parent_name="scatterternary.marker.line", **kwargs
    ):
        super(WidthsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="width", parent_name="scatterternary.marker.line", **kwargs
    ):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ReversescaleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self,
        plotly_name="reversescale",
        parent_name="scatterternary.marker.line",
        **kwargs
    ):
        super(ReversescaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="colorsrc", parent_name="scatterternary.marker.line", **kwargs
    ):
        super(ColorsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorscaleValidator(_plotly_utils.basevalidators.ColorscaleValidator):
    def __init__(
        self,
        plotly_name="colorscale",
        parent_name="scatterternary.marker.line",
        **kwargs
    ):
        super(ColorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"autocolorscale": False}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColoraxisValidator(_plotly_utils.basevalidators.SubplotidValidator):
    def __init__(
        self,
        plotly_name="coloraxis",
        parent_name="scatterternary.marker.line",
        **kwargs
    ):
        super(ColoraxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt=kwargs.pop("dflt", None),
            edit_type=kwargs.pop("edit_type", "calc"),
            regex=kwargs.pop("regex", "/^coloraxis([2-9]|[1-9][0-9]+)?$/"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="color", parent_name="scatterternary.marker.line", **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "style"),
            colorscale_path=kwargs.pop(
                "colorscale_path", "scatterternary.marker.line.colorscale"
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CminValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="cmin", parent_name="scatterternary.marker.line", **kwargs
    ):
        super(CminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"cauto": False}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CmidValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="cmid", parent_name="scatterternary.marker.line", **kwargs
    ):
        super(CmidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CmaxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="cmax", parent_name="scatterternary.marker.line", **kwargs
    ):
        super(CmaxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"cauto": False}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CautoValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="cauto", parent_name="scatterternary.marker.line", **kwargs
    ):
        super(CautoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AutocolorscaleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self,
        plotly_name="autocolorscale",
        parent_name="scatterternary.marker.line",
        **kwargs
    ):
        super(AutocolorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
