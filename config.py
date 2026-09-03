import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


def normalize_endpoint(endpoint: str) -> str:
    endpoint = (endpoint or "").strip().rstrip("/")
    if endpoint.endswith("/openai/v1"):
        endpoint = endpoint[: -len("/openai/v1")]
    return endpoint


@lru_cache(maxsize=1)
def get_settings():
    endpoint = normalize_endpoint(os.getenv("AZURE_OPENAI_ENDPOINT", ""))
    return {
        "endpoint": endpoint,
        "api_key": os.getenv("AZURE_OPENAI_API_KEY", ""),
        "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT", ""),
        "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
    }
