import random
import sys


# Verifying different digits
def diff_dig(comp_num):
    for digit in str(comp_num):
        if str(comp_num).count(digit) > 1:
            return True
    return False


# Checking some errors
def errors(guess):
    def only_int(guess):
        if guess.isdigit():
            return False
        return True

    while only_int(guess):
        guess = input("Provide me only number: ")
    while diff_dig(guess):
        guess = input("Please be careful, you should enter a number with different digits: ")
    guess_int = int(guess)
    if 0 < guess_int // 1000 < 10:
        return False
    return True


# Here the user is guessing
def my_game():
    comp_num = random.randint(1000, 9999)
    while diff_dig(comp_num):
        comp_num = random.randint(1000, 9999)
    while True:
        guess = input("Your turn: ")
        while errors(guess):
            guess = input("My number has 4 digits, try again: ")
        if int(guess) == comp_num:
            sys.exit(f'The game is over, you win. My number was: {comp_num}')
        total_b = 0
        total_s = 0
        for dig_ind, digit in enumerate(str(guess)):
            if str(comp_num).count(digit) > 0 and list(str(comp_num))[dig_ind] == digit:
                total_b += 1
            elif str(comp_num).count(digit) > 0 and list(str(comp_num))[dig_ind] != digit:
                total_s += 1
        print(f'{total_b}B{total_s}S')
        comp_game()


# Generating no duplicate 4-digit nums for computer
def possible_num_func():
    all_numbers = []
    for a in range(10):
        for b in range(10):
            if a == b:
                continue
            for c in range(10):
                if a == c or b == c:
                    continue
                for d in range(10):
                    if a == d or b == d or c == d:
                        continue
                    all_numbers.append(f'{a}{b}{c}{d}')
    return all_numbers


# calculating  Bigs and Smalls for computer
def calculating(comp_guess, human_num):
    comp_total_b = 0
    comp_total_s = 0
    for i in range(4):
        if comp_guess[i] == human_num[i]:
            comp_total_b += 1
        if comp_guess[i] in human_num:
            comp_total_s += 1
    comp_total_s -= comp_total_b
    return f'{comp_total_b}B{comp_total_s}S'


# Here computer is guessing
all_numbers = possible_num_func()
possible_numbers = all_numbers.copy()


# Logic for computer to guess the user number
def comp_game():
    global possible_numbers
    new_possible_numbers = []
    while True:
        comp_guess = random.choice(possible_numbers)
        print(f"I guess your number is {comp_guess}")
        score = input("Enter the score like this 'xByS': ")
        while score.count("B") != 1 or score.count("S") != 1 or len(score) != 4:
            score = input(
                "Please be careful and enter the score in this format 'xByS', where 'x' and 'y' should be numbers: ")
        if score == '4B0S':
            sys.exit(f'The game is over, I win. Your number was: {comp_guess}')
        for number in possible_numbers:
            current_score = calculating(number, comp_guess)
            if current_score == score:
                new_possible_numbers.append(number)
                possible_numbers = new_possible_numbers
        break


print('''Hello, the game is starting!
As I'm very strong, you can start first
''')
if __name__ == "__main__":
    my_game()
