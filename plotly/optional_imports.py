"""
Stand-alone module to provide information about whether optional deps exist.

"""
from __future__ import absolute_import

from importlib import import_module

_not_importable = set()


def get_module(name):
    """
    Return module or None. Absolute import is required.

    :param (str) name: Dot-separated module path. E.g., 'scipy.stats'.
    :raise: (ImportError) Only when exc_msg is defined.
    :return: (module|None) If import succeeds, the module will be returned.

    """
    if name not in _not_importable:
        try:
            return import_module(name)
        except ImportError:
            _not_importable.add(name)
