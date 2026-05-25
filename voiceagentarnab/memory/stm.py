class ShortTermMemory:

    def __init__(self):

        self.messages = [
            {
                "role": "system",
                "content": """
                You are an intelligent voice assistant.

                Keep responses concise and conversational.

                Correct spelling mistakes automatically.

                Maintain conversational context naturally.
                """
            }
        ]

    def add_user_message(self, text):

        self.messages.append({
            "role": "user",
            "content": text
        })

    def add_assistant_message(self, text):

        self.messages.append({
            "role": "assistant",
            "content": text
        })

    def get_messages(self):

        return self.messages

    def clear(self):

        self.messages = []