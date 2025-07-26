# Bangla RAG System - Complete Setup Guide

## System Requirements
- Windows/macOS/Linux
- Python 3.10+
- Minimum 8GB RAM
- 5GB free disk space

## Complete Installation

1. First install these system packages:

**Windows:**
choco install python --version=3.10
choco install tesseract
choco install poppler

text

**macOS:**
brew install python@3.10
brew install tesseract tesseract-lang
brew install poppler

text

**Linux (Ubuntu/Debian):**
sudo apt update
sudo apt install python3.10 python3.10-venv
sudo apt install tesseract-ocr tesseract-ocr-ben
sudo apt install poppler-utils

text

2. Setup Python environment:
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # macOS/Linux
pip install --upgrade pip
pip install -r requirements.txt

text

## API Key Configuration
Create a `.env` file with these keys (get them from respective providers):
COHERE_API_KEY=your_cohere_key_here
GROQ_API_KEY=your_groq_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here

text

## Running the System

1. For command line interface:
python cli.py

text

2. For API server:
uvicorn main:app --reload

text

3. To test the API:
curl -X POST "http://localhost:8000/query" -H "Content-Type: application/json" -d '{"question":"Your question here"}'

text

## Troubleshooting

**OCR Issues:**
tesseract --list-langs # Verify Bangla is installed

text

**Python Errors:**
pip install --force-reinstall -r requirements.txt

text

**API Connection Problems:**
- Verify your API keys
- Check service status pages
- Ensure no firewall blocking
