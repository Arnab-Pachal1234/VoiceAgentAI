import asyncio

from .agent import VoiceAgent


def start():

    agent = VoiceAgent()

    asyncio.run(agent.pipeline())


if __name__ == "__main__":

    start()