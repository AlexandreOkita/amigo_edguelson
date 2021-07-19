import discord
from utils.Singleton import singleton

@singleton
class DiscordService:

    def __init__(self, token):
        self.token = token
        self.client = discord.Client()
        self.teste = ''

    def getBotName(self):
        return self.client.user
    
    def runServer(self):
        self.client.run(self.token)