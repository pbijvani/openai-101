# Azure OpenAI Chat App

A lightweight Python chat app that uses Azure OpenAI in a ChatGPT-like interface.

## Features

- Chat-style UI
- Continue the same conversation in memory
- New chat button to reset context
- No user management
- No persistent chat storage

## Project structure

- `app.py` - Streamlit UI entry point
- `config.py` - environment configuration
- `services/model_client.py` - Azure OpenAI API integration
- `state/chat_state.py` - in-memory conversation handling

## Setup

1. Create a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file from the example:
   cp .env.example .env

4. Fill in your Azure OpenAI values:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_DEPLOYMENT`
   - `AZURE_OPENAI_API_VERSION`

5. Run the app:
   streamlit run app.py

## How conversation works

- Same conversation: messages remain in memory and are sent back with the next prompt.
- New chat: click the `New chat` button to clear the in-memory conversation context.

## Notes

This app intentionally keeps chat context only in memory. It does not maintain user accounts or old conversations.
