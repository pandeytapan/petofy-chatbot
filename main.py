from config.settings import (
    OPENAI_API_KEY
)
from openai import OpenAI


def initialize_chatbot() -> None:
    """Initialize the chatbot with the OpenAI API key and engine."""
    client = OpenAI(api_key=OPENAI_API_KEY)


if __name__ == "__main__":
    initialize_chatbot()