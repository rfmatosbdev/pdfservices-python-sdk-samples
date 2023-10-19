import scipdf
import fitz
from PyPDF2 import PdfReader
import os

os.system('clear')

pdf_path = f'pdfservices-python-sdk-samples/resources/extractPdfInput.pdf'

def parse_pdf_structure(pdf_path):
    return scipdf.parse_pdf_to_dict(pdf_path, as_list=False, return_coordinates=False)


def parse_pdf_pages(pdf_path):
    return fitz.open(pdf_path)


def parse_pdf_pages2(pdf_path):
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    return reader.pages


def parse_pdf_first_page_ranges(pdf_pages):
    global first
    page_labels = pdf_pages.get_page_labels()
    if len(page_labels) > 0:
        first = list(filter(lambda x: 'style' in x and x['style'] == 'D', page_labels))
        return first[0]['startpage'] if len(first) > 0 else int(0)
    else:
        return 0;


pdf_structure = parse_pdf_structure(pdf_path)
pdf_pages = parse_pdf_pages(pdf_path)
pdf_pages2 = parse_pdf_pages2(pdf_path)

