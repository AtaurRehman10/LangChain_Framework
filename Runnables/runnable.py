from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence , RunnablePassthrough , RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal",
    temperature=0,
    max_output_tokens=300,
)
 
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

FirstSequence = RunnableSequence(prompt1, model, parser)
Parallelchaining = RunnableParallel({
       'joke': RunnablePassthrough(),
       'explanation': RunnableSequence(prompt2, model, parser)
     })

chain = RunnableSequence(FirstSequence , Parallelchaining)
print(chain.invoke({'topic':'AI'}))

chain.get_graph().print_ascii()


