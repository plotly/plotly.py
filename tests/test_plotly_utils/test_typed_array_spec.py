"""
Tests for _plotly_utils.utils.to_typed_array_spec's byte order.

plotly.js decodes "bdata" in the browser with typed arrays (e.g.
new Float64Array(buffer)), which always read in the platform's native
order, little-endian on every real browser. to_typed_array_spec must
therefore always produce little-endian bytes, regardless of the host's
own native byte order.

Note: these arrays are built in plain/native order (dtype="float64" etc,
not ">f8"/"<f8"), exactly as every real caller does. An array built with
an explicit non-native byte order (e.g. ">f8") reports str(dtype) as
">f8" rather than "float64", so it never reaches the plotlyjsShortTypes
dispatch in to_typed_array_spec at all, it can't be used to simulate
"a big-endian host" from a little-endian machine. These tests therefore
only catch a real regression when actually run on big-endian hardware
(e.g. z/OS/s390x), not on a little-endian CI runner.
"""

import base64

import numpy as np
import pytest

from _plotly_utils.utils import to_typed_array_spec


@pytest.mark.parametrize(
    "dtype,np_dtype",
    [
        ("float64", "f8"),
        ("float32", "f4"),
        ("int32", "i4"),
        ("int16", "i2"),
        ("uint32", "u4"),
    ],
)
def test_bdata_is_little_endian(dtype, np_dtype):
    v = np.array([1, 2, 3, 4, 5], dtype=dtype)
    assert (
        str(v.dtype) == dtype
    )  # sanity: native order, routes through the real dispatch

    spec = to_typed_array_spec(v)
    assert isinstance(spec, dict), "did not reach the typed-array-spec encoding path"

    raw = base64.b64decode(spec["bdata"])
    decoded_as_browser_would_read_it = np.frombuffer(raw, dtype=f"<{np_dtype}")

    np.testing.assert_array_equal(decoded_as_browser_would_read_it, v)


def test_bdata_is_little_endian_for_floats_with_fraction():
    v = np.array([1.1, 2.3, 3.5])

    spec = to_typed_array_spec(v)

    raw = base64.b64decode(spec["bdata"])
    decoded_as_browser_would_read_it = np.frombuffer(raw, dtype="<f8")

    np.testing.assert_array_equal(decoded_as_browser_would_read_it, v)
