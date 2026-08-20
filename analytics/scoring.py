from __future__ import annotations

def opportunity_score(monthly_sales: float, monthly_revenue: float, review_count: int, rating: float, margin_pct: float) -> float:
    sales = min(max(monthly_sales / 500.0, 0), 1) * 25
    revenue = min(max(monthly_revenue / 25000.0, 0), 1) * 25
    competition = (1 - min(max(review_count / 2000.0, 0), 1)) * 20
    quality = min(max((rating - 3.0) / 2.0, 0), 1) * 10
    margin = min(max(margin_pct / 40.0, 0), 1) * 20
    return round(sales + revenue + competition + quality + margin, 1)
