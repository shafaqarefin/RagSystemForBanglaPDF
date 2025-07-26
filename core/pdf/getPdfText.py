from bangla_pdf_ocr import process_pdf


def getPdfText(path):
    text = process_pdf(path)
    return text
