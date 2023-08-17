import os
"""import openai

openai.api_key="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"

def generate_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.4
    )
    return response.choices[0].text.strip()
def chatbot_pipeline():
    print("ChatBot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() == 'exit':
            break
        
        # User message
        user_message = f"User: {user_input}"
        bot_response = generate_response(user_message)
        
        # Bot response
        print("ChatBot:", bot_response)
chatbot_pipeline() """

import requests
import PIL.Image
import numpy as np

def generate_image(text):
    url = "https://stable-diffusion.cdn.openai.com/v1/generate"
    data = {"prompt": text}
    response = requests.post(url, json=data)
    image_data = np.fromstring(response.content, np.uint8)
    image = PIL.Image.fromarray(image_data)
    return image

image = generate_image("A beautiful landscape with a mountain range in the background")
image.show()