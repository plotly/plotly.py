import os
import os.path as opath
import textwrap
from collections import ChainMap
from importlib import import_module
from io import StringIO
from typing import List, Tuple

from yapf.yapflib.yapf_api import FormatCode

dict_like = (dict, ChainMap)

# Import note
# -----------
# This file may not import anything from the plotly package


def format_source(validator_source):
    formatted_source, _ = FormatCode(validator_source,
                                     style_config={'based_on_style': 'google',
                                                   'DEDENT_CLOSING_BRACKETS': True,
                                                   'COLUMN_LIMIT': 79})
    return formatted_source


def build_from_imports_py(import_pairs):
    buffer = StringIO()
    for from_pkg, class_name in import_pairs:
        if isinstance(class_name, str):
            class_name_str = class_name
        else:
            class_name_str = '(' + ', '.join(class_name) + ')'

        buffer.write(f"""\
from {from_pkg} import {class_name_str}\n""")

    return buffer.getvalue()


def write_source_py(py_source, filepath):
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


CUSTOM_VALIDATOR_DATATYPES = {
    'layout.image.source': '_plotly_utils.basevalidators.ImageUriValidator',
    'frame.data': 'plotly.validators.DataValidator',
    'frame.layout': 'plotly.validators.LayoutValidator'
}

# Use to customize generated class names. If not included, names are
# converted to PascalCase and underscores are removed.
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

