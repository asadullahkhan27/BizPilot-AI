import streamlit as st

from database.database import init_db
from modules.finance import get_financial_summary
from modules.sales import get_sales_summary
from modules.inventory import get_inventory_summary
from modules.employees import get_employee_summary

st.set_page_config(
    page_title="BizPilot AI",
    page_icon="BP",
    layout="wide",
    initial_sidebar_state="expanded"
)

init_db()

st.title("BizPilot AI")
st.caption("AI-powered business operations platform")

st.markdown("""
## Business Command Center

Manage your business finance, sales, inventory, employees,
documents and AI-powered business analysis from one platform.
""")

finance = get_financial_summary()
sales = get_sales_summary()
inventory = get_inventory_summary()
employees = get_employee_summary()

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Revenue",
        f"Rs. {finance['revenue']:,.0f}"
    )

with col2:
    st.metric(
        "Expenses",
        f"Rs. {finance['expenses']:,.0f}"
    )

with col3:
    st.metric(
        "Profit",
        f"Rs. {finance['profit']:,.0f}"
    )

with col4:
    st.metric(
        "Employees",
        employees["count"]
    )

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Sales Leads",
        sales["count"]
    )

with col2:
    st.metric(
        "Pipeline",
        f"Rs. {sales['pipeline']:,.0f}"
    )

with col3:
    st.metric(
        "Low Stock",
        inventory["low_stock"]
    )

if inventory["low_stock"] > 0:
    st.warning(
        f"{inventory['low_stock']} inventory item(s) "
        "are below their reorder level."
    )

st.divider()

st.info(
    "Use the sidebar to open Dashboard, Finance, Sales CRM, "
    "Inventory, Employees, Documents, AI Analyst and Reports."
)
