"""
Tools

A module for converting from mpl language to plotly language.

"""


def check_bar_match(old_bar, new_bar):
    """Check if two bars belong in the same collection (bar chart).

    Positional arguments:
    old_bar -- a previously sorted bar dictionary.
    new_bar -- a new bar dictionary that needs to be sorted.

    """
    tests = []
    tests += new_bar['orientation'] == old_bar['orientation'],
    tests += new_bar['facecolor'] == old_bar['facecolor'],
    if new_bar['orientation'] == 'v':
        new_width = new_bar['x1'] - new_bar['x0']
        old_width = old_bar['x1'] - old_bar['x0']
        tests += new_width - old_width < 0.000001,
        tests += new_bar['y0'] == old_bar['y0'],
    elif new_bar['orientation'] == 'h':
        new_height = new_bar['y1'] - new_bar['y0']
        old_height = old_bar['y1'] - old_bar['y0']
        tests += new_height - old_height < 0.000001,
        tests += new_bar['x0'] == old_bar['x0'],
    if all(tests):
        return True
    else:
        return False


def clean_dict(node, parent=None, node_key=None):
    """Remove None, 'none', 'None', and {} from a dictionary obj.

    When Plotly JSON dictionary entries are populated, Plotly will
    automatically fill in necessary items with defaults. However, if a
    nonsense entry is sent to plotly, it won't know to deal with it. This
    function removes some common 'nonsense' entries like empty dicts, None,
    'None', or 'none'.

    The clean_dict function will typically be called with a dictionary
    argument only, allowing parent and node_key to remain defaults. The
    choice of node reflects that this function works recursively.

    Positional arguments:
    node -- a dictionary that needs to be cleaned

    Keyword arguments:
    parent -- the dictionary that contains node (default None)
    node_key -- parent[node_key] == node (default None)

    """
    del_keys = []
    for key, item in node.items():
        if isinstance(item, dict):
            clean_dict(item, node, key)
        else:
            if item in [None, 'none', 'None']:
                del_keys += [key]
    for key in del_keys:
        del node[key]
    if parent is not None:
        if len(node) == 0:
            del parent[node_key]


def convert_affine_trans(dpi=None, aff=None):
    if aff is not None and dpi is not None:
        try:
            return aff.to_values()[0]*72/dpi
        except AttributeError:
            return aff[0][0]*72/dpi
    else:
        return None


def convert_dash(mpl_dash):
    """Convert mpl line symbol to plotly line symbol and return symbol."""
    if mpl_dash in DASH_MAP:
        return DASH_MAP[mpl_dash]
    else:
        return 'solid'  # default


def convert_path(path):
    verts = path[0]  # may use this later
    code = tuple(path[1])
    if code in PATH_MAP:
        return PATH_MAP[code]
    else:
        return None


def convert_symbol(mpl_symbol):
    """Convert mpl marker symbol to plotly symbol and return symbol."""
    if mpl_symbol in SYMBOL_MAP:
        return SYMBOL_MAP[mpl_symbol]
    else:
        return 'dot'  # default


def convert_va(mpl_va):
    """Convert mpl vertical alignment word to equivalent HTML word.

    Text alignment specifiers from mpl differ very slightly from those used
    in HTML. See the VA_MAP for more details.

    Positional arguments:
    mpl_va -- vertical mpl text alignment spec.

    """
    if mpl_va in VA_MAP:
        return VA_MAP[mpl_va]
    else:
        return None  # let plotly figure it out!


def convert_x_domain(mpl_plot_bounds, mpl_max_x_bounds):
    """Map x dimension of current plot to plotly's domain space.

    The bbox used to locate an axes object in mpl differs from the
    method used to locate axes in plotly. The mpl version locates each
    axes in the figure so that axes in a single-plot figure might have
    the bounds, [0.125, 0.125, 0.775, 0.775] (x0, y0, width, height),
    in mpl's figure coordinates. However, the axes all share one space in
    plotly such that the domain will always be [0, 0, 1, 1]
    (x0, y0, x1, y1). To convert between the two, the mpl figure bounds
    need to be mapped to a [0, 1] domain for x and y. The margins set
    upon opening a new figure will appropriately match the mpl margins.

    Optionally, setting margins=0 and simply copying the domains from
    mpl to plotly would place axes appropriately. However,
    this would throw off axis and title labeling.

    Positional arguments:
    mpl_plot_bounds -- the (x0, y0, width, height) params for current ax **
    mpl_max_x_bounds -- overall (x0, x1) bounds for all axes **

    ** these are all specified in mpl figure coordinates

    """
    mpl_x_dom = [mpl_plot_bounds[0], mpl_plot_bounds[0]+mpl_plot_bounds[2]]
    plotting_width = (mpl_max_x_bounds[1]-mpl_max_x_bounds[0])
    x0 = (mpl_x_dom[0]-mpl_max_x_bounds[0])/plotting_width
    x1 = (mpl_x_dom[1]-mpl_max_x_bounds[0])/plotting_width
    return [x0, x1]


