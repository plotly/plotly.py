
# Create sentinal Undefined object
from traitlets import Undefined
import numpy as np

def _py_to_js(v, widget_manager):
    # print('_py_to_js')
    # print(v)
    if isinstance(v, dict):
        return {k: _py_to_js(v, widget_manager) for k, v in v.items()}
    elif isinstance(v, (list, tuple)):
        return [_py_to_js(v, widget_manager) for v in v]
    elif isinstance(v, np.ndarray):
        if v.ndim == 1 and v.dtype.kind in ['u', 'i', 'f']:  # (un)signed integer or float
            return {'buffer': memoryview(v), 'dtype': str(v.dtype), 'shape': v.shape}
        else:
            return v.tolist()
    else:
        if v is Undefined:
            return '_undefined_'
        else:
            return v


def _js_to_py(v, widget_manager):
    # print('_js_to_py')
    # print(v)
    if isinstance(v, dict):
        return {k: _js_to_py(v, widget_manager) for k, v in v.items()}
    elif isinstance(v, (list, tuple)):
        return [_js_to_py(v, widget_manager) for v in v]
    elif isinstance(v, str) and v == '_undefined_':
        return Undefined
    else:
        return v


custom_serializers = {
    'from_json': _js_to_py,
    'to_json': _py_to_js
}
