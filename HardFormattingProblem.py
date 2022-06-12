#
# Two ways of doing the same thing
#
# Note: Line continuation is allowed because of the parentheses, brackets,
#       and or braces.  Otherwise I would use \ at the end of the line.
#
# 1. Use {} placeholders and use .format to insert the values
#
letter = '''
Dear {} {},

Thank you for your letter.  We are sorry that our {} 
{} in your {}.  Please note that it should never
be used in a {}, especially near any {}.

Send us your receipt and {} for shipping and handling.
We will send you another {} that, in our tests, 
is {}%  less likely to have {}.

Thank you for your support.

Sincerely,
{}
{}
'''

salutation = 'Mr.'
name = 'Freddie Mercury'
product = 'Mission Amplifier'
verbed = 'failed'
room = 'music room'
animals = 'dogs'
amount = '$75.00'
percent = '100'
spokesman = 'The Joker'
job_title = 'Chief Smoother Over'

print(letter.format(salutation,name,product,verbed,room,room,animals,amount,
      product,percent,verbed,spokesman,job_title))
#
# 2. Used {named} placeholders and use format(named=...) to inset the values
#
letter = '''
Dear {salutation} {name},

Thank you for your letter.  We are sorry that our {product} 
{verbed} in your {room}.  Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests, 
is {percent}%  less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''

#
# Note that below I am not repeating the values.  {product} is used twice but
# you only enter it once.
#
print(letter.format(salutation='Mr.',name='Freddie Mercury',product='Who Cares',
      verbed='tanked',room='kitchen',animals='cow',amount='$100.00',percent='100',
      spokesman='R U Kidding',job_title='Patience Tester'))



