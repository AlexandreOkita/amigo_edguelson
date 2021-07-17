import discord
import os
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

print("Starting bot")

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.event(on_ready)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('edgar_register'):
        frases = read_json(file='frases_edgar.json')
        frases["frases"].append(message.content[15:])
        write_json(file='frases_edgar.json', data=frases)        

    elif message.content.startswith('edgar_list'):
        f = read_json(file='frases_edgar.json')
        mensagem = "Atualmente eu sei falar: \n\n"
        for i in f["frases"]:
            mensagem += f"{i}\n"
        await message.channel.send(mensagem)
    
    else:
        await message.channel.send(f'edgar')

def read_json(file):
    with open(file) as f:
        return json.load(f)

def write_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)




client.run(TOKEN)