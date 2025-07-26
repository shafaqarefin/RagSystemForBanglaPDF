PDF RAG SYSTEM BY SHAFAQ AREFN CHOWHDHURY

# Bangla RAG FastAPI Application

A Retrieval-Augmented Generation (RAG) system designed for Bangla language, built using FastAPI, LangChain, Cohere,HuggingFace Embeddings,ChromaDB and Groq LLM.  
It extracts answers from a Bangla textbook PDF corpus with contextual chat history support.


## Requirements

- Python 3.10 or higher
- API Tokenss: Cohere, Groq,HuggingFaceHub
- Packages listed in `requirements.txt`


---

## Installation

### 1. Clone the repository

Open VsCode and run:

```bash
git clone https://github.com/shafaqarefin/RagSystemForBanglaPDF.git in the terminal
```
2.Install all requirments using:
  pip install -r requirements.txt

3.Run python -m venv venv

4. In the env.local.example file create API tokens or keys free of cost and place into respective placeholders or uncomment the tokens there

5.run the command
 ```bash
 bangla-ocr-setup in command prompt of windows with administrative privillege

 if tesseract is not present kindly install from

 tesseract-ocr-w64-setup-5.5.0.20241111.exe by going to this link or  and follow the steps for installation

 after successfull installation of tesseract please navigate to the folder if not already opened in vscode terminal and run

python cli.py for command line interface interaction with RAG system





