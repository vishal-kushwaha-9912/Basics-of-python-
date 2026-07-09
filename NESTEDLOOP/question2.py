# Advanced Level
# 21. Print a right-aligned triangle.
#     *
#    **
#   ***
#  ****
# *****


# for x in range (1,6):
#     space = 5-x
#     for y in range(0,space):
#         print("" , end=" ")
#     for y in range(0,x):
#         print("*",end="")
#     print()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# 22. Print a pyramid.
#     *
#    ***
#   *****
#  *******
# *********



# for x in range (1,10):
#     space = 9 -x
#     for y in range(0, space):
#         print("",end=" ")
#     for y in range(1,x):
#         print("*",end=" ")
#     print()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





# 23. Print an inverted pyramid.
# *********
#  *******
#   *****
#    ***
#     *



# for x in range (5,0,-1):
#     space = 5-x
#     for y in range(0,space):
#         print("",end=" ")
#     for y in range(0,x):
#         print("*",end=" ")
#     print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# 24. Print a diamond.
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *



# for x in range (1,10,2):
#     space = (9-x) // 2
#     for y in range(space):
#         print(" ",end="")
#     for y in range(x):
#         print("*",end="")
#     print()

# for x in range (7,0,-2):
#     space = (9-x)//2
#     for y in range(space):
#         print(" ",end="")
#     for y in range(x):
#         print("*",end="")
#     print()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 25. Print Floyd's Triangle.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15



# num = 1 
# for x in range(1,6):
#     for y in range(1,x+1):
#         print(num,end=" ")
#         num += 1
#     print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 26. Print Pascal's Triangle.
#         1
#       1 1
#     1 2 1
#   1 3 3 1
# 1 4 6 4 1




# 29. Print an X pattern.
# *   *
#  * *
#   *
#  * *
# *   *



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 30. Print a chessboard pattern.
# X O X O X O
# O X O X O X
# X O X O X O
# O X O X O X
# X O X O X O
# O X O X O X

for x in range(1,7):
    for y in range(1,7):
        if (x+y)%2 ==0 :
         print("X", end=" ")
        else:
            print("O", end=" ")
    print()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 🏆 Bonus Challenge Questions
# Print a hollow pyramid.
# Print a butterfly pattern.
# Print a sandglass pattern.
# Print a spiral matrix (5×5).
# Print a zig-zag pattern.
# Print all possible 3-letter combinations (AAA to CCC) using three nested loops.
# Create a simple seating chart (5 rows × 10 seats).
# Create a multiplication chart from 1 to 20.

""" check this file  PATTTERNS QUESTION """
"""forloop/pyramidpattern.ipynb"""