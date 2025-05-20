import streamlit as st
import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import urllib3
import json

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables from .env file
load_dotenv()

# Get environment variables
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
N8N_USERNAME = os.getenv("N8N_USERNAME")
N8N_PASSWORD = os.getenv("N8N_PASSWORD")

# Initialize session state for chat history and message if they don't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'message' not in st.session_state:
    st.session_state.message = ""

st.title("n8n Chat Demo")

if not all([N8N_WEBHOOK_URL, N8N_USERNAME, N8N_PASSWORD]):
    st.error("Please set N8N_WEBHOOK_URL, N8N_USERNAME, and N8N_PASSWORD in your .env file.")
else:
    # Display chat history in a chat-like format
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            st.markdown(f"**You [{message['timestamp']}]**\n> {message['text']}")
            if 'response' in message:
                # Try to parse JSON response
                try:
                    response_json = json.loads(message['response'])
                    agent_reply = response_json.get('output', message['response'])
                except Exception:
                    agent_reply = message['response']
                st.markdown(f"**Agent:**\n> {agent_reply}")
            st.markdown("---")

    def send_message():
        message = st.session_state.message
        if message.strip():
            try:
                response = requests.post(
                    N8N_WEBHOOK_URL,
                    auth=(N8N_USERNAME, N8N_PASSWORD),
                    json={'Message': message},
                    verify=False
                )
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state.chat_history.append({
                    'timestamp': timestamp,
                    'text': message,
                    'status_code': response.status_code,
                    'response': response.text
                })
                st.session_state.message = ""
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a message.")

    # Input area
    with st.container():
        st.text_area("Type your message:", key="message")
        st.button("Send", on_click=send_message)

    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun() 