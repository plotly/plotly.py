import _plotly_utils.basevalidators


class TitleValidator(_plotly_utils.basevalidators.TitleValidator):
    def __init__(self, plotly_name="title", parent_name="layout", **kwargs):
        super(TitleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Title"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            font
                Sets the title font. Note that the title's font
                used to be customized by the now deprecated
                `titlefont` attribute.
            pad
                Sets the padding of the title. Each padding
                value only applies when the corresponding
                `xanchor`/`yanchor` value is set accordingly.
                E.g. for left padding to take effect, `xanchor`
                must be set to "left". The same rule applies if
                `xanchor`/`yanchor` is determined
                automatically. Padding is muted if the
                respective anchor value is "middle*/*center".
            text
                Sets the plot's title. Note that before the
                existence of `title.text`, the title's contents
                used to be defined as the `title` attribute
                itself. This behavior has been deprecated.
            x
                Sets the x position with respect to `xref` in
                normalized coordinates from 0 (left) to 1
                (right).
            xanchor
                Sets the title's horizontal alignment with
                respect to its x position. "left" means that
                the title starts at x, "right" means that the
                title ends at x and "center" means that the
                title's center is at x. "auto" divides `xref`
                by three and calculates the `xanchor` value
                automatically based on the value of `x`.
            xref
                Sets the container `x` refers to. "container"
                spans the entire `width` of the plot. "paper"
                refers to the width of the plotting area only.
            y
                Sets the y position with respect to `yref` in
                normalized coordinates from 0 (bottom) to 1
                (top). "auto" places the baseline of the title
                onto the vertical center of the top margin.
            yanchor
                Sets the title's vertical alignment with
                respect to its y position. "top" means that the
                title's cap line is at y, "bottom" means that
                the title's baseline is at y and "middle" means
                that the title's midline is at y. "auto"
                divides `yref` by three and calculates the
                `yanchor` value automatically based on the
                value of `y`.
            yref
                Sets the container `y` refers to. "container"
                spans the entire `height` of the plot. "paper"
                refers to the height of the plotting area only.
""",
            ),
            **kwargs
        )
