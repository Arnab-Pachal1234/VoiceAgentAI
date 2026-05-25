from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer


class TextToSpeech:

    def __init__(self, api_key, voice):

        self.client = AsyncOpenAI(api_key=api_key)

        self.voice = voice

    async def speak(self, text):

        async with self.client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice=self.voice,
            input=text,
            response_format="pcm"
        ) as response:

            await LocalAudioPlayer().play(response)