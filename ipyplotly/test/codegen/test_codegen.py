import os
import importlib
import pytest
import inspect


# Datatypes modules
# -----------------
datatypes_root = 'ipyplotly/datatypes'
datatype_modules = [dirpath.replace('/', '.')
                    for dirpath, _, _ in os.walk(datatypes_root)
                    if not dirpath.endswith('__pycache__')]


@pytest.fixture(params=datatype_modules)
def datatypes_module(request):
    return request.param


# Validate datatype modules
# -------------------------
def test_import_datatypes(datatypes_module):
    importlib.import_module(datatypes_module)


def test_construct_datatypes(datatypes_module):
    module = importlib.import_module(datatypes_module)
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == datatypes_module:
            datatype_class = obj

            # Call datatype constructor with not arguments
            datatype_class()


# Validate validator modules
# --------------------------
validators_root = 'ipyplotly/validators'
validator_modules = [dirpath.replace('/', '.')
                     for dirpath, _, _ in os.walk(validators_root)
                     if not dirpath.endswith('__pycache__')]


@pytest.fixture(params=validator_modules)
def validators_module(request):
    return request.param


def test_import_validators(validators_module):
    importlib.import_module(validators_module)


def test_construct_validators(validators_module):
    module = importlib.import_module(validators_module)
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == validators_module:
            validator_class = obj

            # Call datatype constructor with not arguments
            validator_class()
