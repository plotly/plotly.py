from __future__ import absolute_import

from plotly import exceptions, optional_imports
from plotly.figure_factory import utils
from plotly.graph_objs import graph_objs
from plotly.validators.heatmap import ColorscaleValidator

# Optional imports, may be None for users that only use our core functionality.
np = optional_imports.get_module('numpy')


def validate_annotated_heatmap(z, x, y, annotation_text):
    """
    Annotated-heatmap-specific validations

    Check that if a text matrix is supplied, it has the same
    dimensions as the z matrix.

    See FigureFactory.create_annotated_heatmap() for params

    :raises: (PlotlyError) If z and text matrices do not  have the same
        dimensions.
    """
    if annotation_text is not None and isinstance(annotation_text, list):
        utils.validate_equal_length(z, annotation_text)
        for lst in range(len(z)):
            if len(z[lst]) != len(annotation_text[lst]):
                raise exceptions.PlotlyError("z and text should have the "
                                             "same dimensions")

    if x:
        if len(x) != len(z[0]):
            raise exceptions.PlotlyError("oops, the x list that you "
                                         "provided does not match the "
                                         "width of your z matrix ")

    if y:
        if len(y) != len(z):
            raise exceptions.PlotlyError("oops, the y list that you "
                                         "provided does not match the "
                                         "length of your z matrix ")


def create_annotated_heatmap(z, x=None, y=None, annotation_text=None,
                             colorscale='RdBu', font_colors=None,
                             showscale=False, reversescale=False,
                             **kwargs):
    """
    BETA function that creates annotated heatmaps

    This function adds annotations to each cell of the heatmap.

    :param (list[list]|ndarray) z: z matrix to create heatmap.
    :param (list) x: x axis labels.
    :param (list) y: y axis labels.
    :param (list[list]|ndarray) annotation_text: Text strings for
        annotations. Should have the same dimensions as the z matrix. If no
        text is added, the values of the z matrix are annotated. Default =
        z matrix values.
    :param (list|str) colorscale: heatmap colorscale.
    :param (list) font_colors: List of two color strings: [min_text_color,
        max_text_color] where min_text_color is applied to annotations for
        heatmap values < (max_value - min_value)/2. If font_colors is not
        defined, the colors are defined logically as black or white
        depending on the heatmap's colorscale.
    :param (bool) showscale: Display colorscale. Default = False
    :param kwargs: kwargs passed through plotly.graph_objs.Heatmap.
        These kwargs describe other attributes about the annotated Heatmap
        trace such as the colorscale. For more information on valid kwargs
        call help(plotly.graph_objs.Heatmap)

    Example 1: Simple annotated heatmap with default configuration
    ```
    import plotly.plotly as py
    import plotly.figure_factory as FF

    z = [[0.300000, 0.00000, 0.65, 0.300000],
         [1, 0.100005, 0.45, 0.4300],
         [0.300000, 0.00000, 0.65, 0.300000],
         [1, 0.100005, 0.45, 0.00000]]

    figure = FF.create_annotated_heatmap(z)
    py.iplot(figure)
    ```
    """

    # Avoiding mutables in the call signature
    font_colors = font_colors if font_colors is not None else []
    validate_annotated_heatmap(z, x, y, annotation_text)

    # validate colorscale
    colorscale_validator = ColorscaleValidator()
    colorscale = colorscale_validator.validate_coerce(colorscale)

    annotations = _AnnotatedHeatmap(z, x, y, annotation_text,
                                    colorscale, font_colors, reversescale,
                                    **kwargs).make_annotations()

    if x or y:
        trace = dict(type='heatmap', z=z, x=x, y=y, colorscale=colorscale,
                     showscale=showscale, **kwargs)
        layout = dict(annotations=annotations,
                      xaxis=dict(ticks='', dtick=1, side='top',
                                 gridcolor='rgb(0, 0, 0)'),
                      yaxis=dict(ticks='', dtick=1, ticksuffix='  '))
    else:
        trace = dict(type='heatmap', z=z, colorscale=colorscale,
                     showscale=showscale, **kwargs)
        layout = dict(annotations=annotations,
                      xaxis=dict(ticks='', side='top',
                                 gridcolor='rgb(0, 0, 0)',
                                 showticklabels=False),
                      yaxis=dict(ticks='', ticksuffix='  ',
                                 showticklabels=False))

    data = [trace]

    return graph_objs.Figure(data=data, layout=layout)


