"""
Sequential color scales are appropriate for most continuous data, but in some cases it \
can be helpful to use a `plotly_express.colors.diverging` or \
`plotly_express.colors.cyclical` scale instead. The color scales in this module are \
mostly meant to be passed in as the `color_continuous_scale` argument to various functions.
"""

from ._swatches import _swatches


def swatches():
    return _swatches(__name__, globals())


swatches.__doc__ = _swatches.__doc__

Plotly = [
    "#0508b8",
    "#1910d8",
    "#3c19f0",
    "#6b1cfb",
    "#981cfd",
    "#bf1cfd",
    "#dd2bfd",
    "#f246fe",
    "#fc67fd",
    "#fe88fc",
    "#fea5fd",
    "#febefe",
    "#fec3fe",
]

Viridis = [
    "#440154",
    "#482878",
    "#3e4989",
    "#31688e",
    "#26828e",
    "#1f9e89",
    "#35b779",
    "#6ece58",
    "#b5de2b",
    "#fde725",
]
Cividis = [
    "#00224e",
    "#123570",
    "#3b496c",
    "#575d6d",
    "#707173",
    "#8a8678",
    "#a59c74",
    "#c3b369",
    "#e1cc55",
    "#fee838",
]

Inferno = [
    "#000004",
    "#1b0c41",
    "#4a0c6b",
    "#781c6d",
    "#a52c60",
    "#cf4446",
    "#ed6925",
    "#fb9b06",
    "#f7d13d",
    "#fcffa4",
]
Magma = [
    "#000004",
    "#180f3d",
    "#440f76",
    "#721f81",
    "#9e2f7f",
    "#cd4071",
    "#f1605d",
    "#fd9668",
    "#feca8d",
    "#fcfdbf",
]
Plasma = [
    "#0d0887",
    "#46039f",
    "#7201a8",
    "#9c179e",
    "#bd3786",
    "#d8576b",
    "#ed7953",
    "#fb9f3a",
    "#fdca26",
    "#f0f921",
]

from .colorbrewer import (  # noqa: F401
    Blues,
    BuGn,
    BuPu,
    GnBu,
    Greens,
    Greys,
    OrRd,
    Oranges,
    PuBu,
    PuBuGn,
    PuRd,
    Purples,
    RdPu,
    Reds,
    YlGn,
    YlGnBu,
    YlOrBr,
    YlOrRd,
)

from .cmocean import (  # noqa: F401
    turbid,
    thermal,
    haline,
    solar,
    ice,
    gray,
    deep,
    dense,
    algae,
    matter,
    speed,
    amp,
    tempo,
)

from .carto import (  # noqa: F401
    Burg,
    Burgyl,
    Redor,
    Oryel,
    Peach,
    Pinkyl,
    Mint,
    Blugrn,
    Darkmint,
    Emrld,
    Aggrnyl,
    Bluyl,
    Teal,
    Tealgrn,
    Purp,
    Purpor,
    Sunset,
    Magenta,
    Sunsetdark,
    Agsunset,
    Brwnyl,
)
