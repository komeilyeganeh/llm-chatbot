from chat import chat
from pricing import calculate_cost
from tokens import count_tokens, count_conversation_tokens

conversations = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "q":
        print("Good Luck :)")
        break
    conversations.append({'role': 'user', 'content': user_input})
    current_tokens = count_conversation_tokens(conversations)
    print(f"\nContext tokens: {current_tokens}")
    print("AI: ", end="")
    answer, response = chat(conversations)
    print()
    conversations.append({'role': 'assistant', 'content': answer})

    print(f"Input tokens: {response.usage.input_tokens}")
    print(f"Output tokens: {response.usage.output_tokens}")
    print(f"Total tokens: {response.usage.total_tokens}")
    cost = calculate_cost(
    response.usage.input_tokens,
    response.usage.output_tokens
    )
    print(
        f"Cost: {cost:.8f}")
