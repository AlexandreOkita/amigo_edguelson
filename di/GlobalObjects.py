from service.DiscordService import DiscordService
from utils.GetEnv import GetEnv

getEnv = GetEnv()
discordService = DiscordService(getEnv.get("DISCORD_TOKEN"))