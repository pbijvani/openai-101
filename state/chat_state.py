SYSTEM_PROMPT = "You are a helpful assistant. Answer clearly and concisely."


def build_initial_messages():
    return [{"role": "system", "content": SYSTEM_PROMPT}]


def reset_conversation():
    return build_initial_messages()


def append_message(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
