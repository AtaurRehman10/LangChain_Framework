from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    provider="featherless-ai",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.5,
)

chatmodel = ChatHuggingFace(llm=llm)

messages = [
    ("system", "You are a helpful teacher. Explain in simple words."),
    ("human", "Explain bubble sort in short.")
]

response = chatmodel.invoke(messages)

print(response.content)
