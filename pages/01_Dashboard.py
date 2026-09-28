import streamlit as st

from modules.finance import get_financial_summary
from modules.sales import get_sales_summary
from modules.inventory import get_inventory_summary
from modules.employees import get_employee_summary


st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("Business Dashboard")


finance = get_financial_summary()
sales = get_sales_summary()
inventory = get_inventory_summary()
employees = get_employee_summary()


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Revenue",
    f"Rs. {finance['revenue']:,.0f}"
)

col2.metric(
    "Expenses",
    f"Rs. {finance['expenses']:,.0f}"
)

col3.metric(
    "Profit",
    f"Rs. {finance['profit']:,.0f}"
)

col4.metric(
    "Pipeline",
    f"Rs. {sales['pipeline']:,.0f}"
)


st.divider()


col1, col2, col3 = st.columns(3)


col1.metric(
    "Sales Leads",
    sales["count"]
)

col2.metric(
    "Inventory Items",
    inventory["items"]
)

col3.metric(
    "Employees",
    employees["count"]
)


if inventory["low_stock"]:

    st.warning(
        f"{inventory['low_stock']} inventory item(s) "
        "need stock review."
    )
