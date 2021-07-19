from routes.edgarRegister import edgarRegister
from routes.edgarBuild import edgarBuild
from routes.edgarFala import edgarFala
from routes.edgarJaDeu import edgarJaDeu
from routes.edgarList import edgarList
from routes.edgarDelete import edgarDelete
from routes.edgarAjuda import edgarAjuda
from di.GlobalObjects import discordService


async def on_message(message):

    if message.author == discordService.getBotName():
        return

    command = message.content.split()[0]

    routes = {
        "edgar_register": edgarRegister,
        "edgar_build": edgarBuild,
        "edgar_fala": edgarFala,
        "edgar_ja_deu": edgarJaDeu,
        "edgar_list": edgarList,
        "edgar_delete": edgarDelete,
        "edgar_ajuda": edgarAjuda
    }

    await routes[command](message)