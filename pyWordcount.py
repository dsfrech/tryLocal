#
#   This program uses Sqlite3 to store the words in a book and how many times the words are used
#   The book is from https://gutenberg.org and stored as a text file in alice.txt.
#

import sqlite3 as sl
import re
import sys

FILENAME = 'data\\alice.txt'                            # the book we are going to parse
DATABASEFILE = 'data\\wordsinbooks.db'                  # where to store the database
STRIPCHARS = ':*,?!.-;/\\|][{}+_()&^%$#@~`<>“"'+"'"     # note ' " and “

try:
    with open(FILENAME, encoding='utf-8') as f:
        contents = f.read()                             # read entire file into contents
except FileNotFoundError:
    print(f'Sorry, the file {FILENAME} does not exist.')
else:
                                                        # use regex to find the words
    words = re.findall('\w+',contents.lower())          # make all lower case
    words.sort()                                        # sort it
    num_words = len(words)                              # how many words in the list
    print(f"The file {FILENAME} has about {num_words} words.")

createDatabase = input("Create WORDS database y/n? ").capitalize()
if createDatabase != 'Y':
    sys.exit(0)                                         # EXIT -- EXIT -- EXIT -- EXIT

print('Table creation')
con = sl.connect(DATABASEFILE)
with con:                                               # create the database
    con.execute("""     
        CREATE TABLE WORDS (
            word TEXT NOT NULL PRIMARY KEY,
            count integer
        );
    """)
sql = 'INSERT INTO WORDS (word, count) values (?,?)'    # specify the SQL insert stmt

print('Add words to table')
timesUsed = 0
priorWord = ''
wordCount = 0

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
        wordCount += 1

print('Unique words: ',wordCount)

print('Get words with over 200 uses')
with con:
    data = con.execute("SELECT * FROM WORDS WHERE count > 200 ORDER BY count")
    for row in data:
        print(row)
