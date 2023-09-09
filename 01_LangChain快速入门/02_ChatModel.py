import os
os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'

import openai

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You are a creative AI."},
        {"role": "user", "content": "请给我的花店起个名"},
    ],
  temperature=0.8,
  max_tokens=60
)

print(response['choices'][0]['message']['content'])

print(response.choices)