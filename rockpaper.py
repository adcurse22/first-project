import random

choises = ['r', 'p', 's']
print('r  > s , s > p , p > r ')
player = input('select: r,p,s  or (quit): ')
while player != 'quit':
    player = player.lower()
    computer = random.choice(choises)
    print(f'You select, {player}, computer select , {computer}')
    if player == computer:
        print('draw')
    elif player == 'r':
        if computer == 's':
            print('you win')
        else:
            print('you lose')
    elif player == 'p':
        print('you win')
        if computer == 's':
            print('you lose')
    elif player == 'p':
        if computer == 's':
            print('you win')
        else:
            print('you lose')
    else:
        print('have error repeat ')
    print()
    player = input('select: r , p ,s')






