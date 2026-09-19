from config import client

def chat(conversations):
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=conversations
    )
    return response.output_text