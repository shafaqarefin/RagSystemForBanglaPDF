from langchain_chroma import Chroma

from core.embeddings.embedText import getEmbeddingModel
from core.retrieval.cohereRank import getCohereRank


def loadSimilarEmbeddings(query, k=3):
    embedding_model = getEmbeddingModel()
    persist_dir = "chroma_store"

    db = Chroma(
        persist_directory=persist_dir,
        embedding_function=embedding_model
    )

    query_embedding = embedding_model.embed_query("query: " + query)

    initial_results = db.similarity_search_by_vector(query_embedding, k=10)

    reranked_results = getCohereRank(query, initial_results, top_k=k)

    return reranked_results
