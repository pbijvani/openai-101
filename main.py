print("Hello, World!")


import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"),
)

response = client.embeddings.create(
    input="Hello world",
    model=os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT"],
)

print(len(response.data[0].embedding))
print(response.data[0].embedding)
print(response)

////

import json
import os

from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

# Make sure these are in your .env
# AZURE_FOUNDRY_ENDPOINT=https://<your-resource>.services.ai.azure.com/api/projects/<project-name>
# AZURE_FOUNDRY_MODEL=<your-model-deployment-name>
# AZURE_FOUNDRY_KEY=<your-azure-ai-foundry-key>

endpoint = os.getenv("AZURE_FOUNDRY_ENDPOINT")
model_name = os.getenv("AZURE_FOUNDRY_MODEL")
api_key = os.getenv("AZURE_FOUNDRY_KEY")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key),
)

SYSTEM_MESSAGE = "You are a helpful assistant."

USER_QUERY = query
SEARCH_RESULTS = results

USER_MESSAGE = f"""
You are provided a user query and the search results based on that query.
Your task is to summarize the results and put the best order for the results.

USER_QUERY