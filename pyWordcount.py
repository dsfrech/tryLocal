"""
    This program uses Sqlite3 to store the words in a book and how many
    times the words are used.  The book is from https://gutenberg.org
    and stored as a text file in alice.txt.
"""

import sqlite3 as sl
import re
import os

FILENAME = 'data\\alice.txt'                            # the book we are going to parse
DATABASEFILE = 'data\\wordsinbooks.db'                  # where to store the database
# DATABASEFILE = ':memory:'                  # where to store the database

STRIPCHARS = ':*,?!.-;/\\|][{}+_()&^%$#@~`<>“"'+"'"     # note ' " and “

try:
    with open(FILENAME, encoding='utf-8') as f:
        contents = f.read()                             # read entire file into contents
except FileNotFoundError:
    print(f'Sorry, the file {FILENAME} does not exist.')
else:
    words = re.findall('\w+',contents.lower())          # lower case, use regex to find the words
    words.sort()                                        # sort it
    num_words = len(words)                              # how many words in the list
    print(f"The file {FILENAME} has about {num_words} words.")

# createDatabase = input("Create WORDS database y/n? ").capitalize()
# if createDatabase != 'Y':
#     sys.exit(0)                                         # EXIT -- EXIT -- EXIT -- EXIT

if os.path.isfile(DATABASEFILE):                    # if the database exists drop the table
    os.remove(DATABASEFILE)

print('Database and Table creation')
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
data = []                                           # make an empty list for later append

for w in words:
    if w == priorWord:
        timesUsed += 1
    else:
        if timesUsed != 0:                          # check 1st time switch
            data.append((priorWord, timesUsed))     # we'll do one big insert
        priorWord = w
        timesUsed = 1
        wordCount += 1

with con:
    con.executemany(sql, data)

print('Unique words: ',wordCount)

print('Get words with over 10000 uses')
with con:
    data = con.execute("SELECT * FROM WORDS WHERE count > 10000 ORDER BY count")
    for row in data:
        print(row)
