from config import client

def chat(message):
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=message
    )
    return response.output_text