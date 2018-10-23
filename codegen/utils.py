import os
import os.path as opath
import textwrap
from collections import ChainMap
from importlib import import_module
from io import StringIO
from typing import List
import re

from yapf.yapflib.yapf_api import FormatCode


# Source code utilities
# =====================
def format_source(input_source):
    """
    Use yapf to format a string containing Python source code

    Parameters
    ----------
    input_source : str
      String containing Python source code

    Returns
    -------
    String containing yapf-formatted python source code
    """
    style_config = {'based_on_style': 'google',
                    'DEDENT_CLOSING_BRACKETS': True,
                    'COLUMN_LIMIT': 79}
    formatted_source, _ = FormatCode(input_source, style_config=style_config)
    return formatted_source


def format_and_write_source_py(py_source, filepath):
    """
    Format Python source code and write to a file, creating parent
    directories as needed.

    Parameters
    ----------
    py_source : str
        String containing valid Python source code. If string is empty,
        no file will be written.
    filepath : str
        Full path to the file to be written
    Returns
    -------
    None
    """
    if py_source:
        try:
            formatted_source = format_source(py_source)
        except Exception as e:
            print(py_source)
            raise e

        # Make dir if needed
        # ------------------
        filedir = opath.dirname(filepath)
        os.makedirs(filedir, exist_ok=True)

        # Write file
        # ----------
        with open(filepath, 'wt') as f:
            f.write(formatted_source)


def build_from_imports_py(imports_info):
    """
    Build a string containing a series of `from X import Y` lines

    Parameters
    ----------
    imports_info : str or list of (str, str or list of str)
          List of import info
            If element is a pair first entry is the package to be imported
            from and the second entry is either a string of the single name
            to be

            If element is a string, insert string directly
    Returns
    -------
    str
        String containing a series of imports
    """
    buffer = StringIO()
    for import_info in imports_info:

        if isinstance(import_info, tuple):
            from_pkg, class_name = import_info
            if isinstance(class_name, str):
                class_name_str = class_name
            else:
                class_name_str = '(' + ', '.join(class_name) + ')'

            buffer.write(f"""\
from {from_pkg} import {class_name_str}\n""")

        elif isinstance(import_info, str):
            buffer.write(import_info)

    return buffer.getvalue()


def write_init_py(pkg_root, path_parts, import_pairs):
    """
    Build __init__.py source code and write to a file

    Parameters
    ----------
    pkg_root : str
        Root package in which the top-level an __init__.py file with empty
        path_parts should reside
    path_parts : tuple of str
        Tuple of sub-packages under pkg_root where the __init__.py
        file should be written
    import_pairs : list of (str, str or list of str)
        List of pairs where first entry is the package to be imported from.
        The second entry is either a string of the single name to be
        imported, or a list of names to be imported.
    Returns
    -------
    None
    """
    # Generate source code
    # --------------------
    init_source = build_from_imports_py(import_pairs)

    # Write file
    # ----------
    filepath = opath.join(pkg_root, *path_parts, '__init__.py')
    format_and_write_source_py(init_source, filepath)


def format_description(desc):

    # Remove surrounding *s from numbers
    desc = re.sub('(^|[\s(,.:])\*([\d.]+)\*([\s),.:]|$)', r'\1\2\3', desc)

    # replace *true* with True
    desc = desc.replace("*true*", "True")
    desc = desc.replace("*false*", "False")

    # Replace *word* with "word"
    desc = re.sub('(^|[\s(,.:])\*(\S+)\*([\s),.:]|$)', r'\1"\2"\3', desc)

    # Special case strings that don't satisfy regex above
    other_strings = ['', 'Courier New', 'Droid Sans', 'Droid Serif',
                     'Droid Sans Mono', 'Gravitas One', 'Old Standard TT',
                     'Open Sans', 'PT Sans Narrow', 'Times New Roman',
                     'bottom plot', 'top plot']

    for s in other_strings:
        desc = desc.replace("*%s*" % s, '"%s"' % s)

    # Replace {array} with list
    desc = desc.replace("an {array}", "a list")
    desc = desc.replace("{array}", "list")

    # Replace {arrays} with lists
    desc = desc.replace("{arrays}", "lists")

    # replace {2D array} with 2D list
    desc = desc.replace("{2D array}", "2D list")

    # replace {2D arrays} with 2D lists
    desc = desc.replace("{2D arrays}", "2D lists")

    return desc


