from llama_index.llms import ChatMessage, OpenAI

messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(role="user", content="What is your name"),
]
resp = OpenAI(api_key="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").chat(messages)
print(resp)