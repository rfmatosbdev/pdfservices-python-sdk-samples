import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    text = ''
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    pdf_file.close()
    return text

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    cleaned_text = ' '.join(cleaned_tokens)
    return cleaned_text

pdf_path = f'/Users/rmatos@fortifi.com/Downloads/bdev/adobeapi/pdfservices-python-sdk-samples/resources/extractPdfInput.pdf'
extracted_text = extract_text_from_pdf(pdf_path)
# preprocessed_text = preprocess_text(extracted_text)

df = pd.read_csv(extracted_text, sep='\t', encoding='utf-8')
df.to_csv('pdfservices-python-sdk-samples/output/x.csv')