def convert_y_domain(mpl_plot_bounds, mpl_max_y_bounds):
    """Map y dimension of current plot to plotly's domain space.

    The bbox used to locate an axes object in mpl differs from the
    method used to locate axes in plotly. The mpl version locates each
    axes in the figure so that axes in a single-plot figure might have
    the bounds, [0.125, 0.125, 0.775, 0.775] (x0, y0, width, height),
    in mpl's figure coordinates. However, the axes all share one space in
    plotly such that the domain will always be [0, 0, 1, 1]
    (x0, y0, x1, y1). To convert between the two, the mpl figure bounds
    need to be mapped to a [0, 1] domain for x and y. The margins set
    upon opening a new figure will appropriately match the mpl margins.

    Optionally, setting margins=0 and simply copying the domains from
    mpl to plotly would place axes appropriately. However,
    this would throw off axis and title labeling.

    Positional arguments:
    mpl_plot_bounds -- the (x0, y0, width, height) params for current ax **
    mpl_max_y_bounds -- overall (y0, y1) bounds for all axes **

    ** these are all specified in mpl figure coordinates

    """
    mpl_y_dom = [mpl_plot_bounds[1], mpl_plot_bounds[1]+mpl_plot_bounds[3]]
    plotting_height = (mpl_max_y_bounds[1]-mpl_max_y_bounds[0])
    y0 = (mpl_y_dom[0]-mpl_max_y_bounds[0])/plotting_height
    y1 = (mpl_y_dom[1]-mpl_max_y_bounds[0])/plotting_height
    return [y0, y1]


def display_to_paper(x, y, layout):
    """Convert mpl display coordinates to plotly paper coordinates.

    Plotly references object positions with an (x, y) coordinate pair in either
    'data' or 'paper' coordinates which reference actual data in a plot or
    the entire plotly axes space where the bottom-left of the bottom-left
    plot has the location (x, y) = (0, 0) and the top-right of the top-right
    plot has the location (x, y) = (1, 1). Display coordinates in mpl reference
    objects with an (x, y) pair in pixel coordinates, where the bottom-left
    corner is at the location (x, y) = (0, 0) and the top-right corner is at
    the location (x, y) = (figwidth*dpi, figheight*dpi). Here, figwidth and
    figheight are in inches and dpi are the dots per inch resolution.

    """
    num_x = x - layout['margin']['l']
    den_x = layout['width'] - (layout['margin']['l'] + layout['margin']['r'])
    num_y = y - layout['margin']['b']
    den_y = layout['height'] - (layout['margin']['b'] + layout['margin']['t'])
    return num_x/den_x, num_y/den_y


def get_axes_bounds(fig):
    """Return the entire axes space for figure.

    An axes object in mpl is specified by its relation to the figure where
    (0,0) corresponds to the bottom-left part of the figure and (1,1)
    corresponds to the top-right. Margins exist in matplotlib because axes
    objects normally don't go to the edges of the figure.

    In plotly, the axes area (where all subplots go) is always specified with
    the domain [0,1] for both x and y. This function finds the smallest box,
    specified by two points, that all of the mpl axes objects fit into. This
    box is then used to map mpl axes domains to plotly axes domains.

    """
    x_min, x_max, y_min, y_max = [], [], [], []
    for axes_obj in fig.get_axes():
        bounds = axes_obj.get_position().bounds
        x_min.append(bounds[0])
        x_max.append(bounds[0]+bounds[2])
        y_min.append(bounds[1])
        y_max.append(bounds[1]+bounds[3])
    x_min, y_min, x_max, y_max = min(x_min), min(y_min), max(x_max), max(y_max)
    return (x_min, x_max), (y_min, y_max)


def get_rect_xmin(data):
    """Find minimum x value from four (x,y) vertices."""
    return min(data[0][0], data[1][0], data[2][0], data[3][0])


