from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmCategory,
    HarmBlockThreshold,
    Image,
    Part,
)

import os
import vertexai
import google.generativeai as genai
import os
from openai import OpenAI
from google.cloud import language_v2
import os
#import openai

client = OpenAI(api_key="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")

#api_key = "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"


#client.api_key = "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"

STRANSLATED_STRING = "'I fucking hate you. I hope you die in a fire'"


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/prithviseran/Desktop/EZSpeech/backend/API_KEY.json"

def get_response(input):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input + " Give me 3 possible responses, each response having a different tone of language. Each response must be in format such that: 1: first option (new line) 2: second option (new line) 3: third option"},
    ]
    )

    return response.choices[0].message.content.strip()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "API_KEY.json"

multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

prompt = 'What can you do?'

contents = [prompt]

responses = multimodal_model.generate_content(contents, stream=True)


print("\n-------Response--------")
for response in responses:
    print(response.text, end="")
