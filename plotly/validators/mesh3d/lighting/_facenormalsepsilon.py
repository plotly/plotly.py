import _plotly_utils.basevalidators


class FacenormalsepsilonValidator(
    _plotly_utils.basevalidators.NumberValidator
):

    def __init__(
        self,
        plotly_name='facenormalsepsilon',
        parent_name='mesh3d.lighting',
        **kwargs
    ):
        super(FacenormalsepsilonValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
