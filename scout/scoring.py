def opportunity_score(product):
    """Transparent demo score; replace inputs with live marketplace data later."""
    demand = min(product["monthly_sales"] / 30, 40)
    review_score = max(0, 25 - min(product["reviews"] / 40, 25))
    rating_score = max(0, (product["rating"] - 3.5) * 15)
    competition_score = {"Low": 25, "Medium": 15, "High": 5}.get(product["competition"], 10)
    return round(max(0, min(100, demand + review_score + rating_score + competition_score)))
