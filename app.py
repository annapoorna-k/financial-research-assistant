from fastapi import FastAPI
from pydantic import BaseModel

from graph import graph
from langfuse_config import langfuse_handler

app = FastAPI(
    title="Financial Research Assistant",
    version="1.0.0"
)


class AnalyzeRequest(BaseModel):
    company: str


@app.get("/")
def health():

    return {
        "status": "UP"
    }


@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    response = graph.invoke(
        {
            "company": request.company
        },
        config={
            "callbacks": [langfuse_handler]
        }
    )

    return response