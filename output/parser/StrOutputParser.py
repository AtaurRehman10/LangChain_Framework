from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    provider="featherless-ai",
    task="text-generation",
    max_new_tokens=500,
    temperature=0.7,
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text.\n{text}',
    input_variables=['text']
)

# prompt1 = template1.invoke({'topic':'black hole'})
# report = model.invoke(prompt1)
# reportparser = parser.invoke(report)

# prompt2 = template2.invoke({'text':reportparser})
# summary = model.invoke(prompt2)
# summaryparser = parser.invoke(summary)

chain = template1 | model | parser | template2 | model | parser
summaryparser = chain.invoke({'topic':'black hole'})

print(summaryparser)
