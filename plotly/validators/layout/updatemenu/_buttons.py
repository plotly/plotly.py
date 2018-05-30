import _plotly_utils.basevalidators


class ButtonsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):

    def __init__(
        self, plotly_name='buttons', parent_name='layout.updatemenu', **kwargs
    ):
        super(ButtonsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Button',
            data_docs="""
            args
                Sets the arguments values to be passed to the
                Plotly method set in `method` on click.
            execute
                When true, the API method is executed. When
                false, all other behaviors are the same and
                command execution is skipped. This may be
                useful when hooking into, for example, the
                `plotly_buttonclicked` method and executing the
                API command manually without losing the benefit
                of the updatemenu automatically binding to the
                state of the plot through the specification of
                `method` and `args`.
            label
                Sets the text label to appear on the button.
            method
                Sets the Plotly method to be called on click.
                If the `skip` method is used, the API
                updatemenu will function as normal but will
                perform no API calls and will not bind
                automatically to state updates. This may be
                used to create a component interface and attach
                to updatemenu events manually via JavaScript.""",
            **kwargs
        )
