import os.path as opath
import textwrap
from io import StringIO

from codegen.utils import CAVEAT, write_source_py


deprecated_mapbox_traces = [
    "scattermapbox",
    "choroplethmapbox",
    "densitymapbox",
]


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
    if plotly_type == "data_array":
        pytype = "numpy.ndarray"
    elif plotly_type == "info_array":
        pytype = "list"
    elif plotly_type == "colorlist":
        pytype = "list"
    elif plotly_type in ("string", "color", "colorscale", "subplotid"):
        pytype = "str"
    elif plotly_type in ("enumerated", "flaglist", "any"):
        pytype = "Any"
    elif plotly_type in ("number", "angle"):
        pytype = "int|float"
    elif plotly_type == "integer":
        pytype = "int"
    elif plotly_type == "boolean":
        pytype = "bool"
    else:
        raise ValueError("Unknown plotly type: %s" % plotly_type)

    if array_ok:
        return f"{pytype}|numpy.ndarray"
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
    assert node.is_compound

    # Handle template traces
    #
    # We want template trace/layout classes like
    # plotly.graph_objs.layout.template.data.Scatter to map to the
    # corresponding trace/layout class (e.g. plotly.graph_objs.Scatter).
    # So rather than generate a class definition, we just import the
    # corresponding trace/layout class
    if node.parent_path_str == "layout.template.data":
        return f"from plotly.graph_objs import {node.name_datatype_class}"
    elif node.path_str == "layout.template.layout":
        return "from plotly.graph_objs import Layout"

    # Extract node properties
    datatype_class = node.name_datatype_class
    literal_nodes = [n for n in node.child_literals if n.plotly_name in ["type"]]

    # Initialze source code buffer
    buffer = StringIO()
    buffer.write(CAVEAT)

    # Imports
    buffer.write(
        f"from plotly.basedatatypes "
        f"import {node.name_base_datatype} as _{node.name_base_datatype}\n"
    )
    buffer.write("import copy as _copy\n")

    if (
        node.name_property in deprecated_mapbox_traces
        or node.name_property == "template"
    ):
        buffer.write("import warnings\n")

    # Write class definition
    buffer.write(
        f"""

class {datatype_class}(_{node.name_base_datatype}):\n"""
    )

    # Layout subplot properties
    if datatype_class == "Layout":
        subplot_nodes = [
            node
            for node in node.child_compound_datatypes
            if node.node_data.get("_isSubplotObj", False)
        ]
        subplot_names = [n.name_property for n in subplot_nodes]
        buffer.write(
            f"""
    _subplotid_prop_names = {repr(subplot_names)}

    import re
    _subplotid_prop_re = re.compile(
        '^(' + '|'.join(_subplotid_prop_names) + r')(\\d+)$')
"""
        )

        subplot_dict_str = (
            "{"
            + ", ".join(
                f'"{subname}": ValidatorCache.get_validator("layout", "{subname}")'
                for subname in subplot_names
            )
            + "}"
        )

        buffer.write(
            f"""
    @property
    def _subplotid_validators(self):
        \"\"\"
        dict of validator classes for each subplot type

        Returns
        -------
        dict
        \"\"\"
        from plotly.validator_cache import ValidatorCache

        return {subplot_dict_str}

    def _subplot_re_match(self, prop):
        return self._subplotid_prop_re.match(prop)
"""
        )

    child_datatype_nodes = node.child_datatypes
    subtype_nodes = child_datatype_nodes
    valid_props_list = sorted(
        [node.name_property for node in subtype_nodes + literal_nodes]
    )
    # class properties
    buffer.write(
        f"""
    _parent_path_str = "{node.parent_path_str}"
    _path_str = "{node.path_str}"
    _valid_props = {{"{'", "'.join(valid_props_list)}"}}
"""
    )

    # Property definitions
    for subtype_node in subtype_nodes:
        if subtype_node.is_array_element:
            prop_type = (
                f"tuple[plotly.graph_objs{node.dotpath_str}."
                + f"{subtype_node.name_datatype_class}]"
            )

        elif subtype_node.is_compound:
            prop_type = (
                f"plotly.graph_objs{node.dotpath_str}."
                + f"{subtype_node.name_datatype_class}"
            )

            # remap template traces to regular traces
            prop_type = prop_type.replace("layout.template.data", "")
        elif subtype_node.is_mapped:
            prop_type = ""
        else:
            prop_type = get_typing_type(subtype_node.datatype, subtype_node.is_array_ok)

        # Get property description
        raw_description = subtype_node.description
        property_description = "\n".join(
            textwrap.wrap(
                raw_description,
                initial_indent=" " * 8,
                subsequent_indent=" " * 8,
                width=79 - 8,
            )
        )

        # Get validator description
        validator = subtype_node.get_validator_instance()
        if validator:
            validator_description = reindent_validator_description(validator, 4)

            # Combine to form property docstring
            if property_description.strip():
                property_docstring = f"""{property_description}

        {validator_description}"""
            else:
                property_docstring = f"        {validator_description}"
        else:
            property_docstring = property_description

        # Write get property
        buffer.write(
            f'''\

    @property
    def {subtype_node.name_property}(self):
        """
{property_docstring}

        Returns
        -------
        {prop_type}
        """
        return self["{subtype_node.name_property}"]'''
        )

        # Write set property
        buffer.write(
            f"""

    @{subtype_node.name_property}.setter
    def {subtype_node.name_property}(self, val):
        self["{subtype_node.name_property}"] = val\n"""
        )

        # Literals
    for literal_node in literal_nodes:
        buffer.write(
            f"""\

    @property
    def {literal_node.name_property}(self):
        return self._props["{literal_node.name_property}"]\n"""
        )

    # Private properties descriptions
    buffer.write(
        """
    @property
    def _prop_descriptions(self):
        return \"\"\"\\"""
    )

    buffer.write(node.get_constructor_params_docstring(indent=8))

    buffer.write(
        """
        \"\"\""""
    )

    mapped_nodes = [n for n in subtype_nodes if n.is_mapped]
    mapped_properties = {n.plotly_name: n.relative_path for n in mapped_nodes}
    if mapped_properties:
        buffer.write(
            f"""

    _mapped_properties = {repr(mapped_properties)}"""
        )

    # Constructor
    buffer.write(
        """
    def __init__(self"""
    )

    add_constructor_params(buffer, subtype_nodes, prepend_extras=["arg"])

    # Constructor Docstring
    header = f"Construct a new {datatype_class} object"
    class_name = (
        f"plotly.graph_objs{node.parent_dotpath_str}.{node.name_datatype_class}"
    )

    extras = [
        (
            "arg",
            "dict of properties compatible with this constructor "
            f"or an instance of :class:`{class_name}`",
        )
    ]

    add_docstring(
        buffer,
        node,
        header=header,
        prepend_extras=extras,
        return_type=node.name_datatype_class,
    )

    buffer.write(
        f"""
        super().__init__("{node.name_property}")
        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return
"""
    )

    if datatype_class == "Layout":
        # Override _valid_props for instance so that instance can mutate set
        # to support subplot properties (e.g. xaxis2)
        buffer.write(
            f"""
        self._valid_props = {{"{'", "'.join(valid_props_list)}"}}
"""
        )

    # Validate arg
    buffer.write(
        f"""
        if arg is None:
            arg = {{}}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(\"\"\"\\
The first argument to the {class_name}
constructor must be a dict or
an instance of :class:`{class_name}`\"\"\")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)
        """
    )

    buffer.write("\n\n")
    for subtype_node in subtype_nodes:
        name_prop = subtype_node.name_property
        if datatype_class == "Template" and name_prop == "data":
            buffer.write(
                f"""
        # Template.data contains a 'scattermapbox' key, which causes a
        # go.Scattermapbox trace object to be created during validation.
        # In order to prevent false deprecation warnings from surfacing,
        # we suppress deprecation warnings for this line only.
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            self._set_property("{name_prop}", arg, {name_prop})"""
            )
        else:
            buffer.write(
                f"""
        self._set_property("{name_prop}", arg, {name_prop})"""
            )

    # Literals
    if literal_nodes:
        buffer.write("\n\n")
        for literal_node in literal_nodes:
            lit_name = literal_node.name_property
            lit_val = repr(literal_node.node_data)
            buffer.write(
                f"""
        self._props["{lit_name}"] = {lit_val}
        arg.pop("{lit_name}", None)"""
            )

    buffer.write(
        """
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
"""
    )

    if node.name_property in deprecated_mapbox_traces:
        buffer.write(
            f"""
        warnings.warn(
            "*{node.name_property}* is deprecated!"
            + " Use *{node.name_property.replace("mapbox", "map")}* instead."
            + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
            stacklevel=2,
            category=DeprecationWarning,
        )
"""
        )

    # Return source string
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
    return ("\n" + " " * extra_indent).join(validator.description().strip().split("\n"))


