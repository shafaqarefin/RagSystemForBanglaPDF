from PyPDF2 import PdfReader


def getPdfText(pdfDocs):
    text = ""

    for pdfDoc in pdfDocs:
        pdf_reader = PdfReader(pdfDoc)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
