import typing as typ


class InputState:
    def __init__(self, ctrl=None, alt=None, shift=None, meta=None, button=None, buttons=None, **_):
        self._ctrl = ctrl
        self._alt = alt
        self._meta = meta
        self._shift = shift
        self._button = button
        self._buttons = buttons

    def __repr__(self):
        return """\
InputState(ctrl={ctrl}, 
           alt={alt}, 
           shift={shift}, 
           meta={meta}, 
           button={button}, 
           buttons={buttons})"""

    @property
    def alt(self) -> bool:
        """
        Whether alt key pressed

        Returns
        -------
        bool
        """
        return self._alt

    @property
    def ctrl(self) -> bool:
        """
        Whether ctrl key pressed

        Returns
        -------
        bool
        """
        return self._ctrl

    @property
    def shift(self) -> bool:
        """
        Whether shift key pressed

        Returns
        -------
        bool
        """
        return self._shift

    @property
    def meta(self) -> bool:
        """
        Whether meta key pressed

        Returns
        -------
        bool
        """
        return self._meta

    @property
    def button(self) -> int:
        """
        Integer code for the button that was pressed on the mouse to trigger the event

        - 0: Main button pressed, usually the left button or the un-initialized state
        - 1: Auxiliary button pressed, usually the wheel button or the middle button (if present)
        - 2: Secondary button pressed, usually the right button
        - 3: Fourth button, typically the Browser Back button
        - 4: Fifth button, typically the Browser Forward button

        Returns
        -------
        int
        """
        return self._button

    @property
    def buttons(self) -> int:
        """
        Integer code for which combination of buttons are pressed on the mouse when the event is triggered.

        -  0: No button or un-initialized
        -  1: Primary button (usually left)
        -  2: Secondary button (usually right)
        -  4: Auxilary button (usually middle or mouse wheel button)
        -  8: 4th button (typically the "Browser Back" button)
        - 16: 5th button (typically the "Browser Forward" button)

        Combinations of buttons are represented as the decimal form of the bitmask of the values above.

        For example, pressing both the primary (1) and auxilary (4) buttons will result in a code of 5

        Returns
        -------
        int
        """
        return self._buttons


class Points:

    def __init__(self, point_inds=None, xs=None, ys=None, trace_name=None, trace_index=None):
        self._point_inds = point_inds
        self._xs = xs
        self._ys = ys
        self._trace_name = trace_name
        self._trace_index = trace_index

    @property
    def point_inds(self) -> typ.List[int]:
        return self._point_inds

    @property
    def xs(self) -> typ.List:
        return self._xs

    @property
    def ys(self) -> typ.List:
        return self._ys

    @property
    def trace_name(self) -> str:
        return self._trace_name

    @property
    def trace_index(self) -> int:
        return self._trace_index


class BoxSelector:
    def __init__(self, xrange=None, yrange=None, **_):
        self._type = 'box'
        self._xrange = xrange
        self._yrange = yrange

    @property
    def type(self) -> str:
        return self._type

    @property
    def xrange(self) -> typ.Tuple[float, float]:
        return self._xrange

    @property
    def yrange(self) -> typ.Tuple[float, float]:
        return self._yrange


class LassoSelector:
    def __init__(self, xs=None, ys=None, **_):
        self._type = 'lasso'
        self._xs = xs
        self._ys = ys

    @property
    def type(self) -> str:
        return self._type

    @property
    def xs(self) -> typ.List[float]:
        return self._xs

    @property
    def ys(self) -> typ.List[float]:
        return self._ys
