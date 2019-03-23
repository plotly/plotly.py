

import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='width', parent_name='scatter3d.line', **kwargs
    ):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            anim=kwargs.pop('anim', True),
            edit_type=kwargs.pop('edit_type', 'calc'),
            min=kwargs.pop('min', 0),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowscaleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='showscale', parent_name='scatter3d.line', **kwargs
    ):
        super(ShowscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class ReversescaleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='reversescale',
        parent_name='scatter3d.line',
        **kwargs
    ):
        super(ReversescaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )


import _plotly_utils.basevalidators


class DashValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='dash', parent_name='scatter3d.line', **kwargs
    ):
        super(DashValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'style'),
            values=kwargs.pop(
                'values',
                ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorsrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(
        self, plotly_name='colorsrc', parent_name='scatter3d.line', **kwargs
    ):
        super(ColorsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'none'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorscaleValidator(_plotly_utils.basevalidators.ColorscaleValidator):

    def __init__(
        self, plotly_name='colorscale', parent_name='scatter3d.line', **kwargs
    ):
        super(ColorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            implied_edits=kwargs.pop(
                'implied_edits', {'autocolorscale': False}
            ),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self, plotly_name='color', parent_name='scatter3d.line', **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop('array_ok', True),
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'style'),
            colorscale_path=kwargs.pop(
                'colorscale_path', 'scatter3d.line.colorscale'
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CminValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='cmin', parent_name='scatter3d.line', **kwargs
    ):
        super(CminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            implied_edits=kwargs.pop('implied_edits', {'cauto': False}),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class CmidValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='cmid', parent_name='scatter3d.line', **kwargs
    ):
        super(CmidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            implied_edits=kwargs.pop('implied_edits', {}),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class CmaxValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='cmax', parent_name='scatter3d.line', **kwargs
    ):
        super(CmaxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            implied_edits=kwargs.pop('implied_edits', {'cauto': False}),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class CautoValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='cauto', parent_name='scatter3d.line', **kwargs
    ):
        super(CautoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            implied_edits=kwargs.pop('implied_edits', {}),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class AutocolorscaleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='autocolorscale',
        parent_name='scatter3d.line',
        **kwargs
    ):
        super(AutocolorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            implied_edits=kwargs.pop('implied_edits', {}),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )
