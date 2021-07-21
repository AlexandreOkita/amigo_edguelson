from service.DiscordService import DiscordService
from service.ChampionBuildService import ChampionBuildService
from service.SpeakingCogService import SpeakingCogService
from service.LolStatService import LolStatService
from repository.Firebase import FirebaseDb
from repository.Lol import Lol
from utils.GetEnv import GetEnv
from riotwatcher import LolWatcher


lol = Lol()
lolWatcher = LolWatcher('RGAPI-14322987-e9ea-4744-a575-30f4f131a08e')
lolStatService = LolStatService(lolWatcher, lol, "br1")
getEnv = GetEnv()
discordService = DiscordService(getEnv.get("DISCORD_TOKEN"))
firebaseDb = FirebaseDb()
championBuildService = ChampionBuildService(lol)
speakingCogService = SpeakingCogService(firebaseDb)
