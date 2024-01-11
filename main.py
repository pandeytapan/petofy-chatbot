from config.settings import (
    OPENAI_API_KEY,JSON_BASE_DIRECTORY
)
from openai import OpenAI
from src.json_reader import load_json_files_from_directory


def initialize_chatbot() -> None:
    """Initialize the chatbot with the OpenAI API key and engine."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    load_json_files_from_directory(JSON_BASE_DIRECTORY)

if __name__ == "__main__":
    initialize_chatbot()