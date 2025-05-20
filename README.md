# Streamlit n8n Webhook Chat Demo

This project demonstrates how to build a simple chat interface in Streamlit that connects to an n8n agent webhook. It is designed for educational purposes and is easy to set up and extend.

## Features
- Chat UI with message history
- Connects to an n8n webhook using basic authentication
- Parses and displays agent responses from JSON
- Easy to extend for more advanced chatbot features

## Project Structure
- `app.py` — Main Streamlit app with chat logic
- `.env` — Environment variables (credentials and webhook URL, not committed)
- `requirements.txt` — Python dependencies
- `.gitignore` — Files and folders to ignore in git
- `README.md` — Project documentation

## Setup Instructions

1. **Clone the repository** (or copy the files to a new directory):
   ```bash
   git clone <your-repo-url>
   cd <project-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root with your n8n credentials and webhook URL:
   ```env
   N8N_WEBHOOK_URL=https://your-n8n-instance/webhook/your-endpoint
   N8N_USERNAME=your_username
   N8N_PASSWORD=your_password
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## How it Works
- The app loads your credentials and webhook URL from the `.env` file using `python-dotenv`.
- You can type a message in the chat box and click "Send".
- The message is sent to the n8n webhook using HTTP POST with basic authentication.
- The agent's response (in JSON) is parsed and displayed in the chat history.
- You can clear the chat history at any time.

## For Students: How to Extend
- Add more fields to the message payload (e.g., user ID, context)
- Improve the UI with Streamlit components (e.g., avatars, colors)
- Add error handling for network issues
- Connect to other types of webhooks or APIs

## Requirements
- Python 3.8+
- Streamlit
- python-dotenv
- requests

## License
MIT (or specify your license)
