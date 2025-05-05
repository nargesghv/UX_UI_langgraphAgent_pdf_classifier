# 📘 LangGraph LLM Agent PDF Classifier — Project Documentation

This is a full-stack, real-time document classification system that uses LangGraph + GPT-4 to intelligently categorize business documents. It supports PDF and DOCX files, previews documents, logs history, and includes a modern UI and dashboard.

---

## 🧠 What It Does

1. A user uploads a `.pdf` or `.docx` file via the React or Streamlit interface.
2. The FastAPI backend stores the file and sends it to a LangGraph agent.
3. The agent decides how to handle it using tool-calling:
   - Convert `.docx` or extract `.pdf`
   - Analyze content with GPT-4
   - Classify the document into:
     - `filling_tax`
     - `contact_client`
     - `launching_a_company`
     - `payroll`
4. The classification is:
   - Displayed in the UI
   - Stored in a SQLite database for history

---

## 📦 Folder Structure

<PRE>
UX_UI_langgraphAgent_pdf_classifier/
├── backend/
│   ├── main.py                # FastAPI app
│   ├── routes.py              # /upload and /history endpoints
│   ├── agent_runner.py        # Agent executor wrapper
│   └── db/
│       ├── models.py          # ORM models
│       ├── crud.py            # Create/read DB records
│       └── database.py        # SQLite session setup
│
├── pipeline/
│   └── graph.py               # LangGraph + LangChain agent tools
│
├── utils/
│   └── file_watch.py          # Folder listener (optional)
│
├── frontend/
│   ├── src/
│   │   ├── App.js             # Upload + display UI
│   │   ├── api.js             # Axios API wrapper
│   │   ├── index.js           # Entry
│   │   ├── index.css          # Tailwind
│   │   └── components/
│   │       └── Preview.js     # PDF preview
│   └── tailwind.config.js
│
├── streamlit_app.py           # Fancy dashboard alternative
├── incoming/                  # Uploaded files
├── requirements.txt           # Backend deps
├── README.md
└── DOCUMENTATION.md
</PRE>

---

## 🚀 How to Run It

### Backend (FastAPI + DB)

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

> First time? Run `from backend.db.models import Base; Base.metadata.create_all(bind=engine)` in Python shell to create the database.

### Frontend (React + Tailwind)

```bash
cd frontend
npm install
npm start
```

### Streamlit Dashboard (optional)

```bash
streamlit run streamlit_app.py
```

---

## 📡 API Routes

- `POST /upload` → upload and classify file  
- `GET /history` → return full classification history

---

## ✅ Example Response

```json
{
  "filename": "contract.docx",
  "classification": "contact_client"
}
```

---

## 🔍 LLM Agent Logic

LangGraph agent uses tools:

- `convert_docx_to_text(path)`
- `extract_text_from_pdf(path)`
- `classify_text(text)`

All orchestrated via GPT-4 + LangChain's function-calling.

---

## 🧠 Classification Stored

```sql
CREATE TABLE records (
  id INTEGER PRIMARY KEY,
  filename TEXT,
  classification TEXT,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔮 Future Ideas

- User login for saved results
- File tagging and search
- Export history to CSV
- Multi-document bulk classification

---

MIT License