from core.embeddings.embedText import getEmbeddingModel
from langchain_chroma import Chroma


def storeEmbeddings(chunks):
    embedding_model = getEmbeddingModel()
    persist_dir = "chroma_store"

    prefixed_chunks = ["passage: " + chunk for chunk in chunks]

    metadatas = [{"chunk_id": i} for i in range(len(chunks))]

    db = Chroma.from_texts(
        texts=prefixed_chunks,
        embedding=embedding_model,
        metadatas=metadatas,
        persist_directory=persist_dir
    )

    print("Embeddings with metadata stored.")
