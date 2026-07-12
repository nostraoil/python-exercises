import pytest
from pressure import psi_to_kpa

def test_converts_whole_number():
    assert psi_to_kpa(100) == 689.476

def test_converts_numeric_string():
    assert psi_to_kpa("100") == 689.476

def test_strips_surrounding_whitespace():
    assert psi_to_kpa(" 100 ") == 689.476

def test_rejects_string_with_units():
    with pytest.raises(ValueError):
        psi_to_kpa("100 psi")

def test_rejects_string_with_comma():
    with pytest.raises(ValueError):
        psi_to_kpa("1,000")