import _plotly_utils.basevalidators


class YrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yref", parent_name="layout.title", **kwargs):
        super(YrefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["container", "paper"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yanchor", parent_name="layout.title", **kwargs):
        super(YanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "top", "middle", "bottom"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="y", parent_name="layout.title", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xref", parent_name="layout.title", **kwargs):
        super(XrefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["container", "paper"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xanchor", parent_name="layout.title", **kwargs):
        super(XanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "left", "center", "right"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="x", parent_name="layout.title", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="text", parent_name="layout.title", **kwargs):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PadValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="pad", parent_name="layout.title", **kwargs):
        super(PadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Pad"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            b
                The amount of padding (in px) along the bottom
                of the component.
            l
                The amount of padding (in px) on the left side
                of the component.
            r
                The amount of padding (in px) on the right side
                of the component.
            t
                The amount of padding (in px) along the top of
                the component.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="font", parent_name="layout.title", **kwargs):
        super(FontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Font"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The Chart Studio Cloud (at
                https://chart-studio.plotly.com or on-premise)
                generates images on a server, where only a
                select number of fonts are installed and
                supported. These include "Arial", "Balto",
                "Courier New", "Droid Sans",, "Droid Serif",
                "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            size

""",
            ),
            **kwargs
        )
