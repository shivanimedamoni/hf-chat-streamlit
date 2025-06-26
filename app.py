import requests
import streamlit as st

# ✅ Set headers with Hugging Face token
headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}

# ✅ Model URL
API_URL = "https://api-inference.huggingface.co/models/MiniMaxAI/MiniMax-M1-80k"

# ✅ Function to query Hugging Face
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        st.error("❌ Failed to decode response from Hugging Face.")
        print("❌ API response:", response.text)
        return []
    # ✅ Streamlit app UI
st.title("Chat with AI (Hugging Face)")

user_input = st.text_input("You:")

if user_input:
    output = query({"inputs": user_input})

    if output and isinstance(output, list) and "generated_text" in output[0]:
        st.write("AI:", output[0]["generated_text"])
    else:
        st.warning("⚠ No valid response from the model.")

