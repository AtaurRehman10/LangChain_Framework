from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser , StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal",
    temperature=0.7,
    max_output_tokens=300,
)

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    provider="featherless-ai",
    task="text-generation",
    max_new_tokens=500,
    temperature=0.1,
)

model2 = ChatHuggingFace(llm=llm)

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2


prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
      (lambda x:x.sentiment == 'positive', prompt2 | model1 | parser1),
      (lambda x:x.sentiment == 'negative', prompt3 | model2 | parser1),
       RunnableLambda(lambda x: "could not find sentiment")
     )

chain = classifier_chain | branch_chain
result = chain.invoke({'feedback': 'This is a beautiful phone'})
print(result)
chain.get_graph().print_ascii()