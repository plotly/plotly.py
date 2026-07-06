import collections.abc

import pytest

from _plotly_utils.importers import relative_import


def _make():
    # Use the stdlib ``collections`` package as a stable lazy-import target.
    return relative_import(
        "collections",
        rel_modules=[".abc"],
        rel_classes=[".abc.Mapping"],
    )


def test_all_lists_module_and_class_leaf_names():
    all_, _getattr, _dir = _make()
    assert sorted(all_) == ["Mapping", "abc"]


def test_getattr_lazily_imports_submodule():
    _all, getattr_, _dir = _make()
    assert getattr_("abc") is collections.abc


def test_getattr_lazily_imports_class():
    _all, getattr_, _dir = _make()
    assert getattr_("Mapping") is collections.abc.Mapping


def test_getattr_unknown_name_raises_attribute_error():
    _all, getattr_, _dir = _make()
    with pytest.raises(AttributeError):
        getattr_("does_not_exist")


def test_dir_returns_all():
    all_, _getattr, dir_ = _make()
    assert sorted(dir_()) == sorted(all_)
