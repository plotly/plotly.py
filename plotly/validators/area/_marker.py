import _plotly_utils.basevalidators


class MarkerValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='marker', parent_name='area', **kwargs):
        super(MarkerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Marker',
            data_docs="""
            color
                Sets themarkercolor. It accepts either a
                specific color or an array of numbers that are
                mapped to the colorscale relative to the max
                and min values of the array or relative to
                `marker.cmin` and `marker.cmax` if set.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            opacity
                Sets the marker opacity.
            opacitysrc
                Sets the source reference on plot.ly for
                opacity .
            size
                Sets the marker size (in px).
            sizesrc
                Sets the source reference on plot.ly for  size
                .
            symbol
                Sets the marker symbol type. Adding 100 is
                equivalent to appending "-open" to a symbol
                name. Adding 200 is equivalent to appending
                "-dot" to a symbol name. Adding 300 is
                equivalent to appending "-open-dot" or "dot-
                open" to a symbol name.
            symbolsrc
                Sets the source reference on plot.ly for
                symbol .
""",
            **kwargs
        )
