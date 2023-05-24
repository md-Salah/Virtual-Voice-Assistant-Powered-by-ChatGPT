import os
import openai
from dotenv import load_dotenv

load_dotenv()


# openai.organization = "org-5NfJ2Lt9sbn9rIhkq8U0GwLQ"
openai.api_key = os.environ.get("OPENAI_API_KEY")
# lis = openai.Model.list()

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

# print(lis)



