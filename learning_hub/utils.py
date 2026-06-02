from pypdf import PdfReader


def extract_pdf_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text



def chunk_text(
    text,
    chunk_size=1000
):

    chunks = []

    for i in range(
        0,
        len(text),
        chunk_size
    ):

        chunks.append(
            text[i:i+chunk_size]
        )

    return chunks