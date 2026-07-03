from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

LLMmodel = GoogleGenerativeAI(
       model="gemini-3.1-flash-lite",
       max_output_tokens=1024,
       temperature=0.5 
     )

response = LLMmodel.invoke("explain AI in simple terms")
print(response)


