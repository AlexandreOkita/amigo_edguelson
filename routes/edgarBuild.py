from di.GlobalObjects import championBuildService

async def edgarBuild(message):
    await message.channel.send(championBuildService.getRandomChampionBuild())