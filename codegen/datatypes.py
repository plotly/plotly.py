import os.path as opath
import textwrap
from io import StringIO

from codegen.utils import (PlotlyNode,
                           format_and_write_source_py)


def get_typing_type(plotly_type, array_ok=False):
    """
    Get Python type corresponding to a valType string from the plotly schema

    Parameters
    ----------
    plotly_type : str
        a plotly datatype string
    array_ok : bool
        Whether lists/arrays are permitted
    Returns
    -------
    str
        Python type string
    """
    if plotly_type == 'data_array':
        pytype = 'numpy.ndarray'
    elif plotly_type == 'info_array':
        pytype = 'list'
    elif plotly_type == 'colorlist':
        pytype = 'list'
    elif plotly_type in ('string', 'color', 'colorscale', 'subplotid'):
        pytype = 'str'
    elif plotly_type in ('enumerated', 'flaglist', 'any'):
        pytype = 'Any'
    elif plotly_type in ('number', 'angle'):
        pytype = 'int|float'
    elif plotly_type == 'integer':
        pytype = 'int'
    elif plotly_type == 'boolean':
        pytype = 'bool'
    else:
        raise ValueError('Unknown plotly type: %s' % plotly_type)

    if array_ok:
        return f'{pytype}|numpy.ndarray'
    else:
        return pytype


