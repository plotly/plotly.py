import _plotly_utils.basevalidators


class ButtonsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):

    def __init__(
        self,
        plotly_name='buttons',
        parent_name='layout.xaxis.rangeselector',
        **kwargs
    ):
        super(ButtonsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Button',
            data_docs="""
            count
                Sets the number of steps to take to update the
                range. Use with `step` to specify the update
                interval.
            label
                Sets the text label to appear on the button.
            step
                The unit of measurement that the `count` value
                will set the range by.
            stepmode
                Sets the range update mode. If *backward*, the
                range update shifts the start of range back
                *count* times *step* milliseconds. If *todate*,
                the range update shifts the start of range back
                to the first timestamp from *count* times
                *step* milliseconds back. For example, with
                `step` set to *year* and `count` set to *1* the
                range update shifts the start of the range back
                to January 01 of the current year. Month and
                year *todate* are currently available only for
                the built-in (Gregorian) calendar.""",
            **kwargs
        )
