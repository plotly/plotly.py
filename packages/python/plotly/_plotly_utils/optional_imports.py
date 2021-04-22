"""
Stand-alone module to provide information about whether optional deps exist.

"""
from __future__ import absolute_import

from importlib import import_module
import logging
import sys

logger = logging.getLogger(__name__)
_not_importable = set()


def get_module(name, should_load=True):
    """
    Return module or None. Absolute import is required.

    :param (str) name: Dot-separated module path. E.g., 'scipy.stats'.
    :raise: (ImportError) Only when exc_msg is defined.
    :return: (module|None) If import succeeds, the module will be returned.

    """
    if name in sys.modules:
        return sys.modules[name]
    if not should_load:
        return None
    if name not in _not_importable:
        try:
            return import_module(name)
        except ImportError:
            _not_importable.add(name)
        except Exception as e:
            _not_importable.add(name)
            msg = f"Error importing optional module {name}"
            logger.exception(msg)
