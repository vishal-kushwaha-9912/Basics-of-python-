
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