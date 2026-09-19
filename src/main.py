from chat import chat

conversations = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "q":
        print("Good Luck :)")
        break
    conversations.append({'role': 'user', 'content': user_input})
    answer = chat(conversations)
    conversations.append({'role': 'assistant', 'content': answer})
    print(f'AI: {answer}')