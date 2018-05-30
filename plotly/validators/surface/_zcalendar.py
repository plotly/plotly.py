import _plotly_utils.basevalidators


class ZcalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='zcalendar', parent_name='surface', **kwargs
    ):
        super(ZcalendarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            values=[
                'gregorian', 'chinese', 'coptic', 'discworld', 'ethiopian',
                'hebrew', 'islamic', 'julian', 'mayan', 'nanakshahi', 'nepali',
                'persian', 'jalali', 'taiwan', 'thai', 'ummalqura'
            ],
            **kwargs
        )
