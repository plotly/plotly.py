import sys
import pytest

version_skip = pytest.mark.skipif(
    sys.version_info < (3, 7), reason="Python version < 3.7"
)
