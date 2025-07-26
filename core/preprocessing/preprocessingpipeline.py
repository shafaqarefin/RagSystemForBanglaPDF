import re


import re


def PreProcessingPipeLine(text: str) -> str:
    # Remove page numbers like --- Page 30 ---
    text = re.sub(r"---\s*Page\s*\d+\s*---", "", text)

    # Remove bracketed IDs like [15026]
    text = re.sub(r"\[\d+\]", "", text)

    # Remove garbage alphanumeric blends (like '১1/1481া6' or OCR noise)
    text = re.sub(r"[a-zA-Z0-9:/\\|+=<>@#$%^&*(){}\[\]~`“”‘’\"\'→•]", "", text)

    # Fix extra spaces
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Preserve MCQ option formatting: (ক) (খ) (গ) (ঘ)
    # No change needed here as we’re not removing Bangla chars or parentheses.

    # Normalize line breaks
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


PreProcessingPipeLine
