from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

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


class TopicFacts(BaseModel):
    fact_1: str = Field(description='Fact 1 about the topic')
    fact_2: str = Field(description='Fact 2 about the topic')
    fact_3: str = Field(description='Fact 3 about the topic')
    fact_4: str = Field(description='Fact 4 about the topic')
    fact_5: str = Field(default=None ,description='Fact 5 about the topic')


parser = PydanticOutputParser(pydantic_object=TopicFacts)

template = PromptTemplate(
    template=(
        "Return only valid JSON. Do not include markdown or extra text.\n"
        "{format_instructions}\n"
        "Give 5 facts about {topic}."
    ),
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})

print(result.model_dump())
