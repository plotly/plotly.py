import _plotly_utils.basevalidators


class TernaryValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='ternary', parent_name='layout', **kwargs):
        super(TernaryValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Ternary'),
            data_docs=kwargs.pop(
                'data_docs', """
            aaxis
                plotly.graph_objs.layout.ternary.Aaxis instance
                or dict with compatible properties
            baxis
                plotly.graph_objs.layout.ternary.Baxis instance
                or dict with compatible properties
            bgcolor
                Set the background color of the subplot
            caxis
                plotly.graph_objs.layout.ternary.Caxis instance
                or dict with compatible properties
            domain
                plotly.graph_objs.layout.ternary.Domain
                instance or dict with compatible properties
            sum
                The number each triplet should sum to, and the
                maximum range of each axis
            uirevision
                Controls persistence of user-driven changes in
                axis `min` and `title`, if not overridden in
                the individual axes. Defaults to
                `layout.uirevision`.
"""
            ),
            **kwargs
        )
