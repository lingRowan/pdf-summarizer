
# importing
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text =''
# read uploaded file
# text preprocessing 
# sentences to chunks

def extract_and_chunk(uploaded_pdf):
    text =''
    pdf = PdfReader(uploaded_pdf)
    for page in pdf.pages:
        text += page.extract_text()
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=250,
            chunk_overlap=50,
            length_function=len,
            strip_whitespace=True)
        chunks = splitter.split_text(text)

        return chunks
