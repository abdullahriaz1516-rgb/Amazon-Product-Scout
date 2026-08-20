from __future__ import annotations

def opportunity_score(rating: float, reviews: int, price: float, margin: float) -> int:
    demand = min(max((reviews / 500) * 30, 0), 30)
    quality = min(max((rating / 5) * 20, 0), 20)
    price_fit = 15 if 20 <= price <= 50 else 8
    profit = min(max(margin, 0), 35)
    return round(min(100, demand + quality + price_fit + profit))


def fba_profit(price: float, product_cost: float, shipping: float, ppc: float, referral_rate: float = 0.15) -> tuple[float, float]:
    referral_fee = price * referral_rate
    profit = price - product_cost - shipping - ppc - referral_fee
    margin = (profit / price * 100) if price else 0
    return profit, margin
