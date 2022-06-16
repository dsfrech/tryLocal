"""
    put the million digit pi into a searchable string
    then we'll look for a given brithday within the string
"""

FILENAME = 'data/pi_million_digits.txt'
birthday = '0928'                           # MMDD

"""
Note that with will cause the file to be closed at the end of the block
"""

with open(FILENAME, encoding='utf-8') as p:
    data = p.readlines()

pi_million = ''
for line in data:
    current_line = line.lstrip().rstrip()
    pi_million += current_line

birthday = input('Enter a birthdate (MMYY): ')
if len(birthday) == 4 and birthday.isdecimal():
    mm = int(birthday[0:2])
    dd = int(birthday[2:4])
    if mm >= 1 and mm <= 12 and dd >= 1 and dd <=31:
        whereIsIt = pi_million.find(birthday)
        if whereIsIt > 0:
            print('yes @', whereIsIt)
        else:
            print('no')
    else:
        print('Invalid birthday')        
else:
    print('Invalid birthday')
