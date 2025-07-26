# Bangla RAG System with FastAPI

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Retrieval-Augmented Generation system for processing Bangla PDF documents with contextual question answering capabilities.

## ✨ Features

- **Bangla Language Support**: Optimized for Bangla text processing
- **PDF Processing**: Extract and analyze text from Bangla PDFs
- **Conversational AI**: Maintains chat history for contextual responses
- **Modern Tech Stack**: 
  - FastAPI backend
  - Groq LLM integration
  - ChromaDB vector storage
  - HuggingFace embeddings

## 🛠️ Installation

### Prerequisites

- Python 3.10 or later
- Tesseract OCR (for Bangla text recognition)
- API keys for:
  - Cohere
  - Groq
  - HuggingFace Hub

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shafaqarefin/RagSystemForBanglaPDF.git
   cd RagSystemForBanglaPDF

   python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
