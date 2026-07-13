kata = (19, 42, 21)

lenght = len(kata)
print(f"The {lenght} numbers are: ", end='')
for i in range(lenght):
    print(f"{kata[i]}", end='')
    if i != lenght - 1:
        print(", ", end="")
print('')
