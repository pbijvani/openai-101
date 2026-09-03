import logging

from openai import AzureOpenAI

from config import get_settings

logger = logging.getLogger(__name__)


def get_client() -> AzureOpenAI:
    settings = get_settings()
    return AzureOpenAI(
        azure_endpoint=settings["endpoint"],
        api_key=settings["api_key"],
        api_version=settings["api_version"],
    )


def get_response(messages):
    settings = get_settings()

    if not settings["endpoint"] or not settings["api_key"] or not settings["deployment_name"]:
        raise ValueError(
            "Missing Azure OpenAI configuration. Set AZURE_OPENAI_ENDPOINT, "
            "AZURE_OPENAI_API_KEY, and AZURE_OPENAI_DEPLOYMENT."
        )

    if "/api/projects/" in settings["endpoint"]:
        raise ValueError(
            "This looks like an Azure AI Foundry project URL, not the Azure OpenAI resource endpoint. "
            "Use the Azure OpenAI resource URL from the 'Keys and Endpoint' page."
        )

    client = get_client()
    response = client.chat.completions.create(
        model=settings["deployment_name"],
        messages=messages,
        temperature=0.7,
        max_tokens=500,
    )

    return response.choices[0].message.content or ""
