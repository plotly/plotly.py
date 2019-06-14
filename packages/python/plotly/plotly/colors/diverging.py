"""
Diverging color scales are appropriate for continuous data that has a natural midpoint \
other otherwise informative special value, such as 0 altitude, or the boiling point
of a liquid. The color scales in this module are \
mostly meant to be passed in as the `color_continuous_scale` argument to various \
functions, and to be used with the `color_continuous_midpoint` argument.
"""

from .colorbrewer import (  # noqa: F401
    BrBG,
    PRGn,
    PiYG,
    PuOr,
    RdBu,
    RdGy,
    RdYlBu,
    RdYlGn,
    Spectral,
)
from .cmocean import balance, delta, curl  # noqa: F401
from .carto import Armyrose, Fall, Geyser, Temps, Tealrose, Tropic, Earth  # noqa: F401


from ._swatches import _swatches


def swatches():
    return _swatches(__name__, globals())


swatches.__doc__ = _swatches.__doc__
