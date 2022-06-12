from cgi import print_arguments

def donothing():
    c = 'mau'
    if c == 'red':
        print('red')
    elif c == 'blu':
        print('blu')
    elif c == 'mau':
        print('mau')
    else:
        print('nop')

    l = 'a'
    m = 'b'
    if l == 'a' and not m == 'c':
        print('yup')

    s = 'abcdefg'
    if 'c' in s:
        print('yup2') 

    l = 'o'
    vowel = {'a','e','i','o','u'}       # set
    if l in vowel:
        print('in set')       

    vowel = ['a','e','i','o','u']       # list
    if l in vowel:
        print('in set')       

    vowel = ('a','e','i','o','u')       # tuple
    if l in vowel:
        print('in set')       

    poem = '''
    There was a Young Lady of Norway,
    Who casually sat in a doorway;
    When the door squeezed her flat,
    She exclaimed, "What of that?"
    This courageous Young Lady of Norway.
    '''
    print(poem)          

    # Create a string from a number
    a = 98.605
    b = str(a)
    print(a,b)

    a = "\"In quotes\""
    print(a)

    a = r'Type a \n to do a newline"'
    print(a)

    a = 'this string ' "that string"        # concatenates with no spaces added
    a = a + a                               # same here
    print(a)

    a = "this"
    b = "that"
    c = "them"
    print(a,b,c)                            # print adds space between items
    print(a+b+c)                            # concatenate, so no spaces

    a = "abc"*4                               # * operator to duplicate string
    print(a)

    a = 'abcdefghijklmnopqrstuvwxyz'
    print(a[6])
    print(a[-1])

    a = "Henny"
    print(a.replace('H','P'))
    print(a)
    print('P'+a[1:])

    ################################################################
    #                                                              #
    #                           SLICING                            #
    # leftmost offset is 0                  rightmost offset is -1 #
    #                                                              #
    # [:] entire string                                            #
    # [start:] from start to end                                   #
    # [:end] from beginning to the end offset minus 1              #
    # [start:end] start offset to end offset minus 1               #
    # [start:end:step] start offset to end offset minus 1 skipping #
    #                  characters by step                          #
    ################################################################
    #                      1         2
    #            01234567890123456789012345
    a = b = c = 'abcdefghijklmnopqrstuvwxyz'
    print(a+'\n'+b+'\n'+c)
    print(a[0:16:2])
    print(a[-10:-3:3])
    print(a[::5])
    print(a[-1::-1])            # # # REVERSE THE STRING
    print(a[::-1])              # # # REVERSE THE STRING

    a = 'get gloves,get mask,give cat vitamins,call ambulance'
    aa = a.split()
    aaa = a.split(',')
    print(a,'\n',aa,'\n',aaa)
    print(aaa[2])

    print('#'.join(aaa))
    b = '$'.join(['ab','cd','ef','gh'])
    print(b)
    print(b.replace('$',','))               
    b = "$12.00$"
    print(b.strip('$'))                     # strips from beg and end
    print(b.lstrip('$'))                    # strips off the left
    print(b.rstrip('$'))                    # strips off the right

    poem = 'To be or not to be, that is the question'
    print( '01234567890123456789012345678901234567890')
    print(poem, len(poem))
    print(poem.startswith('To be'))
    print(poem.endswith('not'))
    print('not found at:',poem.find('not'))
    print('be index at:',poem.index('be'))      # like find but not found throws exception
    print('be rfound at:',poem.rfind('be'))
    print('be found at:',poem.find('be'))
    print('bee not found:',poem.find('bee'))
    print('be occurs:',poem.count('be'),'time(s)')
    print(poem.isalpha())

    print(poem.capitalize())
    print(poem.title())
    print(poem.upper())
    print(poem.lower())             # they're all lower already, so no change
    print(poem.swapcase())

    print(poem.center(50))
    print(poem.ljust(50))
    print(poem.rjust(50))

    ################################################################
    #                                                              #
    #                     Format Strings                           #
    #                                                              #
    # Old style 'format string'%data                               #
    # %s %d %f %x %o %e %g literal % %%                            #
    # %+(-)minwidth.maxcharsTYPE TYPE is s/d/f/x/o/e/g             #
    # + or nothing right align   - left align                      #
    # multiple data is organized as a tuple (,,)                   #
    ################################################################
    print('%s'%"now is the time")
    print('Number %d%% followed by a string %s'%(15,'now'))
    t = 'woodchuck'
    print('%s'%t)
    print('%12s'%t)
    print('%+12s'%t)
    print('%-12s'%t)
    print('%.3s'%t)
    print('%12.3s'%t)
    print('%-12.3s'%t)

    ################################################################
    #                                                              #
    #                     Format Strings                           #
    #                                                              #
    # New Style  formatstring.format(data)
    #
    # See python.org "Format Specification Mini-Language" in the 
    # "The Python Library Reference", "Text Processing Services",
    # "string - Common string operations", ...
    #  
    ################################################################

    count = 1
    while count<=5:
        print(count)
        count += 1

    # while True:
    #     value = input("Integer, please (q to quit): ")
    #     if value == 'q':
    #         break
    #     number = int(value)
    #     if number % 2 == 0:
    #         continue
    #     print(number, "squared is", number*number)
    # else: # break not called
    #     print("Break wasn't called")
        
    word = 'thud'
    offset = 0
    while offset < len(word):
        print(word[offset])
        offset +=1

    for able in word:
        if able == 'x':
            break
        print(able)
    else:
        print('No x in',word)

    for x in range(0,3,1):      # range(start,stop,step)
        print(x)

    a = list(range(0,4))
    print(a)

    for x in range(2,-1,-1):    # note last value is just before stop
        print(x)                # so last value here will be 0

    for x in range(3,-1,-1):
        print(x)

    guessMe = 7
    curg = 1
    while True:
        if curg == guessMe:
            print('found it')
            break
        if curg > guessMe:
            print("oops")
            break
        if curg < guessMe:
            print("to low")
        curg += 1
        print('new curg:',curg)

    guessMe = 5
    for curg in range(10):
        if curg < guessMe:
            print('to low:',curg)
        if curg == guessMe:
            print('found it')
            break
        if curg > guessMe:
            print('oops')
            break

