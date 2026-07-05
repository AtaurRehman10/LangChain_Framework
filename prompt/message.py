from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate(
     [
         ("system", "You are a helpful assistant in Technology and Programming. You will answer questions and provide information related to these topics."),
         MessagesPlaceholder(variable_name="chat_history"),
         ("human", "{input}")
     ]
 )

chathistory = []

with open("message.txt","r") as file:
    chathistory.append(HumanMessage(content=file.read().strip()))

full_prompt = prompt.invoke(
    {
        "chat_history": chathistory,
        "input": "Hello! How can I assist you today?",
    }
)
print(full_prompt)
