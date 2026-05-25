# VoiceAgentArnab

Realtime AI Voice Assistant with:

- 🎙 Speech-to-Text (STT)
- 🧠 Conversational Memory (STM)
- 🤖 OpenAI LLM Integration
- 🔊 Text-to-Speech (TTS)
- ♻ Continuous Conversation Loop
- 🛑 Stop/Exit Voice Commands

Built using:
- Python
- OpenAI API
- SpeechRecognition
- OpenAI TTS

---

# Features

✅ Realtime Voice Conversations  
✅ Short-Term Memory (STM)  
✅ Context-Aware Responses  
✅ Continuous Listening Loop  
✅ User-Controlled API Key  
✅ AI Voice Responses  
✅ Installable Python Package  
✅ CLI Support  

---

# Installation

Install directly from PyPI:

```bash
pip install VoiceAgentArnab
```

---

# Requirements

- Python 3.9+
- Microphone
- Speaker/Headphones
- OpenAI API Key

---

# Setup

Create a `.env` file in your project directory.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Quick Start

## Python Usage

Create a file named `test.py`

```python
import asyncio

from voiceagentarnab import VoiceAgent


agent = VoiceAgent()

asyncio.run(agent.pipeline())
```

Run:

```bash
python test.py
```

---

# CLI Usage

You can also run directly from terminal:

```bash
python -m voiceagentarnab.main
```

Or if CLI PATH is configured correctly:

```bash
voiceagentarnab
```

---

# Example Conversation

```text
Voice Agent Started
Say 'stop' to exit.

Listening...

User: Hello

Assistant: Hello! How can I help you today?

User: My name is Arnab

Assistant: Nice to meet you Arnab.

User: What is my name?

Assistant: Your name is Arnab.

User: stop

Assistant: Goodbye!
```

---

# Short-Term Memory (STM)

This package uses STM (Short-Term Memory).

Conversation history is stored only while the program is running.

When the user says:
- stop
- exit
- quit
- bye

the application terminates and all memory is cleared automatically.

No long-term storage is used by default.

---

# Architecture

```text
User Speech
   ↓
Speech To Text
   ↓
Conversation Memory (STM)
   ↓
OpenAI LLM
   ↓
Assistant Response
   ↓
Text To Speech
```

---

# Package Structure

```text
voiceagentarnab/
│
├── audio/
│   ├── stt.py
│   └── tts.py
│
├── llm/
│   └── chat.py
│
├── memory/
│   └── stm.py
│
├── agent.py
├── main.py
└── __init__.py
```

---

# Voice Commands

## Stop Commands

The assistant stops when user says:

- stop
- exit
- quit
- bye

---

# Customization

## Custom Model

```python
agent = VoiceAgent(
    model="gpt-4.1-mini"
)
```

---

## Custom Voice

```python
agent = VoiceAgent(
    voice="coral"
)
```

Available voices depend on OpenAI TTS support.

---

# Passing API Key Manually

```python
agent = VoiceAgent(
    api_key="your_api_key"
)
```

---

# Dependencies

Main dependencies:

```text
openai
SpeechRecognition
PyAudio
python-dotenv
```

---

# Troubleshooting

## PyAudio Installation Error (Windows)

Try:

```bash
pip install pipwin
pipwin install pyaudio
```

---

# Microphone Not Detected

Test available microphones:

```python
import speech_recognition as sr

print(sr.Microphone.list_microphone_names())
```

---

# OpenAI API Key Missing

Error:

```text
OPENAI_API_KEY missing
```

Fix:
- create `.env`
- add valid API key

Example:

```env
OPENAI_API_KEY=your_key_here
```

---

# Current Limitations

- Uses Google SpeechRecognition backend for STT
- Uses STM only (memory resets after exit)
- Requires internet connection
- Not optimized for ultra-low latency realtime conversations

---

# Future Improvements

Planned features:

- Wake Word Support
- Long-Term Memory (LTM)
- Realtime Streaming
- OpenAI Whisper Integration
- Voice Customization
- Desktop App
- Multi-Agent Support

---

# Development

Clone repository:

```bash
git clone <your_repo_url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
python test.py
```

---

# Build Package

```bash
python -m build
```

---

# Publish Package

```bash
twine upload dist/*
```

---

# License

MIT License

---

# Author

Arnab

---

# PyPI

https://pypi.org/project/VoiceAgentArnab/
