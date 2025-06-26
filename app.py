import requests
import streamlit as st

headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
API_URL = "https://api-inference.huggingface.co/models/MiniMaxAI/MiniMax-M1-80k"

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("Chat with AI (Hugging Face)")

user_input = st.text_input("You: ")

if user_input:
    output = query({"inputs": user_input})
    print(output)
    st.write("AI:", output[0].get('generated_text', 'No response from model'))
