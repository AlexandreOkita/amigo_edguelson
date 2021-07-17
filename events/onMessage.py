from routes.edgarRegister import edgarRegister
from di.GlobalObjects import discordService


async def on_message(message):

    if message.author == discordService.getBotName():
        return

    command = message.content.split()[0]

    routes = {
        "edgar_register": edgarRegister
    }

    await routes[command](message)