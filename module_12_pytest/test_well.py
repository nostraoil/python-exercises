import pytest
from module_08_oop.well_class import Well, InjectionWell

@pytest.fixture
def standard_well():
    return Well("TEST-1", 20000, 10000, 5000, 10.0, 200)

@pytest.fixture
def injection_well():
    return InjectionWell("INJ-TEST", 20000, 10000, 5000, 10.0, 200, 8000, "water")

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

def test_injection_well_inherits_hydrostatic(injection_well):
    assert injection_well.hydrostatic_pressure() == 5200.0


def test_injection_well_uses_child_overbalance_margin(injection_well):
    assert injection_well.overbalance_margin() == -200.0


def test_injection_well_daily_injection_volume(injection_well):
    assert injection_well.daily_injection_volume() == 8000