def build_datatype_py(node):
    """
    Build datatype (graph_objs) class source code string for a datatype
    PlotlyNode

    Parameters
    ----------
    node : PlotlyNode
        The datatype node (node.is_datatype must evaluate to true) for which
        to build the datatype class
    Returns
    -------
    str
        String containing source code for the datatype class definition
    """

    # Validate inputs
    # ---------------
    assert node.is_compound

    # Handle template traces
    # ----------------------
    # We want template trace/layout classes like
    # plotly.graph_objs.layout.template.data.Scatter to map to the
    # corresponding trace/layout class (e.g. plotly.graph_objs.Scatter).
    # So rather than generate a class definition, we just import the
    # corresponding trace/layout class
    if node.parent_path_str == 'layout.template.data':
        return f"from plotly.graph_objs import {node.name_datatype_class}"
    elif node.path_str == 'layout.template.layout':
        return "from plotly.graph_objs import Layout"

    # Extract node properties
    # -----------------------
    undercase = node.name_undercase
    datatype_class = node.name_datatype_class
    literal_nodes = [n for n in node.child_literals if
                     n.plotly_name in ['type']]

    # Initialze source code buffer
    # ----------------------------
    buffer = StringIO()

    # Imports
    # -------
    buffer.write(
        f'from plotly.basedatatypes import {node.name_base_datatype}\n')
    buffer.write(
        f'import copy\n')


    # Write class definition
    # ----------------------
    buffer.write(f"""

class {datatype_class}({node.name_base_datatype}):\n""")

    # ### Property definitions ###
    child_datatype_nodes = node.child_datatypes

    subtype_nodes = child_datatype_nodes
    for subtype_node in subtype_nodes:
        if subtype_node.is_array_element:
            prop_type = (f"tuple[plotly.graph_objs{node.dotpath_str}." +
                         f"{subtype_node.name_datatype_class}]")

        elif subtype_node.is_compound:
            prop_type = (f"plotly.graph_objs{node.dotpath_str}." +
                         f"{subtype_node.name_datatype_class}")
        else:
            prop_type = get_typing_type(
                subtype_node.datatype, subtype_node.is_array_ok)

        # #### Get property description ####
        raw_description = subtype_node.description
        property_description = '\n'.join(
            textwrap.wrap(raw_description,
                          initial_indent=' ' * 8,
                          subsequent_indent=' ' * 8,
                          width=79 - 8))

        # # #### Get validator description ####
        validator = subtype_node.get_validator_instance()
        if validator:
            validator_description = reindent_validator_description(
                validator, 4)

            # #### Combine to form property docstring ####
            if property_description.strip():
                property_docstring = f"""{property_description}
    
        {validator_description}"""
            else:
                property_docstring = f"        {validator_description}"
        else:
            property_docstring = property_description

        # #### Write get property ####
        buffer.write(f"""\

    # {subtype_node.name_property}
    # {'-' * len(subtype_node.name_property)}
    @property
    def {subtype_node.name_property}(self):
        \"\"\"
{property_docstring}

        Returns
        -------
        {prop_type}
        \"\"\"
        return self['{subtype_node.name_property}']""")

        # #### Write set property ####
        buffer.write(f"""

    @{subtype_node.name_property}.setter
    def {subtype_node.name_property}(self, val):
        self['{subtype_node.name_property}'] = val\n""")

        # ### Literals ###
    for literal_node in literal_nodes:
        buffer.write(f"""\

    # {literal_node.name_property}
    # {'-' * len(literal_node.name_property)}
    @property
    def {literal_node.name_property}(self):
        return self._props['{literal_node.name_property}']\n""")

    # ### Private properties descriptions ###
    buffer.write(f"""

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return '{node.parent_path_str}'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return \"\"\"\\""")

    buffer.write(node.get_constructor_params_docstring(indent=8))

    buffer.write(f"""
        \"\"\"""")

    # ### Constructor ###
    buffer.write(f"""
    def __init__(self""")

    add_constructor_params(buffer,
                           subtype_nodes,
                           prepend_extras=['arg'])

    # ### Constructor Docstring ###
    header = f'Construct a new {datatype_class} object'
    class_name = (f'plotly.graph_objs'
                  f'{node.parent_dotpath_str}.'
                  f'{node.name_datatype_class}')

    extras = [(f'arg',
               f'dict of properties compatible with this constructor '
               f'or an instance of {class_name}')]

    add_docstring(buffer, node, header=header, prepend_extras=extras)

    buffer.write(f"""
        super({datatype_class}, self).__init__('{node.name_property}')

        # Validate arg
        # ------------
        if arg is None:
            arg = {{}}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(\"\"\"\\
The first argument to the {class_name} 
constructor must be a dict or 
an instance of {class_name}\"\"\")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        
        # Import validators
        # -----------------
        from plotly.validators{node.parent_dotpath_str} import (
            {undercase} as v_{undercase}) 

        # Initialize validators
        # ---------------------""")
    for subtype_node in subtype_nodes:
        sub_name = subtype_node.name_property
        sub_validator = subtype_node.name_validator_class
        buffer.write(f"""
        self._validators['{sub_name}'] = v_{undercase}.{sub_validator}()""")

    buffer.write(f"""

        # Populate data dict with properties
        # ----------------------------------""")
    for subtype_node in subtype_nodes:
        name_prop = subtype_node.name_property
        if name_prop == 'template':
            # Special handling for layout.template to avoid infinite
            # recursion.  Only initialize layout.template object if non-None
            # value specified
            buffer.write(f"""
        _v = arg.pop('{name_prop}', None)
        _v = {name_prop} if {name_prop} is not None else _v
        if _v is not None:
            self['{name_prop}'] = _v""")
        else:
            buffer.write(f"""
        _v = arg.pop('{name_prop}', None)
        self['{name_prop}'] = {name_prop} \
if {name_prop} is not None else _v""")

    # ### Literals ###
    if literal_nodes:
        buffer.write(f"""

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator""")
        for literal_node in literal_nodes:
            lit_name = literal_node.name_property
            lit_parent = literal_node.parent_path_str
            lit_val = repr(literal_node.node_data)
            buffer.write(f"""
        self._props['{lit_name}'] = {lit_val}
        self._validators['{lit_name}'] =\
LiteralValidator(plotly_name='{lit_name}',\
    parent_name='{lit_parent}', val={lit_val})
        arg.pop('{lit_name}', None)""")

    buffer.write(f"""
    
        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
        
        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
    """)

    # Return source string
    # --------------------
    return buffer.getvalue()


