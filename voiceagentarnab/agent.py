import os
import asyncio

from dotenv import load_dotenv

from .audio.stt import SpeechToText
from .audio.tts import TextToSpeech
from .llm.chat import ChatModel
from .memory.stm import ShortTermMemory

load_dotenv()


class VoiceAgent:

    def __init__(
        self,
        api_key=None,
        model="gpt-4.1-mini",
        voice="coral"
    ):

        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY missing")

        self.stt_engine = SpeechToText()

        self.tts_engine = TextToSpeech(
            api_key=self.api_key,
            voice=voice
        )

        self.chat_engine = ChatModel(
            api_key=self.api_key,
            model=model
        )

        self.memory = ShortTermMemory()

    async def pipeline(self):

        print("Voice Agent Started")
        print("Say 'stop' to exit.\n")

        while True:

            try:

                text = self.stt_engine.listen()

                if not text:
                    continue

                if text in ["stop", "exit", "quit", "bye"]:

                    print("Stopping Voice Agent")

                    await self.tts_engine.speak("Goodbye!")

                    break

                # STORE USER MESSAGE
                self.memory.add_user_message(text)

                # GET RESPONSE
                response = self.chat_engine.generate(
                    self.memory.get_messages()
                )

                # STORE ASSISTANT MESSAGE
                self.memory.add_assistant_message(response)

                print(f"\nAssistant: {response}")

                await self.tts_engine.speak(response)

            except KeyboardInterrupt:

                print("Interrupted")

                break

            except Exception as e:

                print("Error:", e)

    def get_memory(self):

        return self.memory.get_messages()