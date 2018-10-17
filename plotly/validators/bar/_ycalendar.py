import _plotly_utils.basevalidators


class YcalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(self, plotly_name='ycalendar', parent_name='bar', **kwargs):
        super(YcalendarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            values=kwargs.pop(
                'values', [
                    'gregorian', 'chinese', 'coptic', 'discworld', 'ethiopian',
                    'hebrew', 'islamic', 'julian', 'mayan', 'nanakshahi',
                    'nepali', 'persian', 'jalali', 'taiwan', 'thai',
                    'ummalqura'
                ]
            ),
            **kwargs
        )
