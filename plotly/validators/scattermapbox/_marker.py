import _plotly_utils.basevalidators


class MarkerValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='marker', parent_name='scattermapbox', **kwargs
    ):
        super(MarkerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Marker',
            data_docs="""
            autocolorscale
                Has an effect only if `marker.color` is set to
                a numerical array. Determines whether the
                colorscale is a default palette
                (`autocolorscale: true`) or the palette
                determined by `marker.colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            cauto
                Has an effect only if `marker.color` is set to
                a numerical array and `cmin`, `cmax` are set by
                the user. In this case, it controls whether the
                range of colors in `colorscale` is mapped to
                the range of values in the `color` array
                (`cauto: true`), or the `cmin`/`cmax` values
                (`cauto: false`). Defaults to `false` when
                `cmin`, `cmax` are set by the user.
            cmax
                Has an effect only if `marker.color` is set to
                a numerical array. Sets the upper bound of the
                color domain. Value should be associated to the
                `marker.color` array index, and if set,
                `marker.cmin` must be set as well.
            cmin
                Has an effect only if `marker.color` is set to
                a numerical array. Sets the lower bound of the
                color domain. Value should be associated to the
                `marker.color` array index, and if set,
                `marker.cmax` must be set as well.
            color
                Sets the marker color. It accepts either a
                specific color or an array of numbers that are
                mapped to the colorscale relative to the max
                and min values of the array or relative to
                `cmin` and `cmax` if set.
            colorbar
                plotly.graph_objs.scattermapbox.marker.ColorBar
                instance or dict with compatible properties
            colorscale
                Sets the colorscale and only has an effect if
                `marker.color` is set to a numerical array. The
                colorscale must be an array containing arrays
                mapping a normalized value to an rgb, rgba,
                hex, hsl, hsv, or named color string. At
                minimum, a mapping for the lowest (0) and
                highest (1) values are required. For example,
                `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To
                control the bounds of the colorscale in color
                space, use `marker.cmin` and `marker.cmax`.
                Alternatively, `colorscale` may be a palette
                name string of the following list: Greys,
                YlGnBu, Greens, YlOrRd, Bluered, RdBu, Reds,
                Blues, Picnic, Rainbow, Portland, Jet, Hot,
                Blackbody, Earth, Electric, Viridis, Cividis
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            opacity
                Sets the marker opacity.
            opacitysrc
                Sets the source reference on plot.ly for
                opacity .
            reversescale
                Has an effect only if `marker.color` is set to
                a numerical array. Reverses the color mapping
                if true (`cmin` will correspond to the last
                color in the array and `cmax` will correspond
                to the first color).
            showscale
                Has an effect only if `marker.color` is set to
                a numerical array. Determines whether or not a
                colorbar is displayed.
            size
                Sets the marker size (in px).
            sizemin
                Has an effect only if `marker.size` is set to a
                numerical array. Sets the minimum size (in px)
                of the rendered marker points.
            sizemode
                Has an effect only if `marker.size` is set to a
                numerical array. Sets the rule for which the
                data in `size` is converted to pixels.
            sizeref
                Has an effect only if `marker.size` is set to a
                numerical array. Sets the scale factor used to
                determine the rendered size of marker points.
                Use with `sizemin` and `sizemode`.
            sizesrc
                Sets the source reference on plot.ly for  size
                .
            symbol
                Sets the marker symbol. Full list:
                https://www.mapbox.com/maki-icons/ Note that
                the array `marker.color` and `marker.size` are
                only available for *circle* symbols.
            symbolsrc
                Sets the source reference on plot.ly for
                symbol .""",
            **kwargs
        )
