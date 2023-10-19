import json
import requests

# The name of a document type in Sensible, e.g., auto_insurance_quote
DOCUMENT_TYPE = "structured_book"
# The path to the PDF you'd like to extract from
# If the PDF is over ~4.5MB use an async example script in this repo instead
DOCUMENT_PATH = "pdfservices-python-sdk-samples/resources/extractPdfInput.pdf"
# Your Sensible API key
API_KEY = "bece0490d55c3b7c53470d187136cccb44492737a795c66566cbc6d3be4207971b95eaea2b1a50f6a770cd27faed46c8a8484f33584962cf245a288f868394db"


def extract_doc():
    headers = {
        'Authorization': 'Bearer {}'.format(API_KEY),
        'Content-Type': 'application/pdf'
    }
    with open(DOCUMENT_PATH, 'rb') as pdf_file:
        body = pdf_file.read()
    response = requests.request(
        "POST",
        "https://api.sensible.so/v0/extract/{}".format(DOCUMENT_TYPE),
        headers=headers,
        data=body)
    try:
        response.raise_for_status()
    except requests.RequestException:
        print(response.text)
    else:
        print(json.dumps(response.json(), indent=2))


if __name__ == '__main__':
    extract_doc()