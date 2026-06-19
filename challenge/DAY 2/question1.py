# Question 1: While Loop (Easy)
# Count down from 10 to 1

# Write a program using a while loop that prints numbers from 10 down to 1, then prints "Blastoff!" at the end.

# x = 10

# while x >= 1:
#     print(x)
#     x -= 1

# print("Blastoff!")

## or using FOR LOOP


# for x in range(10 ,0,-1):
#     print(x)
    
# print("Blastoff")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# Question 2: If-Else (Medium)
# Grade calculator

# Write a program that asks the user for their score (0-100) and prints their grade based on:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

# score  = int (input("Enter your score : "))
    
# if score in  range(90,101):
#     print("your grade is  : A")
# elif score in range (80 ,90):
#     print("our grade is  :  B")
# elif score in range(70,80):
#     print("our grade is  :  C")
# elif score in range (60 ,70):
#     print("our grade is  :  D")
# else:
#     print("our grade is  :  F")        
            
            
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            

# Question 4: For Loop + If-Else (Medium)
# Sum of even numbers

# Write a program that uses a for loop to find the sum of all even numbers from 1 to 20.
# Expected output: 110 (2+4+6+8+10+12+14+16+18+20)
# total=0
# for x in range(0,21):
  
#   if x%2==0:
    
#     total = total + x
    
# print("the sum of all even numbers is  : ", total )




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# #Question 5: While Loop + If-Else (Hard)
# Simple guessing game

# Write a program where:

# Computer "thinks" of a number between 1-10
# User guesses the number (using input)
# Program tells if guess is too high, too low, or correct
# Loop continues until user guesses right


#ANSWER :::

# import random

# jackpot = random.randint(1,10)

# guess = int(input("Enter the number : "))


# while guess != jackpot:
#     if guess <jackpot:
#         print("Guess Higher")
#     else:
#         print("Guess Lower")
#     guess =int (input("Guess Number is :"))
    
# print("🎉 Correct Guess ")   


##### IMPROVE VERSION ^^^^^

import random

jackpot = random.randint(1,10)
count = 1
guess = int(input("Enter the number : "))


while guess != jackpot:
    if guess <jackpot:
        print("The Number : ",guess)
        print("Guess Higher")
    else:
        print("The Number : ",guess)
        print("Guess Lower")
    guess =int (input("Guess Number is :"))
    count +=1
print("🎉 Correct Guess ")   
print("Total Attempt to Guess the Number : ", count)
print("The number was:", jackpot)