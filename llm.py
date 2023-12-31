import os
import openai

openai.api_key="input your own" #Give key

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
chatbot_pipeline() 
