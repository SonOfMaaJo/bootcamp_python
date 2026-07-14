import sys

length = len(sys.argv)
if length == 1:
    print('Usage: pyton3 exec.py [args]')
    sys.exit()
for i in range(1, length):
    print(f'{sys.argv[length - i][::-1].swapcase()}', end='')
    if (i < length):
        print(' ', end='')
print('')
