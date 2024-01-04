import openai
import os
import requests  # Add this line to import the 'requests' module
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_version = "2023-08-01-preview"
openai.api_base = "https://korbaichatbot.openai.azure.com/"
openai.api_key = os.getenv("OPENAI_API_KEY")
dotenv_path = os.path.join("/home/anmol/Desktop/Petofy-chatbot/config/.env")
load_dotenv(dotenv_path)
deployment_id = "gpt-35-turbo"

search_endpoint = "https://coldtherapy.search.windows.net"
search_key = os.getenv("SEARCH_KEY")
search_index_name = "azuresql-index404"

def setup_byod(deployment_id: str) -> None:
    class BringYourOwnDataAdapter(requests.adapters.HTTPAdapter):
        def send(self, request, **kwargs):
            request.url = f"{openai.api_base}/openai/deployments/{deployment_id}/extensions/chat/completions?api-version={openai.api_version}"
            return super().send(request, **kwargs)

    session = requests.Session()
    session.mount(
        prefix=f"{openai.api_base}/openai/deployments/{deployment_id}",
        adapter=BringYourOwnDataAdapter()
    )
    openai.requestssession = session

setup_byod(deployment_id)

while True:
    # Ask the user for a prompt
    user_prompt = input("You: ")

    # Check if the user wants to exit
    if user_prompt.lower() == 'exit':
        print("Exiting the conversation.")
        break

    # Add user's prompt to the conversation
    message_text = [{"role": "user", "content": user_prompt}]

    # Generate the assistant's response
    completion = openai.ChatCompletion.create(
        messages=message_text,
        deployment_id=deployment_id,
        dataSources=[
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": search_endpoint,
                    "key": search_key,
                    "indexName": search_index_name,
                }
            }
        ]
    )

    # Display and add the assistant's response to the conversation
    assistant_response = completion['choices'][0]['message']['content']
    print(f"Assistant: {assistant_response}")
