import streamlit as st
import pandas as pd

st.set_page_config(page_title="Amazon Product Scout", page_icon="🔎", layout="wide")

st.title("🔎 Amazon Product Scout")
st.caption("MVP — Amazon product research & opportunity analysis")

with st.sidebar:
    st.header("Filters")
    marketplace = st.selectbox("Marketplace", ["Amazon.com (US)", "Amazon.co.uk", "Amazon.ca", "Amazon.ae"])
    min_price = st.number_input("Minimum price ($)", min_value=0.0, value=15.0)
    max_price = st.number_input("Maximum price ($)", min_value=0.0, value=60.0)
    min_rating = st.slider("Minimum rating", 1.0, 5.0, 4.0, 0.1)
    max_reviews = st.number_input("Maximum reviews", min_value=0, value=500, step=50)

st.subheader("Product Research")
query = st.text_input("Search keyword or product niche", placeholder="e.g. kitchen organizer")

if st.button("Analyze Opportunity", type="primary"):
    if not query.strip():
        st.warning("Enter a keyword or niche first.")
    else:
        st.success(f"Research workspace ready for: {query}")
        st.info("Live Amazon/Keepa data connectors will be added in the next phase. The current screen is the functional MVP interface.")

        metrics = st.columns(4)
        metrics[0].metric("Opportunity Score", "—")
        metrics[1].metric("Est. Monthly Sales", "—")
        metrics[2].metric("Competition", "—")
        metrics[3].metric("Est. Profit", "—")

st.divider()
st.subheader("FBA Profit Calculator")
col1, col2, col3, col4 = st.columns(4)
price = col1.number_input("Selling price ($)", min_value=0.0, value=29.99)
cost = col2.number_input("Product cost ($)", min_value=0.0, value=7.0)
shipping = col3.number_input("Shipping to Amazon ($)", min_value=0.0, value=2.5)
ads = col4.number_input("PPC / unit ($)", min_value=0.0, value=3.0)

amazon_fee = price * 0.15
profit = price - cost - shipping - amazon_fee - ads
margin = (profit / price * 100) if price else 0

c1, c2 = st.columns(2)
c1.metric("Estimated profit / unit", f"${profit:.2f}")
c2.metric("Estimated margin", f"{margin:.1f}%")

st.divider()
st.subheader("Product Comparison")
data = pd.DataFrame([
    {"Product": "Sample A", "Price": 24.99, "Reviews": 186, "Rating": 4.4, "Competition": "Medium"},
    {"Product": "Sample B", "Price": 31.99, "Reviews": 92, "Rating": 4.5, "Competition": "Low"},
    {"Product": "Sample C", "Price": 19.99, "Reviews": 421, "Rating": 4.3, "Competition": "High"},
])
st.dataframe(data, use_container_width=True, hide_index=True)

st.caption("Note: Sample values are placeholders. Do not use them as live Amazon market data.")
