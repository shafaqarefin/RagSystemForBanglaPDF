# Bangla RAG System - Complete Setup Guide

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/Framework-FastAPI-green" alt="Framework">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</div>

## 🔧 Features
- Bangla PDF text extraction and processing
- Context-aware question answering with RAG using Langchain Buffer Memory
- FastAPI backend
- Integrations: Cohere reranker, HuggingFace embedding, Groq LLM
- Langchain ChromaDB to store embeddings

---

## 💻 System Requirements
- OS: Windows/macOS/Linux
- Python 3.10+
- Tesseract Bangla Support and Poppler

## 📦 Installation Steps

### 1️⃣ Install System Dependencies

#### 🪟 Windows 
install python --version=3.10 following documentation
install tesseract 
- Tesseract OCR tool with Bangla language support  
  👉 [Download Tesseract](tesseract-ocr-w64-setup-5.5.0.20241111.exe)  for 64 bit system or find appropriate version here (https://digi.bib.uni-mannheim.de/tesseract)
  After installing, For Bangla language capabiliteis  make sure to select bengali language in language script and language data option during installation.
  <img width="638" height="221" alt="image" src="https://github.com/user-attachments/assets/a415ddeb-be7f-481e-965c-4108abb51e94" />
  <img width="520" height="28" alt="image" src="https://github.com/user-attachments/assets/3780c01e-4a50-41b3-9f20-6295dac6a252" />
  Select Bengali 
---

### After that run in Command Prompt with Admin Privillege 
```bash
bangla-pdf-ocr-setup

```
Verify with this command
```bash
bangla-pdf-ocr-verify

```



#### 🍎 macOS (using Homebrew)
```bash
brew install python@3.10
brew install tesseract tesseract-lang
brew install poppler
```

#### 🐧 Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.10 python3.10-venv
sudo apt install tesseract-ocr tesseract-ocr-ben
sudo apt install poppler-utils
```

---

### 2️⃣ Set Up Python Environment

```bash
# Clone the repository
git clone https://github.com/shafaqarefin/RagSystemForBanglaPDF.git
cd RagSystemForBanglaPDF

# Create and activate virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

# Upgrade pip and install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

rename  `.env.example` file in the root directory to .env and add the following keys:

```env
COHERE_API_KEY=your_cohere_key_here 
GROQ_API_KEY=your_groq_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
```

You can get the keys from:

- 🔗 [Cohere API Key](https://dashboard.cohere.com/api-keys)
- 🔗 [Groq API Key](https://console.groq.com/keys)
- 🔗 [Hugging Face API Token](https://huggingface.co/settings/tokens)


---

## 🚀 Running the Project

### ▶️ Run CLI Tool
```bash
python cli.py
```

### 🖥️ Run FastAPI Server
```bash
uvicorn main:app --reload
```

### 🔎 Test the API
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question":"বাংলাদেশের স্বাধীনতা কবে?"}'
```

You can also open your browser at:  
[http://localhost:8000/docs](http://localhost:8000/docs) 

---

## 🧯 Troubleshooting

### ❌ OCR Issues
```bash
tesseract --list-langs
```
Ensure `ben` (Bangla) is listed.

### ❌ Python Errors
```bash
pip install --force-reinstall -r requirements.txt
```

### ❌ API Connection Problems
- Make sure API keys are valid and not expired
- Check firewall or network restrictions
- Confirm external API services are up

### Question and Answer
What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?



## 👨‍💻 Author
Made by [Shafaq Arefin Chowdhury](https://github.com/shafaqarefin)
