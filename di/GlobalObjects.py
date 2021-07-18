from service.DiscordService import DiscordService
from repository.Firebase import Firebase
from utils.GetEnv import GetEnv

getEnv = GetEnv()
discordService = DiscordService(getEnv.get("DISCORD_TOKEN"))
firebaseDb = FirebaseDb()