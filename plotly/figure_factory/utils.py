from __future__ import absolute_import

import collections
import decimal
import six
from numbers import Number

from plotly import exceptions


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
    ],
    
    'Cividis': [
        [0.000000, 'rgb(0,32,76)'], [0.058824, 'rgb(0,42,102)'], 
        [0.117647, 'rgb(0,52,110)'], [0.176471, 'rgb(39,63,108)'], 
        [0.235294, 'rgb(60,74,107)'], [0.294118, 'rgb(76,85,107)'], 
        [0.352941, 'rgb(91,95,109)'], [0.411765, 'rgb(104,106,112)'], 
        [0.470588, 'rgb(117,117,117)'], [0.529412, 'rgb(131,129,120)'], 
        [0.588235, 'rgb(146,140,120)'], [0.647059, 'rgb(161,152,118)'], 
        [0.705882, 'rgb(176,165,114)'], [0.764706, 'rgb(192,177,109)'], 
        [0.823529, 'rgb(209,191,102)'], [0.882353, 'rgb(225,204,92)'], 
        [0.941176, 'rgb(243,219,79)'], [1.000000, 'rgb(255,233,69)']
    ]
    
}


def is_sequence(obj):
    return (isinstance(obj, collections.Sequence) and
            not isinstance(obj, str))


def validate_index(index_vals):
    """
    Validates if a list contains all numbers or all strings

    :raises: (PlotlyError) If there are any two items in the list whose
        types differ
    """
    if isinstance(index_vals[0], Number):
        if not all(isinstance(item, Number) for item in index_vals):
            raise exceptions.PlotlyError("Error in indexing column. "
                                         "Make sure all entries of each "
                                         "column are all numbers or "
                                         "all strings.")

    elif isinstance(index_vals[0], str):
        if not all(isinstance(item, str) for item in index_vals):
            raise exceptions.PlotlyError("Error in indexing column. "
                                         "Make sure all entries of each "
                                         "column are all numbers or "
                                         "all strings.")


def validate_dataframe(array):
    """
    Validates all strings or numbers in each dataframe column

    :raises: (PlotlyError) If there are any two items in any list whose
        types differ
    """
    for vector in array:
        if isinstance(vector[0], Number):
            if not all(isinstance(item, Number) for item in vector):
                raise exceptions.PlotlyError("Error in dataframe. "
                                             "Make sure all entries of "
                                             "each column are either "
                                             "numbers or strings.")
        elif isinstance(vector[0], str):
            if not all(isinstance(item, str) for item in vector):
                raise exceptions.PlotlyError("Error in dataframe. "
                                             "Make sure all entries of "
                                             "each column are either "
                                             "numbers or strings.")


def validate_equal_length(*args):
    """
    Validates that data lists or ndarrays are the same length.

    :raises: (PlotlyError) If any data lists are not the same length.
    """
    length = len(args[0])
    if any(len(lst) != length for lst in args):
        raise exceptions.PlotlyError("Oops! Your data lists or ndarrays "
                                     "should be the same length.")


def validate_positive_scalars(**kwargs):
    """
    Validates that all values given in key/val pairs are positive.

    Accepts kwargs to improve Exception messages.

    :raises: (PlotlyError) If any value is < 0 or raises.
    """
    for key, val in kwargs.items():
        try:
            if val <= 0:
                raise ValueError('{} must be > 0, got {}'.format(key, val))
        except TypeError:
            raise exceptions.PlotlyError('{} must be a number, got {}'
                                         .format(key, val))


def flatten(array):
    """
    Uses list comprehension to flatten array

    :param (array): An iterable to flatten
    :raises (PlotlyError): If iterable is not nested.
    :rtype (list): The flattened list.
    """
    try:
        return [item for sublist in array for item in sublist]
    except TypeError:
        raise exceptions.PlotlyError("Your data array could not be "
                                     "flattened! Make sure your data is "
                                     "entered as lists or ndarrays!")


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

    return (lowcolor[0] + intermed * diff_0,
            lowcolor[1] + intermed * diff_1,
            lowcolor[2] + intermed * diff_2)


