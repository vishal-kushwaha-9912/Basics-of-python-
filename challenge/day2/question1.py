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

# Question 2: If-Else (Medium)
# Grade calculator

# Write a program that asks the user for their score (0-100) and prints their grade based on:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

score  = int (input("Enter your score : "))
    
if score in  range(90,101):
    print("your grade is  : A")
elif score in range (80 ,90):
    print("our grade is  :  B")
elif score in range(70,80):
    print("our grade is  :  C")
elif score in range (60 ,70):
    print("our grade is  :  D")
else:
    print("our grade is  :  F")        
            