from __future__ import absolute_import

import decimal

from plotly import exceptions

DEFAULT_PLOTLY_COLORS = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                         'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                         'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                         'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                         'rgb(188, 189, 34)', 'rgb(23, 190, 207)']

# TODO: make PLOTLY_SCALES below like version in plotly.colors
# requires rewritting scatterplot_matrix code
PLOTLY_SCALES = {
    'Greys': ['rgb(0,0,0)', 'rgb(255,255,255)'],
    'YlGnBu': ['rgb(8,29,88)', 'rgb(255,255,217)'],
    'Greens': ['rgb(0,68,27)', 'rgb(247,252,245)'],
    'YlOrRd': ['rgb(128,0,38)', 'rgb(255,255,204)'],
    'Bluered': ['rgb(0,0,255)', 'rgb(255,0,0)'],
    'RdBu': ['rgb(5,10,172)', 'rgb(178,10,28)'],
    'Reds': ['rgb(220,220,220)', 'rgb(178,10,28)'],
    'Blues': ['rgb(5,10,172)', 'rgb(220,220,220)'],
    'Picnic': ['rgb(0,0,255)', 'rgb(255,0,0)'],
    'Rainbow': ['rgb(150,0,90)', 'rgb(255,0,0)'],
    'Portland': ['rgb(12,51,131)', 'rgb(217,30,30)'],
    'Jet': ['rgb(0,0,131)', 'rgb(128,0,0)'],
    'Hot': ['rgb(0,0,0)', 'rgb(255,255,255)'],
    'Blackbody': ['rgb(0,0,0)', 'rgb(160,200,255)'],
    'Earth': ['rgb(0,0,130)', 'rgb(255,255,255)'],
    'Electric': ['rgb(0,0,0)', 'rgb(255,250,220)'],
    'Viridis': ['#440154', '#fde725']
}


def validate_index(index_vals):
    """
    Validates if a list contains all numbers or all strings

    :raises: (PlotlyError) If there are any two items in the list whose
        types differ
    """
    from numbers import Number
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
    from numbers import Number
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
    from numbers import Number
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
    from numbers import Number
    if colors is None:
        colors = DEFAULT_PLOTLY_COLORS

    if isinstance(colors, str):
        if colors in PLOTLY_SCALES:
            colors = PLOTLY_SCALES[colors]
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

    if colortype == 'rgb':
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
