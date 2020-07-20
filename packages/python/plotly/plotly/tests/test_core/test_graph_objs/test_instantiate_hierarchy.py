from __future__ import absolute_import
from unittest import TestCase
import os
import importlib
import inspect

from plotly.basedatatypes import BasePlotlyType, BaseFigure

datatypes_root = "plotly/graph_objs"
datatype_modules = [
    dirpath.replace("/", ".")
    for dirpath, _, _ in os.walk(datatypes_root)
    if not dirpath.endswith("__pycache__")
]


class HierarchyTest(TestCase):
    def test_construct_datatypes(self):
        for datatypes_module in datatype_modules:
            module = importlib.import_module(datatypes_module)
            for name in getattr(module, "__all__", []):
                if name.startswith("_") or name[0].islower() or name == "FigureWidget":
                    continue
                obj = getattr(module, name)
                try:
                    v = obj()
                except Exception:
                    print(
                        "Failed to construct {obj} in module {module}".format(
                            obj=obj, module=datatypes_module
                        )
                    )
                    raise

                if obj.__module__ == "plotly.graph_objs._deprecations":
                    self.assertTrue(isinstance(v, list) or isinstance(v, dict))
                    obj()
                elif name in ("Figure", "FigureWidget"):
                    self.assertIsInstance(v, BaseFigure)
                else:
                    self.assertIsInstance(v, BasePlotlyType)
