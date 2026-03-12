from transformers import pipeline



Sumarizer = pipeline('summarization', model="knkarthick/MEETING_SUMMARY")

def summary_pdf(chunks):
    summary_result = []
    for  chunk in chunks:
        summary = Sumarizer(chunk)
        summary_result.append(summary[0]["summary_text"])
    return " ".join(summary_result)



