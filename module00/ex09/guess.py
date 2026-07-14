from random import randint


print('This is an interactive guessing gane!',
      'You have to enter a number between 1 and 99 to find out the secret',
      'number.\nType \'exit\' to end the game.\nGood luck!\n', sep='\n')
number = randint(1, 100)
# number = 22
nb_iter = 0
while True:
    nb_iter += 1
    try:
        mes = input('What\'s your guess between 1 and 99?\n>> ')
        if mes == 'exit':
            print('Goodbye')
            break
        u_number = int(mes)
        if (u_number > 99 or u_number < 1):
            print('number should be between 1 and 99.')
            continue
    except ValueError:
        print('That\'s not a number.')
        continue
    if u_number > number:
        print('Too high!')
        continue
    elif u_number < number:
        print('Too low!')
        continue
    elif u_number == number:
        if number == 42:
            print('The answer to the ultimate question of life, the universe',
                  ', the universe and everything is 42.')
        if nb_iter == 1:
            print('Congratulations! You got it on your first try!')
            break
        else:
            print('Congratulations, you\'ve got it!\n',
                  f'You won in {nb_iter} attempts!')
            break
