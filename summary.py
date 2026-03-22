
from google import genai
from google.genai import types

client = genai.Client(api_key="")


# summarization


def summary_pdf(uploaded_pdf):
    prompt = "Summarize this document clearly and briefly."

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            types.Part.from_bytes(
                data=uploaded_pdf.read(),
                mime_type="application/pdf",
            ),
            prompt,
        ],
    )

    return response.text
    
        

def ask_question(question, uploaded_pdf):
    prompt = f"""
Answer the question based only on the context below.
If the answer is not in the context, say: Not found.


Question:
{question}
"""

    response = client.models.generate_content(model="gemini-3-flash-preview",
        contents=[
            types.Part.from_bytes(
                data=uploaded_pdf.read(),
                mime_type="application/pdf",
            ),
            prompt,],)
    return response.text



