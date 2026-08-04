import threading

import pytest

import plotly.graph_objs as go


@pytest.mark.parametrize(
    ("target_type", "target_kwargs", "property_name", "child_property", "expected"),
    [
        pytest.param(
            go.Layout,
            {"font": {"family": "Arial"}},
            "font",
            "family",
            "Arial",
            id="compound-property",
        ),
        pytest.param(
            go.layout.template.Data,
            {"bar": [{"name": "template bar"}]},
            "bar",
            "name",
            "template bar",
            id="compound-array-property",
        ),
    ],
)
def test_concurrent_first_read_keeps_children_attached(
    monkeypatch,
    target_type,
    target_kwargs,
    property_name,
    child_property,
    expected,
):
    target = target_type(**target_kwargs)
    target._compound_props.pop(property_name, None)
    target._compound_array_props.pop(property_name, None)
    validator = target._get_validator(property_name)
    data_class = validator.data_class
    constructors_ready = threading.Barrier(2)
    first_read_complete = threading.Event()
    second_read_complete = threading.Event()
    children = []
    results = []
    errors = []

    def build_child(*args, **kwargs):
        child = data_class(*args, **kwargs)
        constructors_ready.wait(timeout=5)
        if threading.current_thread().name == "second-reader":
            if not first_read_complete.wait(timeout=5):
                raise TimeoutError("First reader did not receive its child")
        return child

    monkeypatch.setattr(validator, "_data_class", build_child)

    def read_child():
        try:
            value = target[property_name]
            if threading.current_thread().name == "first-reader":
                first_read_complete.set()
                if not second_read_complete.wait(timeout=5):
                    raise TimeoutError("Second reader did not receive its child")
            else:
                second_read_complete.set()

            child = value[0] if isinstance(value, tuple) else value
            children.append(child)
            results.append(child[child_property])
        except Exception as error:
            errors.append(error)
            first_read_complete.set()
            second_read_complete.set()

    workers = [
        threading.Thread(target=read_child, name="first-reader"),
        threading.Thread(target=read_child, name="second-reader"),
    ]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join(timeout=5)

    assert all(not worker.is_alive() for worker in workers)
    assert not errors
    assert children[0] is children[1]
    assert results == [expected, expected]
