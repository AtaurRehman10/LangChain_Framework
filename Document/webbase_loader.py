from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate

chatmodel = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal",
    max_output_tokens=1024,
    temperature=0.5,
)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()
url = 'https://en.wikipedia.org/wiki/Muhammad_Ali_Mirza'
loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | chatmodel | parser

print(chain.invoke({'question':'What about engineer?', 'text':docs[0].page_content}))
