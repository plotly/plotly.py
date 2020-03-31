import _plotly_utils.basevalidators


class YanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yanchor", parent_name="layout.slider", **kwargs):
        super(YanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "top", "middle", "bottom"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="y", parent_name="layout.slider", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            max=kwargs.pop("max", 3),
            min=kwargs.pop("min", -2),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xanchor", parent_name="layout.slider", **kwargs):
        super(XanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "left", "center", "right"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="x", parent_name="layout.slider", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            max=kwargs.pop("max", 3),
            min=kwargs.pop("min", -2),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="visible", parent_name="layout.slider", **kwargs):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TransitionValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="transition", parent_name="layout.slider", **kwargs):
        super(TransitionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Transition"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            duration
                Sets the duration of the slider transition
            easing
                Sets the easing function of the slider
                transition
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="tickwidth", parent_name="layout.slider", **kwargs):
        super(TickwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TicklenValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="ticklen", parent_name="layout.slider", **kwargs):
        super(TicklenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="tickcolor", parent_name="layout.slider", **kwargs):
        super(TickcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateitemnameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="templateitemname", parent_name="layout.slider", **kwargs
    ):
        super(TemplateitemnameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StepValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="stepdefaults", parent_name="layout.slider", **kwargs
    ):
        super(StepValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Step"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class StepsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="steps", parent_name="layout.slider", **kwargs):
        super(StepsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Step"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            args
                Sets the arguments values to be passed to the
                Plotly method set in `method` on slide.
            execute
                When true, the API method is executed. When
                false, all other behaviors are the same and
                command execution is skipped. This may be
                useful when hooking into, for example, the
                `plotly_sliderchange` method and executing the
                API command manually without losing the benefit
                of the slider automatically binding to the
                state of the plot through the specification of
                `method` and `args`.
            label
                Sets the text label to appear on the slider
            method
                Sets the Plotly method to be called when the
                slider value is changed. If the `skip` method
                is used, the API slider will function as normal
                but will perform no API calls and will not bind
                automatically to state updates. This may be
                used to create a component interface and attach
                to slider events manually via JavaScript.
            name
                When used in a template, named items are
                created in the output figure in addition to any
                items the figure already has in this array. You
                can modify these items in the output figure by
                making your own item with `templateitemname`
                matching this `name` alongside your
                modifications (including `visible: false` or
                `enabled: false` to hide it). Has no effect
                outside of a template.
            templateitemname
                Used to refer to a named item in this array in
                the template. Named items from the template
                will be created even without a matching item in
                the input figure, but you can modify one by
                making an item with `templateitemname` matching
                its `name`, alongside your modifications
                (including `visible: false` or `enabled: false`
                to hide it). If there is no template or no
                matching item, this item will be hidden unless
                you explicitly show it with `visible: true`.
            value
                Sets the value of the slider step, used to
                refer to the step programatically. Defaults to
                the slider label if not provided.
            visible
                Determines whether or not this step is included
                in the slider.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class PadValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="pad", parent_name="layout.slider", **kwargs):
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


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="name", parent_name="layout.slider", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MinorticklenValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="minorticklen", parent_name="layout.slider", **kwargs
    ):
        super(MinorticklenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LenmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="lenmode", parent_name="layout.slider", **kwargs):
        super(LenmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["fraction", "pixels"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class LenValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="len", parent_name="layout.slider", **kwargs):
        super(LenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="font", parent_name="layout.slider", **kwargs):
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


import _plotly_utils.basevalidators


class CurrentvalueValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="currentvalue", parent_name="layout.slider", **kwargs
    ):
        super(CurrentvalueValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Currentvalue"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            font
                Sets the font of the current value label text.
            offset
                The amount of space, in pixels, between the
                current value label and the slider.
            prefix
                When currentvalue.visible is true, this sets
                the prefix of the label.
            suffix
                When currentvalue.visible is true, this sets
                the suffix of the label.
            visible
                Shows the currently-selected value above the
                slider.
            xanchor
                The alignment of the value readout relative to
                the length of the slider.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BorderwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="borderwidth", parent_name="layout.slider", **kwargs
    ):
        super(BorderwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BordercolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="bordercolor", parent_name="layout.slider", **kwargs
    ):
        super(BordercolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="bgcolor", parent_name="layout.slider", **kwargs):
        super(BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ActivebgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="activebgcolor", parent_name="layout.slider", **kwargs
    ):
        super(ActivebgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ActiveValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="active", parent_name="layout.slider", **kwargs):
        super(ActiveValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
