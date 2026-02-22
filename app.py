import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="RFM Analysis Dashboard", layout="wide")

# --- 2. TRANSLATION DICTIONARY ---
translations = {
    "English": {
        "title": "📊 E-commerce Customer Segmentation",
        "subtitle": "Analyze customer value through **Recency, Frequency, and Monetary** metrics.",
        "sidebar_header": "Filter Settings",
        "filter_label": "Select Segments:",
        "metric_1": "Total Customers",
        "metric_2": "Avg. Recency",
        "metric_3": "Total Revenue",
        "chart_title": "Revenue Distribution by Segment",
        "table_header": "Customer Details",
        "download_btn": "📥 Download Selected List (CSV)",
        "days_label": "Days"
    },
    "Deutsch": {
        "title": "📊 Kundensegmentierung Dashboard",
        "subtitle": "Kundenwertanalyse basierend auf **Recency, Frequency und Monetary**.",
        "sidebar_header": "Filter-Einstellungen",
        "filter_label": "Segmente auswählen:",
        "metric_1": "Gesamtkunden",
        "metric_2": "Durchschn. Recency",
        "metric_3": "Gesamtumsatz",
        "chart_title": "Umsatzverteilung nach Segment",
        "table_header": "Kundendetails",
        "download_btn": "📥 Selektierte Liste herunterladen (CSV)",
        "days_label": "Tage"
    }
}

# --- 3. SIDEBAR LANGUAGE SELECTOR ---
st.sidebar.title("🌍 Language / Sprache")
lang_choice = st.sidebar.radio("", ["English", "Deutsch"])
txt = translations[lang_choice]

# --- 4. DATA LOADING ---
@st.cache_data
def load_data():
    try:
        return pd.read_csv("rfm_data.csv")
    except FileNotFoundError:
        return None

rfm = load_data()

# --- 5. MAIN DASHBOARD LOGIC ---
if rfm is not None:
    st.title(txt["title"])
    st.markdown(txt["subtitle"])
    st.divider()

    # --- 6. SIDEBAR FILTERS ---
    st.sidebar.divider()
    st.sidebar.header(txt["sidebar_header"])
    segments = st.sidebar.multiselect(
        txt["filter_label"], 
        options=rfm['segment'].unique(),
        default=rfm['segment'].unique()
    )

    df_selection = rfm[rfm['segment'].isin(segments)]

    # --- 7. KPIs ---
    col1, col2, col3 = st.columns(3)

    total_customers = len(df_selection)
    avg_recency = df_selection['recency'].mean() if total_customers > 0 else 0
    total_revenue = df_selection['monetary'].sum() if total_customers > 0 else 0

    col1.metric(txt["metric_1"], f"{total_customers:,}")
    col2.metric(txt["metric_2"], f"{avg_recency:.1f} {txt['days_label']}")
    col3.metric(txt["metric_3"], f"€{total_revenue:,.2f}")

    # --- 8. VISUALIZATION ---
    st.write(f"### {txt['chart_title']}")
    if not df_selection.empty:
        fig = px.pie(
            df_selection, 
            values='monetary', 
            names='segment', 
            hole=0.4,
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig, use_container_width=True)

    # --- 9. DATA DETAILS ---
    st.divider()
    st.write(f"### {txt['table_header']}")
    st.dataframe(df_selection, use_container_width=True)

    csv = df_selection.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=txt["download_btn"],
        data=csv,
        file_name='rfm_export.csv',
        mime='text/csv',
    )
else:
    st.error("❌ rfm_data.csv not found!")
