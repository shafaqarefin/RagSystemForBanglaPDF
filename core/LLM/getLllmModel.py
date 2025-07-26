from dotenv import load_dotenv
import os
from groq import Groq
from .chatHistory import getChatHistory, addChatHistory

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)


def getLLMResponse(chunks, query):
    context_text = "\n\n".join(chunk.page_content for chunk in chunks)
    chat_history = getChatHistory()

    prompt = f"""
    You are a helpful assistant fluent in English and Bangla.

    Chat History:
    {chat_history if chat_history else "No prior conversation."}

    Instructions(Read all carefully):
    - Use ONLY the information in the Context below to answer factual questions.If you are not entirely sure then provide with the most likely answer that is most sensible to you.
    - For analytical, follow-up, or conversational questions, rely on Chat History as needed.
    - Be precise and concise.
    - If the answer is a single word or phrase, return ONLY that word or phrase in bangla with correct spelling.
    - Do NOT include the questions or mcq options number,numerics or letter  like ("ক ", "A ","i ", etc.)
    - Correct obvious spelling mistakes in your final answer.
    - If you cannot find a definite answer, reply with Not found.


    Context:
    {context_text}

    Question:
    {query}

    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="qwen/qwen3-32b"
    )

    response = chat_completion.choices[0].message.content.strip()

    addChatHistory(query, response)

    return response
