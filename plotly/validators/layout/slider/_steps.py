import _plotly_utils.basevalidators


class StepsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):

    def __init__(
        self, plotly_name='steps', parent_name='layout.slider', **kwargs
    ):
        super(StepsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Step',
            data_docs="""
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
            value
                Sets the value of the slider step, used to
                refer to the step programatically. Defaults to
                the slider label if not provided.""",
            **kwargs
        )
