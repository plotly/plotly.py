from plotly.validators.layout import TemplateValidator
import textwrap


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
