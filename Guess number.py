import random
num = random.randint(0,100)
print(num)
print('Welcome to Guess Number!\nPlease input a number from 1 to 100:\n')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

def is_valid_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('Maybe we’ll still enter an integer from 1 to 100?')

def compare_number():
    while True:
        counter = 0
        n = is_valid_num()
        if n < num:
            print('Your number is less than the hidden number, try again')
            counter += 1
            print(counter)
        elif n > num:
            print('Your number is greater than the hidden number, try again')
            counter += 1
        else:
            print(f'You guessed it for attempts {counter}, congratulations!')
            print('Thanks for playing the number guessing game. See you again...')
            break

compare_number()


