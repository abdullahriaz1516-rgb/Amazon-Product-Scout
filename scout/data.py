from copy import deepcopy

DEMO_PRODUCTS = [
    {"title":"Adjustable Bamboo Drawer Organizer","price":29.99,"reviews":186,"rating":4.5,"monthly_sales":1450,"monthly_revenue":43485,"competition":"Low"},
    {"title":"Under Sink Storage Organizer","price":24.99,"reviews":412,"rating":4.4,"monthly_sales":2100,"monthly_revenue":52479,"competition":"Medium"},
    {"title":"Stackable Kitchen Cabinet Bins","price":19.99,"reviews":875,"rating":4.3,"monthly_sales":3200,"monthly_revenue":63968,"competition":"High"},
    {"title":"Expandable Spice Rack Organizer","price":27.99,"reviews":94,"rating":4.6,"monthly_sales":980,"monthly_revenue":27430,"competition":"Low"},
    {"title":"Countertop Pantry Organizer","price":22.49,"reviews":265,"rating":4.5,"monthly_sales":1750,"monthly_revenue":39358,"competition":"Medium"},
]

def demo_products():
    return deepcopy(DEMO_PRODUCTS)

def search_products(query, min_price, max_price, max_reviews, min_rating):
    q = (query or "").lower().strip()
    rows = []
    for item in DEMO_PRODUCTS:
        haystack = item["title"].lower()
        relevant = not q or any(word in haystack for word in q.split())
        if relevant and min_price <= item["price"] <= max_price and item["reviews"] <= max_reviews and item["rating"] >= min_rating:
            rows.append(deepcopy(item))
    return rows or [deepcopy(x) for x in DEMO_PRODUCTS if min_price <= x["price"] <= max_price and x["reviews"] <= max_reviews and x["rating"] >= min_rating]
