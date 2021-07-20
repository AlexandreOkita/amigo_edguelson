from di.GlobalObjects import firebaseDb

async def edgarDelete(message):
    if len(message.content.split()) > 1:
        position = int(message.content.split()[1])

        if firebaseDb.deleteOrderedItem("frases", position):
            await  message.channel.send("Nao falo mais entao 😢")
        else:
            await  message.channel.send("Vou continuar falando, to nem ai kkkk")
    else:
        await  message.channel.send("Ala, o cara não sabe nem escrever um número kkkkk")

        