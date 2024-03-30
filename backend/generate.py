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


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "API_KEY.json"

multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

prompt = 'What can you do?'

contents = [prompt]

responses = multimodal_model.generate_content(contents, stream=True)


print("\n-------Response--------")
for response in responses:
    print(response.text, end="")