import os
from openai import AzureOpenAI

def init_AzureOpenAI():
    global api_version, endpoint, subscription_key, deployment, client
    endpoint = "https://openaiop2212.openai.azure.com/"
    model_name = "gpt-5.2-chat"
    deployment = "gpt-5.2-chat"

    subscription_key = "30lrn95LkfYyt6kesu4amHusAuJTtPXpeghsOJeo1ZrcviPQqZa7JQQJ99BLACHYHv6XJ3w3AAABACOGSmwv"
    api_version = "2024-12-01-preview"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    print("App3 initialized.")

def useAzureOpenAI():
    init_AzureOpenAI()
    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Agentic AI assistant.",
        },
        {
            "role": "user",
            "content": "Help me with an area worth exploring for an Agentic AI opportunity",
        },
        {
            "role": "user",
            "content": "Present a pain-point in the first selected industry - something challenging that might be ripe for an Agentic solution.",
        },
        {
            "role": "user",
            "content": "propose the Agentic AI solution.",
        }
    ],
    max_completion_tokens =16384,
    model=deployment
)

    print(response.choices[0].message.content)

def main():
    useAzureOpenAI()

if __name__ == "__main__":
    main() 