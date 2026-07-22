from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

docs = [
    Document(page_content="FAISS is a vector similarity search library developed by Meta."),
    Document(page_content="LangChain is a framework for building LLM-powered applications."),
    Document(page_content="ChromaDB is an open-source vector database with built-in persistence."),
    Document(page_content="Pinecone is a fully managed cloud vector database."),
    Document(page_content="NestJS is a Node.js framework for building scalable backend applications."),
]


splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_documents(docs)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
)

vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("my_faiss_index")
print("Index saved!")


loaded_store = FAISS.load_local(
    "my_faiss_index",
    embeddings,
)

query = "What is a vector database from Meta?"
results = loaded_store.similarity_search(query, k=1)

print("\n--- Search Results ---")
for i, r in enumerate(results, 1):
    print(f"{i}. {r.page_content}")


