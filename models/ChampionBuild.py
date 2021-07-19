class ChampionBuild:

    def __init__(self, champion, items):
        self.champion = champion
        self.items = items

    def __str__(self):
        message = "Mano, olha só a build que eu tava pensando esses dias e que é muito roubada\n\n"
        message += "Champion: " + self.champion + "\n"
        for i in range(6):
            message += f"    {i+1}. {self.items[i].name}\n"
        message += "\nNamoral, algum streamer da Coreia vai copiar ela ainda, fica vendo"
        return message