from pathlib import Path
from core.LLM.getLllmModel import getLLMResponse
from core.chunking.getChunks import getChunks
from core.pdf import getPdfText
from core.preprocessing.preprocessingpipeline import PreProcessingPipeLine
from core.store.storeEmbeddings import storeEmbeddings
from core.retrieval.searchForSimilar import loadSimilarEmbeddings
from utils.helper import extract_answer


def RagPipeLine(query):
    basedir = Path(__file__).resolve().parents[1]

    chroma_dir = basedir / "chroma_store"

    if not chroma_dir.exists():
        print("[INFO] chroma_store not found. Creating knowledge base...")
        pdf_path = basedir / "data" / "HSC26-Bangla1st-Paper.pdf"
        text = getPdfText(pdf_path)
        processedText = PreProcessingPipeLine(text)
        chunkedText = getChunks(processedText)
        storeEmbeddings(chunkedText)

    print("\n[INFO] Ready for queries (type 'exit' to quit):\n\n\n")

    similarEmbeddings = loadSimilarEmbeddings(query)
    answer = getLLMResponse(similarEmbeddings, query)
    formattedAnswer = extract_answer(answer)
    print(formattedAnswer)
    return answer
