import streamlit as st
from pdf_utils import extract_and_chunk
from summary import summary_pdf

st.title("PDF Sumarization")

uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_pdf is not None:
    if st.button("Sumarization"):
        with st.spinner("Processing PDF..."):
            chunks = extract_and_chunk(uploaded_pdf)
            results = summary_pdf(chunks)

            st.write(results)
