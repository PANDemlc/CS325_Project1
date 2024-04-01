# chatgptAPI.py
# Braden Burgener
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()

# Function takes in a string that will act as user response then using a prompt, calls OpenAI's API and outputs an AI response
    # In this specific case, the funciton takes in the body of the article and returns a 50 word summary
def get_ai_response(text):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", # Enter desired GPT model
        messages=[
            {"role": "system", "content": "Summarize the following article in less than 50 words."}, # Create a custom prompt for the AI
            {"role": "user", "content": text},
        ]
    )
    return completion.choices[0].message.content