import pytest
from module_08_oop.well_class import Well

@pytest.fixture
def standard_well():
    return Well("TEST-1", 20000, 10000, 5000, 10.0, 200)

def test_hydrostatic_pressure(standard_well):
    assert standard_well.hydrostatic_pressure() == 5200.0

def test_overbalance_margin(standard_well):
    assert standard_well.overbalance_margin() == 200.0

@pytest.mark.parametrize("temperature, expected", [
    (251, True),
    (250, False),
    (249, False),
])
def test_is_high_temp(temperature, expected):
    well = Well("TEST", 20000, 10000, 5000, 10.0, temperature)
    assert well.is_high_temp() == expected