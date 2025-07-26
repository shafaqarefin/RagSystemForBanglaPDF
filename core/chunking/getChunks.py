from langchain.text_splitter import RecursiveCharacterTextSplitter


def getChunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=350,  # chunk size increases information each chunk contains
        chunk_overlap=50,  # overlap decreases sentence info but increases context
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", "।", "|"]
    )
    return splitter.split_text(text)
