from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)


def getChatHistory():

    messages = memory.chat_memory.messages
    history_lines = []
    for msg in messages:
        role = "User" if msg.type == "human" else "AI"
        history_lines.append(f"{role}: {msg.content}")
    return "\n".join(history_lines)


def addChatHistory(user_input, ai_response):

    memory.chat_memory.add_user_message(user_input)
    memory.chat_memory.add_ai_message(ai_response)


def clearChatHistory():
    memory.clear()
