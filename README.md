# LLM Chatbot

A simple Python-based LLM chatbot built from scratch to explore core LLM application concepts such as streaming, token usage, cost tracking, context windows, and sliding window memory.

This project was built as a hands-on learning project to understand what happens behind a simple LLM chatbot instead of relying on high-level frameworks.

## Features

- 💬 Interactive CLI chatbot
- 🧠 Conversation history
- ⚡ Streaming responses
- 🔢 Input/output token tracking
- 💰 Token-based cost calculation
- 📏 Context token tracking
- 🪟 Sliding window memory
- 🔐 Environment-based API configuration

## Tech Stack

- Python
- OpenAI Python SDK
- Groq API
- tiktoken
- python-dotenv

## Project Structure

```text
llm-chatbot/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── chat.py
│   ├── tokens.py
│   └── pricing.py
├── .env
├── .env.example
├── .gitignore
└── README.md