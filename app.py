import streamlit as st
import pandas as pd
from scout.data import search_products
from scout.scoring import opportunity_score
from scout.calculator import fba_profit

st.set_page_config(page_title="Amazon Product Scout", page_icon="🔎", layout="wide", initial_sidebar_state="expanded")

st.title("🔎 Amazon Product Scout")
st.caption("Amazon product research workspace • Demo mode + API-ready architecture")

with st.sidebar:
    st.header("Research Filters")
    marketplace = st.selectbox("Marketplace", ["Amazon.com (US)", "Amazon.co.uk", "Amazon.ca", "Amazon.ae"])
    query = st.text_input("Keyword / niche", "kitchen organizer")
    min_price = st.number_input("Min price ($)", 0.0, 500.0, 15.0)
    max_price = st.number_input("Max price ($)", 0.0, 500.0, 60.0)
    max_reviews = st.number_input("Max reviews", 0, 100000, 1000, 50)
    min_rating = st.slider("Min rating", 1.0, 5.0, 4.0, 0.1)
    st.divider()
    st.caption("Live Amazon data requires authorized Amazon/Keepa credentials. No scraping or access-control bypass is used.")

products = search_products(query, min_price, max_price, max_reviews, min_rating)
for p in products:
    p["Opportunity"] = opportunity_score(p)

# Dashboard summary
if products:
    best = max(products, key=lambda x: x["Opportunity"])
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Top Opportunity", f"{best['Opportunity']}/100")
    k2.metric("Products Found", len(products))
    k3.metric("Avg. Price", f"${sum(x['price'] for x in products)/len(products):.2f}")
    k4.metric("Avg. Reviews", f"{sum(x['reviews'] for x in products)/len(products):,.0f}")

st.divider()
tab1, tab2, tab3, tab4 = st.tabs(["🔎 Product Research", "💰 Profit Calculator", "📊 Comparison", "⚙️ Data & API"])

with tab1:
    st.subheader(f"Opportunity results — {marketplace}")
    if products:
        df = pd.DataFrame(products).rename(columns={"title":"Product","price":"Price","reviews":"Reviews","rating":"Rating","monthly_sales":"Est. Monthly Sales","monthly_revenue":"Est. Revenue","competition":"Competition","Opportunity":"Opportunity Score"})
        display_cols = ["Product","Price","Reviews","Rating","Est. Monthly Sales","Est. Revenue","Competition","Opportunity Score"]
        st.dataframe(df[display_cols].sort_values("Opportunity Score", ascending=False), use_container_width=True, hide_index=True)
    else:
        st.warning("No products match the current filters. Try widening the price/review range.")

with tab2:
    st.subheader("FBA Profit Calculator")
    a,b,c,d,e = st.columns(5)
    price = a.number_input("Selling price ($)", 0.0, 1000.0, 29.99)
    cost = b.number_input("Product cost ($)", 0.0, 500.0, 7.00)
    shipping = c.number_input("Inbound shipping ($)", 0.0, 100.0, 2.50)
    ppc = d.number_input("PPC / unit ($)", 0.0, 100.0, 3.00)
    fulfillment = e.number_input("FBA fee ($)", 0.0, 100.0, 5.50)
    result = fba_profit(price, cost, shipping, ppc, fulfillment)
    x,y,z = st.columns(3)
    x.metric("Profit / unit", f"${result['profit']:.2f}")
    y.metric("Net margin", f"{result['margin']:.1f}%")
    z.metric("ROI on landed cost", f"{result['roi']:.1f}%")
    st.info("Use actual Amazon fee estimates before purchasing inventory.")

with tab3:
    st.subheader("Side-by-side product comparison")
    if products:
        st.dataframe(pd.DataFrame(products).sort_values("Opportunity", ascending=False), use_container_width=True, hide_index=True)
    else:
        st.info("No products available for comparison.")

with tab4:
    st.subheader("Data connection status")
    st.write("Demo dataset: ✅ Available")
    st.write("Amazon SP-API: 🔌 Integration-ready")
    st.write("Keepa API: 🔌 Integration-ready")
    st.write("AI analysis: 🔌 Integration-ready")
    st.markdown("**Environment variables:** `AMAZON_SP_CLIENT_ID`, `AMAZON_SP_CLIENT_SECRET`, `AMAZON_REFRESH_TOKEN`, `KEEPA_API_KEY`, `OPENAI_API_KEY`.")
    st.warning("Credentials are never stored in GitHub. Add them as deployment secrets/environment variables.")

st.divider()
st.caption("Amazon Product Scout — independent research software. Not affiliated with Jungle Scout or Amazon.")
