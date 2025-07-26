# Bangla RAG System - Complete Setup Guide

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/Framework-FastAPI-green" alt="Framework">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</div>

## 🔧 Features
- Bangla PDF text extraction and processing
- Context-aware question answering with RAG
- FastAPI backend with interactive Swagger UI
- Support for conversational memory
- Integrations: Cohere, HuggingFace, Groq

---

## 💻 System Requirements
- OS: Windows/macOS/Linux
- Python 3.10+
- At least 8GB RAM
- 5GB free disk space

---

## 📦 Installation Steps

### 1️⃣ Install System Dependencies

#### 🪟 Windows (using Chocolatey)
```bash
choco install python --version=3.10
choco install tesseract
choco install poppler
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

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 🔐 3️⃣ Add API Keys

Create a `.env` file in the root folder with:

```bash
COHERE_API_KEY=your_cohere_key_here
GROQ_API_KEY=your_groq_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
```

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
[http://localhost:8000/docs](http://localhost:8000/docs) to use Swagger UI.

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

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author
Made by [Shafaq refin](https://github.com/shafaqarefin)
