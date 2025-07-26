import re


def PreProcessingPipeLine(text: str) -> str:
    text = re.sub(r"---\s*Page\s*\d+\s*---", "", text)

    text = re.sub(r"\[\d+\]", "", text)

    text = re.sub(r"[a-zA-Z0-9:/\\|+=<>@#$%^&*(){}\[\]~`“”‘’\"\'→•]", "", text)

    text = re.sub(r"[ \t]{2,}", " ", text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
