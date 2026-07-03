from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal", 
    max_output_tokens=1024,
    temperature=0.5
)

messages = [
    ("system", "You are a helpful teacher. Explain in simple words."),
    ("human", "Can you explain bubble sort in short?")
]

response = chatmodel.invoke(messages)

print(response.text)