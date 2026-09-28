from pypdf import PdfReader


def extract_pdf_text(uploaded_file):

    reader = PdfReader(uploaded_file)

    pages = []

    for page in reader.pages:

        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def extract_text_file(uploaded_file):

    return uploaded_file.read().decode(
        "utf-8",
        errors="ignore"
    )
