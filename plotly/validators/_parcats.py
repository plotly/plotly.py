import _plotly_utils.basevalidators


class ParcatsValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='parcats', parent_name='', **kwargs):
        super(ParcatsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Parcats'),
            data_docs=kwargs.pop(
                'data_docs', """
            arrangement
                Sets the drag interaction mode for categories
                and dimensions. If `perpendicular`, the
                categories can only move along a line
                perpendicular to the paths. If `freeform`, the
                categories can freely move on the plane. If
                `fixed`, the categories and dimensions are
                stationary.
            bundlecolors
                Sort paths so that like colors are bundled
                together within each category.
            counts
                The number of observations represented by each
                state. Defaults to 1 so that each state
                represents one observation
            countssrc
                Sets the source reference on plot.ly for
                counts .
            dimensions
                The dimensions (variables) of the parallel
                categories diagram.
            dimensiondefaults
                When used in a template (as layout.template.dat
                a.parcats.dimensiondefaults), sets the default
                property values to use for elements of
                parcats.dimensions
            domain
                plotly.graph_objs.parcats.Domain instance or
                dict with compatible properties
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoveron
                Sets the hover interaction mode for the parcats
                diagram. If `category`, hover interaction take
                place per category. If `color`, hover
                interactions take place per color per category.
                If `dimension`, hover interactions take place
                across all categories per dimension.
            labelfont
                Sets the font for the `dimension` labels.
            line
                plotly.graph_objs.parcats.Line instance or dict
                with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            sortpaths
                Sets the path sorting algorithm. If `forward`,
                sort paths based on dimension categories from
                left to right. If `backward`, sort paths based
                on dimensions categories from right to left.
            stream
                plotly.graph_objs.parcats.Stream instance or
                dict with compatible properties
            tickfont
                Sets the font for the `category` labels.
            uid

            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
"""
            ),
            **kwargs
        )
