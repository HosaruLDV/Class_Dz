class bottle:
    color = str
    contains = float

    def __init__(self):
        self.contains = 0

    def get_content(self):
        return self.contains

    def fill(self, contains):
        self.contains = contains


bottle_1 = bottle()
bottle_2 = bottle()

bottle_1.color = "Красная"
bottle_2.color = "Синяя"

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())