# Constants
# =========
# Mapping from full property paths to custom validator classes
CUSTOM_VALIDATOR_DATATYPES = {
    'layout.image.source': '_plotly_utils.basevalidators.ImageUriValidator',
    'layout.template': '_plotly_utils.basevalidators.BaseTemplateValidator',
    'frame.data': 'plotly.validators.DataValidator',
    'frame.layout': 'plotly.validators.LayoutValidator'
}

# Add custom dash validators
CUSTOM_VALIDATOR_DATATYPES.update(
    {prop: '_plotly_utils.basevalidators.DashValidator'
     for prop in [
         'scatter.line.dash',
         'histogram2dcontour.line.dash',
         'scattergeo.line.dash',
         'scatterpolar.line.dash',
         'ohlc.line.dash',
         'ohlc.decreasing.line.dash',
         'ohlc.increasing.line.dash',
         'contourcarpet.line.dash',
         'contour.line.dash',
         'scatterternary.line.dash',
         'scattercarpet.line.dash']})

# Mapping from property string (as found in plot-schema.json) to a custom
# class name. If not included here, names are converted to TitleCase and
# underscores are removed.
OBJECT_NAME_TO_CLASS_NAME = {
    'angularaxis': 'AngularAxis',
    'colorbar': 'ColorBar',
    'error_x': 'ErrorX',
    'error_y': 'ErrorY',
    'error_z': 'ErrorZ',
    'histogram2d': 'Histogram2d',
    'histogram2dcontour': 'Histogram2dContour',
    'mesh3d': 'Mesh3d',
    'radialaxis': 'RadialAxis',
    'scatter3d': 'Scatter3d',
    'xaxis': 'XAxis',
    'xbins': 'XBins',
    'yaxis': 'YAxis',
    'ybins': 'YBins',
    'zaxis': 'ZAxis'
}

# Tuple of types to be considered dicts by PlotlyNode logic
dict_like = (dict, ChainMap)


