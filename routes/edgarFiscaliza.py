from di.GlobalObjects import lolStatService, championBuildService


async def edgarFiscaliza(message):
    await message.channel.send(f"Deixa eu pensar aqui")
    summonerName = message.content.split()[1]
    try:
        summoner_last_match = lolStatService.getSummonerLastMatchStats(summonerName, "americas")
    except:
        await message.channel.send("Ou mano, para de trollar e coloca um nome que existe")
        return
    items = lolStatService.getSummonerItemsList(summoner_last_match)
    mythicItems = list(filter(championBuildService.mythicFilter, items))
    if mythicItems:
        await message.channel.send(f"Huuuum to vendo aqui e você jogou de {summoner_last_match['championName']} na última partida e fez {mythicItems[0].name} \nNão é ruim, mas bom mesmo seria fazer {championBuildService.getRandomMythicItem().name}")
    else:
        await message.channel.send(f"Cara, se vc n fez nem um ítem mítico fica difícil de te ajudar né?")
