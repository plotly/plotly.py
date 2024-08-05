import pytest
from _plotly_utils.basevalidators import AnyValidator
import numpy as np
from plotly.tests.b64 import b64


# Fixtures
# --------
@pytest.fixture()
def validator():
    return AnyValidator("prop", "parent")


@pytest.fixture()
def validator_aok():
    return AnyValidator("prop", "parent", array_ok=True)


# Tests
# -----
# ### Acceptance ###
@pytest.mark.parametrize("val", [set(), "Hello", 123, np.inf, np.nan, {}])
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) is val


# ### Acceptance of arrays ###
@pytest.mark.parametrize(
    "val",
    [
        23,
        "Hello!",
        [],
        (),
        np.array([]),
        ("Hello", "World"),
        ["Hello", "World"],
        [np.pi, np.e, {}],
    ],
)
def test_acceptance_array(val, validator_aok):
    coerce_val = validator_aok.validate_coerce(val)
    if isinstance(val, np.ndarray):
        assert isinstance(coerce_val, np.ndarray)
        assert coerce_val.dtype == "object"
        assert np.array_equal(coerce_val, val)
    elif isinstance(val, (list, tuple)):
        assert coerce_val == list(val)
        assert validator_aok.present(coerce_val) == tuple(val)
    else:
        assert coerce_val == val
        assert validator_aok.present(coerce_val) == val

def test_base64_array(validator_aok):
    val = b64(np.array([1, 2, 3], dtype="int64"))
    coerce_val = validator_aok.validate_coerce(val)
    assert coerce_val['bdata'] == "AQID"
    assert coerce_val['dtype'] == "i1"