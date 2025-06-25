import streamlit as st
import requests

st.title("🤖 Chat with AI (HuggingFace)")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        response = requests.post(
            "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
            headers={"Authorization": f"Bearer {st.secrets['HF_token']}"},
            json={"inputs": {"text": user_input}}
        )

        if response.status_code == 200:
            bot_reply = response.json().get("generated_text", "No reply.")
            st.text_area("Bot:", bot_reply, height=100)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")