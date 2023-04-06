from fastapi import FastAPI, HTTPException
from app.document import Document, CreateDocumentModule


documents: list[Document] = [
#    Document(0, 'First doc', 'Content'),
#    Document(1, 'Second doc', 'Long, long, long, long, long, long, long, long, long, long, long, long, long text')
]

def add_document(content: CreateDocumentModule):
    id = len(documents)
    documents.append(Document(id, content.title, content.body))
    return id

app = FastAPI()

@app.get("/v1/docs")
async def get_docs():
    return documents

@app.post("/v1/docs")
async def add_doc(content: CreateDocumentModule):
    add_document(content)
    return documents[-1]

@app.get("/v1/docs/{id}")
async def get_docs_by_id(id: int):
    result = [item for item in documents if item.id == id]
    if len(result) > 0:
        return result[0]
    
    raise HTTPException(status_code=404, detail="Document not found")

@app.get("/__health")
async def check_service():
    return