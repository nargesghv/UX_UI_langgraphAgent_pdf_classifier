# LangGraph PDF Classifier (Agent-Based)

This project is a full-stack application that allows users to upload `.pdf` or `.docx` files, which are then classified into one of the following categories using an LLM (OpenAI GPT-4):

- `filling_tax`
- `contact_client`
- `launching_a_company`
- `payroll`

It uses LangGraph for tool-based agent orchestration, FastAPI for backend processing, and React + Tailwind for the user interface.

---

## 🧱 Tech Stack

| Component     | Tool                                   |
|--------------|----------------------------------------|
| **Frontend**  | React + Tailwind CSS                  |
| **Backend**   | FastAPI                               |
| **Agent**     | LangGraph + LangChain + OpenAI GPT    |
| **Storage**   | Local file system (`incoming/`)       |

---

## 📁 Project Structure

```
langgraph_pdf_classifier/
├── backend/
│   ├── main.py              # FastAPI server
│   ├── routes.py            # /upload endpoint
│   └── agent_runner.py      # Agent wrapper
├── pipeline/
│   └── graph.py             # LangGraph agent with tool calling
├── utils/
│   └── file_watch.py        # Real-time file monitor
├── frontend/
│   └── ...                  # React frontend for uploading files
├── incoming/                # Folder where uploaded files are stored
├── requirements.txt         # Backend dependencies
└── README.md                # This file
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

> Make sure your FastAPI backend is running on `http://localhost:8000`

---

## 🧠 Agent Behavior

The backend sends uploaded files to an LLM agent built with LangGraph. The agent:
- Uses tools to extract text from PDF or DOCX
- Uses GPT-4 to classify the content
- Returns a category name only

---

## 📦 Sample Output

```
Watching for files in 'incoming/' directory...
File: invoice.docx classified as: payroll
```

---

## 📄 License

MIT License