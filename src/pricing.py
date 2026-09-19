def calculate_cost(input_tokens, output_tokens):
    input_price = 0.15
    output_price = 0.60

    input_cost = (input_tokens / 1_000_000) * input_price
    output_cost = (output_tokens / 1_000_000) * output_price

    return input_cost + output_cost
