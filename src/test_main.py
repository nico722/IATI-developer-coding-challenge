from main import get_total_budget_value

def test_get_total_budget_value():
    assert get_total_budget_value(2018) == float(2000)
