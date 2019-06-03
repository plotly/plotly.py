"""
test__jupyter

"""
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
from ipykernel import kernelspec

from unittest import TestCase
from os import path
import subprocess

PATH_ROOT = path.dirname(__file__)
PATH_NODE_MODULES = path.join(PATH_ROOT, 'node_modules')
PATH_FIXTURES = path.join(PATH_ROOT, 'fixtures')
PATH_JS_TESTS = path.join(PATH_ROOT, 'js_tests')


class PlotlyJupyterTestDeps(TestCase):

    def test_node_modules(self):
        self.assertTrue(path.isdir(PATH_NODE_MODULES))


class Common(TestCase):
    __test__ = False
    name = None

    def setUp(self):
        self.path_test_nb = path.join(PATH_FIXTURES, self.name + '.ipynb')
        self.path_test_html = path.join(PATH_FIXTURES, self.name + '.html')
        self.path_test_js = path.join(PATH_JS_TESTS, self.name + '.js')

        self.kernel_name = kernelspec.KERNEL_NAME

        with open(self.path_test_nb, 'r') as f:
            self.nb = nbformat.read(f, as_version=4)

        self.ep = ExecutePreprocessor(timeout=600,
                                      kernel_name=self.kernel_name)

        self.html_exporter = HTMLExporter()

        self.ep.preprocess(self.nb, {'metadata': {'path': '.'}})
        (self.body, _) = self.html_exporter.from_notebook_node(self.nb)

        with open(self.path_test_html, 'w') as f:
            f.write(self.body)

    def test_js(self):
        cmd = ['npm', 'test', '--', self.path_test_html, self.path_test_js]

        proc = subprocess.Popen(cmd,
                                cwd=PATH_ROOT,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        (_, stderr) = proc.communicate()

        if stderr:
            self.fail('One or more javascript test failed')


class PlotlyJupyterConnectedFalseTestCase(Common):
    __test__ = True
    name = 'connected_false'


class PlotlyJupyterConnectedTrueTestCase(Common):
    __test__ = True
    name = 'connected_true'
