# Data Extraction 
# Api Building
# Agent Development

# TypedDist
# pydantic 
# JSON Schema

from urllib import response

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
     model="gemini-3.1-flash-lite", 
     thinking_level="minimal",
     temperature=0.7, 
     max_output_tokens=300
     )

template = PromptTemplate(
     template="Write a short explanation about the {subject}.",
     input_variables=["subject"]
     )

chain = template | model 
# prompt = template.invoke({"subject": "nature"})
# response = model.invoke(prompt)
response = chain.invoke({"subject": "Software Engineering"})

print(response.text)  