# Streamlit n8n Webhook Demo

This is a simple Streamlit project demonstrating how to connect to an n8n agent webhook.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your credentials and webhook URL to the `.env` file:
   ```env
   N8N_WEBHOOK_URL=https://your-n8n-instance/webhook/your-endpoint
   N8N_API_KEY=your_api_key
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Project Structure

- `app.py` - Main Streamlit app
- `.env` - Environment variables (not committed)
- `requirements.txt` - Python dependencies
- `.gitignore` - Files and folders to ignore in git
- `README.md` - Project documentation
