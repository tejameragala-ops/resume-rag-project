import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI PDF Chatbot", page_icon="📄")

st.title("📄 AI Resume / Document Chatbot")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    # Extract text correctly
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    # Show extracted text for debugging
    st.text(text)

    st.success("✅ PDF processed successfully!")

    query = st.text_input("Ask something about your document:")

    if query:
        query_lower = query.lower()
        lines = text.split("\n")

        answer = "No relevant information found."

        if "summary" in query_lower:
            answer = text[:700]

        elif "skills" in query_lower:
            for i, line in enumerate(lines):
                if "skill" in line.lower():
                    answer = "\n".join(lines[i:i+6])
                    break

        elif "education" in query_lower:
            for i, line in enumerate(lines):
                if "education" in line.lower():
                    answer = "\n".join(lines[i:i+6])
                    break

        elif "experience" in query_lower:
            for i, line in enumerate(lines):
                if "experience" in line.lower():
                    answer = "\n".join(lines[i:i+6])
                    break

        st.markdown("### 🤖 Answer:")
        st.write(answer)