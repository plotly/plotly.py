import itertools
import pytest
from _plotly_utils.basevalidators import FlaglistValidator
import numpy as np


# Fixtures
# --------
@pytest.fixture(params=[None, ['none', 'all']])
def validator(request):
    # Validator with or without extras
    return FlaglistValidator('prop', 'parent', flags=['lines', 'markers', 'text'], extras=request.param)


@pytest.fixture()
def validator_extra():
    return FlaglistValidator('prop', 'parent',
                             flags=['lines', 'markers', 'text'],
                             extras=['none', 'all'])


@pytest.fixture()
def validator_extra_aok():
    return FlaglistValidator('prop', 'parent',
                             flags=['lines', 'markers', 'text'],
                             extras=['none', 'all'],
                             array_ok=True)


@pytest.fixture(params=
                ["+".join(p)
                 for i in range(1, 4)
                 for p in itertools.permutations(['lines', 'markers', 'text'], i)])
def flaglist(request):
    return request.param


@pytest.fixture(params=['none', 'all'])
def extra(request):
    return request.param


# Array not ok (with or without extras)
# -------------------------------------
# ### Acceptance ###
def test_acceptance(flaglist, validator):
    assert validator.validate_coerce(flaglist) == flaglist


# ### Coercion ###
@pytest.mark.parametrize('in_val,coerce_val',
                         [('  lines ', 'lines'),  # Strip outer whitespace
                          (' lines + markers ', 'lines+markers'),  # Remove inner whitespace around '+'
                          ('lines ,markers', 'lines+markers'),  # Accept comma separated
                          ])
def test_coercion(in_val, coerce_val, validator):
    assert validator.validate_coerce(in_val) == coerce_val


# ### Rejection by type ###
@pytest.mark.parametrize('val',
                         [21, (), ['lines'], set(), {}])
def test_rejection_type(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by value ###
@pytest.mark.parametrize('val',
                         ['', 'line', 'markers+line', 'lin es', 'lin es+markers'])
def test_rejection_val(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# Array not ok (with extras)
# --------------------------
# ### Acceptance ###
#     Note: Acceptance of flaglists without extras already tested above
def test_acceptance_extra(extra, validator_extra):
    assert validator_extra.validate_coerce(extra) == extra


# ### Coercion ###
@pytest.mark.parametrize('in_val,coerce_val',
                         [('  none ', 'none'),
                          ('all  ', 'all'),
                          ])
def test_coercion(in_val, coerce_val, validator_extra):
    assert validator_extra.validate_coerce(in_val) == coerce_val


# ### Rejection by value ###
#     Note: Rejection by type already handled above
@pytest.mark.parametrize('val',
                         ['al l',  # Don't remove inner whitespace
                          'lines+all',  # Extras cannot be combined with flags
                          'none+markers',
                          'markers+lines+text+none'])
def test_rejection_val(val, validator_extra):
    with pytest.raises(ValueError) as validation_failure:
        validator_extra.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# Array OK (with extras)
# ----------------------
# ### Acceptance (scalars) ###
def test_acceptance_aok_scalar_flaglist(flaglist, validator_extra_aok):
    assert validator_extra_aok.validate_coerce(flaglist) == flaglist


def test_acceptance_aok_scalar_extra(extra, validator_extra_aok):
    assert validator_extra_aok.validate_coerce(extra) == extra


# ### Acceptance (lists) ###
def test_acceptance_aok_scalarlist_flaglist(flaglist, validator_extra_aok):
    assert np.array_equal(validator_extra_aok.validate_coerce([flaglist]),
                          np.array([flaglist], dtype='unicode'))


@pytest.mark.parametrize('val', [
    ['all', 'markers', 'text+markers'],
    ['lines', 'lines+markers', 'markers+lines+text'],
    ['all', 'all', 'lines+text', 'none']
])
def test_acceptance_aok_list_flaglist(val, validator_extra_aok):
    assert np.array_equal(validator_extra_aok.validate_coerce(val),
                          np.array(val, dtype='unicode'))


# ### Coercion ###
@pytest.mark.parametrize('in_val,expected',
                         [(['  lines ', ' lines + markers ', 'lines ,markers'],
                           ['lines', 'lines+markers', 'lines+markers']),
                          (np.array(['text   +lines']),
                           np.array(['text+lines'], dtype='unicode'))
                          ])
def test_coercion_aok(in_val, expected, validator_extra_aok):
    coerce_val = validator_extra_aok.validate_coerce(in_val)
    if isinstance(in_val, (list, tuple)):
        expected == coerce_val
        validator_extra_aok.present(coerce_val) == tuple(expected)
    else:
        assert np.array_equal(coerce_val, coerce_val)
        assert np.array_equal(
            validator_extra_aok.present(coerce_val),
            coerce_val)


# ### Rejection by type ###
@pytest.mark.parametrize('val',
                         [21, set(), {}])
def test_rejection_aok_type(val, validator_extra_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_extra_aok.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element type ###
@pytest.mark.parametrize('val',
                         [[21, 'markers'],
                          ['lines', ()],
                          ['none', set()],
                          ['lines+text', {}, 'markers']])
def test_rejection_aok_element_type(val, validator_extra_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_extra_aok.validate_coerce(val)

    assert 'Invalid element(s)' in str(validation_failure.value)


# ### Rejection by element values ###
@pytest.mark.parametrize('val', [
    ['all+markers', 'text+markers'],  # extra plus flag
    ['line', 'lines+markers', 'markers+lines+text'],  # Invalid flag
    ['all', '', 'lines+text', 'none']  # Empty string
])
def test_rejection_aok_element_val(val, validator_extra_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_extra_aok.validate_coerce(val)

    assert 'Invalid element(s)' in str(validation_failure.value)
