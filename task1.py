class bottle:
    color = str
    value = float

bottle_1 = bottle()
bottle_2 = bottle()
bottle_3 = bottle()

bottle_1.color = "Красная"
bottle_2.color = "Белая"
bottle_3.color = "Черная"

bottle_1.value = 0.7
bottle_2.value = 0.3
bottle_3.value = 1.0

print(bottle_1.color, bottle_1.value)
print(bottle_2.color, bottle_2.value)
print(bottle_3.color, bottle_3.value)