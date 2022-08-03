#
#   This program uses Sqlite3 to store the words in a book and how many times the words are used
#   The book is from https://gutenberg.org and stored as a text file in alice.txt.
#

import sqlite3 as sl
import sys

filename = 'alice.txt'
stripChars = ':*,?!.-;/\\|][{}+_()&^%$#@~`<>“"'+"'"      # note ' " and “

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()                             # read entire file into contents
except FileNotFoundError:
    print(f'Sorry, the file {filename} does not exist.')
else:
    contents = contents.lower()                         # make all lower case
    words = contents.split()                            # make a list of the words

    unsorted = ''
    for w in words:
        unsorted += w.strip(stripChars) + ' '           # strip junk off words to create a str

    words = unsorted.split()                            # make it a list again
    words.sort()                                        # sort it
    num_words = len(words)                              # how many words in the list
    print(f"The file {filename} has about {num_words} words.")

createDatabase = input("Create WORD database y/n? ").capitalize()
if createDatabase != 'Y':
    sys.exit(0)

con = sl.connect('my-test.db')
with con:
    con.execute("""
        CREATE TABLE WORDS (
            word TEXT NOT NULL PRIMARY KEY,
            count integer
        );
    """)
sql = 'INSERT INTO WORDS (word, count) values (?,?)'

timesUsed = 0
priorWord = ''
for w in words:
    if w == priorWord:
        timesUsed += 1
    else:
        if timesUsed != 0:                               # check 1st time switch
            data = [
                (priorWord, timesUsed)
            ]
            with con:
                con.executemany(sql, data)
        priorWord = w
        timesUsed = 1


with con:
    data = con.execute("SELECT * FROM WORDS WHERE count > 200 ORDER BY count")
    for row in data:
        print(row)

# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write('I am learning programming.\n')
#     file_object.write('I am still learning.\n')
#
# with open(filename, 'a') as file_object:
#     file_object.write('I am participating in a programming love fest\n')
#     file_object.write('I am creating apps\n')
#
# with open(filename) as fo:
#     for record in fo:
#         record = record.rstrip('\n')
#         print(record)
#         record = record.replace('am', 'like')
#         print(record)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
#
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first = input('\nFirst number: ')
#     if first == 'q':
#         break
#     second = input('Second number: ')
#     if second == 'q':
#         break
#
#   The only code that should go in a try block is code that might cause an exception to be raised.
#
#     try:
#         answer = int(first) / int(second)
#     except ZeroDivisionError:
#         print("You can't divide by zero:",first,'/',second)
#     else:
#         print(answer)
