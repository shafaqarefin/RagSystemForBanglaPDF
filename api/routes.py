from fastapi import APIRouter
from core.pipeline import RagPipeLine, extract_answer

router = APIRouter()


@router.get("/ask")
def ask_question(query: str):
    answer = RagPipeLine(query)
    answer = extract_answer(answer)
    return {"answer": answer}
