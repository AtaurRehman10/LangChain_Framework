from langchain_huggingface import HuggingFacePipeline , ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()
      
llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-0.5B-Instruct",
    task = "text-generation",
    pipeline_kwargs = dict(
        max_new_tokens = 200,
        temperature = 0.5,
    ) 
)       
   
chatmodel = ChatHuggingFace(llm=llm)

messages = [
    ("system", "You are a helpful teacher. Explain in simple words."),
    ("human", "Explain bubble sort in short.")
]

response = chatmodel.invoke(messages)

print(response.content)