def get_rect_xmax(data):
    """Find maximum x value from four (x,y) vertices."""
    return max(data[0][0], data[1][0], data[2][0], data[3][0])


def get_rect_ymin(data):
    """Find minimum y value from four (x,y) vertices."""
    return min(data[0][1], data[1][1], data[2][1], data[3][1])


def get_rect_ymax(data):
    """Find maximum y value from four (x,y) vertices."""
    return max(data[0][1], data[1][1], data[2][1], data[3][1])


def is_bar(**props):
    """A test to decide whether a path is a bar from a vertical bar chart."""
    tests = []
    tests += get_rect_ymin(props['data']) == 0,
    if all(tests):
        return True
    else:
        return False


def is_barh(**props):
    """A test to decide whether a path is a bar from a horizontal bar chart."""
    tests = []
    tests += get_rect_xmin(props['data']) == 0,
    if all(tests):
        return True
    else:
        return False


def make_bar(**props):
    """Make an intermediate bar dictionary.

    This creates a bar dictionary which aids in the comparison of new bars to
    old bars from other bar chart (patch) collections. This is not the
    dictionary that needs to get passed to plotly as a data dictionary. That
    happens in PlotlyRenderer in that class's draw_bar method. In other
    words, this dictionary describes a SINGLE bar, whereas, plotly will
    require a set of bars to be passed in a data dictionary.

    """
    return {
        'bar': props['mplobj'],
        'orientation': props['orientation'],
        'x0': get_rect_xmin(props['data']),
        'y0': get_rect_ymin(props['data']),
        'x1': get_rect_xmax(props['data']),
        'y1': get_rect_ymax(props['data']),
        'alpha': props['style']['alpha'],
        'edgecolor': props['style']['edgecolor'],
        'facecolor': props['style']['facecolor'],
        'edgewidth': props['style']['edgewidth'],
        'dasharray': props['style']['dasharray'],
        'zorder': props['style']['zorder']
    }


def repair_data(data):
    """Fixes innapropriate keys and values in plotly data list.

    This function calls repair_key() and repair_val() for each entry in
    DATA_KEY_REPAIRS and DATA_VAL_REPAIRS. It assumes that the keys in these
    dictionaries are tuples with paths to known possible errors.

    Positional arguments:
    data -- a list of plotly data dictionaries

    """
    for data_dict in data:
        for key_path_tup, fix in DATA_KEY_REPAIRS.items():
            repair_key(data_dict, key_path_tup, fix)
        for key_path_tup, repair_dict in DATA_VAL_REPAIRS.items():
                repair_val(data_dict, key_path_tup, repair_dict)


def repair_key(d, key_path_tup, fix):
    """Repairs inappropriate keys caused by referencing self.ax_ct.

    This function allows inappropriate keys to be used in the
    PlotlyRenderer.layout and PlotlyRenderer.data dictionaries. This is done
    for the following reasons:

    - Code is made simpler by treating 1st axes instance the same as
    subsequent axes instances.
    - If future releases of Plotly accept keys such as 'xaxis1' or 'yaxis1',
    renderer.py and plolty_utils.py can be updated simply.

    Dictionaries need not be continuous for use with a key_path_tup. For
    example, layout['annotations'] is actually a list of annotation
    dictionaries. When repair_key() runs into such a list, it assumes that
    the list is populated by dictionaries and continues down the rest of the
    key_path_tup for each dictionary in the list.

    Positional arguments:
    d -- a plotly layout or data dictionary
    key_path_tup -- a tuple of dictionary keys that leads to the conflict
    fix -- the appropriate dictionary key for the key_path_tup

    """
    try:
        for num, key in enumerate(key_path_tup[:-1]):
            d = d[key]
            if isinstance(d, list):
                for sub_d in d:
                    repair_key(sub_d, key_path_tup[num+1:], fix)
        d[fix] = d.pop(key_path_tup[-1])
    except KeyError:
        pass
    except TypeError:
        pass


def repair_layout(layout):
    """Fixes innapropriate keys and values in plotly layout dict.

    This function calls repair_key() and repair_val() for each entry in
    LAYOUT_KEY_REPAIRS and LAYOUT_VAL_REPAIRS. It assumes that the keys in
    these dictionaries are tuples with paths to known possible errors.

    Positional arguments:
    layout -- a plotly layout dictionary

    """
    for key_path_tup, fix in LAYOUT_KEY_REPAIRS.items():
        repair_key(layout, key_path_tup, fix)
    for key_path_tup, repair_dict in LAYOUT_VAL_REPAIRS.items():
            repair_val(layout, key_path_tup, repair_dict)


