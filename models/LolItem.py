class LolItem:

    def __init__(self, itemId, name, description, gold):
        self.id = int(itemId)
        self.name = name
        self.description = description
        self.gold = gold

    def __str__(self):
        return f"{self.name}:\n\n price: {self.gold}\n desc: {self.description}\n"