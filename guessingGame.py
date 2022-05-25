#Number Guessing Game

import random
number = random.randint(1,9)
chance = 0
print("Guess a number (between 1 and 9). You have 5 Guesses")

while chance < 5 :
    guess = int(input("Enter your guess :-"))
    chance = chance + 1
    if guess < number:
        print("you guess was too low , guess a number higher than " , guess)
    elif guess > number:
        print("your guess was too high, guess a number lower than" , guess)  
    elif guess == number:
        print("Congractulations you won!!!")
if not chance < 5:
    print("You lose! The number is ", number)