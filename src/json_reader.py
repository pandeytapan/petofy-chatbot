import json

# json_file_path = "/home/anmol/Desktop/Petofy-chatbot/dataset/Consultant/Consultant.json"
# with open(json_file_path, "r") as json_file:
#     data = json.load(json_file)
# print(data)
def loading(file_path):
    my_dict = {}
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for i in data:
            prompt = i.get("Prompt")
            response = i.get("Response")
            my_dict[prompt] = response
                
    return my_dict

data_dict = loading('/home/anmol/Desktop/Petofy-chatbot/dataset/Consultant/Consultant.json')
print(data_dict)



