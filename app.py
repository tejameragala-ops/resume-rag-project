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
            text += content

    st.success("✅ PDF processed successfully!")

    query = st.text_input("Ask something about your document:")

    if query:
        query_lower = query.lower()

        if "summary" in query_lower:
            answer = text[:700]

        elif "skills" in query_lower:
            lines = text.split("\n")
            skills = [line for line in lines if "skill" in line.lower()]
            answer = "\n".join(skills[:5]) if skills else text[:500]

        elif "education" in query_lower:
            lines = text.split("\n")
            edu = [line for line in lines if "education" in line.lower()]
            answer = "\n".join(edu[:5]) if edu else text[:500]

        else:
            answer = text[:500]

        st.markdown("### 🤖 Answer:")
        st.write(answer)