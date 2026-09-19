from config import client

def chat(conversations):
    full_res = ""
    final_res = None
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=conversations,
        stream=True
    )
    for event in response:
        if event.type == "response.output_text.delta":
            full_res += event.delta
            print(event.delta,end="",flush=True)
        if event.type == "response.completed":
            final_res = event.response
    return full_res, final_res