""" Die class """
from random import randint

class Die:
    """Multi-sided dice"""

    def __init__(self, sides):
        """Set how many sides this dice has"""
        self.sides = sides

    def roll_die(self):
        """roll the dice"""
        return randint(1,self.sides)

for i in 6, 10, 20:             # 10 rolls of various sided dice
    myDie = Die(i)
    for n in range(9):
        print(myDie.roll_die(), end=" ")
    print()
