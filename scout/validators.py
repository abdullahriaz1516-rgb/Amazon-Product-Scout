from __future__ import annotations


def validate_product_inputs(price: float, cost: float, shipping: float, ppc: float) -> list[str]:
    errors: list[str] = []
    if price <= 0:
        errors.append("Selling price must be greater than zero.")
    for name, value in (("Product cost", cost), ("Shipping", shipping), ("PPC", ppc)):
        if value < 0:
            errors.append(f"{name} cannot be negative.")
    if price > 0 and cost + shipping + ppc >= price:
        errors.append("Current costs are equal to or above the selling price.")
    return errors
