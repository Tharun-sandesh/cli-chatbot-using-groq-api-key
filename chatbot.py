from groq import Groq

from dotenv import load_dotenv

load_dotenv()  # gets api key from dotenv file

import os  # gives your script access to your computer's environment variables — that's how it'll read the API key you just set

# This line creates a "connection object" called client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)  

user_question = input("Ask me Anything: ")

#The full structured reply Groq sends back (not just text — includes extra metadata)
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user", 
            "content": user_question  
        }
    ]
)#The actual prompt payload sent in the API call

answer = response.choices[0].message.content
print(answer)
