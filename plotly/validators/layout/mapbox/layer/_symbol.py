import _plotly_utils.basevalidators


class SymbolValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self,
        plotly_name='symbol',
        parent_name='layout.mapbox.layer',
        **kwargs
    ):
        super(SymbolValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Symbol',
            data_docs="""
            icon
                Sets the symbol icon image. Full list:
                https://www.mapbox.com/maki-icons/
            iconsize
                Sets the symbol icon size. Has an effect only
                when `type` is set to "symbol".
            text
                Sets the symbol text.
            textfont
                Sets the icon text font. Has an effect only
                when `type` is set to "symbol".
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
""",
            **kwargs
        )
