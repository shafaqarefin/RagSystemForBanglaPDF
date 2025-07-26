from dotenv import load_dotenv
import requests
import os
from langchain_huggingface import HuggingFaceEndpointEmbeddings

load_dotenv()
huggingfacehub_api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')


def getEmbeddingModel():
    model = "intfloat/multilingual-e5-large"

    embeddingModel = HuggingFaceEndpointEmbeddings(
        model=model,
        task="feature-extraction",
        huggingfacehub_api_token=huggingfacehub_api_token,
    )

    return embeddingModel
