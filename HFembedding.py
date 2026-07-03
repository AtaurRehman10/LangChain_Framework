from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"

)

my_documents = [
    "What is the meaning of life?",
    "Python is an interpreted, high-level programming language.",
    "DevSecOps integrates security practices into the DevOps lifecycle."
]


document_vectors = embeddings.embed_documents(my_documents)


print(f"Total documents embedded: {len(document_vectors)}")
print(f"Dimensions of the first document: {len(document_vectors[0])}")
print(f"Dimensions of the second document: {len(document_vectors[1])}")