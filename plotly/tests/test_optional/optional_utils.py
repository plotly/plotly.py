from __future__ import absolute_import

import numpy as np

from plotly import optional_imports
from plotly.tests.utils import is_num_list
from plotly.utils import get_by_path, node_generator

matplotlylib = optional_imports.get_module('plotly.matplotlylib')

if matplotlylib:
    import matplotlib
    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use('Agg')
    from plotly.matplotlylib import Exporter, PlotlyRenderer


def run_fig(fig):
    renderer = PlotlyRenderer()
    exporter = Exporter(renderer)
    exporter.run(fig)
    return renderer


class NumpyTestUtilsMixin(object):
    """Provides some helper functions to make testing easier."""

    def _format_path(self, path):
        str_path = [repr(p) for p in path]
        return '[' + ']['.join(sp for sp in str_path) + ']'

    def assert_dict_equal(self, d1, d2, msg=None):
        """
        Uses `np.allclose()` on number arrays.

        :raises: (AssertionError) Using TestCase's self.failureException

        """
        self.assertIsInstance(d1, dict, 'First argument is not a dictionary')
        self.assertIsInstance(d2, dict, 'Second argument is not a dictionary')

        for node, path in node_generator(d1):

            # first check that this sub-dict is contained in both dicts
            try:
                comp_node = get_by_path(d2, path)
            except (KeyError, IndexError):
                standard_msg = (
                    'Path {} exists in dict 1, but not dict 2.'
                    .format(path)
                )
                self.fail(self._formatMessage(msg, standard_msg))
            self.assertIsInstance(
                comp_node, dict, 'Value at path {} is not a dict.'.format(path)
            )

            # check that each key in the first is contained in the second
            for key, val in node.items():
                if isinstance(val, dict):
                    continue  # this gets tested as its own node

                # check that the values at this key are equal
                val_path = path + (key, )
                try:
                    comp_val = comp_node[key]
                except KeyError:
                    standard_msg = (
                        'Path {} exists in dict 1, but not dict 2.'
                        .format(self._format_path(val_path))
                    )
                    self.fail(self._formatMessage(msg, standard_msg))

                if (isinstance(val, np.ndarray) or
                        isinstance(comp_val, np.ndarray)):
                    if np.array_equal(val, comp_val):
                        continue
                elif val == comp_val:
                    continue

                if is_num_list(val) and is_num_list(comp_val):
                    if np.allclose(val, comp_val):
                        continue

                standard_msg = (
                    'Value comparison failed at path {}.\n'
                    '{} != {}'
                    .format(self._format_path(val_path), val, comp_val)
                )
                self.fail(self._formatMessage(msg, standard_msg))

            # finally, check that keys in the second are in the first
            for key in comp_node:
                val_path = path + (key, )
                if key not in node:
                    standard_msg = (
                        'Path {} exists in dict 2, but not dict 1.'
                        .format(self._format_path(val_path))
                    )
                    self.fail(self._formatMessage(msg, standard_msg))
