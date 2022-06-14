"""Random Work"""

from random import randint
from random import choice

seed = randint(1,40)
print(seed)
randomNumberToUse = []
for i in range(seed):
    randomNumberToUse.append(randint(1,100))
print(type(randomNumberToUse))
print(randomNumberToUse)
randomNumberToUse.sort()
print(randomNumberToUse)
players = ['charles', 'bob', 'dave', 'keith', 'sheila']
print(choice(players))
