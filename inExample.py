#
# Demo of the in operator
#
letter = 'o'
vowel_set = {'a','e','i','o','u'}
vowel_list = ['a','e','i','o','u']
vowel_tuple = ('a','e','i','o','u')
# Note that in checks the keys, not the values
vowel_dict = {'a':'apple','e':"elephant",'i':'impala','o':'ocelot','u':'unicorn'}
vowel_string = 'aeiou'
if letter in vowel_set:
    print('yup')
if letter in vowel_list:
    print('yup')
if letter in vowel_tuple:
    print('yup')
if letter in vowel_dict:
    print('yup')
if letter in vowel_string:
    print('yup')

#
# Demo of the walrus :=  operator
#
tweet_limit = 280
tweet_string = "Blah" * 80
print(len(tweet_string))
dif = tweet_limit - len(tweet_string)
print(abs(dif))
if (diff := tweet_limit - len(tweet_string)) >= 0:
    print('fitting tweet')
else:
    print('went over by ', abs(diff))

secret = 8
guess = 5

if guess < secret:
    print("too low")
elif guess == secret:
    print("right on")
else:
    print("too high")

#
# Example of triple quote for multiline strings
#
longString = ''' this has a leading space,
    but no trailing space.  We are 
    having a trailing space after are
     and leading space here.'''
print(longString)
longString = ''' this has a leading space,
but no trailing space.  We are 
having a trailing space after are
 and leading space here.'''
print(longString)
#
# note that print will put a space between the items below
#
print('give', 'us', 'some', 'space')

#
# create a string from something else
#
a = str(98.6)

#
# create a raw string
#
info = r'Type a \n to get a new line in a normal string'
print(info)

#
# concatenate some string literals, it won't put spaces between strings
#
info = "my word!" "a gentlemen caller!"
print(info)

#
# duplicate string
#
a = "*** "
a = a * 10
print(a)

#
# get a character in a string with []
#
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0], letters[8])

#
# change a letter in a string via .replace()
#
name = 'Henny'
print('P' + name[1:])
name = name.replace('H','P')
print(name)

