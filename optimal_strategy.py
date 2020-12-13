from random import randint


def strategy(num):
    digit = randint(1, num)
    left, right = 1, num
    middle = (left+right) // 2
    count = 0
    while digit != middle:
        middle = (left+right) // 2
        if middle < digit:
            left = middle + 1
            count += 1
            print('attempt number: ', count)
        elif middle > digit:
            right = middle - 1
            count += 1
            print('attempt number: ', count)
        else:
            return 'You guessed it, congratulations!', middle


print('Strategy from 1 to N: ', end='')
n = int(input())

print(strategy(n))

