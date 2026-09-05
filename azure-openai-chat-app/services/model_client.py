import logging

from openai import AzureOpenAI, OpenAI

from config import get_settings, is_foundry_openai_endpoint

logger = logging.getLogger(__name__)


def get_client():
    settings = get_settings()

    if is_foundry_openai_endpoint(settings["endpoint"]):
        return OpenAI(
            base_url=settings["endpoint"],
            api_key=settings["api_key"],
        )

    return AzureOpenAI(
        azure_endpoint=settings["endpoint"],
        api_key=settings["api_key"],
        api_version=settings["api_version"],
    )


def get_response(messages):
    settings = get_settings()

    if not settings["endpoint"] or not settings["api_key"] or not settings["deployment_name"]:
        raise ValueError(
            "Missing Azure OpenAI or Azure AI Foundry configuration. Set "
            "AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, and AZURE_OPENAI_DEPLOYMENT."
        )

    client = get_client()
    response = client.chat.completions.create(
        model=settings["deployment_name"],
        messages=messages,
        temperature=0.7,
        max_tokens=500,
    )

    return response.choices[0].message.content or ""


def stream_response(messages):
    settings = get_settings()

    if not settings["endpoint"] or not settings["api_key"] or not settings["deployment_name"]:
        raise ValueError(
            "Missing Azure OpenAI or Azure AI Foundry configuration. Set "
            "AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, and AZURE_OPENAI_DEPLOYMENT."
        )

    client = get_client()
    stream = client.chat.completions.create(
        model=settings["deployment_name"],
        messages=messages,
        temperature=0.7,
        max_tokens=500,
        stream=True,
    )

    for chunk in stream:
        choices = getattr(chunk, "choices", None) or []
        if not choices:
            continue

        for choice in choices:
            delta = getattr(choice, "delta", None)
            if delta is None:
                continue

            content = getattr(delta, "content", None)
            if content:
                yield content
