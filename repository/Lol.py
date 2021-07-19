from utils.Singleton import singleton
from models.LolItem import LolItem
from models.LolChampion import LolChampion
import json


def read_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

def getAllItems(itemData):
    ret = []
    data = itemData["data"]
    for item in data:
        ret.append(LolItem(item, data[item]["name"], data[item]["description"], data[item]["gold"]["total"]))
    return ret

def getAllChampions(championData):
    ret = []
    data = championData["data"]
    for champion in data:
        ret.append(LolChampion(data[champion]["name"], data[champion]["title"]))
    return ret

#itens miticos : contem Passivo Mitico e o id é menor que 6693

@singleton
class Lol:
    def __init__(self):
        self.itemData = getAllItems(read_json("./resources/item.json"))
        self.championData = getAllChampions(read_json("./resources/champion.json"))

