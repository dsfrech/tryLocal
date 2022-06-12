''' we use collections, enumerate, range, match'''
# Create a sample collection
users = {'a': 'i', 'b': 'o', 'c': 'i', 'd': 'i'}

# Strategy: iterate over a COPY in case you modify during for
for user, status in users.copy().items():
    if status == 'o':
        del users[user]     # delete from original collection, not copy
        print(users)

for i in range(5):
    print(i,end=' ')
print()

i = range(10)
print(i)

for count, u in enumerate(users):    # enumerate returns index and a value
    print(count, u)

for n in range(2, 43):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:                           # NOTE: else is on the for loop, not if
        print(n, 'is a prime number')

for n in range(2, 10):
    if n % 2 == 0:
        print(n, 'is even')
        continue
    print(n, 'is odd')

point = (0, 0)
print(len(point), point)
match point:
    case (0,0):
        print('origin')
    case _:
        print("didn't match")
