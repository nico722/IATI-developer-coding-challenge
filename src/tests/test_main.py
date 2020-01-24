import os
import unittest
from ..main import get_total_budget_value

def test_get_total_budget_value():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    result = get_total_budget_value(f"{BASE_DIR}/sample_data_fully_valid_10_rows.csv", 2018)
    assert result == float(500)

    result = get_total_budget_value(f"{BASE_DIR}/sample_data_fully_valid_10_rows.csv", '2016')
    assert result == float(200)
