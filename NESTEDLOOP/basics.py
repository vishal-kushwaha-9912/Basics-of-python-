# Nested loop :: A loop that is placed inside another loop is called a nested loop.
# The inner loop executes completely for every iteration of the outer loop.


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Question 1 

# Write a Python program to print a right-angled triangle pattern of stars (*) using nested loops.
# The number of rows should be entered by the user.


row = int(input("Enter the number of rows : "))

for i in range (1, row+1):  # this line means the range(1 is starting , row+1 is ending postion ) 
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


'''Define >> for i in range (1, row+1)'''
# here i is define the row of the *

## this line means the range(1 is starting , row+1 is ending postion ) 
#let we take a example if the user enter the number of rows is 5 then
# the '''row  = 5 
# for i in range (1, row+1): in the place of row be put it's value then its becomes
# for i in range (1, 5+1):  there 5 is row number and the 1 is range doesn't count the ending  value .

'''Define for j in range(0,i):'''

# range(0,i ) is  define the number of star '*' print .
# if row is first then the number of the print star is " 1 " 
# if row is SECOND then the number of the print star is " 2 " 
# range(0, 1)  →  0          →  loops 1 time     (if number of row is 1 )
# range(0, 2)  →  0, 1       →  loops 2 times
# range(0, 3)  →  0, 1, 2    →  loops 3 times
# range(0, 4)  →  0, 1, 2, 3 →  loops 4 times


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Question 2

''' Print a decreasing triangle'''

for i in range (5,0,-1):
    for j in range (0,i):
        print("*", end = " ")
    print()    
# OUTPUT :    
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
'''Define >> for i in range (5,0,-1): '''

# Start = 5 ✅ (the first value)
# Stop = 0      (ending value or last value )
# Step = -1 ✅ (move backward by 1)


# if we print this statement   for i in range (5,0,-1):
                                #    print("*", end =" ")
                    
#  OUTPUT :
# 5
# 4
# 3
# 2
# 1
'''Define for j in range (0,i):'''


# range(0,i ) is  define the number of star '*' print .
# if row is 5 then the number of the print star is " 5 " 

# range(0, 5)  →  * * * * *         →  loops 5 time     
# range(0, 4)  →  * * * *           →  loops 4 times
# range(0, 3)  →  * * *             →  loops 3 times
# range(0, 2)  →  * *               →  loops 2 times
# range(0, 1)  → *                  →  loops 1 times

# ROW 1 → range(0, 5) → * * * * * → prints 5 stars
# ROW 2 → range(0, 4) → * * * *   → prints 4 stars
# ROW 3 → range(0, 3) → * * *     → prints 3 stars
# ROW 4 → range(0, 2) → * *       → prints 2 stars
# ROW 5 → range(0, 1) → *         → prints 1 star


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 
 
# Question 3
 
 
""" A QUESTION  :: WHAT ❌  IN THIS CODE"""

for i in range (0,5,-1):
    for j in range (0,i):
        print("*", end = " ")
    print()   
    
''' Define ::  for i in range (0,5,-1):'''

# in these first code of the line we can see there is for i in range (o , 5, -1):
# for i in range (0 , 5, -1):
    #   print("*",end = " " )
    
# whats its print  >>>>>>>> NOTHING PRINT Because there is a problem in these line 

# if we see range (0 , 5,-1)
# it prints in reverse order but the
# starting number is 0 so it cannot
# go backwards to reach 5
# therefore NOTHING PRINTS

 # ❌ WRONG
# range(0, 5, -1)  # start(0) is LESS than stop(5)

# ✅ CORRECT FIX
# range(5, 0, -1)  # start(5) is GREATER than stop(0)