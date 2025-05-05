import streamlit as st
import requests
import os
from pypdf import PdfReader

# App title
st.set_page_config(page_title="📄 LangGraph AI Document Classifier", layout="centered")

st.markdown("""
# 📄 LangGraph AI Document Classifier
Upload a **PDF or DOCX** file to classify it using an LLM agent.
""")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])

# File preview (PDF only)
if uploaded_file and uploaded_file.type == "application/pdf":
    st.markdown("### 📑 Preview (first page only)")
    pdf_reader = PdfReader(uploaded_file)
    first_page = pdf_reader.pages[0].extract_text()
    st.code(first_page[:1000] + "..." if first_page else "Unable to extract text", language="text")

# Submit and classify
if uploaded_file and st.button("🔍 Classify Document"):
    with st.spinner("Classifying..."):
        res = requests.post("http://localhost:8000/upload", files={"file": uploaded_file})
        if res.status_code == 200:
            classification = res.json().get("classification", "unknown")
            st.success(f"✅ Classification Result: `{classification}`")
        else:
            st.error("❌ Classification failed.")

# History panel
st.markdown("### 🕘 Previous Classifications")
try:
    hist_res = requests.get("http://localhost:8000/history")
    if hist_res.ok:
        history = hist_res.json()
        if not history:
            st.info("No history found yet.")
        else:
            for entry in history:
                st.markdown(f"- **{entry['filename']}** → `{entry['classification']}` *(at {entry['timestamp']})*")
    else:
        st.warning("Could not load history.")
except:
    st.warning("History feature unavailable. Is the backend running?")
