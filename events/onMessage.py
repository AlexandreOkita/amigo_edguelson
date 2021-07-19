from routes.edgarRegister import edgarRegister
from routes.edgarBuild import edgarBuild
from routes.edgarList import edgarList
from routes.edgarDelete import edgarDelete
from di.GlobalObjects import discordService


async def on_message(message):

    if message.author == discordService.getBotName():
        return

    command = message.content.split()[0]

    routes = {
        "edgar_register": edgarRegister,
        "edgar_build": edgarBuild,
        "edgar_list": edgarList,
        "edgar_delete": edgarDelete
    }

    await routes[command](message)