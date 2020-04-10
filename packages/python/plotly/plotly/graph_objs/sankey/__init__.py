import sys

if sys.version_info < (3, 7):
    from ._textfont import Textfont
    from ._stream import Stream
    from ._node import Node
    from ._link import Link
    from ._hoverlabel import Hoverlabel
    from ._domain import Domain
    from . import node
    from . import link
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".node", ".link", ".hoverlabel"],
        [
            "._textfont.Textfont",
            "._stream.Stream",
            "._node.Node",
            "._link.Link",
            "._hoverlabel.Hoverlabel",
            "._domain.Domain",
        ],
    )
