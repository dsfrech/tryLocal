''' Try some things out'''
numTuple = 1,2,3,4
print(numTuple,type(numTuple))

marx = 'Groucho',           # Create a tuple
print(marx," ",type(marx))
marx = ('Groucho',)         # Create a tuple
print(marx," ",type(marx))
marx = ('Groucho')          # Note no comma and it is a string
print(marx," ",type(marx))

marxTuple = 'Groucho', 'Harpo', 'Chico'     # Tuple () or just ,
marxList = list(marxTuple)    # List []     # convert tuple to list
print(marxTuple, type(marxTuple))
print(marxList, type(marxList))
cvtTuple = tuple(marxList)                  # convert list to tuple
print(cvtTuple,type(cvtTuple),id(cvtTuple))

cvtTuple *= 3
print(cvtTuple)

# Convert a string to a list of single characters

nuList = list('cattle')
print(nuList)

simpleDate = '09/19/2022'
print(simpleDate.split('/'))                # create list from split string
splitDate = simpleDate.split('/')
print(splitDate,type(splitDate))

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[1])
print(marxes[-1])
print(len(marxes))

# Get items with a slice
print(marxes[1:3])
try:
    print(marxes[3])
except:
    print("Don't forget that end of slice is exclusive (+1 len)")

print(marxes)
marxes.reverse()    # works on tuples, not lists
print(marxes)

marxTuple = 'Groucho', 'Harpo', 'Chico'     # Tuple () or just ,
#
#   NOTICE the = after the variable name, causes the print statement
#   to print the variable name as well as values using f'...'
#
print(f"{marxTuple=}")
print(f"{marxTuple[::-1]=}")

marxes = ['Groucho', 'Chico', 'Harpo']
print(f'{marxes=}')
print(f"{marxes[::-1]=}")

marxesR = marxes[::-1]
print(f"{marxesR=}")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
bigList = list(range(1,1000000))
print(min(bigList)," ",max(bigList))
print('start range')
print(sum(bigList))
print('end range')
print(bigList[0:10])

marx = ['Groucho', 'Chico', 'Harpo']
print(marx)
marx.append('Zeppo')        # append to end of list
print(marx)
marx.insert(1,'Gummo')      # insert BEFORE
print(marx)

marx = ['Groucho', 'Chico', 'Harpo']
other = ['Zeppo', 'Gummo']
marx.extend(other)          # append other list to end
print(f'{marx=}')
marx=marx[:3]
print(f'{marx=}')
marx += other               # append other list to end
print(f'{marx=}')

marx=marx[:3]
marx.append(other)         # append other as single list
print(f'{marx=}')


marx = ['Groucho', 'Chico', 'Harpo']
marx[1] = 'Wanda'
print(f'{marx=}')

marx = ['Groucho', 'Chico', 'Harpo']
marx[1:2] = ['Zeppo','Wanda']
print(f'{marx=}')