def to_rgb_color_list(color_str, default):
    if 'rgb' in color_str:
        return [int(v) for v in color_str.strip('rgb()').split(',')]
    elif '#' in color_str:
        return utils.hex_to_rgb(color_str)
    else:
        return default


class _AnnotatedHeatmap(object):
    """
    Refer to TraceFactory.create_annotated_heatmap() for docstring
    """
    def __init__(self, z, x, y, annotation_text, colorscale,
                 font_colors, reversescale, **kwargs):

        self.z = z
        if x:
            self.x = x
        else:
            self.x = range(len(z[0]))
        if y:
            self.y = y
        else:
            self.y = range(len(z))
        if annotation_text is not None:
            self.annotation_text = annotation_text
        else:
            self.annotation_text = self.z
        self.colorscale = colorscale
        self.reversescale = reversescale
        self.font_colors = font_colors

    def get_text_color(self):
        """
        Get font color for annotations.

        The annotated heatmap can feature two text colors: min_text_color and
        max_text_color. The min_text_color is applied to annotations for
        heatmap values < (max_value - min_value)/2. The user can define these
        two colors. Otherwise the colors are defined logically as black or
        white depending on the heatmap's colorscale.

        :rtype (string, string) min_text_color, max_text_color: text
            color for annotations for heatmap values <
            (max_value - min_value)/2 and text color for annotations for
            heatmap values >= (max_value - min_value)/2
        """
        # Plotly colorscales ranging from a lighter shade to a darker shade
        colorscales = ['Greys', 'Greens', 'Blues',
                       'YIGnBu', 'YIOrRd', 'RdBu',
                       'Picnic', 'Jet', 'Hot', 'Blackbody',
                       'Earth', 'Electric', 'Viridis', 'Cividis']
        # Plotly colorscales ranging from a darker shade to a lighter shade
        colorscales_reverse = ['Reds']
        if self.font_colors:
            min_text_color = self.font_colors[0]
            max_text_color = self.font_colors[-1]
        elif self.colorscale in colorscales and self.reversescale:
            min_text_color = '#000000'
            max_text_color = '#FFFFFF'
        elif self.colorscale in colorscales:
            min_text_color = '#FFFFFF'
            max_text_color = '#000000'
        elif self.colorscale in colorscales_reverse and self.reversescale:
            min_text_color = '#FFFFFF'
            max_text_color = '#000000'
        elif self.colorscale in colorscales_reverse:
            min_text_color = '#000000'
            max_text_color = '#FFFFFF'
        elif isinstance(self.colorscale, list):

            min_col = to_rgb_color_list(self.colorscale[0][1],
                                        [255, 255, 255])
            max_col = to_rgb_color_list(self.colorscale[-1][1],
                                        [255, 255, 255])

            if (min_col[0]*0.299 + min_col[1]*0.587 + min_col[2]*0.114) > 186:
                min_text_color = '#000000'
            else:
                min_text_color = '#FFFFFF'
            if (max_col[0]*0.299 + max_col[1]*0.587 + max_col[2]*0.114) > 186:
                max_text_color = '#000000'
            else:
                max_text_color = '#FFFFFF'
        else:
            min_text_color = '#000000'
            max_text_color = '#000000'
        return min_text_color, max_text_color

    def get_z_mid(self):
        """
        Get the mid value of z matrix

        :rtype (float) z_avg: average val from z matrix
        """
        if np and isinstance(self.z, np.ndarray):
            z_min = np.amin(self.z)
            z_max = np.amax(self.z)
        else:
            z_min = min(min(self.z))
            z_max = max(max(self.z))
        z_mid = (z_max+z_min) / 2
        return z_mid

    def make_annotations(self):
        """
        Get annotations for each cell of the heatmap with graph_objs.Annotation

        :rtype (list[dict]) annotations: list of annotations for each cell of
            the heatmap
        """
        min_text_color, max_text_color = _AnnotatedHeatmap.get_text_color(self)
        z_mid = _AnnotatedHeatmap.get_z_mid(self)
        annotations = []
        for n, row in enumerate(self.z):
            for m, val in enumerate(row):
                font_color = min_text_color if val < z_mid else max_text_color
                annotations.append(
                    graph_objs.layout.Annotation(
                        text=str(self.annotation_text[n][m]),
                        x=self.x[m],
                        y=self.y[n],
                        xref='x1',
                        yref='y1',
                        font=dict(color=font_color),
                        showarrow=False))
        return annotations
