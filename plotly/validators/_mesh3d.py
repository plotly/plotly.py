import _plotly_utils.basevalidators


class Mesh3dValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='mesh3d', parent_name='', **kwargs):
        super(Mesh3dValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Mesh3d',
            data_docs="""
            alphahull
                Determines how the mesh surface triangles are
                derived from the set of vertices (points)
                represented by the `x`, `y` and `z` arrays, if
                the `i`, `j`, `k` arrays are not supplied. For
                general use of `mesh3d` it is preferred that
                `i`, `j`, `k` are supplied. If "-1", Delaunay
                triangulation is used, which is mainly suitable
                if the mesh is a single, more or less layer
                surface that is perpendicular to
                `delaunayaxis`. In case the `delaunayaxis`
                intersects the mesh surface at more than one
                point it will result triangles that are very
                long in the dimension of `delaunayaxis`. If
                ">0", the alpha-shape algorithm is used. In
                this case, the positive `alphahull` value
                signals the use of the alpha-shape algorithm,
                _and_ its value acts as the parameter for the
                mesh fitting. If 0,  the convex-hull algorithm
                is used. It is suitable for convex bodies or if
                the intention is to enclose the `x`, `y` and
                `z` point set into a convex hull.
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
                `intensity`) or the bounds set in `cmin` and
                `cmax`  Defaults to `false` when `cmin` and
                `cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Value
                should have the same units as `intensity` and
                if set, `cmin` must be set as well.
            cmin
                Sets the lower bound of the color domain. Value
                should have the same units as `intensity` and
                if set, `cmax` must be set as well.
            color
                Sets the color of the whole mesh
            colorbar
                plotly.graph_objs.mesh3d.ColorBar instance or
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
            contour
                plotly.graph_objs.mesh3d.Contour instance or
                dict with compatible properties
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            delaunayaxis
                Sets the Delaunay axis, which is the axis that
                is perpendicular to the surface of the Delaunay
                triangulation. It has an effect if `i`, `j`,
                `k` are not provided and `alphahull` is set to
                indicate Delaunay triangulation.
            facecolor
                Sets the color of each face Overrides "color"
                and "vertexcolor".
            facecolorsrc
                Sets the source reference on plot.ly for
                facecolor .
            flatshading
                Determines whether or not normal smoothing is
                applied to the meshes, creating meshes with an
                angular, low-poly look via flat reflections.
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
                plotly.graph_objs.mesh3d.Hoverlabel instance or
                dict with compatible properties
            i
                A vector of vertex indices, i.e. integer values
                between 0 and the length of the vertex vectors,
                representing the "first" vertex of a triangle.
                For example, `{i[m], j[m], k[m]}` together
                represent face m (triangle m) in the mesh,
                where `i[m] = n` points to the triplet `{x[n],
                y[n], z[n]}` in the vertex arrays. Therefore,
                each element in `i` represents a point in
                space, which is the first vertex of a triangle.
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            intensity
                Sets the vertex intensity values, used for
                plotting fields on meshes
            intensitysrc
                Sets the source reference on plot.ly for
                intensity .
            isrc
                Sets the source reference on plot.ly for  i .
            j
                A vector of vertex indices, i.e. integer values
                between 0 and the length of the vertex vectors,
                representing the "second" vertex of a triangle.
                For example, `{i[m], j[m], k[m]}`  together
                represent face m (triangle m) in the mesh,
                where `j[m] = n` points to the triplet `{x[n],
                y[n], z[n]}` in the vertex arrays. Therefore,
                each element in `j` represents a point in
                space, which is the second vertex of a
                triangle.
            jsrc
                Sets the source reference on plot.ly for  j .
            k
                A vector of vertex indices, i.e. integer values
                between 0 and the length of the vertex vectors,
                representing the "third" vertex of a triangle.
                For example, `{i[m], j[m], k[m]}` together
                represent face m (triangle m) in the mesh,
                where `k[m] = n` points to the triplet  `{x[n],
                y[n], z[n]}` in the vertex arrays. Therefore,
                each element in `k` represents a point in
                space, which is the third vertex of a triangle.
            ksrc
                Sets the source reference on plot.ly for  k .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            lighting
                plotly.graph_objs.mesh3d.Lighting instance or
                dict with compatible properties
            lightposition
                plotly.graph_objs.mesh3d.Lightposition instance
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
            stream
                plotly.graph_objs.mesh3d.Stream instance or
                dict with compatible properties
            text
                Sets the text elements associated with the
                vertices. If trace `hoverinfo` contains a
                "text" flag and "hovertext" is not set, these
                elements will be seen in the hover labels.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            uid

            vertexcolor
                Sets the color of each vertex Overrides
                "color".
            vertexcolorsrc
                Sets the source reference on plot.ly for
                vertexcolor .
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            x
                Sets the X coordinates of the vertices. The nth
                element of vectors `x`, `y` and `z` jointly
                represent the X, Y and Z coordinates of the nth
                vertex.
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                Sets the Y coordinates of the vertices. The nth
                element of vectors `x`, `y` and `z` jointly
                represent the X, Y and Z coordinates of the nth
                vertex.
            ycalendar
                Sets the calendar system to use with `y` date
                data.
            ysrc
                Sets the source reference on plot.ly for  y .
            z
                Sets the Z coordinates of the vertices. The nth
                element of vectors `x`, `y` and `z` jointly
                represent the X, Y and Z coordinates of the nth
                vertex.
            zcalendar
                Sets the calendar system to use with `z` date
                data.
            zsrc
                Sets the source reference on plot.ly for  z .
""",
            **kwargs
        )
