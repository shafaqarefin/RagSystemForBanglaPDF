import streamlit as st

from core.pdf.getPdfText import getPdfText
from core.chunking.getChunks import getChunks


def mainUI():
    st.set_page_config(
        page_title='Chat with my bangla pdf chatbot', page_icon='books:')
    st.header('Chat with mutiple  pdfs')
    st.text_input("Ask a queston about your document")

    with st.sidebar:
        st.subheader("Your document")
        docs = st.file_uploader('Upload you pdf', accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner("Processing...."):
                # get pdf text
                raw_text = getPdfText(docs)
                text_chunks = getChunks(raw_text)
                st.write(text_chunks)
