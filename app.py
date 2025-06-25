import requests

headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
API_URL = "https://api-inference.huggingface.co/models/your-model-name"

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit app UI
import streamlit as st

st.title("Chat with AI (HuggingFace)")

user_input = st.text_input("You: ")

if user_input:
    output = query({"inputs": user_input})
    st.write("AI:", output[0]['generated_text'])