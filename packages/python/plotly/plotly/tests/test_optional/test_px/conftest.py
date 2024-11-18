import pandas as pd
import polars as pl
import pyarrow as pa
import pytest

from narwhals.typing import IntoDataFrame
from narwhals.utils import parse_version


def pandas_constructor(obj) -> IntoDataFrame:
    return pd.DataFrame(obj)  # type: ignore[no-any-return]


def pandas_nullable_constructor(obj) -> IntoDataFrame:
    return pd.DataFrame(obj).convert_dtypes(dtype_backend="numpy_nullable")  # type: ignore[no-any-return]


def pandas_pyarrow_constructor(obj) -> IntoDataFrame:
    return pd.DataFrame(obj).convert_dtypes(dtype_backend="pyarrow")  # type: ignore[no-any-return]


def polars_eager_constructor(obj) -> IntoDataFrame:
    return pl.DataFrame(obj)


def pyarrow_table_constructor(obj) -> IntoDataFrame:
    return pa.table(obj)  # type: ignore[no-any-return]


constructors = [polars_eager_constructor, pyarrow_table_constructor, pandas_constructor]

if parse_version(pd.__version__) >= parse_version("2.0.0"):
    constructors.extend(
        [
            pandas_nullable_constructor,
            pandas_pyarrow_constructor,
        ]
    )


@pytest.fixture(params=constructors)
def constructor(request: pytest.FixtureRequest):
    return request.param  # type: ignore[no-any-return]


@pytest.fixture(params=["pandas", "pyarrow", "polars"])
def backend(request: pytest.FixtureRequest) -> str:
    return request.param  # type: ignore[no-any-return]
