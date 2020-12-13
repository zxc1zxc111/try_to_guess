from random import randint


def try_to_guess(num):
    digit = randint(1, 100)
    while num != digit:
        if num > digit:
            print('Too much, try again!')
        elif num < digit:
            print('Too little, try again!')
        try:
            print('Try once more: ', end='')
            num = int(input())
        except ValueError:
            print('Enter a valid integer: ', end='')
            num = int(input())
    else:
        return 'You guessed it, congratulations!'


try:
    print('Try to guess: ', end='')
    n = int(input())
except ValueError:
    print('Enter a valid integer: ', end='')
    n = int(input())

print(try_to_guess(n))
