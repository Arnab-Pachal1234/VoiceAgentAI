from openai import OpenAI


class ChatModel:

    def __init__(self, api_key, model):

        self.client = OpenAI(api_key=api_key)

        self.model = model

    def generate(self, messages):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return response.choices[0].message.content