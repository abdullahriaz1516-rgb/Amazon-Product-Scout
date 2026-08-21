from scout.calculator import fba_profit
from scout.scoring import opportunity_score


def test_fba_profit_returns_expected_values():
    result = fba_profit(30, 7, 2.5, 3, 5.5)
    assert round(result["profit"], 2) == 7.5
    assert round(result["margin"], 2) == 25.0
    assert round(result["roi"], 2) == 78.95


def test_opportunity_score_is_bounded():
    product = {
        "monthly_sales": 1000,
        "reviews": 10,
        "rating": 5.0,
        "competition": "Low",
    }
    assert 0 <= opportunity_score(product) <= 100
