import os
import PyPDF2
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import Ollama
from langchain.embeddings import GPT4AllEmbeddings
from langchain.chains import RetrievalQA

# Nombre de la base de datos Chroma
chroma_db_name = "db_digesto20240524"
# Carpeta que contiene los PDFs
pdf_folder = "C:/Users/jumaf/Documents/GitHub/ia_datos-espaciales/ChatDigestoIA/base_conocimiento"

# Inicializa Chroma con el nombre y limpia la base de datos
embeddings = GPT4AllEmbeddings()
chroma_db = Chroma(embedding_function=embeddings, 
                   persist_directory="C:/Users/jumaf/Documents/GitHub/ia_datos-espaciales/ChatDigestoIA", 
                   collection_name=chroma_db_name)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages(page_num)
            text += page.extract_text()
    return text

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

def split_text_into_chunks(text):
    return text_splitter.split_text(text)

# Obtiene todas las rutas de los archivos PDF en la carpeta
pdf_paths = [os.path.join(pdf_folder, file) for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

for pdf_path in pdf_paths:
    print(f'Archivo: {pdf_path}')
    text = extract_text_from_pdf(pdf_path)
    chunks = split_text_into_chunks(text)
    # Crea y añade los documentos fragmentados a la base de datos
    for chunk in chunks:
        # Verifica si el chunk contiene la frase no deseada antes de añadirlo a la base de datos
        if "El texto de los documentos publicados" not in chunk:
            chroma_db.add_texts([chunk], metadatas=[{"source": pdf_path}])
chroma_db.persist()

# Inicializa el modelo Llama2 con Ollama
llm = Ollama(model="llama2")

# Crea una cadena de QA con recuperación usando Chroma
qa_chain = RetrievalQA.from_chain_type(llm, retriever=chroma_db.as_retriever())

# Ejecuta una consulta
query = "¿Cuál es el contenido del PDF sobre 'tema específico'?"
response = qa_chain.run(query)
print(response)
