from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

chatmodel = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    thinking_level="minimal", 
    max_output_tokens=1024,
    temperature=0.5
)

st.title("Chat App with gemini")

with st.form("gemini_prompt_form"):
    prompt = st.text_input("Enter prompt for Gemini")
    submitted = st.form_submit_button("Send")

if submitted:
    if not prompt.strip():
        st.warning("Please enter a prompt before sending.")
    else:
        with st.spinner("Gemini is thinking..."):
            response = chatmodel.invoke(prompt)
        st.write(response.text)
