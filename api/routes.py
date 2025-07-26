from fastapi import APIRouter
from core.pipeline import RagPipeLine

router = APIRouter()


@router.get("/ask")
def ask_question(query: str):
    answer = RagPipeLine(query)
    return {"answer": answer}
