from routes.edgarRegister import edgarRegister
from routes.edgarBuild import edgarBuild
from routes.edgarFala import edgarFala
from routes.edgarJaDeu import edgarJaDeu
from routes.edgarList import edgarList
from routes.edgarDelete import edgarDelete
from routes.edgarAjuda import edgarAjuda
from routes.edgarFiscaliza import edgarFiscaliza
from di.GlobalObjects import discordService


async def on_message(message):

    if message.author == discordService.getBotName():
        return

    command = message.content.split()[0]

    routes = {
        "edgar_add": edgarRegister,
        "edgar_build": edgarBuild,
        "edgar_fala": edgarFala,
        "edgar_ja_deu": edgarJaDeu,
        "edgar_list": edgarList,
        "edgar_delete": edgarDelete,
        "edgar_fiscaliza": edgarFiscaliza,
        "edgar_ajuda": edgarAjuda
    }

    print(command)
    if command.startswith("edgar_") and not command in routes:
        await message.channel.send("Você poderia falar algo que faz sentido, por favorzinho??")
    else:
        await routes[command](message)
