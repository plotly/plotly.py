import _plotly_utils.basevalidators


class HeaderValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='header', parent_name='table', **kwargs):
        super(HeaderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Header',
            data_docs="""
            align
                Sets the horizontal alignment of the `text`
                within the box. Has an effect only if `text`
                spans more two or more lines (i.e. `text`
                contains one or more <br> HTML tags) or if an
                explicit width is set to override the text
                width.
            alignsrc
                Sets the source reference on plot.ly for  align
                .
            fill
                plotly.graph_objs.table.header.Fill instance or
                dict with compatible properties
            font
                plotly.graph_objs.table.header.Font instance or
                dict with compatible properties
            format
                Sets the cell value formatting rule using d3
                formatting mini-language which is similar to
                those of Python. See https://github.com/d3/d3-f
                ormat/blob/master/README.md#locale_format
            formatsrc
                Sets the source reference on plot.ly for
                format .
            height
                The height of cells.
            line
                plotly.graph_objs.table.header.Line instance or
                dict with compatible properties
            prefix
                Prefix for cell values.
            prefixsrc
                Sets the source reference on plot.ly for
                prefix .
            suffix
                Suffix for cell values.
            suffixsrc
                Sets the source reference on plot.ly for
                suffix .
            values
                Header cell values. `values[m][n]` represents
                the value of the `n`th point in column `m`,
                therefore the `values[m]` vector length for all
                columns must be the same (longer vectors will
                be truncated). Each value must be a finite
                number or a string.
            valuessrc
                Sets the source reference on plot.ly for
                values .
""",
            **kwargs
        )
