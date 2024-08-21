from langchain_community.llms import LlamaCpp
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
import os

# Descargado de https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q5_K_S.gguf
DIRECTORIO_LLM_MODELS = 'C:/Users/jumaf/OneDrive/Documentos/llm-models/'
MODEL_NAME = "llama-2-7b-chat.Q5_K_S.gguf"
FOLDER_PATH = 'C:/Users/jumaf/Documents/GitHub/ia_datos-espaciales/IA-Luján/data/pdfs/'

N_GPU_LAYERS = 0 # Sin GPU
N_BATCH = 512
callbacks = [StreamingStdOutCallbackHandler()]
local_path = (DIRECTORIO_LLM_MODELS + MODEL_NAME)

llm_model = LlamaCpp(
    model_path = local_path,
    n_gpu_layers=N_GPU_LAYERS,
    n_batch=N_BATCH,
    n_ctx=2048,
    f16_kv=True,
    callbacks=callbacks,
)

# Load PDF
print("\nInicio de carga de documentos (RAG): ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

# Obtener la lista de archivos PDF en el directorio
pdf_files = [file for file in os.listdir(FOLDER_PATH) if file.endswith('.pdf')]

for filename in pdf_files:

    print(f'Cargando PDF: {filename}')
    
    # Cargar el PDF
    loader = PyPDFLoader(FOLDER_PATH + filename, extract_images=True)
    docs = loader.load()
    
    # Splitting de texto
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    splits = text_splitter.split_documents(docs)
    
    # Almacenamiento de resultados divididos
    vectorstore = Chroma.from_documents(documents=splits, embedding=GPT4AllEmbeddings())
    
    # Retriever
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    
    print(f'PDF {filename} procesado y almacenado en el vectorstore.')

print('Proceso de load de documentos finalizado.')


template = """Responde la pregunta en sólo en idioma español basado fundamentalmente en el contexto:
{context}

Pregunta: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

setup_and_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)


output_parser = StrOutputParser()

chain = setup_and_retrieval | prompt | llm_model | output_parser

chat_history = []

question = ""

while question != 'salir':
    question = input('Haga una pregunta al LLM: (escriba "salir" para terminar)\n\n')
    if question != 'salir':
        print("\nInicio: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        ai_msg = chain.invoke(question)
        chat_history.extend([HumanMessage(content=question), AIMessage(content=ai_msg)])
        print("Finalización: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
