from chat import chat

conversations = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "q":
        print("Good Luck :)")
        break
    conversations.append({'role': 'user', 'content': user_input})
    print("AI: ", end="")
    answer, response = chat(conversations)
    print()
    conversations.append({'role': 'assistant', 'content': answer})