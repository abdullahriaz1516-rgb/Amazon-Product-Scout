# Amazon Product Scout

A standalone Amazon product-research dashboard inspired by the workflow of commercial research tools.

## Included now
- Amazon marketplace selector
- Keyword/niche research filters
- Demo product dataset
- Transparent Opportunity Score (0–100)
- Demand, reviews, rating and competition signals
- FBA profit, margin and ROI calculator
- Product comparison table
- API-ready data architecture
- Secret-safe configuration plan

## Planned production integrations
- Amazon SP-API for authorized catalog/product data
- Keepa API for historical price/rank data
- Licensed keyword/search-volume provider
- ASIN analyzer and competitor analysis
- AI product insights
- Saved products, watchlists and exports
- Authentication and production deployment

## Important
The application does not copy Jungle Scout's proprietary implementation or data. Live marketplace metrics require properly licensed/API-accessible data. Demo values are placeholders and should not be used for purchasing decisions.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Environment secrets
Configure these outside Git:
- `AMAZON_SP_CLIENT_ID`
- `AMAZON_SP_CLIENT_SECRET`
- `AMAZON_REFRESH_TOKEN`
- `KEEPA_API_KEY`
- `OPENAI_API_KEY`
