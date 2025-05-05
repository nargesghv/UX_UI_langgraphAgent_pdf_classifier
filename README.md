# LangGraph PDF Classifier (Full-Stack + Agent-Based)

This project is a full-stack AI application that lets users upload `.pdf` or `.docx` files and classify them into categories using a LangGraph agent powered by OpenAI GPT. The system includes a React frontend, a FastAPI backend, a LangGraph agent pipeline, PDF preview, and a history-saving database. An optional Streamlit dashboard is available for quick testing.

---

## 🧱 Tech Stack

| Component     | Tool                                   |
|--------------|----------------------------------------|
| **Frontend**  | React + Tailwind CSS                  |
| **Backend**   | FastAPI                               |
| **Agent**     | LangGraph + LangChain + OpenAI GPT    |
| **Database**  | SQLite + SQLAlchemy                   |
| **Dashboard** | Optional: Streamlit                   |

---

## 🧠 Features

- Upload `.pdf` or `.docx` documents
- Auto classification using GPT-4 via LangGraph agent
- Preview uploaded PDFs
- Save classification history to SQLite
- Optionally use a Streamlit dashboard

---

## 📁 Project Structure

```
UX_UI_langgraphAgent_pdf_classifier/
├── backend/
│   ├── main.py              # FastAPI app entry
│   ├── routes.py            # /upload route
│   ├── agent_runner.py      # LangGraph agent wrapper
│   └── db/
│       ├── models.py        # SQLAlchemy ORM models
│       ├── crud.py          # Create/read database records
│       └── database.py      # DB engine + session factory
│
├── pipeline/
│   └── graph.py             # LangGraph agent and tools
│
├── utils/
│   └── file_watch.py        # Local folder watcher (optional)
│
├── frontend/
│   ├── src/
│   │   ├── App.js           # Upload + preview UI
│   │   ├── api.js           # Axios API helper
│   │   ├── index.js         # React entry point
│   │   ├── index.css        # Tailwind styles
│   │   └── components/
│   │       └── Preview.js   # PDF preview using react-pdf
│   └── tailwind.config.js   # Tailwind config
│
├── streamlit_app.py         # Python UI for quick testing
├── incoming/                # Folder to store uploaded files
├── requirements.txt         # Backend dependencies
├── README.md                # Project overview
└── DOCUMENTATION.md         # Technical documentation
```

---

## 🚀 How to Run

### 1. Backend (FastAPI)

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

### 2. Frontend (React)

```bash
cd frontend
npm install
npm start
```

### 3. Optional: Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Sample Output

```json
{
  "filename": "report.docx",
  "classification": "contact_client"
}
```

## 📄 License

MIT License