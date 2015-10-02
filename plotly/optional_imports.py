"""
Stand-alone module to provide information about whether optional deps exist.

"""
from __future__ import absolute_import

import importlib

__all__ = ['get_module']

import_cache = {}


def get_module(name, raise_exc=False, msg=None):
    """
    Return the module if it's available. Raise if desired.

    A wrapper around importlib.import_module that only allows absolute import.

    :param (str) name: Dot-separated module path. E.g., 'scipy.stats'.
    :param (bool) raise_exc: Raise ImportError if not found?
    :param (str|None) msg: Optional message to raise with ImportError.
    :raises: (ImportError) If `raise_exception` is True, this can happen.
    :return: (module|None) If import succeeds, the module will be returned.

    """
    if name in import_cache:
        return import_cache[name]

    try:
        module = importlib.import_module(name)  # only allow absolute imports
    except ImportError:
        if raise_exc:
            if msg is None:
                raise  # just raise the current import error
            else:
                raise ImportError(msg)
    else:
        import_cache[name] = module

    return import_cache.get(name, None)  # Don't store the None!
