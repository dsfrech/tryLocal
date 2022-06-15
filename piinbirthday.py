"""
    put the million digit pi into a searchable string
    then we'll look for a given brithday within the string
"""

FILENAME = 'data/pi_million_digits.txt'

"""
Note that with will cause the file to be closed at the end of the block
"""
p = open('data/pi_digits.txt')
d = p.readline().lstrip().rstrip()
e = p.readline().lstrip().rstrip()
f = d + e
print(f)
