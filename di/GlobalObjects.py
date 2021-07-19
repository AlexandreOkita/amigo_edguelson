from service.DiscordService import DiscordService
from service.ChampionBuildService import ChampionBuildService
from repository.Firebase import FirebaseDb
from repository.Lol import Lol
from utils.GetEnv import GetEnv

lol = Lol()
getEnv = GetEnv()
discordService = DiscordService(getEnv.get("DISCORD_TOKEN"))
firebaseDb = FirebaseDb()
championBuildService = ChampionBuildService(lol)
