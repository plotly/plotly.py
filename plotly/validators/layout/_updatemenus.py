import _plotly_utils.basevalidators


class UpdatemenusValidator(
    _plotly_utils.basevalidators.CompoundArrayValidator
):

    def __init__(
        self, plotly_name='updatemenus', parent_name='layout', **kwargs
    ):
        super(UpdatemenusValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Updatemenu',
            data_docs="""
            active
                Determines which button (by index starting from
                0) is considered active.
            bgcolor
                Sets the background color of the update menu
                buttons.
            bordercolor
                Sets the color of the border enclosing the
                update menu.
            borderwidth
                Sets the width (in px) of the border enclosing
                the update menu.
            buttons
                plotly.graph_objs.layout.updatemenu.Button
                instance or dict with compatible properties
            direction
                Determines the direction in which the buttons
                are laid out, whether in a dropdown menu or a
                row/column of buttons. For `left` and `up`, the
                buttons will still appear in left-to-right or
                top-to-bottom order respectively.
            font
                Sets the font of the update menu button text.
            pad
                Sets the padding around the buttons or dropdown
                menu.
            showactive
                Highlights active dropdown item or active
                button if true.
            type
                Determines whether the buttons are accessible
                via a dropdown menu or whether the buttons are
                stacked horizontally or vertically
            visible
                Determines whether or not the update menu is
                visible.
            x
                Sets the x position (in normalized coordinates)
                of the update menu.
            xanchor
                Sets the update menu's horizontal position
                anchor. This anchor binds the `x` position to
                the *left*, *center* or *right* of the range
                selector.
            y
                Sets the y position (in normalized coordinates)
                of the update menu.
            yanchor
                Sets the update menu's vertical position anchor
                This anchor binds the `y` position to the
                *top*, *middle* or *bottom* of the range
                selector.""",
            **kwargs
        )
