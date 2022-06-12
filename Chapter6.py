for value in [3,2,1,0]:
    print(value)

count = 1
while count <= 5:
    print(count)
    count+=1

while 1:
    stuff = input('String to capitalize: q-quit: ')
    if stuff == 'q':
        break   
    print(stuff.capitalize())

while True:
    value = input('Integer q=quit: ')
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0: # an even number
        continue
    print(number, " squared is ", number*number)
#
#   This is an example of the while...else.  There is also a for...else.
#                             ============
#
numbers = [1, 3, 4, 5]
position = 0

while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:   # break not called <<<<=============NOTE while else, not if else
    print('No even number found')
# Program will continue here after the while .. else is executed

word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

for letter in word:
    print(letter)

for letter in word:
    if letter == 'u':
        break
    print(letter)

for letter in word:
    if letter == 'u':
        continue
    print(letter)

#
#   for ... else usage
#
word = 'Third'
for letter in word:
    if letter == 'u':
        break
    print(letter)
else:
    print('No -u- in word')

for x in range(0,3):
    print(x)

print("list(range(0,3)): ")
print(list(range(0,3)))

for t in [3, 2, 1, 0]:
    print(t)

