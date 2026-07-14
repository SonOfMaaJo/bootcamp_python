import sys

lenght = len(sys.argv)
if lenght == 1:
    print('Usage: python3 whois.py <number>')
    sys.exit()

try:
    if lenght > 2:
        raise IndexError()
    number = int(sys.argv[1])
    if number != 0 and number % 2 == 0:
        print("I'm Even.")
    elif number % 2 == 1:
        print("I'm Odd.")
    else:
        print("I'm Zero.")
except ValueError:
    print('AssertionError: argument is not an integer', file=sys.stderr)
except IndexError:
    print('AssertionError: more than one argument is provided')
