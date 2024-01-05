import json
import os

def loading(file_path):
    local_dict = {}
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        print(type(data))
        for i in data:
            prompt = i.get("Prompt")
            response = i.get("Response")
            local_dict[prompt] = response
                
    return local_dict

def load_json_files(base_directory):
    my_dict = {}

    if os.path.isdir(base_directory):
        for root, dirs, files in os.walk(base_directory):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    local_dict = loading(file_path)
                    my_dict.update(local_dict)
    return my_dict

base_directory_path = '/home/anmol/Desktop/Petofy-chatbot/dataset'
result_dict = load_json_files(base_directory_path)
print(result_dict)
