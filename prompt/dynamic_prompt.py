from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate , load_prompt

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
paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = load_prompt("template.json")

if st.button("Generate Summary"):
    

     with st.spinner("Gemini is generating the summary..."):
           chain = template | chatmodel
           response = chain.invoke({
             "paper_input": paper_input,
             "style_input": style_input,
             "length_input": length_input,
           })
          #  prompt = template.invoke({
          #    "paper_input": paper_input,
          #    "style_input": style_input,
          #    "length_input": length_input,
          #  })
          #  response = chatmodel.invoke(prompt)
     st.write(response.text)
