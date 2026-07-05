from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage ,SystemMessage
# from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from typer import prompt



load_dotenv()

chatmodel = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal", 
    max_output_tokens=200,
    temperature=0.5
)

# prompt = ChatPromptTemplate([
#     ("system", "You are a helpful assistant in Technology and Programming. You will answer questions and provide information related to these topics."),
#     ("human", "{input}")
# ])

chathistory = [
      SystemMessage(content="You are a helpful assistant in Technology and Programming. You will answer questions and provide information related to these topics.")
     ]
while True:
    user_input = prompt("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print(chathistory)
        break
    chathistory.append(HumanMessage(content=user_input))
    response = chatmodel.invoke(chathistory)
    chathistory.append(AIMessage(content=response.text))
    print(f"AI: {response.text}")

    