class PlotlyNode:

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        self.plotly_schema = plotly_schema
        if isinstance(node_path, str):
            node_path = (node_path,)
        self.node_path = node_path

        # Compute children
        if isinstance(self.node_data, dict_like):
            self._children = [self.__class__(self.plotly_schema,
                                             node_path=self.node_path + (c,),
                                             parent=self)
                              for c in self.node_data if c and c[0] != '_']

            # Sort by plotly name
            self._children = sorted(self._children,
                                    key=lambda node: node.plotly_name)
        else:
            self._children = []

        # Parent
        self._parent = parent

    def __repr__(self):
        return self.dir_str

    # Abstract methods
    # ----------------
    @property
    def node_data(self) -> dict:
        raise NotImplementedError()

    @property
    def description(self) -> str:
        raise NotImplementedError()

    @property
    def base_datatype_class(self):
        raise NotImplementedError

    # Names
    # -----
    @property
    def base_name(self):
        raise NotImplementedError()

    @property
    def plotly_name(self) -> str:
        if len(self.node_path) == 0:
            return self.base_name
        else:
            return self.node_path[-1]

    @property
    def name_pascal_case(self) -> str:
        if self.plotly_name in OBJECT_NAME_TO_CLASS_NAME:
            return OBJECT_NAME_TO_CLASS_NAME[self.plotly_name]
        else:
            return self.plotly_name.title().replace('_', '')

    @property
    def name_undercase(self) -> str:
        if not self.plotly_name:
            # Empty plotly_name
            return self.plotly_name

        # Lowercase leading char
        # ----------------------
        name1 = self.plotly_name[0].lower() + self.plotly_name[1:]

        # Replace capital chars by underscore-lower
        # -----------------------------------------
        name2 = ''.join([('' if not c.isupper() else '_') + c.lower() for c in name1])

        return name2

    @property
    def name_property(self) -> str:
        return self.plotly_name + ('s' if self.is_array_element else '')

    @property
    def name_validator(self) -> str:
        return self.name_pascal_case + ('s' if self.is_array_element else '') + 'Validator'

    @property
    def name_base_validator(self) -> str:
        if self.dir_str in CUSTOM_VALIDATOR_DATATYPES:
            validator_base = f"{CUSTOM_VALIDATOR_DATATYPES[self.dir_str]}"
        else:
            validator_base = (f"_plotly_utils.basevalidators."
                              f"{self.datatype_pascal_case}Validator")

        return validator_base

    def get_constructor_params_docstring(self, indent=12):
        assert self.is_compound

        buffer = StringIO()

        subtype_nodes = self.child_datatypes
        for subtype_node in subtype_nodes:
            raw_description = subtype_node.description
            if raw_description:
                subtype_description = raw_description
            elif subtype_node.is_compound:
                class_name = (f'plotly.graph_objs'
                              f'{subtype_node.parent_pkg_str}.'
                              f'{subtype_node.name_class}')

                subtype_description = (f'{class_name} instance or '
                                      'dict with compatible properties')
            else:
                subtype_description = ''

            subtype_description = '\n'.join(
                textwrap.wrap(subtype_description,
                              subsequent_indent=' ' * (indent + 4),
                              width=79 - (indent + 4)))

            buffer.write('\n' + ' ' * indent + subtype_node.name_property)
            buffer.write('\n' + ' ' * (indent + 4) + subtype_description)

        return buffer.getvalue()

    def get_validator_params(self):

        params = {'plotly_name': repr(self.name_property),
                  'parent_name': repr(self.parent_dir_str)}

        if self.is_array_element:
            params['element_class'] = repr(self.name_class)
            params['element_docs'] = (
                    '\"\"\"' +
                    self.get_constructor_params_docstring() +
                    '\"\"\"')

        elif self.is_compound:
            params['data_class'] = repr(self.name_class)
            params['data_docs'] = (
                    '\"\"\"' +
                    self.get_constructor_params_docstring() +
                    '\"\"\"')
        else:
            assert self.is_simple

            # Exclude general properties
            excluded_props = ['valType', 'description', 'role', 'dflt']
            if self.datatype == 'subplotid':
                # Default is required for subplotid validator
                excluded_props.remove('dflt')

            attr_nodes = [n for n in self.simple_attrs
                          if n.plotly_name not in excluded_props]

            for node in attr_nodes:
                params[node.name_undercase] = repr(node.node_data)

            # Add extra properties
            if self.datatype == 'color' and self.parent:
                # Check for colorscale sibling
                colorscale_node_list = [node for node in
                                        self.parent.child_datatypes
                                        if node.datatype == 'colorscale']
                if colorscale_node_list:
                    colorscale_path = colorscale_node_list[0].dir_str
                    params['colorscale_path'] = repr(colorscale_path)

        return params

    def get_validator_instance(self):
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

    @property
    def name_class(self) -> str:
        return self.name_pascal_case

    # Datatypes
    # ---------
    @property
    def datatype(self) -> str:
        if self.is_array_element:
            return 'compound_array'
        elif self.is_compound:
            return 'compound'
        elif self.is_simple:
            return self.node_data.get('valType')
        else:
            return 'literal'

    @property
    def datatype_pascal_case(self) -> str:
        return self.datatype.title().replace('_', '')

    @property
    def is_compound(self) -> bool:
        return isinstance(self.node_data, dict_like) and not self.is_simple and self.plotly_name != 'impliedEdits'

    @property
    def is_literal(self) -> bool:
        return isinstance(self.node_data, str)

    @property
    def is_simple(self) -> bool:
        return isinstance(self.node_data, dict_like) and 'valType' in self.node_data

    @property
    def is_array(self) -> bool:
        return isinstance(self.node_data, dict_like) and \
               self.node_data.get('role', '') == 'object' and \
               'items' in self.node_data

    @property
    def is_array_element(self):
        if self.parent and self.parent.parent:
            return self.parent.parent.is_array
        else:
            return False

    @property
    def is_datatype(self) -> bool:
        return self.is_simple or self.is_compound

    # Node path
    # ---------
    def tidy_dir_path(self, p):
        return p

    @property
    def dir_path(self) -> Tuple[str]:
        res = [self.base_name] if self.base_name else []
        for i, p in enumerate(self.node_path):
            if p == 'items' or \
                    (i < len(self.node_path) - 1 and self.node_path[i+1] == 'items'):
                # e.g. [parcoords, dimensions, items, dimension] -> [parcoords, dimension]
                pass
            else:
                res.append(self.tidy_dir_path(p))
        return tuple(res)

    # Node path strings
    # -----------------
    @property
    def dir_str(self) -> str:
        return '.'.join(self.dir_path)

    @property
    def parent_dir_path(self) -> Tuple[str]:
        return self.dir_path[:-1]

    @property
    def parent_dir_str(self) -> str:
        return '.'.join(self.dir_path[:-1])

    @property
    def parent_pkg_str(self) -> str:
        """Empty or has leading dot"""
        path_str = ''
        for p in self.dir_path[:-1]:
            path_str += '.' + p
        return path_str

    @property
    def pkg_str(self) -> str:
        """Empty or has leading dot"""
        path_str = ''
        for p in self.dir_path:
            path_str += '.' + p
        return path_str

    # Children
    # --------
    @property
    def children(self) -> List['PlotlyNode']:
        return self._children

    @property
    def simple_attrs(self) -> List['PlotlyNode']:
        if not self.is_simple:
            raise ValueError(f"Cannot get simple attributes of the simple object '{self.dir_str}'")

        return [n for n in self.children if n.plotly_name not in ['valType', 'description', 'role']]

    @property
    def parent(self) -> 'PlotlyNode':
        return self._parent

    @property
    def child_datatypes(self) -> List['PlotlyNode']:
        """
        Returns
        -------
        children: list of TraceNode
        """
        nodes = []
        for n in self.children:
            if n.is_array:
                nodes.append(n.children[0].children[0])
            elif n.is_datatype:
                nodes.append(n)

        return nodes

    @property
    def child_compound_datatypes(self) -> List['PlotlyNode']:
        return [n for n in self.child_datatypes if n.is_compound]

    @property
    def child_simple_datatypes(self) -> List['PlotlyNode']:
        return [n for n in self.child_datatypes if n.is_simple]

    @property
    def child_literals(self) -> List['PlotlyNode']:
        return [n for n in self.children if n.is_literal]

    # Static helpers
    # --------------
    @staticmethod
    def get_all_compound_datatype_nodes(plotly_schema, node_class) -> List['PlotlyNode']:
        nodes = []
        nodes_to_process = [node_class(plotly_schema)]

        while nodes_to_process:
            node = nodes_to_process.pop()

            if node.plotly_name and not node.is_array:
                nodes.append(node)

            nodes_to_process.extend(node.child_compound_datatypes)

        return nodes

    @staticmethod
    def get_all_datatype_nodes(plotly_schema, node_class) -> List['PlotlyNode']:
        nodes = []
        nodes_to_process = [node_class(plotly_schema)]

        while nodes_to_process:
            node = nodes_to_process.pop()

            if node.plotly_name and not node.is_array:
                nodes.append(node)

            nodes_to_process.extend(node.child_datatypes)

        return nodes


