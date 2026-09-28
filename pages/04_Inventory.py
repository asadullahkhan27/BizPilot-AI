import streamlit as st

from modules.inventory import (
    add_inventory_item,
    get_inventory,
    get_inventory_summary
)


st.set_page_config(
    page_title="Inventory",
    layout="wide"
)

st.title("Inventory Management")


with st.form("inventory_form"):

    product = st.text_input(
        "Product"
    )

    sku = st.text_input(
        "SKU"
    )

    quantity = st.number_input(
        "Quantity",
        min_value=0,
        step=1
    )

    reorder_level = st.number_input(
        "Reorder Level",
        min_value=0,
        value=5,
        step=1
    )

    unit_price = st.number_input(
        "Unit Price (PKR)",
        min_value=0.0,
        step=100.0
    )

    submit = st.form_submit_button(
        "Add Product"
    )


if submit:

    if not product.strip():

        st.error(
            "Product name is required."
        )

    else:

        add_inventory_item(
            product,
            sku,
            quantity,
            reorder_level,
            unit_price
        )

        st.success(
            "Inventory item added."
        )

        st.rerun()


summary = get_inventory_summary()


col1, col2, col3 = st.columns(3)


col1.metric(
    "Products",
    summary["items"]
)

col2.metric(
    "Low Stock",
    summary["low_stock"]
)

col3.metric(
    "Stock Value",
    f"Rs. {summary['stock_value']:,.0f}"
)


df = get_inventory()


if not df.empty:

    df["Status"] = df.apply(
        lambda row:
        "LOW STOCK"
        if row["quantity"] <= row["reorder_level"]
        else "OK",
        axis=1
    )


st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
