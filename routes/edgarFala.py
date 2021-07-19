from di.GlobalObjects import speakingCogService

async def edgarFala(message):
    speakingCogService.startCog(message.channel)