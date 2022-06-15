""" my first python attempt to read a file """

FILENAME = 'data/pi_digits.txt'

"""
Note that with will cause the file to be closed at the end of the block
"""

with open(FILENAME, encoding='utf-8') as file_object:
    contents = file_object.read()                           # Read entire file at once
#file_object.read()                                         # if I attempt this, error because file closed by with
print(contents)

mydata = open(FILENAME, encoding='utf-8')                   # another way of doing it
contents = mydata.read()
print(contents)
mydata.close()

with open(FILENAME, encoding='utf-8') as myfile:
    for line in myfile:                                     # process file a line at a time
        print(line.rstrip())                                # peel off the trailing newline

#
#   readlines() returns a list containing each line in the file as a list item
#   readlines(number) will return up to number bytes and won't return the rest
#
with open(FILENAME, encoding='utf-8') as mydata:
    data = mydata.readlines()
for line in data:
    word = line.split()
    print(word)

#
#   Read(number) reads number characters at a time
#
mydata = open(FILENAME, encoding='utf-8')
for n in range(40):
    print(mydata.read(1).rstrip(), end=' ')
mydata.close()