class TraceNode(PlotlyNode):

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        super().__init__(plotly_schema, node_path, parent)

    @property
    def base_datatype_class(self):
        if len(self.node_path) <= 1:
            return 'BaseTraceType'
        else:
            return 'BaseTraceHierarchyType'

    @property
    def base_name(self):
        return ''

    # Raw data
    # --------
    @property
    def node_data(self) -> dict:
        if not self.node_path:
            node_data = self.plotly_schema['traces']
        else:
            node_data = self.plotly_schema['traces'][self.node_path[0]]['attributes']
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
            desc = self.plotly_schema['traces'][self.node_path[0]]['meta'].get('description', '')
        else:
            desc = self.node_data.get('description', '')

        if isinstance(desc, list):
            desc = ''.join(desc)

        return desc


class LayoutNode(PlotlyNode):

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        # Get main layout properties
        layout = plotly_schema['layout']['layoutAttributes']

        # Get list of additional layout properties for each trace
        trace_layouts = [
            plotly_schema['traces'][trace].get('layoutAttributes', {})
            for trace in plotly_schema['traces']]

        # Chain together into layout_data
        self.layout_data = ChainMap(layout, *trace_layouts)

        # Call superclass constructor
        super().__init__(plotly_schema, node_path, parent)

    @property
    def base_datatype_class(self):
        if len(self.node_path) == 0:
            return 'BaseLayoutType'
        else:
            return 'BaseLayoutHierarchyType'

    @property
    def base_name(self):
        return 'layout'

    @property
    def plotly_name(self) -> str:
        if len(self.node_path) == 0:
            return self.base_name
        # elif len(self.node_path) == 1:
        #     return 'layout'  # override 'layoutAttributes'
        else:
            return self.node_path[-1]

    # def tidy_dir_path(self, p):
    #     return 'layout' if p == 'layoutAttributes' else p

    # Description
    # -----------
    @property
    def description(self) -> str:
        desc = self.node_data.get('description', '')
        if isinstance(desc, list):
            desc = ''.join(desc)
        return desc

    # Raw data
    # --------
    @property
    def node_data(self) -> dict:
        node_data = self.layout_data
        for prop_name in self.node_path:
            node_data = node_data[prop_name]

        return node_data


class FrameNode(PlotlyNode):

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        super().__init__(plotly_schema, node_path, parent)

    @property
    def base_datatype_class(self):
        return 'BaseFrameHierarchyType'

    @property
    def base_name(self):
        return ''

    @property
    def plotly_name(self) -> str:
        if len(self.node_path) < 2:
            return self.base_name
        elif len(self.node_path) == 2:
            return 'frame'  # override 'frames_entry'
        else:
            return self.node_path[-1]

    def tidy_dir_path(self, p):
        return 'frame' if p == 'frames_entry' else p

    # Description
    # -----------
    @property
    def description(self) -> str:
        desc = self.node_data.get('description', '')
        if isinstance(desc, list):
            desc = ''.join(desc)
        return desc

    # Raw data
    # --------
    @property
    def node_data(self) -> dict:
        node_data = self.plotly_schema['frames']
        for prop_name in self.node_path:
            node_data = node_data[prop_name]

        return node_data
