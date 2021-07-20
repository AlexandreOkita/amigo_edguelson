from di.GlobalObjects import firebaseDb

async def edgarRegister(message):
        firebaseDb.add('frases', message.content[10:])
        await message.channel.send("Opa, mais uma frase pra eu encher o saco :)")
