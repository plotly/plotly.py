import pytest
from _plotly_utils.basevalidators import StringValidator
import numpy as np


# Fixtures
# --------
@pytest.fixture()
def validator():
    return StringValidator('prop', 'parent')


@pytest.fixture()
def validator_values():
    return StringValidator('prop', 'parent', values=['foo', 'BAR', ''])


@pytest.fixture()
def validator_no_blanks():
    return StringValidator('prop', 'parent', no_blank=True)


@pytest.fixture()
def validator_strict():
    return StringValidator('prop', 'parent', strict=True)


@pytest.fixture
def validator_aok():
    return StringValidator('prop', 'parent', array_ok=True, strict=False)


@pytest.fixture
def validator_aok_strict():
    return StringValidator('prop', 'parent', array_ok=True, strict=True)

@pytest.fixture
def validator_aok_values():
    return StringValidator('prop', 'parent', values=['foo', 'BAR', '', 'baz'], array_ok=True)


@pytest.fixture()
def validator_no_blanks_aok():
    return StringValidator('prop', 'parent', no_blank=True, array_ok=True)


# Array not ok
# ------------
# Not strict
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         ['bar', 234, np.nan,
                          'HELLO!!!', 'world!@#$%^&*()', ''])
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) == str(val)


# ### Rejection by value ###
@pytest.mark.parametrize('val',
                         [(), [], [1, 2, 3], set()])
def test_rejection(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# Valid values
# ------------
@pytest.mark.parametrize('val',
                         ['foo', 'BAR', ''])
def test_acceptance_values(val, validator_values):
    assert validator_values.validate_coerce(val) == val


@pytest.mark.parametrize('val',
                         ['FOO', 'bar', 'other', '1234'])
def test_rejection_values(val, validator_values):
    with pytest.raises(ValueError) as validation_failure:
        validator_values.validate_coerce(val)

    assert 'Invalid value'.format(val=val) in str(validation_failure.value)
    assert "['foo', 'BAR', '']" in str(validation_failure.value)


# ### No blanks ###
@pytest.mark.parametrize('val',
                         ['bar', 'HELLO!!!', 'world!@#$%^&*()'])
def test_acceptance_no_blanks(val, validator_no_blanks):
    assert validator_no_blanks.validate_coerce(val) == val


@pytest.mark.parametrize('val',
                         [''])
def test_rejection_no_blanks(val, validator_no_blanks):
    with pytest.raises(ValueError) as validation_failure:
        validator_no_blanks.validate_coerce(val)

    assert 'A non-empty string' in str(validation_failure.value)


# Strict
# ------
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         ['bar', 'HELLO!!!', 'world!@#$%^&*()', ''])
def test_acceptance_strict(val, validator_strict):
    assert validator_strict.validate_coerce(val) == val


# ### Rejection by value ###
@pytest.mark.parametrize('val',
                         [(), [], [1, 2, 3], set(), np.nan, np.pi, 23])
def test_rejection_strict(val, validator_strict):
    with pytest.raises(ValueError) as validation_failure:
        validator_strict.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# Array ok
# --------
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         ['foo', 'BAR', '', 'baz'])
def test_acceptance_aok_scalars(val, validator_aok):
    assert validator_aok.validate_coerce(val) == val


@pytest.mark.parametrize('val',
                         ['foo',
                          ['foo'],
                          np.array(['BAR', ''], dtype='object'),
                          ['baz', 'baz', 'baz'],
                          ['foo', None, 'bar']])
def test_acceptance_aok_list(val, validator_aok):
    coerce_val = validator_aok.validate_coerce(val)
    if isinstance(val, np.ndarray):
        assert isinstance(coerce_val, np.ndarray)
        assert np.array_equal(coerce_val,
                              np.array(val, dtype=coerce_val.dtype))
    elif isinstance(val, list):
        assert validator_aok.present(val) == tuple(val)
    else:
        assert coerce_val == val


# ### Rejection by type ###
@pytest.mark.parametrize('val',
                         [['foo', ()], ['foo', 3, 4], [3, 2, 1]])
def test_rejection_aok(val, validator_aok_strict):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok_strict.validate_coerce(val)

    assert 'Invalid element(s)' in str(validation_failure.value)


# ### Rejection by value ###
@pytest.mark.parametrize('val',
                         [['foo', 'bar'],
                          ['3', '4'],
                          ['BAR', 'BAR', 'hello!'],
                          ['foo', None]])
def test_rejection_aok_values(val, validator_aok_values):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok_values.validate_coerce(val)

    assert 'Invalid element(s)' in str(validation_failure.value)


# ### No blanks ###
@pytest.mark.parametrize('val',
                         ['123',
                          ['bar', 'HELLO!!!'],
                          np.array(['bar', 'HELLO!!!'], dtype='object'),
                          ['world!@#$%^&*()']])
def test_acceptance_no_blanks_aok(val, validator_no_blanks_aok):
    coerce_val = validator_no_blanks_aok.validate_coerce(val)
    if isinstance(val, np.ndarray):
        assert np.array_equal(coerce_val,
                              np.array(val, dtype=coerce_val.dtype))
    elif isinstance(val, list):
        assert validator_no_blanks_aok.present(coerce_val) == tuple(val)
    else:
        assert coerce_val == val


@pytest.mark.parametrize('val',
                         ['',
                          ['foo', 'bar', ''],
                          np.array(['foo', 'bar', ''], dtype='object'),
                          [''],
                          np.array([''], dtype='object')])
def test_rejection_no_blanks_aok(val,
                                 validator_no_blanks_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_no_blanks_aok.validate_coerce(val)

    assert 'A non-empty string' in str(validation_failure.value)