# PlotlyNode classes
# ==================
class PlotlyNode:
    """
    Base class that represents a node in the plot-schema.json file
    """

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        """
        Superclass constructor for all node types

        Parameters
        ----------
        plotly_schema : dict
            JSON-parsed version of the default-schema.xml file
        node_path : str or tuple
            Path of from the 'root' node for the current trace type to the
            particular node that this instance represents
        parent : PlotlyNode
            Reference to the node's parent
        """
        # Save params
        # -----------
        self.plotly_schema = plotly_schema
        self._parent = parent

        # ### Process node path ###
        if isinstance(node_path, str):
            node_path = (node_path,)
        self.node_path = node_path

        # Compute children
        # ----------------
        # Note the node_data is a property that must be computed by the
        # subclass based on plotly_schema and node_path
        if isinstance(self.node_data, dict_like):
            childs_parent = (
                parent
                if self.node_path and self.node_path[-1] == 'items'
                else self)

            self._children = [self.__class__(self.plotly_schema,
                                             node_path=self.node_path + (c,),
                                             parent=childs_parent)
                              for c in self.node_data if c and c[0] != '_']

            # Sort by plotly name
            self._children = sorted(self._children,
                                    key=lambda node: node.plotly_name)
        else:
            self._children = []

    # Magic methods
    # -------------
    def __repr__(self):
        return self.path_str

    # Abstract methods
    # ----------------
    @property
    def node_data(self):
        """
        Dictionary of the subtree of the plotly_schema that this node
        represents

        Returns
        -------
        dict
        """
        raise NotImplementedError()

    @property
    def description(self):
        """
        Description of the node

        Returns
        -------
        str or None
        """
        raise NotImplementedError()

    @property
    def name_base_datatype(self):
        """
        Superclass to use when generating a datatype class for this node

        Returns
        -------
        str
        """
        raise NotImplementedError

    # Names
    # -----
    @property
    def root_name(self):
        """
        Name of the node with empty node_path

        Returns
        -------
        str
        """
        raise NotImplementedError()

    @property
    def plotly_name(self) :
        """
        Name of the node. Either the base_name or the name directly out of
        the plotly_schema

        Returns
        -------
        str
        """
        if len(self.node_path) == 0:
            return self.root_name
        else:
            return self.node_path[-1]

    @property
    def name_datatype_class(self):
        """
        Name of the Python datatype class representing this node

        Returns
        -------
        str
        """
        if self.plotly_name in OBJECT_NAME_TO_CLASS_NAME:
            return OBJECT_NAME_TO_CLASS_NAME[self.plotly_name]
        else:
            return self.plotly_name.title().replace('_', '')

    @property
    def name_undercase(self):
        """
        Name of node converted to undercase (all lowercase with underscores
        separating words)

        Returns
        -------
        str
        """
        if not self.plotly_name:
            # Empty plotly_name
            return self.plotly_name

        # Lowercase leading char
        # ----------------------
        name1 = self.plotly_name[0].lower() + self.plotly_name[1:]

        # Replace capital chars by underscore-lower
        # -----------------------------------------
        name2 = ''.join([('' if not c.isupper() else '_') + c.lower()
                         for c in name1])

        return name2

    @property
    def name_property(self):
        """
        Name of the Python property corresponding to this node. This is the
        same as `name_undercase` for compound nodes, but an 's' is appended
        to the name for array nodes

        Returns
        -------
        str
        """

        return self.plotly_name + (
            's' if self.is_array_element and
                   # Don't add 's' to layout.template.data.scatter etc.
                   not (self.parent and
                        self.parent.parent and
                        self.parent.parent.parent and
                        self.parent.parent.parent.name_property == 'template')
            else '')

    @property
    def name_validator_class(self) -> str:
        """
        Name of the Python validator class representing this node

        Returns
        -------
        str
        """
        return (self.name_datatype_class +
                ('s' if self.is_array_element else '') +
                'Validator')

    @property
    def name_base_validator(self) -> str:
        """
        Superclass to use when generating a validator class for this node

        Returns
        -------
        str
        """
        if self.path_str in CUSTOM_VALIDATOR_DATATYPES:
            validator_base = f"{CUSTOM_VALIDATOR_DATATYPES[self.path_str]}"
        elif self.plotly_name.endswith('src') and self.datatype == 'string':
            validator_base = (f"_plotly_utils.basevalidators."
                              f"SrcValidator")
        else:
            datatype_title_case = self.datatype.title().replace('_', '')
            validator_base = (f"_plotly_utils.basevalidators."
                              f"{datatype_title_case}Validator")

        return validator_base

    # Validators
    # ----------
    def get_validator_params(self):
        """
        Get kwargs to pass to the constructor of this node's validator
        superclass.

        Returns
        -------
        dict
            The keys are strings matching the names of the constructor
            params of this node's validator superclass. The values are
            repr-strings of the values to be passed to the constructor.
            These values are ready to be used to code generate calls to the
            constructor. The values should be evald before being passed to
            the constructor directly.

        """
        params = {'plotly_name': repr(self.name_property),
                  'parent_name': repr(self.parent_path_str)}

        if self.is_compound:
            params['data_class_str'] = repr(self.name_datatype_class)
            params['data_docs'] = (
                    '\"\"\"' +
                    self.get_constructor_params_docstring() +
                    '\n\"\"\"')
        else:
            assert self.is_simple

            # Exclude general properties
            excluded_props = ['valType', 'description', 'dflt']
            if self.datatype == 'subplotid':
                # Default is required for subplotid validator
                excluded_props.remove('dflt')

            attr_nodes = [n for n in self.simple_attrs
                          if n.plotly_name not in excluded_props]

            for node in attr_nodes:
                params[node.name_undercase] = repr(node.node_data)

            # Add extra properties
            if self.datatype == 'color' and self.parent:
                # Check for colorscale sibling. We use the presence of a
                # colorscale sibling to determine whether numeric color
                # values are permissible
                colorscale_node_list = [node for node in
                                        self.parent.child_datatypes
                                        if node.datatype == 'colorscale']
                if colorscale_node_list:
                    colorscale_path = colorscale_node_list[0].path_str
                    params['colorscale_path'] = repr(colorscale_path)
            elif self.datatype == 'literal':
                params['val'] = self.node_data

        return params

    def get_validator_instance(self):
        """
        Return a constructed validator for this node

        Returns
        -------
        BaseValidator
        """

        # Evaluate validator params to convert repr strings into values
        # e.g. '2' -> 2
        params = {prop: eval(repr_val)
                  for prop, repr_val in self.get_validator_params().items()}

        validator_parts = self.name_base_validator.split('.')
        if validator_parts[0] != '_plotly_utils':
            return None
        else:
            validator_class_str = validator_parts[-1]
            validator_module = '.'.join(validator_parts[:-1])

            validator_class = getattr(import_module(validator_module),
                                      validator_class_str)

            return validator_class(**params)

    # Datatypes
    # ---------
    @property
    def datatype(self) -> str:
        """
        Datatype string for this node. One of 'compound_array', 'compound',
        'literal', or the value of the 'valType' attribute

        Returns
        -------
        str
        """
        if self.is_array_element:
            return 'compound_array'
        elif self.is_compound:
            return 'compound'
        elif self.is_simple:
            return self.node_data.get('valType')
        else:
            return 'literal'

    @property
    def is_array_ok(self) -> bool:
        """
        Return true if arrays of datatype are acceptable

        Returns
        -------
        bool
        """
        return self.node_data.get('arrayOk', False)

    @property
    def is_compound(self) -> bool:
        """
        Node has a compound (in contrast to simple) datatype.
        Note: All array and array_element types are also considered compound

        Returns
        -------
        bool
        """
        return (isinstance(self.node_data, dict_like) and
                not self.is_simple and
                self.plotly_name not in ('items', 'impliedEdits', 'transforms'))

    @property
    def is_literal(self) -> bool:
        """
        Node has a particular literal value (e.g. 'foo', or 23)

        Returns
        -------
        bool
        """
        return isinstance(self.node_data, (str, int, float))

    @property
    def is_simple(self) -> bool:
        """
        Node has a simple datatype (e.g. boolean, color, colorscale, etc.)

        Returns
        -------
        bool
        """
        return (isinstance(self.node_data, dict_like) and
                'valType' in self.node_data and
                self.plotly_name != 'items')

    @property
    def is_array(self) -> bool:
        """
        Node has an array datatype

        Returns
        -------
        bool
        """
        return (isinstance(self.node_data, dict_like) and
                self.node_data.get('role', '') == 'object' and
                'items' in self.node_data and
                self.name_property != 'transforms')

    @property
    def is_array_element(self):
        """
        Node has an array-element datatype

        Returns
        -------
        bool
        """
        if self.parent:
            return self.parent.is_array
        else:
            return False

    @property
    def is_datatype(self) -> bool:
        """
        Node represents any kind of datatype

        Returns
        -------
        bool
        """
        return self.is_simple or self.is_compound or self.is_array

    # Node path
    # ---------
    def tidy_path_part(self, p):
        """
        Return a tidy version of raw path entry. This allows subclasses to
        adjust the raw property names in the plotly_schema

        Parameters
        ----------
        p : str
            Path element string

        Returns
        -------
        str
        """
        return p

    @property
    def path_parts(self):
        """
        Tuple of strings locating this node in the plotly_schema
        e.g. ('layout', 'images', 'opacity')

        Returns
        -------
        tuple of str
        """
        res = [self.root_name] if self.root_name else []
        for i, p in enumerate(self.node_path):
            # Handle array datatypes
            if (p == 'items' or
                    (i < len(self.node_path) - 1 and
                     self.node_path[i+1] == 'items')):
                # e.g. [parcoords, dimensions, items, dimension] ->
                #      [parcoords, dimension]
                pass
            else:
                res.append(self.tidy_path_part(p))
        return tuple(res)

    # Node path strings
    # -----------------
    @property
    def path_str(self):
        """
        String containing path_parts joined on periods
        e.g. 'layout.images.opacity'

        Returns
        -------
        str
        """
        return '.'.join(self.path_parts)

    @property
    def dotpath_str(self):
        """
        path_str prefixed by a period if path_str is not empty, otherwise empty

        Returns
        -------
        str
        """
        path_str = ''
        for p in self.path_parts:
            path_str += '.' + p
        return path_str

    @property
    def parent_path_parts(self):
        """
        Tuple of strings locating this node's parent in the plotly_schema

        Returns
        -------
        tuple of str
        """
        return self.path_parts[:-1]

    @property
    def parent_path_str(self):
        """
        String containing parent_path_parts joined on periods

        Returns
        -------
        str
        """
        return '.'.join(self.path_parts[:-1])

    @property
    def parent_dotpath_str(self):
        """
        parent_path_str prefixed by a period if parent_path_str is not empty,
        otherwise empty

        Returns
        -------
        str
        """
        path_str = ''
        for p in self.parent_path_parts:
            path_str += '.' + p
        return path_str

    # Children
    # --------
    @property
    def parent(self):
        """
        Parent node

        Returns
        -------
        PlotlyNode
        """
        return self._parent

    @property
    def children(self):
        """
        List of all child nodes

        Returns
        -------
        list of PlotlyNode
        """
        return self._children

    @property
    def simple_attrs(self):
        """
        List of simple attribute child nodes
        (only valid when is_simple == True)

        Returns
        -------
        list of PlotlyNode
        """
        if not self.is_simple:
            raise ValueError(
                f"Cannot get simple attributes of the simple object '{self.path_str}'")

        return [n for n in self.children if n.plotly_name not in ['valType', 'description']]

    @property
    def child_datatypes(self):
        """
        List of all datatype child nodes

        Returns
        -------
        list of PlotlyNode
        """
        nodes = []
        for n in self.children:
            if n.is_array:
                # Add array element node
                nodes.append(n.children[0].children[0])

                # Add elementdefaults node. Require parent_path_parts not
                # empty to avoid creating defaults classes for traces
                if (n.parent_path_parts and
                        n.parent_path_parts != ('layout', 'template', 'data')):

                    nodes.append(ElementDefaultsNode(n, self.plotly_schema))

            elif n.is_datatype:
                nodes.append(n)

        return nodes

    @property
    def child_compound_datatypes(self):
        """
        List of all compound datatype child nodes

        Returns
        -------
        list of PlotlyNode
        """
        return [n for n in self.child_datatypes if n.is_compound]

    @property
    def child_simple_datatypes(self) -> List['PlotlyNode']:
        """
        List of all simple datatype child nodes

        Returns
        -------
        list of PlotlyNode
        """
        return [n for n in self.child_datatypes if n.is_simple]

    @property
    def child_literals(self) -> List['PlotlyNode']:
        """
        List of all literal child nodes

        Returns
        -------
        list of PlotlyNode
        """
        return [n for n in self.children if n.is_literal]

    def get_constructor_params_docstring(self, indent=12):
        """
        Return a docstring-style string containing the names and
        descriptions of all of the node's child datatypes

        Parameters
        ----------
        indent : int
            Leading indent of the string

        Returns
        -------
        str
        """
        assert self.is_compound

        buffer = StringIO()

        subtype_nodes = self.child_datatypes
        for subtype_node in subtype_nodes:
            raw_description = subtype_node.description
            if raw_description:
                subtype_description = raw_description
            elif subtype_node.is_compound:
                class_name = (f'plotly.graph_objs'
                              f'{subtype_node.parent_dotpath_str}.'
                              f'{subtype_node.name_datatype_class}')

                subtype_description = (f'{class_name} instance or '
                                      'dict with compatible properties')
            else:
                subtype_description = ''

            subtype_description = '\n'.join(
                textwrap.wrap(subtype_description,
                              initial_indent=' ' * (indent + 4),
                              subsequent_indent=' ' * (indent + 4),
                              width=79 - (indent + 4)))

            buffer.write('\n' + ' ' * indent + subtype_node.name_property)
            buffer.write('\n' + subtype_description)

        return buffer.getvalue()

    # Static helpers
    # --------------
    @staticmethod
    def get_all_compound_datatype_nodes(plotly_schema, node_class):
        """
        Build a list of the entire hierarchy of compound datatype nodes for
        a given PlotlyNode subclass

        Parameters
        ----------
        plotly_schema : dict
            JSON-parsed version of the default-schema.xml file
        node_class
            PlotlyNode subclass

        Returns
        -------
        list of PlotlyNode
        """
        nodes = []
        nodes_to_process = [node_class(plotly_schema)]

        while nodes_to_process:
            node = nodes_to_process.pop()

            if node.plotly_name and not node.is_array:
                nodes.append(node)

            non_defaults_compound_children = [
                node for node in node.child_compound_datatypes
                if not isinstance(node, ElementDefaultsNode)]

            nodes_to_process.extend(non_defaults_compound_children)

        return nodes

    @staticmethod
    def get_all_datatype_nodes(plotly_schema, node_class):
        """
        Build a list of the entire hierarchy of datatype nodes for a given
        PlotlyNode subclass

        Parameters
        ----------
        plotly_schema : dict
            JSON-parsed version of the default-schema.xml file
        node_class
            PlotlyNode subclass

        Returns
        -------
        list of PlotlyNode
        """
        nodes = []
        nodes_to_process = [node_class(plotly_schema)]

        while nodes_to_process:
            node = nodes_to_process.pop()

            if node.plotly_name and not node.is_array:
                nodes.append(node)

            nodes_to_process.extend(node.child_datatypes)

        return nodes


