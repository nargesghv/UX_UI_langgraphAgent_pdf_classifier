from typing import TypedDict
from pathlib import Path
from langchain_core.tools import tool
from langchain.agents import tool as agent_tool
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from pypdf import PdfReader
from docx import Document

class AgentState(TypedDict):
    file_path: str
    text_content: str
    classification: str

@agent_tool
def convert_docx_to_text(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

@agent_tool
def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

@agent_tool
def classify_text(text: str) -> str:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    system_prompt = (
        "Classify the following document into one of the categories:\n"
        "- filling_tax\n"
        "- contact_client\n"
        "- launching_a_company\n"
        "- payroll\n"
        "Respond with only the category name."
    )
    message = f"{system_prompt}\n\nDocument Content:\n{text}"
    response = llm.invoke(message)
    return response.content.strip().lower()

def create_and_run_graph(file_path: str) -> AgentState:
    tools = [convert_docx_to_text, extract_text_from_pdf, classify_text]
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    agent = create_openai_functions_agent(llm, tools)
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        result = executor.invoke({"input": f"Extract text and classify this PDF file: {file_path}"})
    elif ext == ".docx":
        result = executor.invoke({"input": f"Convert and classify this DOCX file: {file_path}"})
    else:
        raise ValueError("Unsupported file format.")

    return {
        "file_path": file_path,
        "text_content": "",
        "classification": result["output"]
    }
