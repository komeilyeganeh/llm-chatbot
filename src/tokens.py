import tiktoken

def count_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    return len(tokens)

def count_conversation_tokens(conversations):
    total_tokens = 0
    for message in conversations:
        total_tokens += count_tokens(message["content"])
    return total_tokens