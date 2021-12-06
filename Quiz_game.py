#first game code!
#This game is a quiz game to test your IQ

    #welcoming user 
print("welcome to my game!") 

    #input commands 
User = input("\nWhat is your name? : ") 
print("Weclome", User)

User = input("\nWould you like to play? ")
if User.lower() != ("yes"):
    print("Bad choice I guess you are unlucky")
    quit()

print("Great let's test your IQ :)!!!")


Score = 0   #keeping track of score
            #Start of the questions
question = input("\nQ1: What does CPU stand for?\nOptions:\n a:central processing unit\n b:idek\n c:command power unit\n d:none of above\n answer: ")
if question.lower() == "central processing unit" or "a": 
    print("YES!! Good job you seem very smart")
    Score += 1
else: 
    print("NOPE! You can't even solve an easy problem what a shame")

question_b = input("\nQ2:How many hours are there in a day?\nOptions:\n a:12\n b:24\n c:48\n d:64\n answer: ")
if question_b.lower() == "24" or "b":
    print("OMG!! you are very smart")
    Score += 1
else: 
    print("Damn you must be living under a rock lol")

question_c = input("\nQ3:Which specific month has 28 days?\n Options:\n a:all 12 months\n b:month of january\n c:february\n d:all of above\n answer: ")
if question_c.lower() == "february" or "c": 
    print("Bravo")
    Score += 1
else: 
    print("Man you suck")

question_d =  input("\nQ4:How many days in a year?\nOptions:\n a:331\n b:361\n c:365\n d:389\n answer: ")
if question_d.lower() == "365" or "c": 
    print("CORRECT!!!! You're smart")
    Score += 1
else: 
    print("Incorrect")

#calculate score and % 
print("You got " + str(Score) + " answers correct!")
print("You got " + str((Score / 4) * 100) + "%")

#calculating their final IQ because this is a IQ game
if Score == 0: 
    print("Your IQ level based on the questions you got correct is 0 and you maybe retarded")
elif Score == 1: 
    print("Your IQ level based on the questions you got correct is less then 50")
elif Score == 2: 
    print("Your IQ level based on the questions you got correct is less then 70")
elif Score == 3: 
    print("Your IQ level based on the questions you got correct is less then 90") 
else: 
    print("Your IQ level is above 100 and you are smarter than Elon Musk")
    
print("\nThanks for playing my game! and testing your IQ")
