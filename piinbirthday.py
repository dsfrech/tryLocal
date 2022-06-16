"""
    put the million digit pi into a searchable string
    then we'll look for a given brithday within the string
"""

FILENAME = 'data/pi_million_digits.txt'
BIRTHDAY = '0928'                           # MMDD

"""
Note that with will cause the file to be closed at the end of the block
"""

with open(FILENAME, encoding='utf-8') as p:
    data = p.readlines()

pi_million = ''
for line in data:
    current_line = line.lstrip().rstrip()
    pi_million += current_line

#  print(pi_million)

whereIsIt = pi_million.find(BIRTHDAY)

if whereIsIt > 0:
    print('yes @', whereIsIt)
else:
    print('no')
