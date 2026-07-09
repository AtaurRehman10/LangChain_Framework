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

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

# sequential_chain
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic': 'Unemployment in pakistan'})

print(result)

chain.get_graph().print_ascii()