class TraceNode(PlotlyNode):
    """
    Class representing datatypes in the trace hierarchy
    """

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        super().__init__(plotly_schema, node_path, parent)

    @property
    def name_base_datatype(self):
        if len(self.node_path) <= 1:
            return 'BaseTraceType'
        else:
            return 'BaseTraceHierarchyType'

    @property
    def root_name(self):
        return ''

    # Raw data
    # --------
    @property
    def node_data(self) -> dict:
        if not self.node_path:
            node_data = self.plotly_schema['traces']
        else:
            trace_name = self.node_path[0]
            node_data = self.plotly_schema['traces'][trace_name]['attributes']
            for prop_name in self.node_path[1:]:
                node_data = node_data[prop_name]

        return node_data

    # Description
    # -----------
    @property
    def description(self) -> str:
        if len(self.node_path) == 0:
            desc = ""
        elif len(self.node_path) == 1:
            # Get trace descriptions
            trace_name = self.node_path[0]
            desc = (self.plotly_schema['traces'][trace_name]
                    ['meta'].get('description', ''))
        else:
            # Get datatype description
            desc = self.node_data.get('description', '')

        if isinstance(desc, list):
            desc = ''.join(desc)

        return format_description(desc)


class LayoutNode(PlotlyNode):
    """
    Class representing datatypes in the layout hierarchy
    """

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        # Get main layout properties
        layout = plotly_schema['layout']['layoutAttributes']

        # Get list of additional layout properties for each trace
        trace_layouts = [
            plotly_schema['traces'][trace].get('layoutAttributes', {})
            for trace in plotly_schema['traces'] if trace != 'barpolar']

        extra_polar_nodes = (plotly_schema['traces']['barpolar']
                             .get('layoutAttributes', {}))
        layout['polar'].update(extra_polar_nodes)

        # Chain together into layout_data
        self.layout_data = ChainMap(layout, *trace_layouts)

        # Call superclass constructor
        super().__init__(plotly_schema, node_path, parent)

    @property
    def name_base_datatype(self):
        if len(self.node_path) == 0:
            return 'BaseLayoutType'
        else:
            return 'BaseLayoutHierarchyType'

    @property
    def root_name(self):
        return 'layout'

    @property
    def plotly_name(self) -> str:
        if len(self.node_path) == 0:
            return self.root_name
        else:
            return self.node_path[-1]

    # Description
    # -----------
    @property
    def description(self) -> str:
        desc = self.node_data.get('description', '')
        if isinstance(desc, list):
            desc = ''.join(desc)
        return format_description(desc)

    # Raw data
    # --------
    @property
    def node_data(self) -> dict:
        node_data = self.layout_data
        for prop_name in self.node_path:
            node_data = node_data[prop_name]

        return node_data


