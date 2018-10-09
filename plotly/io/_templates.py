from plotly.validators.layout import TemplateValidator
from _plotly_utils.basevalidators import (
    CompoundValidator, CompoundArrayValidator, is_array)

import textwrap
import copy


# Templates configuration class
# -----------------------------
class TemplatesConfig(object):
    """
    Singleton object containing the current figure templates (aka themes)
    """
    def __init__(self):

        # Initialize properties dict
        self._templates = {}
        self._validator = TemplateValidator()
        self._default = None

    # ### Magic methods ###
    # Make this act as a dict of templates
    def __len__(self):
        return len(self._templates)

    def __contains__(self, item):
        return item in self._templates

    def __iter__(self):
        return iter(self._templates)

    def __getitem__(self, item):
        return self._templates[item]

    def __setitem__(self, key, value):
        self._templates[key] = self._validator.validate_coerce(value)

    def __delitem__(self, key):
        # Remove template
        del self._templates[key]

        # Check if we need to remove it as the default
        if self._default == key:
            self._default = None

    def keys(self):
        return self._templates.keys()

    def items(self):
        return self._templates.items()

    def update(self, d={}, **kwargs):
        """
        Update one or more templates from a dict or from input keyword
        arguments.

        Parameters
        ----------
        d: dict
            Dictionary from template names to new template values.

        kwargs
            Named argument value pairs where the name is a template name
            and the value is a new template value.
        """
        for k, v in dict(d, **kwargs).items():
            self[k] = v

    # ### Properties ###
    @property
    def default(self):
        """
        The name of the default template, or None if no there is no default

        If not None, the default template is automatically applied to all
        figures during figure construction if no explicit template is
        specified.

        The names of available templates may be retrieved with:

        >>> import plotly.io as pio
        >>> list(pio.templates)

        Returns
        -------
        str
        """
        return self._default

    @default.setter
    def default(self, value):
        if value is not None and value not in self._templates:
            raise ValueError("""
Cannot set default template to {value}
because there is no template registered with this name.

    Available templates:
{available}""".format(
                value=repr(value),
                available=self._available_templates_str()))

        self._default = value

    def __repr__(self):
        return """\
Templates configuration
-----------------------
    Default template: {default}
    Available templates:
{available}
""".format(default=repr(self.default),
           available=self._available_templates_str())

    def _available_templates_str(self):
        """
        Return nicely wrapped string representation of all
        available template names
        """
        available = '\n'.join(textwrap.wrap(
            repr(list(self)),
            width=79 - 8,
            initial_indent=' ' * 8,
            subsequent_indent=' ' * 9
        ))
        return available


# Make config a singleton object
# ------------------------------
templates = TemplatesConfig()
del TemplatesConfig


# Template utilities
# ------------------
def walk_push_to_template(fig_obj, template_obj, skip):
    """

    Parameters
    ----------
    fig_obj: plotly.basedatatypes.BasePlotlyType
    template_obj: plotly.basedatatypes.BasePlotlyType
    skip: set of str
        Set of names of properties to skip
    """
    for prop in list(fig_obj._props):
        if prop == 'template' or prop in skip:
            # Avoid infinite recursion
            continue

        fig_val = fig_obj[prop]
        template_val = template_obj[prop]

        validator = fig_obj._validators[prop]

        if isinstance(validator, CompoundValidator):
            walk_push_to_template(fig_val, template_val, skip)
            if not fig_val._props:
                # Check if we can remove prop itself
                fig_obj[prop] = None
        elif isinstance(validator, CompoundArrayValidator) and fig_val:
            template_elements = list(template_val)
            template_element_names = [el.name for el in template_elements]
            template_propdefaults = template_obj[prop[:-1] + 'defaults']

            for fig_el in fig_val:
                element_name = fig_el.name
                if element_name:
                    # No properties are skipped inside a named array element
                    skip = set()
                    if fig_el.name in template_element_names:
                        item_index = template_element_names.index(fig_el.name)
                        template_el = template_elements[item_index]
                        walk_push_to_template(fig_el, template_el, skip)
                    else:
                        template_el = fig_el.__class__()
                        walk_push_to_template(fig_el, template_el, skip)
                        template_elements.append(template_el)
                        template_element_names.append(fig_el.name)

                    # Restore element name
                    # since it was pushed to template above
                    fig_el.name = element_name
                else:
                    walk_push_to_template(fig_el, template_propdefaults, skip)

            template_obj[prop] = template_elements

        elif not validator.array_ok or not is_array(fig_val):
            # Move property value from figure to template
            template_obj[prop] = fig_val
            try:
                fig_obj[prop] = None
            except ValueError:
                # Property cannot be set to None, move on.
                pass



def to_templated(fig, skip=('title', 'text')):
    """

    Parameters
    ----------
    fig: plotly.basedatatypes.BaseFigure
    skip
        collection of names of properties to skip when moving properties to
        the template.

    Returns
    -------

    """

    # Process skip
    if not skip:
        skip = set()
    else:
        skip = set(skip)

    # Always skip uids
    skip.add('uid')

    # Initialize templated figure with copy of input current figure
    templated_fig = copy.deepcopy(fig)

    # Initialize template object
    if templated_fig.layout.template is None:
        templated_fig.layout.template = {}

    # Handle layout
    walk_push_to_template(templated_fig.layout,
                          templated_fig.layout.template.layout,
                          skip=skip)

    # Handle traces
    trace_type_indexes = {}
    for trace in list(templated_fig.data):
        template_index = trace_type_indexes.get(trace.type, 0)

        # Extend template traces if necessary
        template_traces = list(templated_fig.layout.template.data[trace.type])
        while len(template_traces) <= template_index:
            # Append empty trace
            template_traces.append(trace.__class__())

        # Get corresponding template trace
        template_trace = template_traces[template_index]

        # Perform push properties to template
        walk_push_to_template(trace, template_trace, skip=skip)

        # Update template traces in templated_fig
        templated_fig.layout.template.data[trace.type] = template_traces

        # Update trace_type_indexes
        trace_type_indexes[trace.type] = template_index + 1

    # Remove useless trace arrays
    for trace_type in templated_fig.layout.template.data:
        traces = templated_fig.layout.template.data[trace_type]
        is_empty = [trace.to_plotly_json() == {'type': trace_type}
                    for trace in traces]
        if all(is_empty):
            templated_fig.layout.template.data[trace_type] = None

    return templated_fig
