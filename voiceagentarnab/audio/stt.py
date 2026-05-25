import speech_recognition as sr


class SpeechToText:

    def listen(self):

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source)

            recognizer.pause_threshold = 2

            print("\nListening...")

            audio = recognizer.listen(source)

        try:

            text = recognizer.recognize_google(audio)

            print(f"\nUser: {text}")

            return text.lower()

        except Exception:

            print("Could not recognize speech")

            return None