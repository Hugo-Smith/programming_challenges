import numpy as np

def check_input( rand_int, turn):
    turn = turn + 1
    input_num = input('Please guess a number from 1 to 100\n')
    input_num = int(input_num)

    if input_num < 1 or input_num > 100:
        print('Your number is outside the range')
        check_input(rand_int, turn)
    
    if input_num > rand_int:
        print('That number is too high!')
        check_input(rand_int, turn)

    elif input_num < rand_int:
        print('That number is too low!')
        check_input(rand_int, turn)
    elif input_num == rand_int:
        print(f'You got it! It took {turn} turns')

if __name__ == '__main__':
    rand_int = np.random.randint(1,100)
    print("Welcome to the number guessing game!")
    check_input(rand_int, 0)
    