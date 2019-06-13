import pytest
from _plotly_utils.basevalidators import DashValidator


# Constants
# ---------
dash_types = ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']


# Fixtures
# --------
@pytest.fixture()
def validator():
    return DashValidator('prop', 'parent', dash_types)


# Acceptance
# ----------
@pytest.mark.parametrize('val',
                         dash_types)
def test_acceptance_dash_types(val, validator):
    # Values should be accepted and returned unchanged
    assert validator.validate_coerce(val) == val


@pytest.mark.parametrize('val',
                         ['2', '2.2', '2.002', '1 2 002',
                          '1,2,3', '1, 2, 3',
                          '1px 2px 3px', '1.5px, 2px, 3.9px',
                          '23% 18% 13px', '200%   3px'])
def test_acceptance_dash_lists(val, validator):
    # Values should be accepted and returned unchanged
    assert validator.validate_coerce(val) == val


# Rejection
# ---------
# ### Value Rejection ###
@pytest.mark.parametrize('val', ['bogus', 'not-a-dash'])
def test_rejection_by_bad_dash_type(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


@pytest.mark.parametrize('val',
                         ['', '1,,3,4', '2 3 C', '2pxx 3 4'])
def test_rejection_by_bad_dash_list(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)
