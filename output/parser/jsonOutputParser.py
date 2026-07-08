from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    provider="featherless-ai",
    task="text-generation",
    max_new_tokens=500,
    temperature=0.1,
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template=(
        "Return only valid JSON. Do not include markdown or extra text.\n"
        "{format_instructions}\n"
        "Give me exactly 5 facts about {topic}."
    ),
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# PromptTemplate=template.invoke({'topic':'black hole'})
# model_output = model.invoke(PromptTemplate)
# result = parser.invoke(model_output)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})

       
print(result)
    