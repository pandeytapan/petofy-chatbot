from config.settings import OPENAI_API_KEY, JSON_BASE_DIRECTORY
from openai import OpenAI
from src.json_reader import load_json_files_from_directory
from log.timestamp import logger  
def initialize_chatbot() -> None:
    """Initialize the chatbot with the OpenAI API key and engine."""
    try:
            logger.info('Initializing chatbot...')
            client = OpenAI(api_key=OPENAI_API_KEY)
            logger.info('Chatbot initialized successfully!')
            

            logger.info('Loading JSON files from directory...')
            result_dict = load_json_files_from_directory(JSON_BASE_DIRECTORY)
            logger.info(result_dict)
            logger.info('JSON files loaded successfully!')
            a=1/0
    except:
         logger.error('PetofyChatbot not initilize...')
    
if __name__ == "__main__":
    initialize_chatbot()