class FrameNode(PlotlyNode):
    """
    Class representing datatypes in the frames hierarchy
    """

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        super().__init__(plotly_schema, node_path, parent)

    @property
    def name_base_datatype(self):
        return 'BaseFrameHierarchyType'

    @property
    def root_name(self):
        return ''

    @property
    def plotly_name(self) -> str:
        if len(self.node_path) < 2:
            return self.root_name
        elif len(self.node_path) == 2:
            return 'frame'  # override 'frames_entry'
        else:
            return self.node_path[-1]

    def tidy_path_part(self, p):
        return 'frame' if p == 'frames_entry' else p

    # Description
    # -----------
    @property
    def description(self) -> str:
        desc = self.node_data.get('description', '')
        if isinstance(desc, list):
            desc = ''.join(desc)
        return format_description(desc)

    # Raw data
    # --------
    @property
    def node_data(self) -> dict:
        node_data = self.plotly_schema['frames']
        for prop_name in self.node_path:
            node_data = node_data[prop_name]

        return node_data


class ElementDefaultsNode(PlotlyNode):

    def __init__(self, array_node, plotly_schema):
        """
        Create node that represents element defaults properties
        (e.g. layout.annotationdefaults).  Construct as a wrapper around the
        corresponding array property node (e.g. layout.annotations)

        Parameters
        ----------
        array_node: PlotlyNode
        """
        super().__init__(plotly_schema,
                         node_path=array_node.node_path,
                         parent=array_node.parent)

        assert array_node.is_array
        self.array_node = array_node
        self.element_node = array_node.children[0].children[0]

    @property
    def node_data(self):
        return {}

    @property
    def description(self):
        array_property_path = (self.parent_path_str +
                               '.' + self.array_node.name_property)

        if isinstance(self.array_node, TraceNode):
            data_path = 'data.'
        else:
            data_path = ''

        defaults_property_path = ('layout.template.' +
                                  data_path +
                                  self.parent_path_str +
                                  '.' + self.plotly_name)
        return f"""\
When used in a template
(as {defaults_property_path}),
sets the default property values to use for elements
of {array_property_path}"""

    @property
    def name_base_datatype(self):
        return self.element_node.name_base_datatype

    @property
    def root_name(self):
        return self.array_node.root_name

    @property
    def plotly_name(self):
        return self.element_node.plotly_name + 'defaults'

    @property
    def name_datatype_class(self):
        return self.element_node.name_datatype_class
