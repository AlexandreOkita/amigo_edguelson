from discord.ext import tasks, commands
from utils.Singleton import singleton
import random

@singleton
class SpeakingCogService(commands.Cog):
    def __init__(self, firebase):
        self.firebase = firebase
        self.channels = {}

    def startCog(self, channel):
        self.speak.start()
        self.channels[channel] = True

    def stopCog(self, channel):
        self.speak.cancel()
        self.channels[channel] = False

    @tasks.loop(seconds=5.0)
    async def speak(self):
        frases = list(self.firebase.getAllItems("frases").values())
        msg = random.choice(frases)
        for channel in self.channels:
            if self.channels[channel]:
                await channel.send(msg)

        