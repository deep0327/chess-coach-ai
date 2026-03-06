import streamlit as st
from google import genai
import os

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Page design
st.set_page_config(page_title="Chess Coach AI", page_icon="♟️")
st.title("♟️ Chess Coach AI")
st.markdown("*Your personal chess coach — ask me anything about chess!*")

# Chat history store karo
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages dikhao
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input lo
user_input = st.chat_input("Ask your chess question here...")

if user_input:
    # User ka message dikhao
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Gemini se jawab lo
    system_prompt = "You are an expert chess coach with 30 years of experience. Answer all questions related to chess in a simple, encouraging and clear way."
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt + "\n\nUser question: " + user_input
    )

    # Chess Coach ka jawab dikhao
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})