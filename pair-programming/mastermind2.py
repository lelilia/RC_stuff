# Mastermind in python 3

import random

color = [1,2,3,4,5,6]
guesses = []
clues = []

def make_code():
    return [random.choice(color) for _ in range(4)]

def get_guess():
    print ("Make a guess")
    guess = list(map(int,list(input().replace(" ",""))))
    return check_if_guess_is_allowed(guess)

def check_if_guess_is_allowed(guess):
    if len(guess) != 4:
        print("Something went wrong with your guess! You have to guess 4 numebers between 1 and 6")
        return get_guess()
    for g in guess:
        if g not in color:
            print("Something went wrong with your guess! You are only allowed to guess numbers between 1 and 6")
            return get_guess()
    return guess

def check_guess(guess, code):
    code_copy = code.copy()
    guess_copy = guess.copy()
    right_place = 0
    right_color = 0
    for i in range(len(guess)):
        if guess_copy[i] == code[i]:
            guess_copy[i] = 0
            code_copy[i] = 0
            right_place += 1
    for i in range(len(guess)):
        if guess_copy[i] == 0:
            continue
        if guess_copy[i] in code_copy:
            right_color += 1
            code_copy.remove(guess_copy[i])
    return right_place, right_color 
            
print("M A S T E R M I N D !")
print()
print("In this game the numbers from 1 - 6 represent the colors. The first number you get as a result is the number of right colors in the right spot and the second number is the right color but in the wrong spot.")
print()
code = make_code()


for i in range(10):
    print("You have",10-i,"guesses left!")
    guess = get_guess()
    guesses.append(guess)
    right_place, right_color = check_guess(guess, code)
    if right_place == 4:
        print("You did it!")
        break
    clues.append([right_place, right_color])
    for j in range(len(guesses)):
        print(guesses[j], clues[j])

    if i == 9:
        print("Sorry you lost! The code was:")
        print(code)
        

