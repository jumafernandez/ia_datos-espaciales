import os

import panel as pn

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

pn.extension()

os.environ["OPENAI_API_KEY"] = "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"

async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    await chain.apredict(input=contents)

chat_interface = pn.chat.ChatInterface(callback=callback, callback_user="ChatGPT")

callback_handler = pn.chat.langchain.PanelCallbackHandler(chat_interface)

llm = ChatOpenAI(streaming=True, callbacks=[callback_handler])
memory = ConversationBufferMemory()

chain = ConversationChain(llm=llm, memory=memory)

chat_interface.send(
    "Send a message to get a reply from ChatGPT!", user="System", respond=False)
chat_interface.servable()
