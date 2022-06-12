# print('just inputting a string')
# secret = input("enter a number: ")
# guess = input("enter a guess: ")
# if guess == secret:
#     print('good guess')
# elif guess > secret:
#     print('too high')
# else:
#     print('too low')
# print('converting the string to an integer')
# secret = int(input("enter a number: "))
# guess = int(input("enter a guess: "))
# if guess == secret:
#     print('good guess')
# elif guess > secret:
#     print('too high')
# else:
#     print('too low')
#
# ''' below just creates a multiline string that the compiler throws out
# since it is not assigned to anything
#
''' now is the time for all men to 
come to the aid of their country.
Who casually sat in a doorway;
She exclaimed, "What of that?"
This courageous Young Lady of Norway.
'''
jj = ''' now is the time for all men to 
come to the aid of their country.
Who casually sat in a doorway;
She exclaimed, "What of that?"
This courageous Young Lady of Norway.
'''
print(jj)

# a = "time" + ' away ' + "for" + ' good behavior '
# a = a[0:27]
# print(a)
# b = a + " "
# print(b*2)
# c = a.split()
# print(c[2])
# d = '-'.join(c)
# print(d)
# e = d.replace('-','/',2)
# print(e)
# f = '   ' + d + '    '
# g = f.strip(' ')
# print(f)
# print(g)

# Working with jj now
print(jj)
print(jj[3:10])

print(jj.find('"What of'))

print(jj.find('the'))
print(jj.find('zebra'))
# print(jj.index('zebra')) will raise an exception if zebra not found
print(jj.rfind('the'))

print(jj.count('the'))

kk = jj
print(kk.upper())
print(kk.title())
print(kk.capitalize())
#print(kk.capitalize(kk.strip(' ')))
ll = kk.strip()
print(ll)
print(ll.capitalize())

ll = ll[:24]
print('"'+ll+'"')
ll = ll.strip()
print('"'+ll.center(30)+'"')
print('"'+ll.rjust(30)+'"')
print('"'+ll.ljust(30)+'"')
print('"'+'A'+'"')

#
# f-strings for formatting
#
thing = 'wereduck'
place = 'werepond'
print(f'The {thing =} is in the {place =}')
