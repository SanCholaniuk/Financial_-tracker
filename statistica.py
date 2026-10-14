class Statistic:

    category = None

    def __init__(self):
        self.value = 0.0

    def __iadd__(self, item):
        self.value += item["price expense"]

    def get_result(self):
        return self.value

class House_goods(Statistic):
    category = "house goods"

class Food(Statistic):
    category = "food"

class Study(Statistic): 
    category = "study"

class Enterteimant(Statistic):
    category = "enterteimant"

class Other_goods(Statistic):
    category = "other goods"


