import pytest


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()


def test_capital_case():
    assert capital_case('spirit') == 'Spirit'


def test_raises_exception_on_non_strung_arguments():
    with pytest.raises(TypeError):
        capital_case(9)