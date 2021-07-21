from riotwatcher import LolWatcher
from utils.Singleton import singleton

@singleton
class LolStatService:
    def __init__(self, lolWatcher, lolRepository, region):
        self.region = region
        self.lolWatcher = lolWatcher
        self.lolRepository = lolRepository
    
    def getSummonerByName(self, summonerName):
        return self.lolWatcher.summoner.by_name(self.region, summonerName)
    
    def getSummonerLastMatch(self, summonerPuuid, region):
        matches = self.lolWatcher.match_v5.matchlist_by_puuid('AMERICAS', summonerPuuid)
        return self.lolWatcher.match_v5.by_id(region, matches[0])
    
    def getSummonerLastMatchStats(self, summonerName, match_region):
        summoner = self.getSummonerByName(summonerName)
        last_match = self.getSummonerLastMatch(summoner['puuid'], match_region)
        for participant in last_match['info']['participants']:
            if participant['summonerName'] == summonerName:
                return participant
    
    def getSummonerItemsList(self, summonerDict):
        return [
            self.lolRepository.getItemById(str(summonerDict["item0"])),
            self.lolRepository.getItemById(str(summonerDict["item1"])),
            self.lolRepository.getItemById(str(summonerDict["item2"])),
            self.lolRepository.getItemById(str(summonerDict["item3"])),
            self.lolRepository.getItemById(str(summonerDict["item4"])),
            self.lolRepository.getItemById(str(summonerDict["item5"])),
            self.lolRepository.getItemById(str(summonerDict["item6"]))
        ]

if __name__ == "__main__":
    lolWatcher = LolWatcher('RGAPI-14322987-e9ea-4744-a575-30f4f131a08e')
    lolStatService = LolStatService(lolWatcher, "br1")
    stats = lolStatService.getSummonerLastMatchStats("okinacius", "americas")