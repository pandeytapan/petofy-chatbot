from dotenv import load_dotenv
load_dotenv()
# openai.api_type = "azure"
# openai.api_base = "https://korbaichatbot.openai.azure.com/"
# openai.api_version = "2023-07-01-preview"
# openai.api_key = os.getenv("OPENAI_API_KEY")
# #print(os.getenv("OPENAI_API_KEY"))


# message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"hwllo"},{"role":"assistant","content":"Hello! How can I assist you today?"},{"role":"user","content":"what is india"},{"role":"assistant","content":"India is a country located in South Asia. It is the seventh largest country in the world by land area and the second most populous country, with over 1.3 billion people. India is known for its diverse culture, history, and religions. It is also a rapidly growing economy and a major player in the global tech industry."},{"role":"user","content":"what is chatgpt"},{"role":"assistant","content":"ChatGPT is a conversational AI model developed by OpenAI. It is based on the GPT (Generative Pre-trained Transformer) architecture and is trained on a large corpus of text data from the internet. ChatGPT can generate human-like responses to text-based queries and can carry on a conversation with users in a natural and engaging way. It has a wide range of applications, including customer service, chatbots, and personal assistants."}]

# completion = openai.ChatCompletion.create(
#   engine="gpt-35-turbo",
#   messages = message_text,
#   temperature=0.7,
#   max_tokens=800,
#   top_p=0.95,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=None
# )
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") 
# openai.api_type = 'azure'
# openai.api_version = "2023-07-01-preview" 

# deployment_name='gpt-35-turbo' #This will correspond to the custom name you chose for your deployment when you deployed a model. 


# start_phrase = input("Ask your query here: ")
# response = openai.Completion.create(engine=deployment_name, 
#   prompt=start_phrase,
#   temperature=0.7, 
#   max_tokens=800,
#   top_p=0.95,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=None)
# text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
# print(f"{start_phrase}: {text}")
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://korbaichatbot.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
dotenv_path = os.path.join("/home/anmol/Desktop/Petofy-chatbot/config/.env")
load_dotenv(dotenv_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Start with an empty conversation
message_text = [{"role": "system", "content": "You are an AI assistant that helps people find information."}]

while True:
    # Ask the user for a prompt
    user_prompt = input("Enter a prompt (type 'exit' to quit): ")

    # Check if the user wants to exit
    if user_prompt.lower() == 'exit':
        print("Exiting the conversation.")
        break

    # Add the user's prompt to the conversation
    message_text.append({"role": "user", "content": user_prompt})

    # Send a completion call to generate a response
    completion = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    
    # Get and print the assistant's response
    assistant_response = completion['choices'][0]['message']['content']
    print(f"Assistant: {assistant_response}")

    # Add the assistant's response to the conversation
    message_text.append({"role": "assistant", "content": assistant_response})
    #print(message_text)