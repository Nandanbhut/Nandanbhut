#This is a Number guessing game. 

#welcome user
Player = input("Welcome to this number guessing game | What is your name?: ")
print("Hello", Player)

#Main code for the game
import random
from types import TracebackType 
User = input("Please type a number to proceed: ")

if User.isdigit(): 
    User = int(User)
elif User <= 0: 
    print("Please type in a number greater than 0")
    quit()
else:
    print("please type a number next time")
random_number = random.randint(0, User)
guess = 0

while True: 
    
    Userguess = input("Guess a number: ")
    if Userguess.isdigit(): 
        Userguess = int(Userguess)
    else:
        print("please type a number next time")
        continue
    
    if Userguess == random_number: 
        print("You got it")
        break
    elif Userguess < random_number: 
        print("Guess higher")
    else: 
        print("Guess lower")
    guess += 1
    print("you got it in", guess, "guesses")
        