import pandas as pd

from well_report import filter_high_pressure


def test_filter_high_pressure():
    wells = pd.DataFrame({
        "pressure_psi": [2500, 2000, 1500, None],
    })

    result = filter_high_pressure(wells)

    assert len(result) == 1
    assert result["pressure_psi"].tolist() == [2500.0]