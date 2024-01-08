import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.join("./config/.env")  # Update with your .env file path
load_dotenv(dotenv_path)

# OpenAI API configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")

# Chatbot settings
GPT_ENGINE = os.getenv("GPT_ENGINE")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 800))
TOP_P = float(os.getenv("TOP_P", 0.95))
FREQUENCY_PENALTY = float(os.getenv("FREQUENCY_PENALTY", 0))
PRESENCE_PENALTY = float(os.getenv("PRESENCE_PENALTY", 0))
STOP = os.getenv("STOP")
