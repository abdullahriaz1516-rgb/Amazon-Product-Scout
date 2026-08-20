from __future__ import annotations

import io
import pandas as pd


def products_to_csv(products: list[dict]) -> bytes:
    """Return product records as a downloadable UTF-8 CSV."""
    frame = pd.DataFrame(products)
    return frame.to_csv(index=False).encode("utf-8")


def products_to_excel(products: list[dict]) -> bytes:
    """Return product records as an Excel workbook."""
    output = io.BytesIO()
    pd.DataFrame(products).to_excel(output, index=False, engine="openpyxl")
    return output.getvalue()
