# Nested loop :: A loop that is placed inside another loop is called a nested loop.
# The inner loop executes completely for every iteration of the outer loop.


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Question 1 

# Write a Python program to print a right-angled triangle pattern of stars (*) using nested loops.
# The number of rows should be entered by the user.


row = int(input("Enter the number of rows : "))

for i in range (1, row+1):
    for j in range(0,i):
        print("*", end= " ")
    print  ()    
   
   
# #OUTPUT ::     
# Enter the number of rows :    5



# *
# * *
# * * *
# * * * *
# * * * * *