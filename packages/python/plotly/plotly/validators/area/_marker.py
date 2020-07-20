import _plotly_utils.basevalidators


class MarkerValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="marker", parent_name="area", **kwargs):
        super(MarkerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Marker"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Area traces are deprecated! Please switch to
                the "barpolar" trace type. Sets themarkercolor.
                It accepts either a specific color or an array
                of numbers that are mapped to the colorscale
                relative to the max and min values of the array
                or relative to `marker.cmin` and `marker.cmax`
                if set.
            colorsrc
                Sets the source reference on Chart Studio Cloud
                for  color .
            opacity
                Area traces are deprecated! Please switch to
                the "barpolar" trace type. Sets the marker
                opacity.
            opacitysrc
                Sets the source reference on Chart Studio Cloud
                for  opacity .
            size
                Area traces are deprecated! Please switch to
                the "barpolar" trace type. Sets the marker size
                (in px).
            sizesrc
                Sets the source reference on Chart Studio Cloud
                for  size .
            symbol
                Area traces are deprecated! Please switch to
                the "barpolar" trace type. Sets the marker
                symbol type. Adding 100 is equivalent to
                appending "-open" to a symbol name. Adding 200
                is equivalent to appending "-dot" to a symbol
                name. Adding 300 is equivalent to appending
                "-open-dot" or "dot-open" to a symbol name.
            symbolsrc
                Sets the source reference on Chart Studio Cloud
                for  symbol .
""",
            ),
            **kwargs
        )