def add_constructor_params(
    buffer, subtype_nodes, prepend_extras=(), append_extras=(), output_type=None
):
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
        buffer.write(
            f""",
            {extra}=None"""
        )

    for i, subtype_node in enumerate(subtype_nodes):
        buffer.write(
            f""",
            {subtype_node.name_property}=None"""
        )

    for extra in append_extras:
        buffer.write(
            f""",
            {extra}=None"""
        )

    buffer.write(
        """,
            **kwargs"""
    )
    buffer.write(
        """
        )"""
    )
    if output_type:
        buffer.write(f'-> "{output_type}"')
    buffer.write(":")


def add_docstring(
    buffer, node, header, prepend_extras=(), append_extras=(), return_type=None
):
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
    return_type :
        The docstring return type
    Returns
    -------

    """
    # Validate inputs
    assert node.is_compound

    # Build wrapped description
    node_description = node.description
    if node_description:
        description_lines = textwrap.wrap(
            node_description,
            width=79 - 8,
            initial_indent=" " * 8,
            subsequent_indent=" " * 8,
        )

        node_description = "\n".join(description_lines) + "\n\n"

    # Write header and description
    buffer.write(
        f"""
        \"\"\"
        {header}

{node_description}        Parameters
        ----------"""
    )

    # Write parameter descriptions

    # Write any prepend extras
    for p, v in prepend_extras:
        v_wrapped = "\n".join(
            textwrap.wrap(
                v, width=79 - 12, initial_indent=" " * 12, subsequent_indent=" " * 12
            )
        )
        buffer.write(
            f"""
        {p}
{v_wrapped}"""
        )

    # Write core docstring
    buffer.write(node.get_constructor_params_docstring(indent=8))

    # Write any append extras
    for p, v in append_extras:
        if "\n" in v:
            # If v contains newlines assume it's already wrapped
            v_wrapped = v
        else:
            v_wrapped = "\n".join(
                textwrap.wrap(
                    v,
                    width=79 - 12,
                    initial_indent=" " * 12,
                    subsequent_indent=" " * 12,
                )
            )
        buffer.write(
            f"""
        {p}
{v_wrapped}"""
        )

    # Write return block and close docstring
    buffer.write(
        f"""

        Returns
        -------
        {return_type}
        \"\"\""""
    )


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

    # Build file path
    # filepath = opath.join(outdir, "graph_objs", *node.parent_path_parts, "__init__.py")
    filepath = opath.join(
        outdir, "graph_objs", *node.parent_path_parts, "_" + node.name_undercase + ".py"
    )

    # Generate source code
    datatype_source = build_datatype_py(node)

    # Write file
    write_source_py(datatype_source, filepath, leading_newlines=2)
