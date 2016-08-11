"""
colors
=====

Functions that manipulate colors and arrays of colors

There are three basic types of color types: rgb, hex and tuple:

rgb - An rgb color is a string of the form 'rgb(a,b,c)' where a, b and c are
floats between 0 and 255 inclusive.

hex - A hex color is a string of the form '#xxxxxx' where each x is a
character that belongs to the set [0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f]. This is
just the list of characters used in the hexadecimal numeric system.

tuple - A tuple color is a 3-tuple of the form (a,b,c) where a, b and c are
floats between 0 and 1 inclusive.

"""
from __future__ import absolute_import
from plotly import exceptions
from numbers import Number

DEFAULT_PLOTLY_COLORS = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                         'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                         'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                         'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                         'rgb(188, 189, 34)', 'rgb(23, 190, 207)']

PLOTLY_SCALES = {
    'Greys': [
        [0, 'rgb(0,0,0)'], [1, 'rgb(255,255,255)']
    ],

    'YlGnBu': [
        [0, 'rgb(8,29,88)'], [0.125, 'rgb(37,52,148)'],
        [0.25, 'rgb(34,94,168)'], [0.375, 'rgb(29,145,192)'],
        [0.5, 'rgb(65,182,196)'], [0.625, 'rgb(127,205,187)'],
        [0.75, 'rgb(199,233,180)'], [0.875, 'rgb(237,248,217)'],
        [1, 'rgb(255,255,217)']
    ],

    'Greens': [
        [0, 'rgb(0,68,27)'], [0.125, 'rgb(0,109,44)'],
        [0.25, 'rgb(35,139,69)'], [0.375, 'rgb(65,171,93)'],
        [0.5, 'rgb(116,196,118)'], [0.625, 'rgb(161,217,155)'],
        [0.75, 'rgb(199,233,192)'], [0.875, 'rgb(229,245,224)'],
        [1, 'rgb(247,252,245)']
    ],

    'YlOrRd': [
        [0, 'rgb(128,0,38)'], [0.125, 'rgb(189,0,38)'],
        [0.25, 'rgb(227,26,28)'], [0.375, 'rgb(252,78,42)'],
        [0.5, 'rgb(253,141,60)'], [0.625, 'rgb(254,178,76)'],
        [0.75, 'rgb(254,217,118)'], [0.875, 'rgb(255,237,160)'],
        [1, 'rgb(255,255,204)']
    ],

    'Bluered': [
        [0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']
    ],

    # modified RdBu based on
    # www.sandia.gov/~kmorel/documents/ColorMaps/ColorMapsExpanded.pdf
    'RdBu': [
        [0, 'rgb(5,10,172)'], [0.35, 'rgb(106,137,247)'],
        [0.5, 'rgb(190,190,190)'], [0.6, 'rgb(220,170,132)'],
        [0.7, 'rgb(230,145,90)'], [1, 'rgb(178,10,28)']
    ],

    # Scale for non-negative numeric values
    'Reds': [
        [0, 'rgb(220,220,220)'], [0.2, 'rgb(245,195,157)'],
        [0.4, 'rgb(245,160,105)'], [1, 'rgb(178,10,28)']
    ],

    # Scale for non-positive numeric values
    'Blues': [
        [0, 'rgb(5,10,172)'], [0.35, 'rgb(40,60,190)'],
        [0.5, 'rgb(70,100,245)'], [0.6, 'rgb(90,120,245)'],
        [0.7, 'rgb(106,137,247)'], [1, 'rgb(220,220,220)']
    ],

    'Picnic': [
        [0, 'rgb(0,0,255)'], [0.1, 'rgb(51,153,255)'],
        [0.2, 'rgb(102,204,255)'], [0.3, 'rgb(153,204,255)'],
        [0.4, 'rgb(204,204,255)'], [0.5, 'rgb(255,255,255)'],
        [0.6, 'rgb(255,204,255)'], [0.7, 'rgb(255,153,255)'],
        [0.8, 'rgb(255,102,204)'], [0.9, 'rgb(255,102,102)'],
        [1, 'rgb(255,0,0)']
    ],

    'Rainbow': [
        [0, 'rgb(150,0,90)'], [0.125, 'rgb(0,0,200)'],
        [0.25, 'rgb(0,25,255)'], [0.375, 'rgb(0,152,255)'],
        [0.5, 'rgb(44,255,150)'], [0.625, 'rgb(151,255,0)'],
        [0.75, 'rgb(255,234,0)'], [0.875, 'rgb(255,111,0)'],
        [1, 'rgb(255,0,0)']
    ],

    'Portland': [
        [0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'],
        [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'],
        [1, 'rgb(217,30,30)']
    ],

    'Jet': [
        [0, 'rgb(0,0,131)'], [0.125, 'rgb(0,60,170)'],
        [0.375, 'rgb(5,255,255)'], [0.625, 'rgb(255,255,0)'],
        [0.875, 'rgb(250,0,0)'], [1, 'rgb(128,0,0)']
    ],

    'Hot': [
        [0, 'rgb(0,0,0)'], [0.3, 'rgb(230,0,0)'],
        [0.6, 'rgb(255,210,0)'], [1, 'rgb(255,255,255)']
    ],

    'Blackbody': [
        [0, 'rgb(0,0,0)'], [0.2, 'rgb(230,0,0)'],
        [0.4, 'rgb(230,210,0)'], [0.7, 'rgb(255,255,255)'],
        [1, 'rgb(160,200,255)']
    ],

    'Earth': [
        [0, 'rgb(0,0,130)'], [0.1, 'rgb(0,180,180)'],
        [0.2, 'rgb(40,210,40)'], [0.4, 'rgb(230,230,50)'],
        [0.6, 'rgb(120,70,20)'], [1, 'rgb(255,255,255)']
    ],

    'Electric': [
        [0, 'rgb(0,0,0)'], [0.15, 'rgb(30,0,100)'],
        [0.4, 'rgb(120,0,100)'], [0.6, 'rgb(160,90,0)'],
        [0.8, 'rgb(230,200,0)'], [1, 'rgb(255,250,220)']
    ],

    'Viridis': [
        [0, '#440154'], [0.06274509803921569, '#48186a'],
        [0.12549019607843137, '#472d7b'], [0.18823529411764706, '#424086'],
        [0.25098039215686274, '#3b528b'], [0.3137254901960784, '#33638d'],
        [0.3764705882352941, '#2c728e'], [0.4392156862745098, '#26828e'],
        [0.5019607843137255, '#21918c'], [0.5647058823529412, '#1fa088'],
        [0.6274509803921569, '#28ae80'], [0.6901960784313725, '#3fbc73'],
        [0.7529411764705882, '#5ec962'], [0.8156862745098039, '#84d44b'],
        [0.8784313725490196, '#addc30'], [0.9411764705882353, '#d8e219'],
        [1, '#fde725']
    ]
}


def color_parser(colors, function):
    """
    Takes color(s) and a function and applies the function on the color(s)

    In particular, this function identifies whether the given color object
    is an iterable or not and applies the given color-parsing function to
    the color or iterable of colors. If given an iterable, it will only be
    able to work with it if all items in the iterable are of the same type
    - rgb string, hex string or tuple

    """
    if isinstance(colors, str):
        return function(colors)

    if isinstance(colors, tuple) and isinstance(colors[0], Number):
        return function(colors)

    if hasattr(colors, '__iter__'):
        if isinstance(colors, tuple):
            new_color_tuple = tuple(function(item) for item in colors)
            return new_color_tuple

        else:
            new_color_list = [function(item) for item in colors]
            return new_color_list


def validate_colors(colors):
    """
    Validates color(s) and returns an error for invalid colors
    """
    colors_list = []

    if isinstance(colors, str):
        if colors in PLOTLY_SCALES:
            return
        elif 'rgb' in colors or '#' in colors:
            colors_list = [colors]
        else:
            raise exceptions.PlotlyError(
                "If your colors variable is a string, it must be a "
                "Plotly scale, an rgb color or a hex color."
            )

    elif isinstance(colors, tuple):
        if isinstance(colors[0], Number):
            colors_list = [colors]
        else:
            colors_list = list(colors)

    if isinstance(colors, dict):
        colors_list.extend(colors.values())

    elif isinstance(colors, list):
        colors_list = colors

    # Validate colors in colors_list
    for j, each_color in enumerate(colors_list):
        if 'rgb' in each_color:
            each_color = color_parser(
                each_color, unlabel_rgb
            )
            for value in each_color:
                if value > 255.0:
                    raise exceptions.PlotlyError(
                        "Whoops! The elements in your rgb colors "
                        "tuples cannot exceed 255.0."
                    )

        elif '#' in each_color:
            each_color = color_parser(
                each_color, hex_to_rgb
            )

        elif isinstance(each_color, tuple):
            for value in each_color:
                if value > 1.0:
                    raise exceptions.PlotlyError(
                        "Whoops! The elements in your colors tuples "
                        "cannot exceed 1.0."
                    )
    return colors


def convert_colors_to_same_type(colors, colortype='rgb'):
    """
    Converts color(s) to the specified color type

    Takes a single color or an iterable of colors and outputs a list of the
    color(s) converted all to an rgb or tuple color type. If colors is a
    Plotly Scale name then the cooresponding colorscale will be outputted and
    colortype will not be applicable
    """
    colors_list = []

    if isinstance(colors, str):
        if colors in PLOTLY_SCALES:
            return PLOTLY_SCALES[colors]
        elif 'rgb' in colors or '#' in colors:
            colors_list = [colors]
        else:
            raise exceptions.PlotlyError(
                "If your colors variable is a string, it must be a Plotly "
                "scale, an rgb color or a hex color.")

    elif isinstance(colors, tuple):
        if isinstance(colors[0], Number):
            colors_list = [colors]
        else:
            colors_list = list(colors)

    elif isinstance(colors, list):
        colors_list = colors

    # convert all colors to rgb
    for j, each_color in enumerate(colors_list):
        if '#' in each_color:
            each_color = color_parser(
                each_color, hex_to_rgb
            )
            each_color = color_parser(
                each_color, label_rgb
            )
            colors_list[j] = each_color

        elif isinstance(each_color, tuple):
            each_color = color_parser(
                each_color, convert_to_RGB_255
            )
            each_color = color_parser(
                each_color, label_rgb
            )
            colors_list[j] = each_color

    if colortype == 'rgb':
        return colors_list
    elif colortype == 'tuple':
        for j, each_color in enumerate(colors_list):
            each_color = color_parser(
                each_color, unlabel_rgb
            )
            each_color = color_parser(
                each_color, unconvert_from_RGB_255
            )
            colors_list[j] = each_color
        return colors_list
    else:
        raise exceptions.PlotlyError("You must select either rgb or tuple "
                                     "for your colortype variable.")


def convert_dict_colors_to_same_type(colors, colortype='rgb'):
    """
    Converts color(s) to the specified color type

    Takes a single color or an iterable of colors and outputs a list of the
    color(s) converted all to an rgb or tuple color type. If colors is a
    Plotly Scale name then the cooresponding colorscale will be outputted
    """
    for key in colors:
        if '#' in colors[key]:
            colors[key] = color_parser(
                colors[key], hex_to_rgb
            )
            colors[key] = color_parser(
                colors[key], label_rgb
            )

        elif isinstance(colors[key], tuple):
            colors[key] = color_parser(
                colors[key], convert_to_RGB_255
            )
            colors[key] = color_parser(
                colors[key], label_rgb
            )

    if colortype == 'rgb':
        return colors
    elif colortype == 'tuple':
        for key in colors:
            colors[key] = color_parser(
                colors[key], unlabel_rgb
            )
            colors[key] = color_parser(
                colors[key], unconvert_from_RGB_255
            )
        return colors
    else:
        raise exceptions.PlotlyError("You must select either rgb or tuple "
                                     "for your colortype variable.")


def make_colorscale(colors, scale=None):
    """
    Makes a colorscale from a list of colors and a scale

    Takes a list of colors and scales and constructs a colorscale based
    on the colors in sequential order. If 'scale' is left empty, a linear-
    interpolated colorscale will be generated. If 'scale' is a specificed
    list, it must be the same legnth as colors and must contain all floats
    For documentation regarding to the form of the output, see
    https://plot.ly/python/reference/#mesh3d-colorscale
    """
    colorscale = []

    # validate minimum colors length of 2
    if len(colors) < 2:
        raise exceptions.PlotlyError("You must input a list of colors that "
                                     "has at least two colors.")

    if not scale:
        scale_incr = 1./(len(colors) - 1)
        return [[i * scale_incr, color] for i, color in enumerate(colors)]

    else:
        # validate scale
        if len(colors) != len(scale):
            raise exceptions.PlotlyError("The length of colors and scale "
                                         "must be the same.")

        if (scale[0] != 0) or (scale[-1] != 1):
            raise exceptions.PlotlyError(
                "The first and last number in scale must be 0.0 and 1.0 "
                "respectively."
            )

        for j in range(1, len(scale)):
            if scale[j] <= scale[j-1]:
                raise exceptions.PlotlyError(
                    "'scale' must be a list that contains an increasing "
                    "sequence of numbers where the first and last number are"
                    "0.0 and 1.0 respectively."
                )

        colorscale = [list(tup) for tup in zip(scale, colors)]
        return colorscale


def find_intermediate_color(lowcolor, highcolor, intermed):
    """
    Returns the color at a given distance between two colors

    This function takes two color tuples, where each element is between 0
    and 1, along with a value 0 < intermed < 1 and returns a color that is
    intermed-percent from lowcolor to highcolor

    """
    diff_0 = float(highcolor[0] - lowcolor[0])
    diff_1 = float(highcolor[1] - lowcolor[1])
    diff_2 = float(highcolor[2] - lowcolor[2])

    inter_colors = (lowcolor[0] + intermed * diff_0,
                    lowcolor[1] + intermed * diff_1,
                    lowcolor[2] + intermed * diff_2)
    return inter_colors


def unconvert_from_RGB_255(colors):
    """
    Return a tuple where each element gets divided by 255

    Takes a (list of) color tuple(s) where each element is between 0 and
    255. Returns the same tuples where each tuple element is normalized to
    a value between 0 and 1

    """
    un_rgb_color = (colors[0]/(255.0),
                    colors[1]/(255.0),
                    colors[2]/(255.0))

    return un_rgb_color


def convert_to_RGB_255(colors):
    """
    Multiplies each element of a triplet by 255
    """
    return (colors[0]*255.0, colors[1]*255.0, colors[2]*255.0)


def n_colors(lowcolor, highcolor, n_colors):
    """
    Splits a low and high color into a list of n_colors colors in it

    Accepts two color tuples and returns a list of n_colors colors
    which form the intermediate colors between lowcolor and highcolor
    from linearly interpolating through RGB space

    """
    diff_0 = float(highcolor[0] - lowcolor[0])
    incr_0 = diff_0/(n_colors - 1)
    diff_1 = float(highcolor[1] - lowcolor[1])
    incr_1 = diff_1/(n_colors - 1)
    diff_2 = float(highcolor[2] - lowcolor[2])
    incr_2 = diff_2/(n_colors - 1)
    color_tuples = []

    for index in range(n_colors):
        new_tuple = (lowcolor[0] + (index * incr_0),
                     lowcolor[1] + (index * incr_1),
                     lowcolor[2] + (index * incr_2))
        color_tuples.append(new_tuple)

    return color_tuples


def label_rgb(colors):
    """
    Takes tuple (a, b, c) and returns an rgb color 'rgb(a, b, c)'
    """
    return ('rgb(%s, %s, %s)' % (colors[0], colors[1], colors[2]))


def unlabel_rgb(colors):
    """
    Takes rgb color(s) 'rgb(a, b, c)' and returns tuple(s) (a, b, c)

    This function takes either an 'rgb(a, b, c)' color or a list of
    such colors and returns the color tuples in tuple(s) (a, b, c)

    """
    str_vals = ''
    for index in range(len(colors)):
        try:
            float(colors[index])
            str_vals = str_vals + colors[index]
        except ValueError:
            if colors[index] == ',' or colors[index] == '.':
                str_vals = str_vals + colors[index]

    str_vals = str_vals + ','
    numbers = []
    str_num = ''
    for char in str_vals:
        if char != ',':
            str_num = str_num + char
        else:
            numbers.append(float(str_num))
            str_num = ''
    return (numbers[0], numbers[1], numbers[2])


def hex_to_rgb(value):
    """
    Calculates rgb values from a hex color code.

    :param (string) value: Hex color string

    :rtype (tuple) (r_value, g_value, b_value): tuple of rgb values
    """
    value = value.lstrip('#')
    hex_total_length = len(value)
    rgb_section_length = hex_total_length // 3
    return tuple(int(value[i:i + rgb_section_length], 16)
                 for i in range(0, hex_total_length, rgb_section_length))


def colorscale_to_colors(colorscale):
    """
    Converts a colorscale into a list of colors
    """
    color_list = []
    for color in colorscale:
        color_list.append(color[1])
    return color_list
