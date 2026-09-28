import streamlit as st

from datetime import date

from modules.finance import (
    add_finance_record,
    get_transactions,
    get_financial_summary
)

from utils.calculations import (
    calculate_profit_margin
)


st.set_page_config(
    page_title="Finance",
    layout="wide"
)

st.title("Finance Management")


with st.form("finance_form"):

    kind = st.selectbox(
        "Transaction Type",
        [
            "Revenue",
            "Expense"
        ]
    )

    category = st.text_input(
        "Category",
        placeholder="Sales, Salary, Marketing..."
    )

    amount = st.number_input(
        "Amount (PKR)",
        min_value=0.0,
        step=100.0
    )

    description = st.text_input(
        "Description"
    )

    transaction_date = st.date_input(
        "Date",
        value=date.today()
    )

    submit = st.form_submit_button(
        "Add Transaction"
    )


if submit:

    if not category.strip():

        st.error(
            "Category is required."
        )

    elif amount <= 0:

        st.error(
            "Amount must be greater than zero."
        )

    else:

        add_finance_record(
            kind,
            category,
            amount,
            description,
            transaction_date.isoformat()
        )

        st.success(
            "Transaction added successfully."
        )

        st.rerun()


summary = get_financial_summary()


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Revenue",
    f"Rs. {summary['revenue']:,.0f}"
)

col2.metric(
    "Expenses",
    f"Rs. {summary['expenses']:,.0f}"
)

col3.metric(
    "Profit",
    f"Rs. {summary['profit']:,.0f}"
)

col4.metric(
    "Profit Margin",
    f"{calculate_profit_margin(summary['revenue'], summary['expenses']):.1f}%"
)


st.divider()

st.subheader("Transactions")

df = get_transactions()

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
