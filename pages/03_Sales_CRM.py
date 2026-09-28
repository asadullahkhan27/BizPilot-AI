import streamlit as st

from modules.sales import (
    add_sales_lead,
    get_leads
)


st.set_page_config(
    page_title="Sales CRM",
    layout="wide"
)

st.title("Sales CRM")


with st.form("lead_form"):

    customer = st.text_input(
        "Customer Name"
    )

    company = st.text_input(
        "Company"
    )

    value = st.number_input(
        "Deal Value (PKR)",
        min_value=0.0,
        step=1000.0
    )

    status = st.selectbox(
        "Status",
        [
            "New",
            "Contacted",
            "Qualified",
            "Proposal",
            "Negotiation",
            "Won",
            "Lost"
        ]
    )

    followup = st.date_input(
        "Next Follow-up"
    )

    notes = st.text_area(
        "Notes"
    )

    submit = st.form_submit_button(
        "Add Lead"
    )


if submit:

    if not customer.strip():

        st.error(
            "Customer name is required."
        )

    else:

        add_sales_lead(
            customer,
            company,
            value,
            status,
            followup.isoformat(),
            notes
        )

        st.success(
            "Lead added successfully."
        )

        st.rerun()


df = get_leads()


if df.empty:

    st.info(
        "No sales leads yet."
    )

else:

    st.metric(
        "Total Pipeline",
        f"Rs. {df['value'].sum():,.0f}"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