def n_colors(lowcolor, highcolor, n_colors, colortype='tuple'):
    """
    Splits a low and high color into a list of n_colors colors in it

    Accepts two color tuples and returns a list of n_colors colors
    which form the intermediate colors between lowcolor and highcolor
    from linearly interpolating through RGB space. If colortype is 'rgb'
    the function will return a list of colors in the same form.
    """
    if colortype == 'rgb':
        # convert to tuple
        lowcolor = unlabel_rgb(lowcolor)
        highcolor = unlabel_rgb(highcolor)

    diff_0 = float(highcolor[0] - lowcolor[0])
    incr_0 = diff_0/(n_colors - 1)
    diff_1 = float(highcolor[1] - lowcolor[1])
    incr_1 = diff_1/(n_colors - 1)
    diff_2 = float(highcolor[2] - lowcolor[2])
    incr_2 = diff_2/(n_colors - 1)
    list_of_colors = []

    for index in range(n_colors):
        new_tuple = (lowcolor[0] + (index * incr_0),
                     lowcolor[1] + (index * incr_1),
                     lowcolor[2] + (index * incr_2))
        list_of_colors.append(new_tuple)

    if colortype == 'rgb':
        # back to an rgb string
        list_of_colors = color_parser(list_of_colors, label_rgb)

    return list_of_colors


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


def unconvert_from_RGB_255(colors):
    """
    Return a tuple where each element gets divided by 255

    Takes a (list of) color tuple(s) where each element is between 0 and
    255. Returns the same tuples where each tuple element is normalized to
    a value between 0 and 1

    """
    return (colors[0]/(255.0),
            colors[1]/(255.0),
            colors[2]/(255.0))


def convert_to_RGB_255(colors):
    """
    Multiplies each element of a triplet by 255

    Each coordinate of the color tuple is rounded to the nearest float and
    then is turned into an integer. If a number is of the form x.5, then
    if x is odd, the number rounds up to (x+1). Otherwise, it rounds down
    to just x. This is the way rounding works in Python 3 and in current
    statistical analysis to avoid rounding bias
    """
    rgb_components = []

    for component in colors:
        rounded_num = decimal.Decimal(str(component*255.0)).quantize(
            decimal.Decimal('1'), rounding=decimal.ROUND_HALF_EVEN
        )
        # convert rounded number to an integer from 'Decimal' form
        rounded_num = int(rounded_num)
        rgb_components.append(rounded_num)

    return (rgb_components[0], rgb_components[1], rgb_components[2])


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


def validate_colors(colors, colortype='tuple'):
    """
    Validates color(s) and returns a list of color(s) of a specified type
    """
    if colors is None:
        colors = DEFAULT_PLOTLY_COLORS

    if isinstance(colors, str):
        if colors in PLOTLY_SCALES:
            colors_list = colorscale_to_colors(PLOTLY_SCALES[colors])
            colors = [colors_list[0]] + [colors_list[-1]]
        elif 'rgb' in colors or '#' in colors:
            colors = [colors]
        else:
            raise exceptions.PlotlyError(
                "If your colors variable is a string, it must be a "
                "Plotly scale, an rgb color or a hex color.")

    elif isinstance(colors, tuple):
        if isinstance(colors[0], Number):
            colors = [colors]
        else:
            colors = list(colors)

    # convert color elements in list to tuple color
    for j, each_color in enumerate(colors):
        if 'rgb' in each_color:
            each_color = color_parser(each_color, unlabel_rgb)
            for value in each_color:
                if value > 255.0:
                    raise exceptions.PlotlyError(
                        "Whoops! The elements in your rgb colors "
                        "tuples cannot exceed 255.0."
                    )
            each_color = color_parser(each_color, unconvert_from_RGB_255)
            colors[j] = each_color

        if '#' in each_color:
            each_color = color_parser(each_color, hex_to_rgb)
            each_color = color_parser(each_color, unconvert_from_RGB_255)

            colors[j] = each_color

        if isinstance(each_color, tuple):
            for value in each_color:
                if value > 1.0:
                    raise exceptions.PlotlyError(
                        "Whoops! The elements in your colors tuples "
                        "cannot exceed 1.0."
                    )
            colors[j] = each_color

    if colortype == 'rgb' and not isinstance(colors, six.string_types):
        for j, each_color in enumerate(colors):
            rgb_color = color_parser(each_color, convert_to_RGB_255)
            colors[j] = color_parser(rgb_color, label_rgb)

    return colors


def validate_colors_dict(colors, colortype='tuple'):
    """
    Validates dictioanry of color(s)
    """
    # validate each color element in the dictionary
    for key in colors:
        if 'rgb' in colors[key]:
            colors[key] = color_parser(colors[key], unlabel_rgb)
            for value in colors[key]:
                if value > 255.0:
                    raise exceptions.PlotlyError(
                        "Whoops! The elements in your rgb colors "
                        "tuples cannot exceed 255.0."
                    )
            colors[key] = color_parser(colors[key], unconvert_from_RGB_255)

        if '#' in colors[key]:
            colors[key] = color_parser(colors[key], hex_to_rgb)
            colors[key] = color_parser(colors[key], unconvert_from_RGB_255)

        if isinstance(colors[key], tuple):
            for value in colors[key]:
                if value > 1.0:
                    raise exceptions.PlotlyError(
                        "Whoops! The elements in your colors tuples "
                        "cannot exceed 1.0."
                    )

    if colortype == 'rgb':
        for key in colors:
            colors[key] = color_parser(colors[key], convert_to_RGB_255)
            colors[key] = color_parser(colors[key], label_rgb)

    return colors


