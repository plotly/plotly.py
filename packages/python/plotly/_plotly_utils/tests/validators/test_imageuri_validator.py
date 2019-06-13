import base64

import pytest
from _plotly_utils.basevalidators import ImageUriValidator
import numpy as np
from PIL import Image


# Fixtures
# --------
@pytest.fixture()
def validator():
    return ImageUriValidator('prop', 'parent')


# Tests
# -----
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    'http://somewhere.com/images/image12.png',
    'data:image/png;base64,iVBORw0KGgoAAAANSU',
])
def test_validator_acceptance(val, validator):
    assert validator.validate_coerce(val) == val


# ### Coercion from PIL Image ###
def test_validator_coercion_PIL(validator):
    # Single pixel black png (http://png-pixel.com/)

    img_path = '_plotly_utils/tests/resources/1x1-black.png'
    with open(img_path, 'rb') as f:
        hex_bytes = base64.b64encode(f.read()).decode('ascii')
        expected_uri = 'data:image/png;base64,' + hex_bytes

    img = Image.open(img_path)
    coerce_val = validator.validate_coerce(img)
    assert coerce_val == expected_uri


# ### Rejection ###
@pytest.mark.parametrize('val', [
    23, set(), []
])
def test_rejection_by_type(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)
