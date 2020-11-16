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
from .cmocean import balance, delta, curl, oxy  # noqa: F401
from .carto import Armyrose, Fall, Geyser, Temps, Tealrose, Tropic, Earth  # noqa: F401

from .plotlyjs import Picnic, Portland  # noqa: F401

from ._swatches import _swatches, _swatches_continuous


def swatches(template=None):
    return _swatches(__name__, globals(), template)


swatches.__doc__ = _swatches.__doc__


def swatches_continuous(template=None):
    return _swatches_continuous(__name__, globals(), template)


swatches_continuous.__doc__ = _swatches_continuous.__doc__

# Prefix variable names with _ so that they will not be added to the swatches
_contents = dict(globals())
for _k, _cols in _contents.items():
    if _k.startswith("_") or _k.startswith("swatches") or _k.endswith("_r"):
        continue
    globals()[_k + "_r"] = _cols[::-1]


__all__ = ["swatches"]
