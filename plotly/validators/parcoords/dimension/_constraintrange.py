import _plotly_utils.basevalidators


class ConstraintrangeValidator(
    _plotly_utils.basevalidators.InfoArrayValidator
):

    def __init__(
        self,
        plotly_name='constraintrange',
        parent_name='parcoords.dimension',
        **kwargs
    ):
        super(ConstraintrangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dimensions='1-2',
            edit_type='calc',
            free_length=True,
            items=[
                {
                    'valType': 'number',
                    'editType': 'calc'
                }, {
                    'valType': 'number',
                    'editType': 'calc'
                }
            ],
            role='info',
            **kwargs
        )