def convert_colors_to_same_type(colors, colortype='rgb', scale=None,
                                return_default_colors=False,
                                num_of_defualt_colors=2):
    """
    Converts color(s) to the specified color type

    Takes a single color or an iterable of colors, as well as a list of scale
    values, and outputs a 2-pair of the list of color(s) converted all to an
    rgb or tuple color type, aswell as the scale as the second element. If
    colors is a Plotly Scale name, then 'scale' will be forced to the scale
    from the respective colorscale and the colors in that colorscale will also
    be coverted to the selected colortype. If colors is None, then there is an
    option to return portion of the DEFAULT_PLOTLY_COLORS

    :param (str|tuple|list) colors: either a plotly scale name, an rgb or hex
        color, a color tuple or a list/tuple of colors
    :param (list) scale: see docs for validate_scale_values()

    :rtype (tuple) (colors_list, scale) if scale is None in the function call,
        then scale will remain None in the returned tuple
    """
    #if colors_list is None:
    colors_list = []

    if colors is None and return_default_colors is True:
        colors_list = DEFAULT_PLOTLY_COLORS[0:num_of_defualt_colors]

    if isinstance(colors, str):
        if colors in PLOTLY_SCALES:
            colors_list = colorscale_to_colors(PLOTLY_SCALES[colors])
            if scale is None:
                scale = colorscale_to_scale(PLOTLY_SCALES[colors])

        elif 'rgb' in colors or '#' in colors:
            colors_list = [colors]

    elif isinstance(colors, tuple):
        if isinstance(colors[0], Number):
            colors_list = [colors]
        else:
            colors_list = list(colors)

    elif isinstance(colors, list):
        colors_list = colors

    # validate scale
    if scale is not None:
        validate_scale_values(scale)

        if len(colors_list) != len(scale):
            raise exceptions.PlotlyError(
                'Make sure that the length of your scale matches the length '
                'of your list of colors which is {}.'.format(len(colors_list))
            )

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
        return (colors_list, scale)
    elif colortype == 'tuple':
        for j, each_color in enumerate(colors_list):
            each_color = color_parser(
                each_color, unlabel_rgb
            )
            each_color = color_parser(
                each_color, unconvert_from_RGB_255
            )
            colors_list[j] = each_color
        return (colors_list, scale)
    else:
        raise exceptions.PlotlyError('You must select either rgb or tuple '
                                     'for your colortype variable.')


def colorscale_to_colors(colorscale):
    """
    Extracts the colors from colorscale as a list
    """
    color_list = []
    for item in colorscale:
        color_list.append(item[1])
    return color_list


def colorscale_to_scale(colorscale):
    """
    Extracts the interpolation scale values from colorscale as a list
    """
    scale_list = []
    for item in colorscale:
        scale_list.append(item[0])
    return scale_list


def validate_scale_values(scale):
    """
    Validates scale values from a colorscale

    :param (list) scale: a strictly increasing list of floats that begins
        with 0 and ends with 1. Its usage derives from a colorscale which is
        a list of two-lists (a list with two elements) of the form
        [value, color] which are used to determine how interpolation weighting
        works between the colors in the colorscale. Therefore scale is just
        the extraction of these values from the two-lists in order
    """
    if len(scale) < 2:
        raise exceptions.PlotlyError('You must input a list of scale values '
                                     'that has at least two values.')

    if (scale[0] != 0) or (scale[-1] != 1):
        raise exceptions.PlotlyError(
            'The first and last number in your scale must be 0.0 and 1.0 '
            'respectively.'
        )

    if not all(x < y for x, y in zip(scale, scale[1:])):
            raise exceptions.PlotlyError(
                "'scale' must be a list that contains a strictly increasing "
                "sequence of numbers."
            )


def validate_colorscale(colorscale):
    """Validate the structure, scale values and colors of colorscale."""
    if not isinstance(colorscale, list):
        #TODO Write tests for these exceptions
        raise exceptions.PlotlyError("A valid colorscale must be a list.")
    if not all(isinstance(innerlist, list) for innerlist in colorscale):
        raise exceptions.PlotlyError(
            "A valid colorscale must be a list of lists."
        )
    colorscale_colors = colorscale_to_colors(colorscale)
    scale_values = colorscale_to_scale(colorscale)

    validate_scale_values(scale_values)
    validate_colors(colorscale_colors)