def reindent_validator_description(validator, extra_indent):
    """
    Return validator description with modified indenting. The string that is
    returned has no leading indent, and the subsequent lines are indented by 4
    spaces (the default for validator descriptions) plus `extra_indent` spaces

    Parameters
    ----------
    validator : BaseValidator
        Validator from which to extract the description
    extra_indent : int
        Number of spaces of indent to add to subsequent lines (those after
        the first line). Validators description start with in indent of 4
        spaces

    Returns
    -------
    str
        Validator description string
    """
    # Remove leading indent and add extra spaces to subsequent indent
    return ('\n' + ' ' * extra_indent).join(
        validator.description().strip().split('\n'))


def add_constructor_params(buffer,
                           subtype_nodes,
                           prepend_extras=(),
                           append_extras=()):
    """
    Write datatype constructor params to a buffer

    Parameters
    ----------
    buffer : StringIO
        Buffer to write to
    subtype_nodes : list of PlotlyNode
        List of datatype nodes to be written as constructor params
    prepend_extras : list[str]
        List of extra parameters to include at the beginning of the params
    append_extras : list[str]
        List of extra parameters to include at the end of the params
    Returns
    -------
    None
    """
    for extra in prepend_extras:
        buffer.write(f""",
            {extra}=None""")

    for i, subtype_node in enumerate(subtype_nodes):
        buffer.write(f""",
            {subtype_node.name_property}=None""")

    for extra in append_extras:
        buffer.write(f""",
            {extra}=None""")

    buffer.write(""",
            **kwargs""")
    buffer.write(f"""
        ):""")


def add_docstring(buffer, node, header, prepend_extras=(), append_extras=()):
    """
    Write docstring for a compound datatype node

    Parameters
    ----------
    buffer : StringIO
        Buffer to write to
    node : PlotlyNode
        Compound datatype plotly node for which to write docstring
    header :
        Top-level header for docstring that will preceded the input node's
        own description. Header should be < 71 characters long
    prepend_extras :
        List or tuple of propery name / description pairs that should be
        included at the beginning of the docstring
    append_extras :
        List or tuple of propery name / description pairs that should be
        included at the end of the docstring
    Returns
    -------

    """
    # Validate inputs
    # ---------------
    assert node.is_compound

    # Build wrapped description
    # -------------------------
    node_description = node.description
    if node_description:
        description_lines = textwrap.wrap(
            node_description,
            width=79-8,
            initial_indent=' ' * 8,
            subsequent_indent=' ' * 8)

        node_description = '\n'.join(description_lines) + '\n\n'

    # Write header and description
    # ----------------------------
    buffer.write(f"""
        \"\"\"
        {header}
        
{node_description}        Parameters
        ----------""")

    # Write parameter descriptions
    # ----------------------------
    # Write any prepend extras
    for p, v in prepend_extras:
        v_wrapped = '\n'.join(textwrap.wrap(
            v,
            width=79 - 12,
            initial_indent=' ' * 12,
            subsequent_indent=' ' * 12))
        buffer.write(f"""
        {p}
{v_wrapped}""")

    # Write core docstring
    buffer.write(node.get_constructor_params_docstring(
        indent=8))

    # Write any append extras
    for p, v in append_extras:
        v_wrapped = '\n'.join(textwrap.wrap(
            v,
            width=79-12,
            initial_indent=' ' * 12,
            subsequent_indent=' ' * 12))
        buffer.write(f"""
        {p}
{v_wrapped}""")

    # Write return block and close docstring
    # --------------------------------------
    buffer.write(f"""

        Returns
        -------
        {node.name_datatype_class}
        \"\"\"""")


def write_datatype_py(outdir, node):
    """
    Build datatype (graph_objs) class source code and write to a file

    Parameters
    ----------
    outdir :
        Root outdir in which the graph_objs package should reside
    node :
        The datatype node (node.is_datatype must evaluate to true) for which
        to build the datatype class

    Returns
    -------
    None
    """
    # Generate source code
    # --------------------
    datatype_source = build_datatype_py(node)

    # Write file
    # ----------
    filepath = opath.join(outdir, 'graph_objs',
                          *node.parent_path_parts,
                          '_' + node.name_undercase + '.py')
    format_and_write_source_py(datatype_source, filepath)
