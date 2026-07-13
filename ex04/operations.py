import sys

lenght = len(sys.argv)
if lenght == 1:
    print('Usage: python3 operations.py <number1> <number>')
    sys.exit()
try:
    if lenght > 3:
        raise AssertionError('too many arguments')
    elif lenght < 3:
        raise AssertionError('too few arguments')
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"sum :       {a + b}")
    print(f"Difference: {a - b}")
    print(f'Product:    {a * b}')
    print(f"Quotient:   {a / b}")
    print(f"Remainder:  {a % b}")
except ZeroDivisionError:
    print('Quotient:    ERROR (division by zero)')
    print('Remainder:   ERROR (modulo by zero)')
except AssertionError as e:
    print(f'AssertionError: {e}', file=sys.stderr)
except ValueError:
    print("ValueError: only intergers", file=sys.stderr)
