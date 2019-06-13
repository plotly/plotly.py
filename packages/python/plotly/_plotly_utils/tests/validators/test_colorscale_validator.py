import pytest
from _plotly_utils.basevalidators import ColorscaleValidator
import numpy as np


# Fixtures
# --------
@pytest.fixture()
def validator():
    return ColorscaleValidator('prop', 'parent')


@pytest.fixture(params=['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu', 'Reds', 'Blues',
                        'Picnic', 'Rainbow', 'Portland', 'Jet', 'Hot', 'Blackbody', 'Earth', 'Electric', 
                        'Viridis', 'Cividis'])
def named_colorscale(request):
    return request.param


# Tests
# -----
# ### Acceptance by name ###
def test_acceptance_named(named_colorscale, validator):
    # As-is
    assert validator.validate_coerce(named_colorscale) == named_colorscale

    # Uppercase
    assert (validator.validate_coerce(named_colorscale.upper()) ==
           named_colorscale.upper())
    
    assert validator.present(named_colorscale) == named_colorscale

# ### Acceptance as array ###
@pytest.mark.parametrize('val', [
    ((0, 'red'),),
    ((0.1, 'rgb(255,0,0)'), (0.3, 'green')),
    ((0, 'purple'), (0.2, 'yellow'), (1.0, 'rgba(255,0,0,100)')),
])
def test_acceptance_array(val, validator):
    assert validator.validate_coerce(val) == val

# ### Coercion as array ###
@pytest.mark.parametrize('val', [
    ([0, 'red'],),
    [(0.1, 'rgb(255, 0, 0)'), (0.3, 'GREEN')],
    (np.array([0, 'Purple'], dtype='object'), (0.2, 'yellow'), (1.0, 'RGBA(255,0,0,100)')),
])
def test_acceptance_array(val, validator):
    # Compute expected (tuple of tuples where color is
    # lowercase with no spaces)
    expected = [[e[0], e[1]] for e in val]
    coerce_val = validator.validate_coerce(val)
    assert coerce_val == expected

    expected_present = tuple([tuple(e) for e in expected])
    assert validator.present(coerce_val) == expected_present


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    23, set(), {}, np.pi
])
def test_rejection_type(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by string value ###
@pytest.mark.parametrize('val', [
    'Invalid', ''
])
def test_rejection_str_value(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by array ###
@pytest.mark.parametrize('val', [
    [0, 'red'],                                     # Elements must be tuples
    [[0.1, 'rgb(255,0,0)', None], (0.3, 'green')],   # length 3 element
    ([1.1, 'purple'], [0.2, 'yellow']),             # Number > 1
    ([0.1, 'purple'], [-0.2, 'yellow']),            # Number < 0
    ([0.1, 'purple'], [0.2, 123]),                  # Color not a string
    ([0.1, 'purple'], [0.2, 'yellowww']),           # Invalid color string
])
def test_rejection_array(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)
