import streamlit as st

from modules.reports import (
    build_business_report
)

from modules.ai_engine import (
    ask_ai
)


st.set_page_config(
    page_title="Reports",
    layout="wide"
)

st.title("Business Reports")


report = build_business_report()


st.subheader(
    "Business Report"
)


st.text(
    report
)


st.download_button(
    "Download Report",
    report,
    file_name="bizpilot_business_report.txt",
    mime="text/plain"
)


st.divider()


st.subheader(
    "AI Executive Summary"
)


if st.button(
    "Generate Executive Summary"
):

    prompt = f"""
Create a concise executive summary
for a business owner.

Use only the following report:

{report}

Include:

- Current situation
- Important observations
- Areas to review
- Suggested next steps

Do not invent data.
"""


    with st.spinner(
        "Generating executive summary..."
    ):

        result = ask_ai(
            prompt
        )


    st.markdown(
        result
    )
