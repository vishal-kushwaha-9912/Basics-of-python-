"""     🎮 Rock Paper Scissors Game """


import random
while True :
    
   

    computer = random.choice(["rock" , "paper", "scissors"])

    user = input("Enter you [rock , paper, scissors]  : ")
    print(f"Computer chose: {computer}")


 #  WINNING CONDTION 
 
    if user == "rock" and computer == "scissors":
        print("User Win  ")
    elif  user == "paper"  and computer == "rock":
        print("User Win ")
    elif  user == "scissors"  and computer == "paper":
        print("User Win ")
        
    
# computer winning condtions

    elif user == "paper" and computer == "scissors":
        print (" Computer  Wins ")
    elif user == "rock" and computer == "paper" :
        print (" Computer  Wins  ")
    elif user == "scissors" and computer == "rock":
        print ("Computer  Wins ")
    
    
    #draw match 
    
    elif user == "paper" and computer == "paper" :
        print("Match Draw ")
    elif user == "scissors" and computer == "scissors" :
        print("Match Draw ")
    elif user == "rock"  and computer == "rock"  :
        print("Match Draw")

# invalid condition 
    else :
        print (f"{user} is not valid ")

    choice = input("\nDo you want to perform ? (yes/no): ")

    if choice.lower() != "yes":
        print(" closed. Goodbye! 👋")
        break
