import streamlit as st
import requests

# Hugging Face API token
api_token = "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"  # Replace with your actual token
headers = {"Authorization": f"Bearer {api_token}"}

def get_response(prompt, model="gpt2"):
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {"inputs": prompt}
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"
    
    response_json = response.json()
    if isinstance(response_json, list) and len(response_json) > 0 and 'generated_text' in response_json[0]:
        return response_json[0]['generated_text']
    else:
        return f"Unexpected response format: {response_json}"

# Streamlit app
st.set_page_config(page_title="GPT-2 Chatbot", page_icon="🤖", layout="centered")
st.title("Chatbot")
st.write("A way to easily interact.")

# Sidebar settings
st.sidebar.title("Settings")
model = st.sidebar.text_input("Model", "gpt2")

# User input and response
user_input = st.text_area("You: ", "")
if st.button("Send"):
    if user_input:
        with st.spinner("Generating response..."):
            response = get_response(user_input, model=model)
        st.text_area("Bot:", response, height=200)
    else:
        st.error("Please enter a message to send to the bot.")

# Footer
st.markdown("---")
st.markdown("Made with [Streamlit](https://streamlit.io/) and [Hugging Face](https://huggingface.co/).")
