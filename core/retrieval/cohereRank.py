import os
import cohere


def getCohereRank(query, documents, top_k=3):

    passages = [doc.page_content for doc in documents]

    co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY")
                         )

    response = co.rerank(
        model="rerank-multilingual-v3.5",
        query=query,
        documents=passages,
        top_n=top_k,
    )

    # Rank returned by Cohere with indices
    reranked = [documents[r.index] for r in response.results]
    return reranked
