from routes.edgarRegister import edgarRegister
from routes.edgarBuild import edgarBuild
from routes.edgarFala import edgarFala
from routes.edgarJaDeu import edgarJaDeu
from di.GlobalObjects import discordService


async def on_message(message):

    if message.author == discordService.getBotName():
        return

    command = message.content.split()[0]

    routes = {
        "edgar_register": edgarRegister,
        "edgar_build": edgarBuild,
        "edgar_fala": edgarFala,
        "edgar_ja_deu": edgarJaDeu
    }

    await routes[command](message)