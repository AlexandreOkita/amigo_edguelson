import requests
import random
from repository.Lol import Lol
from models.ChampionBuild import ChampionBuild
from utils.Singleton import singleton


def mythicFilter(item):
    return "Passivo Mítico" in item.description and item.id <= 6693

def bootFilter(item):
    return "Botas " in item.name

def legendaryFilter(item):
    return item.gold >= 1600 and not "Passivo Mítico" in item.description

@singleton
class ChampionBuildService:

    def __init__(self, lolRepository: Lol):
        self.lolRepository = lolRepository

    def mythicFilter(self, item):
        return "Passivo Mítico" in item.description and item.id <= 6693

    def getRandomMythicItem(self):
        items = self.lolRepository.itemData
        mythicItems = list(filter(mythicFilter, items))
        return random.choice(mythicItems)

    def getRandomBoots(self, items):
        boots = list(filter(bootFilter, items))
        return random.choice(boots)

    def getLegendaryItems(self, items, qtt=4):
        legendaryItems = list(filter(legendaryFilter, items))
        return random.sample(legendaryItems, qtt)

    def getRandomChampion(self, champions):
        return random.choice(champions)

    def getRandomChampionBuild(self):
        items = self.lolRepository.itemData
        champions = self.lolRepository.championData

        champion = getRandomChampion(champions)

        mythic = getRandomMythicItem()
        boots = getRandomBoots(items)
        legendaries = getLegendaryItems(items)

        return ChampionBuild(f"{champion.name}, {champion.title}", [mythic] + [boots] + legendaries)

