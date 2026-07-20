from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

chatmodel = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal",
    max_output_tokens=1024,
    temperature=0.5,
)

parser = StrOutputParser()
loader = TextLoader('cricket.txt', encoding='utf-8')
docs = loader.load()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)


# print(type(docs))
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | chatmodel | parser
print(chain.invoke({'poem':docs[0].page_content}))
