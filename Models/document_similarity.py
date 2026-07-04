from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    output_dimensionality=300
)


documents = [
    "Python is a popular programming language used for data science.",
    "Machine learning allows computers to learn patterns from data.",
    "Deep learning uses neural networks with many layers.",
    "Natural language processing helps computers understand human language.",
    "The solar system contains eight planets that orbit the Sun.",
]

query = "Deep learning what uses?"

doc_vectors = embeddings.embed_documents(documents)
query_vectors = embeddings.embed_query(query)
      
scores = cosine_similarity([query_vectors], doc_vectors)[0]


data = list(enumerate(scores))

index , score = sorted(data, key=lambda x: x[1] , reverse=True)[0]
print(f"Document: {documents[index]}")
print(f"Score: {score:.3f}")