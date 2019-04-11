from __future__ import absolute_import

from inspect import getargspec
from unittest import TestCase

from requests.compat import json as _json

from plotly.utils import (PlotlyJSONEncoder, get_by_path, memoize,
                          node_generator)


class TestJSONEncoder(TestCase):

    def test_nan_to_null(self):
        array = [1, float('NaN'), float('Inf'), float('-Inf'), 'platypus']
        result = _json.dumps(array, cls=PlotlyJSONEncoder)
        expected_result = '[1, null, null, null, "platypus"]'
        self.assertEqual(result, expected_result)


class TestGetByPath(TestCase):

    def test_get_by_path(self):

        # should be able to traverse into a nested dict/list with key array

        figure = {'data': [{}, {'marker': {'color': ['red', 'blue']}}]}
        path = ('data', 1, 'marker', 'color')
        value = get_by_path(figure, path)
        expected_value = ['red', 'blue']
        self.assertEqual(value, expected_value)


class TestNodeGenerator(TestCase):

    def test_node_generator(self):

        # should generate a (node, path) pair for each dict in a dict

        node4 = {'h': 5}
        node3 = {'g': 7}
        node2 = {'e': node3}
        node1 = {'c': node2, 'd': ['blah']}
        node0 = {'a': node1, 'b': 8}

        expected_node_path_tuples = [
            (node0, ()),
            (node1, ('a',)),
            (node2, ('a', 'c')),
            (node3, ('a', 'c', 'e')),
            (node4, ('a', 'c', 'f'))
        ]
        for i, item in enumerate(node_generator(node0)):
            self.assertEqual(item, expected_node_path_tuples[i])


class TestMemoizeDecorator(TestCase):

    # In Python 2.x, globals should be module-scoped. By defining and
    # instantiating a class, we *access* the global first before attempting
    # to update a value. I.e., you *cannot* simply mutate the global value
    # on it's own.
    class Namespace(object):
        pass

    def test_memoize(self):
        name_space = self.Namespace()
        name_space.call_count = 0

        @memoize()
        def add(a, b):
            name_space.call_count += 1
            return a + b

        tests = [[(1, 1), 2], [(2, 3), 5], [(3, -3), 0]]

        self.assertEqual(name_space.call_count, 0)
        for i, (inputs, result) in enumerate(tests, 1):
            for _ in range(10):
                self.assertEqual(add(*inputs), result)
                self.assertEqual(name_space.call_count, i)

    def test_memoize_maxsize(self):
        name_space = self.Namespace()
        name_space.call_count = 0

        maxsize = 10

        @memoize(maxsize=maxsize)
        def identity(a):
            name_space.call_count += 1
            return a

        # Function hasn't been called yet, we should get *up to* maxsize cache.
        for i in range(maxsize):
            self.assertEqual(identity(i), i)
            self.assertEqual(name_space.call_count, i + 1)

        # Nothing should have been discarded yet. no additional calls.
        for i in range(maxsize):
            self.assertEqual(identity(i), i)
            self.assertEqual(name_space.call_count, maxsize)

        # Make a new call...
        self.assertEqual(identity(maxsize), maxsize)
        self.assertEqual(name_space.call_count, maxsize + 1)

        # All but the first call should be remembered.
        for i in range(1, maxsize + 1):
            self.assertEqual(identity(i), i)
            self.assertEqual(name_space.call_count, maxsize + 1)

        # The *initial* call should now be forgotten for each new call.
        for i in range(maxsize):
            self.assertEqual(identity(i), i)
            self.assertEqual(name_space.call_count, maxsize + 1 + i + 1)

    def test_memoize_maxsize_none(self):
        name_space = self.Namespace()
        name_space.call_count = 0

        @memoize(maxsize=None)
        def identity(a):
            name_space.call_count += 1
            return a

        # Function hasn't been called yet, we should get *up to* maxsize cache.
        for i in range(400):
            self.assertEqual(identity(i), i)
            self.assertEqual(name_space.call_count, i + 1)

        # Nothing should have been discarded. no additional calls.
        for i in range(400):
            self.assertEqual(identity(i), i)
            self.assertEqual(name_space.call_count, 400)

    def test_memoize_function_info(self):
        # We use the decorator module to assure that function info is not
        # overwritten by the decorator.

        @memoize()
        def foo(a, b, c='see?'):
            """Foo is foo."""
            pass

        self.assertEqual(foo.__doc__, 'Foo is foo.')
        self.assertEqual(foo.__name__, 'foo')
        self.assertEqual(getargspec(foo).args, ['a', 'b', 'c'])
        self.assertEqual(getargspec(foo).defaults, ('see?',))
