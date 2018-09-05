import _plotly_utils.basevalidators


class ConeValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='cone', parent_name='', **kwargs):
        super(ConeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Cone',
            data_docs="""
            anchor
                Sets the cones' anchor with respect to their
                x/y/z positions. Note that "cm" denote the
                cone's center of mass which corresponds to 1/4
                from the tail to tip.
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `colorscale`. In case
                `colorscale` is unspecified or `autocolorscale`
                is true, the default  palette will be chosen
                according to whether numbers in the `color`
                array are all positive, all negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                u/v/w norm) or the bounds set in `cmin` and
                `cmax`  Defaults to `false` when `cmin` and
                `cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as u/v/w norm and if
                set, `cmin` must be set as well.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as u/v/w norm and if
                set, `cmax` must be set as well.
            colorbar
                plotly.graph_objs.cone.ColorBar instance or
                dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)', [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in color space, use`cmin` and
                `cmax`. Alternatively, `colorscale` may be a
                palette name string of the following list: Grey
                s,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,
                Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth
                ,Electric,Viridis,Cividis.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                plotly.graph_objs.cone.Hoverlabel instance or
                dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                plotly.graph_objs.cone.Lighting instance or
                dict with compatible properties
            lightposition
                plotly.graph_objs.cone.Lightposition instance
                or dict with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the surface.
            reversescale
                Reverses the color mapping if true. If true,
                `cmin` will correspond to the last color in the
                array and `cmax` will correspond to the first
                color.
            scene
                Sets a reference between this trace's 3D
                coordinate system and a 3D scene. If "scene"
                (the default value), the (x,y,z) coordinates
                refer to `layout.scene`. If "scene2", the
                (x,y,z) coordinates refer to `layout.scene2`,
                and so on.
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace.
            sizemode
                Determines whether `sizeref` is set as a
                "scaled" (i.e unitless) scalar (normalized by
                the max u/v/w norm in the vector field) or as
                "absolute" value (in the same units as the
                vector field).
            sizeref
                Adjusts the cone size scaling. The size of the
                cones is determined by their u/v/w norm
                multiplied a factor and `sizeref`. This factor
                (computed internally) corresponds to the
                minimum "time" to travel across two successive
                x/y/z positions at the average velocity of
                those two successive positions. All cones in a
                given trace use the same factor. With
                `sizemode` set to "scaled", `sizeref` is
                unitless, its default value is 0.5 With
                `sizemode` set to "absolute", `sizeref` has the
                same units as the u/v/w vector field, its the
                default value is half the sample's maximum
                vector norm.
            stream
                plotly.graph_objs.cone.Stream instance or dict
                with compatible properties
            text
                Sets the text elements associated with the
                cones. If trace `hoverinfo` contains a "text"
                flag and "hovertext" is not set, these elements
                will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            u
                Sets the x components of the vector field.
            uid

            usrc
                Sets the source reference on plot.ly for  u .
            v
                Sets the y components of the vector field.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            vsrc
                Sets the source reference on plot.ly for  v .
            w
                Sets the z components of the vector field.
            wsrc
                Sets the source reference on plot.ly for  w .
            x
                Sets the x coordinates of the vector field and
                of the displayed cones.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the y coordinates of the vector field and
                of the displayed cones.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the z coordinates of the vector field and
                of the displayed cones.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            **kwargs
        )
