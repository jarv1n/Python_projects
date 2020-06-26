#this is a guess the nummber game

import random

print('Hello! What is your name?')
name = input()

print('\nHello ' + name + '! I am thinking of a number from 1 to 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 6):
    guess = input('\nTake a guess\n')
    
    if guess.isnumeric():
        guess = int(guess)
        if guess < secretNumber:
            print('You guessed too low')
        elif guess > secretNumber:
            print('You guessed too high')
        else:
            break #This condition is for the correct guess 
    else:
        print('Please enter an integer. . .')
        
        
if guess == secretNumber:
    print('Great job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('\n\nNope, I was thinking of ' + str(secretNumber))




