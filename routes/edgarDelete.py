from di.GlobalObjects import firebaseDb

async def edgarDelete(message):
        if firebaseDb.deleteItem(message.content):
        	await  message.channel.send("Nao falo mais entao 😢")
        else:
                await  message.channel.send("Vou continuar falando, to nem ai kkkk")
        