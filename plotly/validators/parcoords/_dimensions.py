import _plotly_utils.basevalidators


class DimensionsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):

    def __init__(
        self, plotly_name='dimensions', parent_name='parcoords', **kwargs
    ):
        super(DimensionsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Dimension',
            data_docs="""
            constraintrange
                The domain range to which the filter on the
                dimension is constrained. Must be an array of
                `[fromValue, toValue]` with `fromValue <=
                toValue`, or if `multiselect` is not disabled,
                you may give an array of arrays, where each
                inner array is `[fromValue, toValue]`.
            label
                The shown name of the dimension.
            multiselect
                Do we allow multiple selection ranges or just a
                single range?
            range
                The domain range that represents the full,
                shown axis extent. Defaults to the `values`
                extent. Must be an array of `[fromValue,
                toValue]` with finite numbers as elements.
            tickformat
                Sets the tick label formatting rule using d3
                formatting mini-language which is similar to
                those of Python. See https://github.com/d3/d3-f
                ormat/blob/master/README.md#locale_format
            ticktext
                Sets the text displayed at the ticks position
                via `tickvals`. Only has an effect if
                `tickmode` is set to *array*. Used with
                `tickvals`.
            ticktextsrc
                Sets the source reference on plot.ly for
                ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to *array*. Used with `ticktext`.
            tickvalssrc
                Sets the source reference on plot.ly for
                tickvals .
            values
                Dimension values. `values[n]` represents the
                value of the `n`th point in the dataset,
                therefore the `values` vector for all
                dimensions must be the same (longer vectors
                will be truncated). Each value must be a finite
                number.
            valuessrc
                Sets the source reference on plot.ly for
                values .
            visible
                Shows the dimension when set to `true` (the
                default). Hides the dimension for `false`.""",
            **kwargs
        )
