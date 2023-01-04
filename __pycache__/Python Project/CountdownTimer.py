import time
userInput = int(input())


def count(userInput):
    while userInput:
        mins, sec = divmod(userInput, 60)
        print('{:02d} : {:02d}'.format(mins, sec))
        time.sleep(1)
        userInput = userInput - 1
    print('times up!')


count(userInput)
