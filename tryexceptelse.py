""" Experiment with try/except/else """
print("Give me two integers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first = input('\nFirst number: ')
    if first == 'q':
        break
    second = input('Second number: ')
    if second == 'q':
        break

#   The only code that should go in a try block is code that might cause an exception to be raised.

    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print("You can't divide by zero:",first,'/',second)
    else:
        print(answer)
