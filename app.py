import streamlit as st
from summary import summary_pdf
from summary import ask_question

st.title("PDF Sumarization")

uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")
ask_me = st.chat_input("Ask Me")

if uploaded_pdf is not None:
        if st.button('Summarization'):
            with st.spinner("Processing PDF..."):
                  results = summary_pdf(uploaded_pdf)
                  st.write(results)

if ask_me is not None:
        st.write(uploaded_pdf)
        answer = ask_question(ask_me, uploaded_pdf)
        st.write(answer)