def endpts_to_intervals(endpts):
    """
    Returns a list of intervals for categorical colormaps

    Accepts a list or tuple of sequentially increasing numbers and returns
    a list representation of the mathematical intervals with these numbers
    as endpoints. For example, [1, 6] returns [[-inf, 1], [1, 6], [6, inf]]

    :raises: (PlotlyError) If input is not a list or tuple
    :raises: (PlotlyError) If the input contains a string
    :raises: (PlotlyError) If any number does not increase after the
        previous one in the sequence
    """
    length = len(endpts)
    # Check if endpts is a list or tuple
    if not (isinstance(endpts, (tuple)) or isinstance(endpts, (list))):
        raise exceptions.PlotlyError("The intervals_endpts argument must "
                                     "be a list or tuple of a sequence "
                                     "of increasing numbers.")
    # Check if endpts contains only numbers
    for item in endpts:
        if isinstance(item, str):
            raise exceptions.PlotlyError("The intervals_endpts argument "
                                         "must be a list or tuple of a "
                                         "sequence of increasing "
                                         "numbers.")
    # Check if numbers in endpts are increasing
    for k in range(length - 1):
        if endpts[k] >= endpts[k + 1]:
            raise exceptions.PlotlyError("The intervals_endpts argument "
                                         "must be a list or tuple of a "
                                         "sequence of increasing "
                                         "numbers.")
    else:
        intervals = []
        # add -inf to intervals
        intervals.append([float('-inf'), endpts[0]])
        for k in range(length - 1):
            interval = []
            interval.append(endpts[k])
            interval.append(endpts[k + 1])
            intervals.append(interval)
        # add +inf to intervals
        intervals.append([endpts[length - 1], float('inf')])
        return intervals


def annotation_dict_for_label(text, lane, num_of_lanes, subplot_spacing,
                              row_col='col', flipped=True, right_side=True,
                              text_color='#0f0f0f'):
    """
    Returns annotation dict for label of n labels of a 1xn or nx1 subplot.

    :param (str) text: the text for a label.
    :param (int) lane: the label number for text. From 1 to n inclusive.
    :param (int) num_of_lanes: the number 'n' of rows or columns in subplot.
    :param (float) subplot_spacing: the value for the horizontal_spacing and
        vertical_spacing params in your plotly.tools.make_subplots() call.
    :param (str) row_col: choose whether labels are placed along rows or
        columns.
    :param (bool) flipped: flips text by 90 degrees. Text is printed
        horizontally if set to True and row_col='row', or if False and
        row_col='col'.
    :param (bool) right_side: only applicable if row_col is set to 'row'.
    :param (str) text_color: color of the text.
    """
    l = (1 - (num_of_lanes - 1) * subplot_spacing) / (num_of_lanes)
    if not flipped:
        xanchor = 'center'
        yanchor = 'middle'
        if row_col == 'col':
            x = (lane - 1) * (l + subplot_spacing) + 0.5 * l
            y = 1.03
            textangle = 0
        elif row_col == 'row':
            y = (lane - 1) * (l + subplot_spacing) + 0.5 * l
            x = 1.03
            textangle = 90
    else:
        if row_col == 'col':
            xanchor = 'center'
            yanchor = 'bottom'
            x = (lane - 1) * (l + subplot_spacing) + 0.5 * l
            y = 1.0
            textangle = 270
        elif row_col == 'row':
            yanchor = 'middle'
            y = (lane - 1) * (l + subplot_spacing) + 0.5 * l
            if right_side:
                x = 1.0
                xanchor = 'left'
            else:
                x = -0.01
                xanchor = 'right'
            textangle = 0

    annotation_dict = dict(
        textangle=textangle,
        xanchor=xanchor,
        yanchor=yanchor,
        x=x,
        y=y,
        showarrow=False,
        xref='paper',
        yref='paper',
        text=text,
        font=dict(
            size=13,
            color=text_color
        )
    )
    return annotation_dict


def list_of_options(iterable, conj='and', period=True):
    """
    Returns an English listing of objects seperated by commas ','

    For example, ['foo', 'bar', 'baz'] becomes 'foo, bar and baz'
    if the conjunction 'and' is selected.
    """
    if len(iterable) < 2:
        raise exceptions.PlotlyError(
            'Your list or tuple must contain at least 2 items.'
        )
    template = (len(iterable) - 2)*'{}, ' + '{} ' + conj + ' {}' + period*'.'
    return template.format(*iterable)
