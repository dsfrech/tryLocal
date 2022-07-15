import timeit

print(timeit.timeit('random.randint(1,100)', 'import random', number=10000000)) 