import fitz


def extract_text(pdf_path):

    pdf = fitz.open(pdf_path)

    text = ""

    print(f"Pages Found: {len(pdf)}")

    for page_num in range(len(pdf)):

        page = pdf[page_num]

        page_text = page.get_text()

        print(
            f"Page {page_num+1} Characters:",
            len(page_text)
        )

        text += page_text

    return text