def fba_profit(price, product_cost, shipping, ppc, fulfillment_fee, referral_rate=0.15):
    referral_fee = price * referral_rate
    landed_cost = product_cost + shipping
    profit = price - landed_cost - referral_fee - fulfillment_fee - ppc
    margin = (profit / price * 100) if price else 0
    roi = (profit / landed_cost * 100) if landed_cost else 0
    return {"profit": profit, "margin": margin, "roi": roi, "referral_fee": referral_fee, "landed_cost": landed_cost}
