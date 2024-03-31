# chatgptAPI.py
# Braden Burgener
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()

def get_ai_response(text):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize the following article in less than 50 words."},
            {"role": "user", "content": text},
        ]
    )
    return completion.choices[0].message.content