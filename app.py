import requests
import streamlit as st

# ✅ Correct headers with proper token
headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}

# ✅ Correct API URL
API_URL = "https://api-inference.huggingface.co/models/MiniMaxAI/MiniMax-M1-80k"

# ✅ Query function with error handling
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        st.error("❌ Failed to decode response from Hugging Face. Please check your token or model name.")
        print("❌ Raw response from API:", response.text)  # For debugging in logs
        return []
 ✅ Streamlit UI starts here
st.title("Chat with AI (Hugging Face)")

user_input = st.text_input("You:")

if user_input:
    output = query({"inputs": user_input})
    
    # ✅ Display chatbot response if available
    if output and isinstance(output, list) and "generated_text" in output[0]:
        st.write("AI:", output[0]["generated_text"])
    else:
        st.warning("⚠ No response from model or unexpected format.")