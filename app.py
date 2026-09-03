import streamlit as st

from config import get_settings
from services.model_client import get_response
from state.chat_state import build_initial_messages, reset_conversation

st.set_page_config(page_title="Azure OpenAI Chat", page_icon="💬")


if "messages" not in st.session_state:
    st.session_state.messages = build_initial_messages()


st.title("Azure OpenAI Chat")
st.caption("A simple ChatGPT-like app using Azure OpenAI and in-memory conversation state.")


if st.sidebar.button("New chat"):
    st.session_state.messages = reset_conversation()
    st.rerun()


for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        settings = get_settings()
        if not settings["endpoint"] or not settings["api_key"] or not settings["deployment_name"]:
            raise ValueError("Missing Azure OpenAI environment settings.")

        with st.spinner("Thinking..."):
            assistant_reply = get_response(st.session_state.messages)

        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

        with st.chat_message("assistant"):
            st.markdown(assistant_reply)
    except Exception as exc:
        error_message = f"Error: {exc}"
        st.error(error_message)
        st.session_state.messages.append({"role": "assistant", "content": error_message})
        with st.chat_message("assistant"):
            st.markdown(error_message)
