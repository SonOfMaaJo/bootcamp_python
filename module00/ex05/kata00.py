kata = (19, 42, 21)

lenght = len(kata)
print(f"The {lenght} numbers are: ", end='')
print(*kata, sep=', ')
