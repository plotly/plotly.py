from io import StringIO
from os import path as opath

from codegen.utils import format_and_write_source_py

# Build dict with info about deprecated datatypes
DEPRECATED_DATATYPES = {
    # List types
    'Data':
        {'base_type': list,
         'new': ['Scatter', 'Bar', 'Area', 'Histogram', 'etc.']},
    'Annotations':
        {'base_type': list,
         'new': ['layout.Annotation', 'layout.scene.Annotation']},
    'Frames':
        {'base_type': list,
         'new': ['Frame']},

    # Dict types
    'AngularAxis':
        {'base_type': dict,
         'new': ['layout', 'layout.polar']},
    'Annotation':
        {'base_type': dict,
         'new': ['layout', 'layout.scene']},
    'ColorBar':
        {'base_type': dict,
         'new': ['scatter.marker', 'surface', 'etc.']},
    'Contours':
        {'base_type': dict,
         'new': ['contour', 'surface', 'etc.']},
    'ErrorX':
        {'base_type': dict,
         'new': ['scatter', 'histogram', 'etc.']},
    'ErrorY':
        {'base_type': dict,
         'new': ['scatter', 'histogram', 'etc.']},
    'ErrorZ':
        {'base_type': dict,
         'new': ['scatter3d']},
    'Font':
        {'base_type': dict,
         'new': ['layout', 'layout.hoverlabel', 'etc.']},
    'Legend':
        {'base_type': dict,
         'new': ['layout']},
    'Line':
        {'base_type': dict,
         'new': ['scatter', 'layout.shape', 'etc.']},
    'Margin':
        {'base_type': dict,
         'new': ['layout']},
    'Marker':
        {'base_type': dict,
         'new': ['scatter', 'histogram.selected', 'etc.']},
    'RadialAxis':
        {'base_type': dict,
         'new': ['layout', 'layout.polar']},
    'Scene':
        {'base_type': dict,
         'new': ['Scene']},
    'Stream':
        {'base_type': dict,
         'new': ['scatter', 'area']},
    'XAxis':
        {'base_type': dict,
         'new': ['layout', 'layout.scene']},
    'YAxis':
        {'base_type': dict,
         'new': ['layout', 'layout.scene']},
    'ZAxis':
        {'base_type': dict,
         'new': ['layout.scene']},
    'XBins':
        {'base_type': dict,
         'new': ['histogram', 'histogram2d']},
    'YBins':
        {'base_type': dict,
         'new': ['histogram', 'histogram2d']},
    'Trace':
        {'base_type': dict,
         'new': ['Scatter', 'Bar', 'Area', 'Histogram', 'etc.']},
    'Histogram2dcontour':
        {'base_type': dict,
         'new': ['Histogram2dContour']},
}


def build_deprecated_datatypes_py():
    """
    Build datatype (graph_objs) class source code string for deprecated
    datatypes

    Returns
    -------
    str
    """

    # Initialize source code buffer
    # -----------------------------
    buffer = StringIO()

    # Write warnings import
    # ---------------------
    buffer.write('import warnings\n')

    # Write warnings filter
    # ---------------------
    # Use filter to enable DeprecationWarnings on our deprecated classes
    buffer.write(r"""
warnings.filterwarnings('default',
                        r'plotly\.graph_objs\.\w+ is deprecated',
                        DeprecationWarning)


""")

    # Write deprecated class definitions
    # ----------------------------------
    for class_name, opts in DEPRECATED_DATATYPES.items():
        base_class_name = opts['base_type'].__name__
        depr_msg = build_deprecation_message(class_name, **opts)

        buffer.write(f"""\
class {class_name}({base_class_name}):
    \"\"\"
    {depr_msg}
    \"\"\"
    def __init__(self, *args, **kwargs):
        \"\"\"
        {depr_msg}
        \"\"\"
        warnings.warn(\"\"\"{depr_msg}\"\"\", DeprecationWarning)
        super({class_name}, self).__init__(*args, **kwargs)\n\n\n""")

    # Return source string
    # --------------------
    return buffer.getvalue()


def build_deprecation_message(class_name, base_type, new):
    """
    Build deprecation warning message for a deprecated class

    Parameters
    ----------
    class_name : str
        Name of a deprecated class
    base_type: type
        base class (either list or dict)
    new: list of str
        List of replacements that users should use instead.
        Replacements may be:
            - A package string relative to plotly.graph_objs. In this case the
              replacement class is assumed to be named `class_name`.
              e.g. `new` == ['layout`] and `class_name` == 'XAxis` corresponds
              to the 'plotly.graph_objs.layout.XAxis' class
            - String containing the package and class. The string is
              identified as containing a class name if the final name in the
              package string begins with an uppercase letter.
              e.g. `new` == ['Scatter'] corresponds to the
              ['plotly.graph_objs.Scatter'] class.
            - The literal string 'etc.'. This string is not interpreted as a
              package or class and is displayed to the user as-is to
              indicate that the list of replacement classes is not complete.

    Returns
    -------
    str
    """
    replacements = []
    for repl in new:

        if repl == 'etc.':
            replacements.append(repl)
        else:
            repl_parts = repl.split('.')

            # Add class_name if class not provided
            repl_is_class = repl_parts[-1][0].isupper()
            if not repl_is_class:
                repl_parts.append(class_name)

            # Add plotly.graph_objs prefix
            full_class_str = '.'.join(['plotly', 'graph_objs'] + repl_parts)
            replacements.append(full_class_str)

    replacemens_str = '\n  - '.join(replacements)

    if base_type == list:
        return f"""\
plotly.graph_objs.{class_name} is deprecated.
Please replace it with a list or tuple of instances of the following types
  - {replacemens_str}
"""
    else:
        return f"""\
plotly.graph_objs.{class_name} is deprecated.
Please replace it with one of the following more specific types
  - {replacemens_str}
"""


def write_deprecated_datatypes(outdir):
    """
    Build source code for deprecated datatype class definitions and write
    them to a file

    Parameters
    ----------
    outdir :
        Root outdir in which the graph_objs package should reside

    Returns
    -------
    None
    """
    # Generate source code
    # --------------------
    datatype_source = build_deprecated_datatypes_py()
    filepath = opath.join(outdir, 'graph_objs', '_deprecations.py')

    # Write file
    # ----------
    format_and_write_source_py(datatype_source, filepath)


def write_graph_objs_graph_objs(outdir):
    """
    Write the plotly/graph_objs/graph_objs.py file

    This module just imports everything from the plotly.graph_objs package.
    We write it for backward compatibility with legacy imports like:

    from plotly.graph_objs import graph_objs

    Parameters
    ----------
    outdir : str
        Root outdir in which the graph_objs package should reside

    Returns
    -------
    None
    """
    filepath = opath.join(outdir, 'graph_objs', 'graph_objs.py')
    with open(filepath, 'wt') as f:
        f.write("""\
from plotly.graph_objs import *
""")
