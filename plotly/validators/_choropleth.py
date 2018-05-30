import _plotly_utils.basevalidators


class ChoroplethValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='choropleth', parent_name='', **kwargs):
        super(ChoroplethValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Choropleth',
            data_docs="""
            autocolorscale
                Determines whether or not the colorscale is
                picked using the sign of the input z values.
            colorbar
                plotly.graph_objs.choropleth.ColorBar instance
                or dict with compatible properties
            colorscale
                Sets the colorscale. The colorscale must be an
                array containing arrays mapping a normalized
                value to an rgb, rgba, hex, hsl, hsv, or named
                color string. At minimum, a mapping for the
                lowest (0) and highest (1) values are required.
                For example, `[[0, 'rgb(0,0,255)', [1,
                'rgb(255,0,0)']]`. To control the bounds of the
                colorscale in z space, use zmin and zmax
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, *scatter* traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            geo
                Sets a reference between this trace's
                geospatial coordinates and a geographic map. If
                *geo* (the default value), the geospatial
                coordinates refer to `layout.geo`. If *geo2*,
                the geospatial coordinates refer to
                `layout.geo2`, and so on.
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
                plotly.graph_objs.choropleth.Hoverlabel
                instance or dict with compatible properties
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
            locationmode
                Determines the set of locations used to match
                entries in `locations` to regions on the map.
            locations
                Sets the coordinates via location IDs or names.
                See `locationmode` for more info.
            locationssrc
                Sets the source reference on plot.ly for
                locations .
            marker
                plotly.graph_objs.choropleth.Marker instance or
                dict with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            reversescale
                Reverses the colorscale.
            selected
                plotly.graph_objs.choropleth.Selected instance
                or dict with compatible properties
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
                plotly.graph_objs.choropleth.Stream instance or
                dict with compatible properties
            text
                Sets the text elements associated with each
                location.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            uid

            unselected
                plotly.graph_objs.choropleth.Unselected
                instance or dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If *legendonly*, the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            z
                Sets the color values.
            zauto
                Determines the whether or not the color domain
                is computed with respect to the input data.
            zmax
                Sets the upper bound of color domain.
            zmin
                Sets the lower bound of color domain.
            zsrc
                Sets the source reference on plot.ly for  z .""",
            **kwargs
        )
