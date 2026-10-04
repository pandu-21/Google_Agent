from dotenv import load_dotenv
load_dotenv()

import os
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", google_api_key=os.getenv("GOOGLE_API_KEY"))

st.title("QnA Chatbot")

st.markdown("This is a simple QnA chatbot using Google Generative AI. Type your question below and press Enter to get an answer.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)
           

query=st.chat_input("Ask anything:")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    st.chat_message("ai").markdown(res.text)
    st.session_state.messages.append({"role": "ai", "content": res.text})


# while True:
    # query=st.chat_input("User:")
#     if query.lower() in ["exit","quit"]:
#         print("Exiting...")
#         break
#     res=llm.invoke(query)
#     print("AI:",res.text)
