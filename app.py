import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI PDF Chatbot", page_icon="📄")

st.title("📄 AI Resume / Document Chatbot")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    st.success("✅ PDF processed successfully!")

    query = st.text_input("Ask something about your document:")

    if query:
        lines = text.split("\n")
        answer = "No relevant information found."

        for i, line in enumerate(lines):
            if query.lower() in line.lower():
                answer = "\n".join(lines[i:i+6])
                break

        st.markdown("### 🤖 Answer:")
        st.write(answer)