#
# Chapter 7 Tuples
# 
def chapter7():
    emptyTuple = ()
    oneElementTuple = 'element',    # , makes it a tuple; without it is just a str
    print(oneElementTuple,type(oneElementTuple))    

    mTuple = (1,2,3)
    a,b,c = mTuple                  # tuple unpacking
    print('a=',a,'b=',b,'c=',c)

    p = 'fish'                      # str
    i = 'tutu'
    p,i = i,p                       # USING TUPLES TO EXCHANGE VALUES
    print('p=',p,'i=',i)            # but the individuals are still str
    print(type(p))

    mList = ['g','c','h']
    print(mList)
    mTuple = tuple(mList)
    print(mTuple)

    mTuple = mTuple*3               # * will duplicate the item
    print(mTuple)

    mList = list('cat')
    print(mList)

    sq = (1,4,9,16)             # make a tuple
    for i in range(5,10):
        sq = sq + (i*i,)        # (blah,) makes it a tuple
    print(sq)
    print(sq[3])                # address individual element via []
    sq = 1,2,3                  # still a tuple, but normally  use ()
    print(sq)

    emptyList = []
    print(emptyList)

    r = ['p',{'good':'phil'},'feb 2',sq,emptyList]
    print(r)

    cat = 'cat'
    catList = list(cat)       # cvt string to list
    print(catList)

    bday = '09/28/1948'
    bdayList = bday.split('/')  # break apart by delimiter
    print(bdayList)
    print(bdayList[1:])         # slice it up
    bdayList.reverse()          # reverse list
    print(bdayList)
    mbday = '04/16/1953'
    odayList = bdayList
    print(id(odayList),id(bdayList))  # NOTE THEY ARE THE SAME OBJECT
    odayList.append(mbday.split('/')) # SOME MY ATTEMPT TO FORK FAILS
    print(odayList)

    print(bdayList)
    d = bdayList
    d += mbday.split('/')
    print(d)

    del d[3]
    print(d)
    print(bdayList)

    n = [1,2,3,4]
    n[1:3] = [8,9]      # replace elements in list
    print(n)
    n.remove(9)         # remove an item by value
    print(n)

    m = ['a','b','c','d','e']
    print(m.pop(),m)            # get item and remove from list
    m = ['a','b','c','d','e']
    print(m.pop(0),m)
    print(m.clear(),m)

    txt = ('Now is the time for all good men '
        'to come to the aid of their country')
    print(txt)

    a, b, c = 0, 1, 10      # MULTIPLE asssignment
    while a < c:
        print(a, end=',')
        a, b = b, a+b
    print('\n')

    for n in range(2,10):
        for x in range(2,n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)  # // is floor
                break
        else:               # when you exhaust the inner for do this
            print(n, 'is a prime')

#
#   Tutorial
#

def initLog(*args):     # define a function
    pass                # pass does nothing, just occupies space

class Point:
    x: int
    y: int

    def __init__(self,x,y):
        self.x = x
        self.y = y


def where(point):
    match point:
        case Point(x=0,y=0):
            print('origin')
        case _:
            print('not a point')

point = Point(0,1)
where(point)