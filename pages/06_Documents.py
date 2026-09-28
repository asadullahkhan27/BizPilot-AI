import streamlit as st

from modules.documents import (
    extract_pdf_text,
    extract_text_file
)


st.set_page_config(
    page_title="Documents",
    layout="wide"
)

st.title("Document Intelligence")


uploaded_file = st.file_uploader(
    "Upload Business Document",
    type=[
        "pdf",
        "txt"
    ]
)


if uploaded_file:

    if uploaded_file.name.lower().endswith(".pdf"):

        text = extract_pdf_text(
            uploaded_file
        )

    else:

        text = extract_text_file(
            uploaded_file
        )


    st.success(
        f"Extracted {len(text):,} characters."
    )


    st.text_area(
        "Document Content",
        text,
        height=500
    )


    st.download_button(
        "Download Text",
        text,
        file_name="document_text.txt",
        mime="text/plain"
    )
