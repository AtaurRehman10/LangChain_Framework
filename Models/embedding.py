from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    output_dimensionality=32
)

query_vector = embeddings.embed_query("What is the meaning of life?")
print(f"Single Query Dimensions: {len(query_vector)}")

documents = [
    "Pluto is a dwarf planet.", 
    "Python is an interpreted language."
]

doc_vectors = embeddings.embed_documents(
    documents, 
    output_dimensionality=32
)
print(f"Batch Document 1 Dimensions: {len(doc_vectors)}")
print(f"this is 1 Dimensions: {doc_vectors[0][0]}")