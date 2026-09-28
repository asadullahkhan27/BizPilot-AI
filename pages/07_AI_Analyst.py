import streamlit as st

from modules.ai_engine import ask_ai

from modules.finance import (
    get_transactions,
    get_financial_summary
)

from modules.sales import get_leads
from modules.inventory import get_inventory
from modules.employees import get_employees


st.set_page_config(
    page_title="AI Business Analyst",
    layout="wide"
)

st.title("AI Business Analyst")

st.write(
    "Ask questions about the business data stored in BizPilot AI."
)


question = st.text_area(
    "Your Business Question",
    placeholder=(
        "Example: Analyze my expenses and "
        "tell me which areas need review."
    ),
    height=150
)


if st.button(
    "Analyze Business",
    type="primary"
):

    if not question.strip():

        st.warning(
            "Please enter a business question."
        )

    else:

        financial_summary = (
            get_financial_summary()
        )

        transactions = (
            get_transactions()
            .head(50)
            .to_dict(
                orient="records"
            )
        )

        leads = (
            get_leads()
            .head(50)
            .to_dict(
                orient="records"
            )
        )

        inventory = (
            get_inventory()
            .head(50)
            .to_dict(
                orient="records"
            )
        )

        employees = (
            get_employees()
            .head(50)
            .to_dict(
                orient="records"
            )
        )


        prompt = f"""
Business Question:

{question}


FINANCIAL SUMMARY:

{financial_summary}


TRANSACTIONS:

{transactions}


SALES LEADS:

{leads}


INVENTORY:

{inventory}


EMPLOYEES:

{employees}


Analyze the supplied business data.

Give:

1. Key observations
2. Important trends
3. Areas that deserve review
4. Practical next steps

Do not invent information.
Clearly identify assumptions.
"""


        with st.spinner(
            "Analyzing business data..."
        ):

            result = ask_ai(
                prompt
            )


        st.subheader(
            "AI Analysis"
        )

        st.markdown(
            result
        )
