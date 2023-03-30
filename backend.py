import openai
import os
import env
import random


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv('API_KEY')

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=4000,
            temperature=random.randint(0, 100)/100,
        ).choices[0].text
        return response


if __name__ == '__main__':
    chatbot = Chatbot()
    response = chatbot.get_response('write a joke about birds')
    print(response)
