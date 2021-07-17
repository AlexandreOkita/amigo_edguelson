import discord

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

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