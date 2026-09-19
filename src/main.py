from chat import chat

while True:
    user_input = input("You: ")
    if user_input.lower() == "q":
        print("Good Luck :)")
        break
    answer = chat(user_input)
    print(f'AI: {answer}')