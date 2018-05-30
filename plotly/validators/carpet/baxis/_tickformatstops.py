import _plotly_utils.basevalidators


class TickformatstopsValidator(
    _plotly_utils.basevalidators.CompoundArrayValidator
):

    def __init__(
        self,
        plotly_name='tickformatstops',
        parent_name='carpet.baxis',
        **kwargs
    ):
        super(TickformatstopsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Tickformatstop',
            data_docs="""
            dtickrange
                range [*min*, *max*], where *min*, *max* -
                dtick values which describe some zoom level, it
                is possible to omit *min* or *max* value by
                passing *null*
            value
                string - dtickformat for described zoom level,
                the same as *tickformat*""",
            **kwargs
        )
