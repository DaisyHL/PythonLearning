from random import randint

x=randint(0,300)

for count in range(0,10):
    digit = int (input('Please input a number between 0~300:'))
    if digit == x:
        print('Bingo!')
    elif digit>x:
        print('Too large,please try again.')
    else:
        print('Too samll,please try again.')
