from config.settings import (
    OPENAI_API_KEY, OPENAI_API_TYPE, OPENAI_API_BASE, OPENAI_API_VERSION,
    GPT_ENGINE, TEMPERATURE, MAX_TOKENS, TOP_P, FREQUENCY_PENALTY, PRESENCE_PENALTY, STOP
)
from openai import OpenAI


def initialize_chatbot() -> None:
    """Initialize the chatbot with the OpenAI API key and engine."""
    client = OpenAI(api_key=OPENAI_API_KEY)


if __name__ == "__main__":
    initialize_chatbot()