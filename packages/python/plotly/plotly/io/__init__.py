from _plotly_utils.importers import relative_import
import sys

if sys.version_info < (3, 7):
    from ._orca import to_image, write_image
    from . import orca
    from ._json import to_json, from_json, read_json, write_json
    from ._templates import templates, to_templated
    from ._html import to_html, write_html
    from ._renderers import renderers, show
    from . import base_renderers

    __all__ = [
        "to_image",
        "write_image",
        "orca",
        "to_json",
        "from_json",
        "read_json",
        "write_json",
        "templates",
        "to_templated",
        "to_html",
        "write_html",
        "renderers",
        "show",
        "base_renderers",
    ]
else:
    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".orca", ".base_renderers"],
        [
            "._orca.to_image",
            "._orca.write_image",
            "._json.to_json",
            "._json.from_json",
            "._json.read_json",
            "._json.write_json",
            "._templates.templates",
            "._templates.to_templated",
            "._html.to_html",
            "._html.write_html",
            "._renderers.renderers",
            "._renderers.show",
        ],
    )

    # Set default template (for < 3.7 this is done in ploty/__init__.py)
    from plotly.io import templates

    templates._default = "plotly"
