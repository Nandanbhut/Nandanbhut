
import random 

#Rock Paper Sciccors Game
print("Welcome to my game of Rock/Paper/Sciccors")

#Point System
User = 0
Computer = 0 
Options = ["rock", "paper", "Sciccors"]

#While true and if statments
Total_input = 0
while True: 
    User_1 = input("type Rock/Paper/Sciccors or q to quit: ").lower()    
    if User_1 == "q": 
        print("Thanks for playing")
        break
        
    if User_1 not in Options: 
        print("Please choose Rock, Paper, or Sciccors")
        continue 

    random_number = random.randint(0, 2)
#0 is rock, 1 is paper and 2 is Sciccors 
    computer_pick = Options[random_number]
    print("Computer picked " + computer_pick + ".")
#Rock paper and Sciccors game code

    if User_1 == "rock" and computer_pick == "Sciccors":
        print("you win")
        User += 1
        Total_input += 1  
        print(str(User) + "/" + str(Total_input))

    elif User_1 == "paper" and computer_pick == "rock": 
        print("you win")
        User += 1
        Total_input += 1  
        print(str(User) + "/" + str(Total_input))

    elif User_1 == "Sciccors" and computer_pick == "paper": 
        print("you win")
        User += 1
        Total_input += 1  
        print(str(User) + "/" + str(Total_input))

    else: 
        print("You lose")
        Computer += 1
        Total_input += 1  
        print(str(User) + "/" + str(Total_input))

print("You won " + str(User) + " times out of " + str(Total_input) + ".") 
print("Computer won " + str(Computer) + " times " + str(Total_input) + ".")
