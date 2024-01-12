import json
import os
from typing import Dict
from config.settings import JSON_BASE_DIRECTORY  # Import the base directory from settings


def load_json_file(file_path: str) -> Dict[str, str]:
    """
    Loads a JSON file and returns a dictionary mapping prompts to responses.
    :param file_path: Path to the JSON file.
    :return: Dictionary of prompt-response pairs.
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return {item.get("Prompt"): item.get("Response") for item in data}


def load_json_files_from_directory(base_directory: str) -> Dict[str, str]:
    """
    Loads all JSON files in a directory (and subdirectories) into a single dictionary.
    :param base_directory: Path to the base directory.
    :return: Dictionary of prompt-response pairs from all files.
    """
    combined_dict = {}

    if os.path.isdir(base_directory):
        for root, _, files in os.walk(base_directory):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    combined_dict.update(load_json_file(file_path))

    return combined_dict


if __name__ == "__main__":
    result_dict = load_json_files_from_directory(JSON_BASE_DIRECTORY)
    
