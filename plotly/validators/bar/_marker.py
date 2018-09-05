import _plotly_utils.basevalidators


class MarkerValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='marker', parent_name='bar', **kwargs):
        super(MarkerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Marker',
            data_docs="""
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `marker.colorscale`. Has an
                effect only if in `marker.color`is set to a
                numerical array. In case `colorscale` is
                unspecified or `autocolorscale` is true, the
                default  palette will be chosen according to
                whether numbers in the `color` array are all
                positive, all negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `marker.color`) or the bounds set in
                `marker.cmin` and `marker.cmax`  Has an effect
                only if in `marker.color`is set to a numerical
                array. Defaults to `false` when `marker.cmin`
                and `marker.cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Has
                an effect only if in `marker.color`is set to a
                numerical array. Value should have the same
                units as in `marker.color` and if set,
                `marker.cmin` must be set as well.
            cmin
                Sets the lower bound of the color domain. Has
                an effect only if in `marker.color`is set to a
                numerical array. Value should have the same
                units as in `marker.color` and if set,
                `marker.cmax` must be set as well.
            color
                Sets themarkercolor. It accepts either a
                specific color or an array of numbers that are
                mapped to the colorscale relative to the max
                and min values of the array or relative to
                `marker.cmin` and `marker.cmax` if set.
            colorbar
                plotly.graph_objs.bar.marker.ColorBar instance
                or dict with compatible properties
            colorscale
                Sets the colorscale. Has an effect only if in
                `marker.color`is set to a numerical array. The
                colorscale must be an array containing arrays
                mapping a normalized value to an rgb, rgba,
                hex, hsl, hsv, or named color string. At
                minimum, a mapping for the lowest (0) and
                highest (1) values are required. For example,
                `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To
                control the bounds of the colorscale in color
                space, use`marker.cmin` and `marker.cmax`.
                Alternatively, `colorscale` may be a palette
                name string of the following list: Greys,YlGnBu
                ,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,R
                ainbow,Portland,Jet,Hot,Blackbody,Earth,Electri
                c,Viridis,Cividis.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            line
                plotly.graph_objs.bar.marker.Line instance or
                dict with compatible properties
            opacity
                Sets the opacity of the bars.
            opacitysrc
                Sets the source reference on plot.ly for
                opacity .
            reversescale
                Reverses the color mapping if true. Has an
                effect only if in `marker.color`is set to a
                numerical array. If true, `marker.cmin` will
                correspond to the last color in the array and
                `marker.cmax` will correspond to the first
                color.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace. Has an effect only if
                in `marker.color`is set to a numerical array.
""",
            **kwargs
        )
