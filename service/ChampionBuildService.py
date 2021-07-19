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

def getRandomMythicItem(items):
    mythicItems = list(filter(mythicFilter, items))
    return random.choice(mythicItems)

def getRandomBoots(items):
    boots = list(filter(bootFilter, items))
    return random.choice(boots)

def getLegendaryItems(items):
    legendaryItems = list(filter(legendaryFilter, items))
    return random.sample(legendaryItems, 4)

def getRandomChampion(champions):
    return random.choice(champions)

@singleton
class ChampionBuildService:

    def __init__(self, lolRepository: Lol):
        self.lolRepository = lolRepository

    def getRandomChampionBuild(self):
        items = self.lolRepository.itemData
        champions = self.lolRepository.championData

        champion = getRandomChampion(champions)

        mythic = getRandomMythicItem(items)
        boots = getRandomBoots(items)
        legendaries = getLegendaryItems(items)

        return ChampionBuild(f"{champion.name}, {champion.title}", [mythic] + [boots] + legendaries)

