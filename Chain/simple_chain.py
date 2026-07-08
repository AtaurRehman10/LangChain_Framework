from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal",
    temperature=0.7,
    max_output_tokens=300,
)

parser = StrOutputParser()
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# Simple Chain in Langchain
chain = prompt | model | parser
Result = chain.invoke({'topic':'Software Engineering'})
print(Result)


