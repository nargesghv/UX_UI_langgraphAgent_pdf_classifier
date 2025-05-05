from pipeline.graph import create_and_run_graph

def classify_document(file_path: str) -> str:
    result = create_and_run_graph(file_path)
    return result["classification"]
