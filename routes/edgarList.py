from di.GlobalObjects import firebaseDb

async def edgarList(message):
        edgarMemory = firebaseDb.getAllItems('frases')
        edgarResp = "--- Meu cérebro começa aqui 👇👇👇 ---\n\n"
        cont = 1
        for record in edgarMemory:
                edgarResp += f"{cont}. {edgarMemory[record]}\n"
                cont+=1
        edgarResp+= "\n--- Meu cérebro acaba  aqui ☝️☝️☝️ ---"
        await  message.channel.send(edgarResp)
       
