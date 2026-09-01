from module_08_oop.well_class import Well

def test_hydrostatic_pressure():
    well = Well("TEST-1", 20000, 10000, 5000, 10.0, 200)
    assert well.hydrostatic_pressure() == 5200.0

def test_overbalance_margin():
    well = Well("TEST-2", 20000, 10000, 5000, 10.0, 200)
    assert well.overbalance_margin() == 200.0

def test_is_high_temp_when_above_250():
    well = Well("TEST-3", 20000, 10000, 5000, 10.0, 251)
    assert well.is_high_temp()

def test_is_high_temp_when_at_250():
    well = Well("TEST-4", 20000, 10000, 5000, 10.0, 250)
    assert not well.is_high_temp()

def test_is_high_temp_when_below_250():
    well = Well("TEST-5", 20000, 10000, 5000, 10.0, 249)
    assert not well.is_high_temp()