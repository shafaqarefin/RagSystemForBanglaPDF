import re


def extract_answer(text):
    match = re.search(r"</think>\s*(?:[Aa]nswer:\s*)?(.*)", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return "Ase kintu ai bal detect korte pare na"
