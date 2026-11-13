class Statistic:

    category = None

    def __init__(self):
        self.value = 0.0

    def __iadd__(self, item):
        self.value += item["price_expense"]
        return self

    def result_expense(self):
        return self.value

class House_goods(Statistic):
    category = "house goods"

class Food(Statistic):
    category = "food"

class Study(Statistic): 
    category = "study"

class Entertainment(Statistic):
    category = "entertainment"

class Other_goods(Statistic):
    category = "other goods"