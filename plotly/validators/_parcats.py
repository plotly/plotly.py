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
                Assign an id to this trace, Use this to provide
                object constancy between traces during
                animations and transitions.
            uirevision
                Controls persistence of some user-driven
                changes to the trace: `constraintrange` in
                `parcoords` traces, as well as some `editable:
                true` modifications such as `name` and
                `colorbar.title`. Defaults to
                `layout.uirevision`. Note that other user-
                driven trace attribute changes are controlled
                by `layout` attributes: `trace.visible` is
                controlled by `layout.legend.uirevision`,
                `selectedpoints` is controlled by
                `layout.selectionrevision`, and
                `colorbar.(x|y)` (accessible with `config:
                {editable: true}`) is controlled by
                `layout.editrevision`. Trace changes are
                tracked by `uid`, which only falls back on
                trace index if no `uid` is provided. So if your
                app can add/remove traces before the end of the
                `data` array, such that the same trace has a
                different index, you can still preserve user-
                driven changes if you give each trace a `uid`
                that stays with it as it moves.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
"""
            ),
            **kwargs
        )