def repair_val(d, key_path_tup, repair_dict):
    """Repairs inappropriate values caused by referencing self.ax_ct.

    This function allows inappropriate values to be used in the
    PlotlyRenderer.layout and PlotlyRenderer.data dictionaries. This is done
    for the following reasons:

    - Code is made simpler by treating 1st axes instance the same as
    subsequent axes instances.
    - If future releases of Plotly accept values such as 'x1' or 'y1',
    renderer.py and plolty_utils.py can be updated simply.

    Dictionaries need not be continuous for use with a key_path_tup. For
    example, layout['annotations'] is actually a list of annotation
    dictionaries. When repair_val() runs into such a list, it assumes that
    the list is populated by dictionaries and continues down the rest of the
    key_path_tup for each dictionary in the list.

    Positional arguments:
    d -- a plotly layout or data dictionary
    key_path_tup -- a tuple of dictionary keys that leads to the conflict
    repair_dict -- a dictionary that contains {bad_value: good_value} entries

    """
    try:
        for num, key in enumerate(key_path_tup[:-1]):
            d = d[key]
            if isinstance(d, list):
                for sub_d in d:
                    repair_val(sub_d, key_path_tup[num+1:], repair_dict)
        for bug, fix in repair_dict.items():
            if d[key_path_tup[-1]] == bug:
                d[key_path_tup[-1]] = fix
    except KeyError:
        pass
    except TypeError:
        pass


def walk_and_strip(node, safe_keys):
    """Walk a dictionary or list structure and set unsafe keys to None

    This function is used primarly for stripping style properties from the
    data and layout dictionaries created by a PlotlyRenderer. It will walk
    through a collection, test keys against the specified 'safe-keys' list which
    are not to be deleted, and fill in a None value for unsafe key values.

    Cleaning the dictionary of these None values is relegated to the
    clean_dict function, which already has the capability to take care of this.

    Positional arguments:
    node -- the list or collection to be walked, tested, and stripped
    safe_keys -- a list of safe keys, intended for use with SAFE_KEYS[*]

    """
    if isinstance(node, dict):
        for key in node:
            if key in safe_keys:
                if isinstance(node[key], (dict, list)):
                    walk_and_strip(node[key], safe_keys)
            else:
                node[key] = None
    elif isinstance(node, list):
        for item in node:
            if isinstance(item, dict):
                walk_and_strip(item, safe_keys)

DATA_KEY_REPAIRS = {}

DATA_VAL_REPAIRS = {
    ('xaxis',): {'x1': None},
    ('yaxis',): {'y1': None}
}

LAYOUT_KEY_REPAIRS = {
    ('xaxis1',): 'xaxis',
    ('yaxis1',): 'yaxis'
}

LAYOUT_VAL_REPAIRS = {
    ('xaxis', 'anchor'): {'y1': 'y'},
    ('yaxis', 'anchor'): {'x1': 'x'},
    ('annotations', 'xref'): {'x1': 'x'},
    ('annotations', 'yref'): {'y1': 'y'}
}


DASH_MAP = {
    '10,0': 'solid',
    '6,6': 'dash',
    '2,2': 'dot',
    '4,4,2,4': 'dashdot',
    'none': 'solid'
}

PATH_MAP = {
    ('M', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'Z'): 'o',
    ('M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'Z'): '*',
    ('M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'Z'): '8',
    ('M', 'L', 'L', 'L', 'L', 'L', 'Z'): 'h',
    ('M', 'L', 'L', 'L', 'L', 'Z'): 'p',
    ('M', 'L', 'M', 'L', 'M', 'L'): '1',
    ('M', 'L', 'L', 'L', 'Z'): 's',
    ('M', 'L', 'M', 'L'): '+',
    ('M', 'L', 'L', 'Z'): '^',
    ('M', 'L'): '|'
}

SYMBOL_MAP = {
    'o': 'dot',
    'v': 'triangle-down',
    '^': 'triangle-up',
    '<': 'triangle-left',
    '>': 'triangle-right',
    's': 'square',
    '+': 'cross',
    'x': 'x',
    '*': 'x',  # no star yet in plotly!!
    'D': 'diamond',
    'd': 'diamond',
}

VA_MAP = {
    'center': 'middle',
    'baseline': 'bottom',
    'top': 'top'
}
