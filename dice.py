from random import randint


class Dice:
    def __init__(self, name, faces):
        self.faces = faces
        self.name = name
        print(f"{self.name} is a D{self.faces} ! ")

    # Make up a class.

    def roll(self):
        result = randint(1, self.faces)
        return result


# Define a new function, namely to throw a dice and read its face number.

die = Dice('Tom', 6)
value = die.roll()
summary = {}
for i in range(1, die.faces + 1):
    summary[i] = 0
for n in range(1000000):
    test = die.roll()
    if test in summary.keys():
        summary[test] += 1
for i in summary.items():
    print(i)
