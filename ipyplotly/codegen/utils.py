import importlib
import inspect
import textwrap
from typing import List, Dict

from io import StringIO
from yapf.yapflib.yapf_api import FormatCode

from ipyplotly.basevalidators import BaseValidator, CompoundValidator, CompoundArrayValidator


def format_source(validator_source):
    formatted_source, _ = FormatCode(validator_source,
                                     style_config={'based_on_style': 'google',
                                                   'DEDENT_CLOSING_BRACKETS': True,
                                                   'COLUMN_LIMIT': 119})
    return formatted_source


custom_validator_datatypes = {
    'layout.image.source': 'ipyplotly.basevalidators.ImageUriValidator',
    'frame.data': 'ipyplotly.validators.DataValidator',
    'frame.layout': 'ipyplotly.validators.LayoutValidator'
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
        if isinstance(self.node_data, dict):
            self._children = [self.__class__(self.plotly_schema,
                                             node_path=self.node_path + (c,),
                                             parent=self)
                              for c in self.node_data if c and c[0] != '_']
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
        if self.dir_str in custom_validator_datatypes:
            validator_base = f"{custom_validator_datatypes[self.dir_str]}"
        else:
            validator_base = f"ipyplotly.basevalidators.{self.datatype_pascal_case}Validator"

        return validator_base

    def get_constructor_params_docstring(self, indent=12, extra_nodes=[]):
        assert self.is_compound

        buffer = StringIO()

        subtype_nodes = self.child_datatypes + extra_nodes
        for subtype_node in subtype_nodes:
            raw_description = subtype_node.description
            subtype_description = '\n'.join(textwrap.wrap(raw_description,
                                                          subsequent_indent=' ' * (indent + 4),
                                                          width=80 - (indent + 4)))

            buffer.write('\n' + ' ' * indent + subtype_node.name_property)
            buffer.write('\n' + ' ' * (indent + 4) + subtype_description)

        return buffer.getvalue()

    @property
    def validator_instance(self) -> BaseValidator:

        module_parts = self.name_base_validator.split('.')
        module_path = '.'.join(module_parts[:-1])
        cls_name = module_parts[-1]

        validators_module = importlib.import_module(module_path)

        validator_class_list = [cls
                                for _, cls in inspect.getmembers(validators_module, inspect.isclass)
                                if cls.__name__ == cls_name]
        if not validator_class_list:
            raise ValueError(f"Unknown base validator '{self.name_base_validator}'")

        validator_class = validator_class_list[0]

        args = dict(plotly_name=self.name_property, parent_name=self.parent_dir_str)

        if validator_class == CompoundValidator:
            data_class_str = f"<class ipyplotly.datatypes.{self.parent_dir_str}.{self.name_class}>"
            extra_args = {'data_class': data_class_str, 'data_docs': self.get_constructor_params_docstring()}
        elif validator_class == CompoundArrayValidator:
            element_class_str = f"<class ipyplotly.datatypes.{self.parent_dir_str}.{self.name_class}>"
            extra_args = {'element_class': element_class_str, 'element_docs': self.get_constructor_params_docstring()}
        else:
            extra_args = {n.name_undercase: n.node_data for n in self.simple_attrs}

            # Add extra properties
            if self.datatype == 'color':
                # Check for colorscale sibling
                colorscale_node_list = [node for node in self.parent.child_datatypes
                                        if node.datatype == 'colorscale']
                if colorscale_node_list:
                    colorscale_path = colorscale_node_list[0].dir_str
                    extra_args['colorscale_path'] = repr(colorscale_path)

        return validator_class(**args, **extra_args)

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
        return isinstance(self.node_data, dict) and not self.is_simple and self.plotly_name != 'impliedEdits'

    @property
    def is_literal(self) -> bool:
        return isinstance(self.node_data, str)

    @property
    def is_simple(self) -> bool:
        return isinstance(self.node_data, dict) and 'valType' in self.node_data

    @property
    def is_array(self) -> bool:
        return isinstance(self.node_data, dict) and \
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
    def dir_path(self) -> List[str]:
        res = [self.base_name] if self.base_name else []
        for i, p in enumerate(self.node_path):
            if p == 'items' or \
                    (i < len(self.node_path) - 1 and self.node_path[i+1] == 'items'):
                # e.g. [parcoords, dimensions, items, dimension] -> [parcoords, dimension]
                pass
            else:
                res.append(self.tidy_dir_path(p))
        return res

    # Node path strings
    # -----------------
    @property
    def dir_str(self) -> str:
        return '.'.join(self.dir_path)

    @property
    def parent_dir_str(self) -> str:
        return '.'.join(self.dir_path[:-1])

    @property
    def pkg_str(self) -> str:
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
        # if self.is_array:
        #     items_child = [c for c in self.children if c.plotly_name == 'items'][0]
        #     return items_child.children
        # else:
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

            if not node.is_array:
                nodes.append(node)

            nodes_to_process.extend(node.child_compound_datatypes)

        return nodes

    @staticmethod
    def get_all_trace_layout_nodes(plotly_schema) -> Dict[str, 'LayoutNode']:
        trace_names = plotly_schema['traces'].keys()

        datatype_nodes = {}
        nodes_to_process = [TraceLayoutNode(plotly_schema, trace_name)
                            for trace_name in trace_names]

        while nodes_to_process:
            parent_node = nodes_to_process.pop()
            for node in parent_node.child_simple_datatypes:
                datatype_nodes[node.dir_str] = node

        return datatype_nodes


class TraceNode(PlotlyNode):

    # Constructor
    # -----------
    def __init__(self, plotly_schema, node_path=(), parent=None):
        super().__init__(plotly_schema, node_path, parent)

    @property
    def base_datatype_class(self):
        if len(self.node_path) == 0:
            return 'BaseTraceType'
        else:
            return 'BaseTraceHierarchyType'

    @property
    def base_name(self):
        return 'trace'

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
        super().__init__(plotly_schema, node_path, parent)

    @property
    def base_datatype_class(self):
        if len(self.node_path) == 0:
            return 'BaseLayoutType'
        else:
            return 'BaseLayoutHierarchyType'

    @property
    def base_name(self):
        return ''

    @property
    def plotly_name(self) -> str:
        if len(self.node_path) == 0:
            return self.base_name
        elif len(self.node_path) == 1:
            return 'layout'  # override 'layoutAttributes'
        else:
            return self.node_path[-1]

    def tidy_dir_path(self, p):
        return 'layout' if p == 'layoutAttributes' else p

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
        node_data = self.plotly_schema['layout']
        for prop_name in self.node_path:
            node_data = node_data[prop_name]

        return node_data


class TraceLayoutNode(LayoutNode):

    # Constructor
    # -----------
    def __init__(self, plotly_schema, trace_name=None, node_path=(), parent=None):

        # Handle trace name
        assert parent is not None or trace_name is not None
        if parent is not None:
            trace_name = parent.trace_name

        self.trace_name = trace_name
        super().__init__(plotly_schema, node_path, parent)

    @property
    def base_name(self):
        return 'layout'

    @property
    def plotly_name(self) -> str:
        if len(self.node_path) == 0:
            return self.base_name
        else:
            return self.node_path[-1]

    # Raw data
    # --------
    @property
    def node_data(self) -> dict:
        try:
            node_data = (self.plotly_schema['traces']
                         [self.trace_name]['layoutAttributes'])

            for prop_name in self.node_path:
                node_data = node_data[prop_name]

        except KeyError:
            node_data = []

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
