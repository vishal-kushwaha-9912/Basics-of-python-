# 🔴 Advanced Level
# 21. Print this pattern.
# *
# **
# ***
# ****
# *****
# for x in range(1,7):
#     for y in range(1,x):
#         print("*",end=" ")
#     print()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 22. Print this pattern.
# *****
# ****
# ***
# **
# *


# for x in range(6,1,-1):
#     for y in range(1,x):
#         print("*",end=" ")
#     print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 23. Print this pattern.
# 1
# 12
# 123
# 1234
# 12345

# for x in range(1,6):
#     for y in range(1,x+1):
#         print(y,end=" ")
#     print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 24. Print this pattern.
# 1
# 22
# 333
# 4444
# 55555

# for x in range(1,6):
#     for y in range(0,x):
#         print(x,end=" ")
#     print()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 25. Print this pattern.
# A
# AB
# ABC
# ABCD
# ABCDE

for x in range(1,6):
    for y in range(0,x):
        print(chr(y+65),end="")
    print()
    
    
# Logic to remember

# For alphabet patterns:

# chr(65 + y) → Prints A B C D...
# chr(97 + y) → Prints a b c d...
# Pattern Formula
# Print increasing alphabets: chr(65 + y)
# Print the same alphabet repeatedly: chr(64 + x)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 26. Print the factorial of a number.

# Example:

# 5! = 120
# 27. Check if a number is prime.
# 28. Print all prime numbers from 1 to 100.
# 29. Count the frequency of each character in a string.

# Example:

# banana

# Output:

# # b = 1
# a = 3
# n = 2


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 30. Create a star pyramid.
#     *
#    ***
#   *****
#  *******
# *********

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 🎯 Challenge Questions
# Print the first 20 Fibonacci numbers.
# Find all Armstrong numbers from 1 to 1000.
# Print Pascal's Triangle.
# Create a simple loading animation using a for loop.
# Create a progress bar (e.g., █████----- 50%) using a for loop.